"""Repo health check: size budgets, dead links, data files, forecast table.

    uv run python process/check.py

Exits non-zero on any failure. Run it before every commit of an update; the
static build runs the link check too. Budgets are in words (`wc -w`).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLISHED = ["report", "research", "forecasts", "signals"]

# Hard limits, in words. A file over its limit must be cut, not excused.
FILE_BUDGETS = {
    "report/index.md": 1_800,
    "report/stack.md": 3_000,
    "report/theory.md": 2_200,
    "report/methodology.md": 700,
    "forecasts/register.md": 5_000,
    "signals/2026-10-18-market-views.md": 600,
    "AGENTS.md": 700,
    "README.md": 600,
    "process/README.md": 900,
    "process/briefs.md": 900,
}
FOLDER_FILE_BUDGETS = {"research": 3_500, "signals": 400}  # per file
TOTAL_MARKDOWN_BUDGET = 150_000
DATA_FILE_BYTES = 300_000
DATA_TOTAL_BYTES = 1_500_000
GONE = ["reviews", "tasks", "scripts"]  # folders that must not come back

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
ROW_RE = re.compile(r"^\|\s*\**([A-Z]\d[a-z]?)\**\s*[:|].*?\|\s*(\d+)%\s*\|\s*(\d+)%\s*\|\s*(\d+)%\s*\|\s*$")


def words(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def markdown_files() -> list[Path]:
    skip = {".venv", "site", "work", ".git", ".wrangler"}
    return sorted(p for p in ROOT.rglob("*.md") if not skip & set(p.relative_to(ROOT).parts))


def dead_links() -> list[str]:
    """Internal links in published pages that point at nothing."""
    pages = {"/"}
    for section in PUBLISHED:
        for p in (ROOT / section).rglob("*.md"):
            pages.add(f"/{section}/{p.relative_to(ROOT / section).with_suffix('').as_posix()}")
    dead = []
    for section in PUBLISHED:
        for p in sorted((ROOT / section).rglob("*.md")):
            if p.stem in ("README", "TEMPLATE"):
                continue
            for href in LINK_RE.findall(p.read_text(encoding="utf-8")):
                if re.match(r"[a-z][a-z0-9+.-]*:|#", href, re.I):
                    continue
                target = href.split("#")[0].split("?")[0]
                if not target.startswith("/"):  # relative to the page's folder
                    base = "/" + p.parent.relative_to(ROOT).as_posix()
                    target = "/" + (ROOT / base.strip("/") / target).resolve().relative_to(ROOT).as_posix() \
                        if (ROOT / base.strip("/") / target).resolve().is_relative_to(ROOT) else target
                if target.startswith(("/data/", "/raw/")) or target in ("/data", "/llms.txt", "/robots.txt"):
                    ok = (ROOT / target.strip("/").removeprefix("raw/")).exists() or target == "/data"
                    ok = ok or target in ("/llms.txt", "/robots.txt")
                else:
                    ok = target.removesuffix(".md").rstrip("/") in pages or target == "/"
                if not ok:
                    dead.append(f"{p.relative_to(ROOT)}: {href}")
    return dead


def forecast_rows(path: Path) -> dict[str, tuple[str, str, str]]:
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = m.groups()[1:]
    return rows


def main() -> None:
    fails, md = [], markdown_files()

    print(f"{'folder':12s} {'files':>5s} {'words':>8s}")
    folders: dict[str, list[int]] = {}
    for p in md:
        rel = p.relative_to(ROOT)
        key = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        folders.setdefault(key, []).append(words(p))
    for key, counts in sorted(folders.items()):
        print(f"{key:12s} {len(counts):5d} {sum(counts):8d}")
    total = sum(sum(c) for c in folders.values())
    data = sorted((ROOT / "data").glob("*.csv"))
    data_bytes = sum(p.stat().st_size for p in data)
    print(f"{'markdown':12s} {len(md):5d} {total:8d}   (budget {TOTAL_MARKDOWN_BUDGET})")
    print(f"{'data':12s} {len(data):5d} {data_bytes / 1e6:7.2f}M   (budget {DATA_TOTAL_BYTES / 1e6:.1f}M)")

    if total > TOTAL_MARKDOWN_BUDGET:
        fails.append(f"markdown total {total} words over {TOTAL_MARKDOWN_BUDGET}")
    for p in md:
        rel = p.relative_to(ROOT).as_posix()
        limit = FILE_BUDGETS.get(rel) or FOLDER_FILE_BUDGETS.get(rel.split("/")[0])
        if limit and words(p) > limit:
            fails.append(f"{rel}: {words(p)} words, limit {limit}")
    fails += [f"{name}/ exists; it was removed on purpose" for name in GONE if (ROOT / name).exists()]
    fails += [f"dead link in {link}" for link in dead_links()]

    published = "".join(p.read_text(encoding="utf-8") for s in PUBLISHED for p in (ROOT / s).rglob("*.md"))
    if data_bytes > DATA_TOTAL_BYTES:
        fails.append(f"data/ is {data_bytes / 1e6:.2f} MB, limit {DATA_TOTAL_BYTES / 1e6:.1f} MB")
    for p in data:
        if p.stat().st_size > DATA_FILE_BYTES:
            fails.append(f"data/{p.name}: {p.stat().st_size // 1000} KB, limit {DATA_FILE_BYTES // 1000} KB")
        if not p.read_text(encoding="utf-8").startswith("# source:"):
            fails.append(f"data/{p.name}: no '# source:' header line")
        if p.name not in published:
            fails.append(f"data/{p.name}: not linked from any published page")

    register = forecast_rows(ROOT / "forecasts/register.md")
    for qid, probs in forecast_rows(ROOT / "report/index.md").items():
        if qid in register and register[qid] != probs:
            fails.append(f"front page {qid} = {'/'.join(probs)}, register says {'/'.join(register[qid])}")

    leftovers = [p.name for p in (ROOT / "work").glob("*")] if (ROOT / "work").exists() else []
    if leftovers:
        print(f"note: work/ holds {len(leftovers)} file(s); empty it when the update is done")
    for f in fails:
        print("FAIL", f)
    print("OK" if not fails else f"{len(fails)} failure(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
