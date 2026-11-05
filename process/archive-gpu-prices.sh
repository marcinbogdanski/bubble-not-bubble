#!/bin/zsh
# Archive the latest published GPU rental prints. Run from any directory:
#   zsh process/archive-gpu-prices.sh
# Requires curl and python3 (standard library only); no browser or API key.
#
# Endpoint verified 2026-10-25: the Ornn H100 market page links "Free JSON"
# and its Dataset JSON-LD advertises /api/public-index/gpu/<GPU>/index-history.
# GPU identifiers are H100 SXM, H200, B200 and A100 SXM4; histories return
# success, gpu_type, and data[{timestamp, index_value}] (rolling public-3mo).
# Silicon Data's H100 page exposes the dated Neo-Cloud SDH100RT display in
# server-rendered HTML. Only that display is parsed, never the stale FAQ.
# If HTTP/parsing fails or a browser becomes necessary, write unavailable
# for that series and continue. Unavailable values are missing observations.
#
# CSV date is the PUBLISHER'S observation date, not the capture date; accessed
# is the local capture date. OCPI timestamps are converted to New York dates.
# An older latest print retains its date and is never carried forward to today.
# Skip any series already recorded for today, and also deduplicate older
# observation dates. A file lock protects the final check-and-append on reruns.
# These five columns do not establish publisher quality flags or fresh-day
# coverage by themselves; unavailable rows must never enter forecast means.

set -eu
repo_dir=${0:A:h:h}
exec python3 - "$repo_dir/data/gpu-index-daily.csv" <<'PY'
import csv
import fcntl
import io
import json
import re
import subprocess
import sys
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from urllib.parse import quote
from zoneinfo import ZoneInfo

csv_path = sys.argv[1]
today = date.today().isoformat()
columns = ["date", "series", "value", "source URL", "accessed"]


def read_rows(handle):
    handle.seek(0)
    reader = csv.DictReader(line for line in handle if not line.startswith("#"))
    if reader.fieldnames != columns:
        raise ValueError("unexpected CSV columns; refusing to append")
    return {(row["date"], row["series"]) for row in reader}


def fetch(url):
    result = subprocess.run(
        ["curl", "--fail", "--location", "--silent", "--show-error",
         "--connect-timeout", "10", "--max-time", "30",
         "--user-agent", "Mozilla/5.0", url],
        capture_output=True, text=True, encoding="utf-8", timeout=35,
    )
    if result.returncode:
        raise ValueError(result.stderr.strip() or f"curl exited {result.returncode}")
    return result.stdout


def price(value):
    if isinstance(value, bool):
        raise ValueError("invalid boolean price")
    number = Decimal(str(value))
    if not number.is_finite() or number <= 0:
        raise ValueError("price must be positive and finite")
    return format(number, "f")


def ocpi(url, gpu):
    payload = json.loads(fetch(url), parse_float=Decimal)
    if (not isinstance(payload, dict) or payload.get("success") is not True
            or payload.get("gpu_type") != gpu):
        raise ValueError("unexpected OCPI response or GPU identifier")
    points = payload["data"]
    if not isinstance(points, list) or not points:
        raise ValueError("empty OCPI history")
    dated = []
    for point in points:
        if not isinstance(point, dict) or not isinstance(point.get("timestamp"), str):
            raise ValueError("invalid OCPI history point")
        stamp = datetime.fromisoformat(point["timestamp"].replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("OCPI timestamp lacks timezone")
        dated.append((stamp, point))
    stamp, point = max(dated, key=lambda item: item[0])
    observed = stamp.astimezone(ZoneInfo("America/New_York")).date().isoformat()
    return observed, price(point["index_value"])


class DisplayText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def silicon(url):
    parser = DisplayText()
    parser.feed(fetch(url))
    text = " ".join(" ".join(parser.parts).split())
    if "H100 Rental Price Index" not in text or "SDH100RT" not in text:
        raise ValueError("H100 SDH100RT display not found; browser may be required")
    matches = re.findall(
        r"\bNeo-Cloud\s+Hyperscaler\s+As of\s+"
        r"([A-Z][a-z]{2}\s+\d{1,2},\s+\d{4})\s+"
        r"\$?(\d+(?:\.\d+)?)\s+USD\s*/\s*GPU-hour\b", text,
    )
    if len(matches) != 1:
        raise ValueError("dated Neo-Cloud display unavailable; browser may be required")
    stamp, value = matches[0]
    observed = datetime.strptime(stamp, "%b %d, %Y").date().isoformat()
    return observed, price(value)


with open(csv_path, newline="", encoding="utf-8") as handle:
    existing = read_rows(handle)

series = []
for label, gpu in [("H100", "H100 SXM"), ("H200", "H200"),
                   ("B200", "B200"), ("A100", "A100 SXM4")]:
    url = "https://data.ornn.com/api/public-index/gpu/" + quote(gpu, safe="") + "/index-history"
    series.append((f"OCPI-{label}_USD_per_GPU-hour", url, gpu))
series.append(("SDH100RT_USD_per_GPU-hour",
               "https://www.silicondata.com/products/silicon-index/h100", None))

pending = []
for name, url, gpu in series:
    if (today, name) in existing:
        print(f"Skipped {name}: row for {today} already exists.")
        continue
    try:
        observed, value = ocpi(url, gpu) if gpu else silicon(url)
        if observed > today:
            raise ValueError(f"publisher date {observed} is in the future")
    except (ValueError, KeyError, TypeError, InvalidOperation, OSError,
            subprocess.TimeoutExpired) as exc:
        observed, value = today, "unavailable"
        print(f"{name}: unavailable ({exc})", file=sys.stderr)
    if (observed, name) in existing:
        print(f"Skipped {name}: latest publisher date {observed} already exists.")
        continue
    pending.append([observed, name, value, url, today])

# Recheck under an exclusive lock: another invocation may have finished fetching.
with open(csv_path, "r+", newline="", encoding="utf-8") as handle:
    fcntl.flock(handle, fcntl.LOCK_EX)
    existing = read_rows(handle)
    handle.seek(0, 2)
    writer = csv.writer(handle, lineterminator="\n")
    for row in pending:
        observed, name = row[:2]
        if (today, name) in existing or (observed, name) in existing:
            print(f"Skipped {name}: row already exists.")
            continue
        writer.writerow(row)
        handle.flush()
        existing.add((observed, name))
        output = io.StringIO()
        csv.writer(output, lineterminator="\n").writerow(row)
        print(output.getvalue(), end="")
PY
