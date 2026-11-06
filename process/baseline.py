"""No-view reference probabilities for the market forecasts and layer rows.

    uv run --with numpy python process/baseline.py [YYYY-MM-DD]

Circular ten-day block bootstrap of demeaned daily log returns since
2025-03-28, 20,000 paths, daily-rebalanced baskets, touch rule as in
forecasts/register.md. Three runs: no drift, no drift at 1.5x volatility,
and +10% a year. Horizons are the trading days left to the register's fixed
dates. The optional argument is the "as of" close (default: latest common
date). M1 names and the Nasdaq-100 come from data/ai-basket-performance.csv;
other layer constituents are fetched from Yahoo's chart API and cached in
work/ (ignored by git), on US trading dates with foreign closes carried
forward. M3 fixes the 6 October 2026 peak.
"""

import csv
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
START, ORIGIN, PEAK_NDX = "2025-03-28", "2026-10-16", 31224.69
HORIZONS = {"6m": "2027-04-17", "12m": "2027-10-17", "24m": "2028-10-17"}
M1 = ["NVDA", "AVGO", "TSM", "ORCL", "CRWV", "AMD", "MU", "VRT"]
M1A, M1B = ["NVDA", "AVGO", "TSM", "AMD", "MU"], ["ORCL", "CRWV", "VRT"]
LAYERS = {
    "Equipment": ["ASML", "AMAT", "LRCX", "KLAC", "8035.T"],
    "Foundry": ["TSM"],
    "Memory": ["MU", "000660.KS", "005930.KS"],
    "Accelerators": ["NVDA", "AMD", "AVGO"],
    "Hyperscalers": ["MSFT", "GOOGL", "AMZN", "META"],
    "Oracle (equity only)": ["ORCL"],
    "Neoclouds (equity only)": ["CRWV", "NBIS", "IREN", "CIFR", "WULF", "APLD", "CORZ", "HUT"],
    "Power and datacenter (equity only)": ["VRT", "GEV", "EQIX", "DLR"],
}
N, BLOCK, SEED = 20_000, 10, 7


def committed() -> dict[str, dict[str, float]]:
    px: dict[str, dict[str, float]] = {}
    with open(ROOT / "data/ai-basket-performance.csv") as f:
        for d, tk, c in list(csv.reader(l for l in f if not l.startswith("#")))[1:]:
            px.setdefault(tk, {})[d] = float(c)
    return px


def fetch(ticker: str) -> dict[str, float]:
    cache = ROOT / "work" / f"closes-{ticker}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ticker)}?range=2y&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research-bot)"})
    res = json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]
    offset = res["meta"].get("gmtoffset", 0)
    out = {}
    for ts, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]):
        if c is not None:
            out[dt.datetime.fromtimestamp(ts + offset, dt.timezone.utc).date().isoformat()] = float(c)
    cache.parent.mkdir(exist_ok=True)
    cache.write_text(json.dumps(out))
    return out


def main() -> None:
    px = committed()
    names = sorted({t for members in LAYERS.values() for t in members} | set(M1) | {"^NDX"})
    for t in names:
        if t not in px:
            px[t] = fetch(t)
    asof = sys.argv[1] if len(sys.argv) > 1 else max(d for d in px["NVDA"] if all(d in px[t] for t in M1 + ["^NDX"]))
    dates = sorted(d for d in px["NVDA"] if START <= d <= asof)

    def series(t: str) -> np.ndarray:  # closes on US dates, carried forward
        out, last = [], None
        for d in dates:
            last = px[t].get(d, last)
            if last is None:
                last = min((v for k, v in px[t].items() if k >= d), default=np.nan)
            out.append(last)
        return np.array(out)

    P = np.column_stack([series(t) for t in names])
    R = np.diff(np.log(P), axis=0)
    R = R - R.mean(axis=0)
    base = P[dates.index(ORIGIN)] if ORIGIN in dates else P[-1]
    last = P[-1]
    col = {t: i for i, t in enumerate(names)}
    today = dt.date.fromisoformat(asof)
    H = {k: max(1, int(np.busday_count(today, dt.date.fromisoformat(v)) * 252 / 261)) for k, v in HORIZONS.items()}
    T = max(H.values())
    rng = np.random.default_rng(SEED)

    def touch(hit: np.ndarray) -> str:
        return "/".join(f"{100 * hit[:, h - 1].mean():.0f}" for h in H.values())

    def level(members: list[str], basket_base: np.ndarray) -> float:  # buy-and-hold proxy for the index level
        return float(100 * np.mean([last[col[m]] / basket_base[col[m]] for m in members]))

    print(f"as of {asof}; {len(R)} sessions; horizons in trading days {H}")
    for scale, drift in ((1.0, 0.0), (1.5, 0.0), (1.0, 0.10)):
        starts = rng.integers(0, len(R), size=(N, T // BLOCK + 1))
        idx = ((starts[:, :, None] + np.arange(BLOCK)[None, None, :]) % len(R)).reshape(N, -1)[:, :T]
        r = R[idx] * scale + drift / 252
        cum = np.cumsum(r, axis=1)
        print(f"\nvolatility x{scale}, drift {drift:+.0%} a year (6/12/24m, %)")
        for label, members in (("M1", M1), ("M1a", M1A), ("M1b", M1B)):
            j = [col[m] for m in members]
            start = level(members, base)
            path = start * np.cumprod(1 + (np.exp(r[:, :, j]) - 1).mean(axis=2), axis=1)
            print(f"  {label:36s} from {start:5.1f}: {touch(np.minimum.accumulate(path, axis=1) <= 60)}")
        ndx = last[col["^NDX"]] * np.exp(cum[:, :, col["^NDX"]])
        print(f"  {'M3 (NDX 30% below the 6 Oct peak)':36s} from {last[col['^NDX']]:,.0f}: {touch(np.minimum.accumulate(ndx, axis=1) <= 0.70 * PEAK_NDX)}")
        for layer, members in LAYERS.items():
            hits = np.zeros((N, T), dtype=bool)
            for m in members:
                lv = last[col[m]] * np.exp(cum[:, :, col[m]])
                hits |= np.minimum.accumulate(lv, axis=1) <= 0.6 * base[col[m]]
            closest = min(members, key=lambda m: last[col[m]] / (0.6 * base[col[m]]))
            gap = 1 - 0.6 * base[col[closest]] / last[col[closest]]
            print(f"  {layer:36s} any of {len(members)}: {touch(hits)}   closest {closest}, {gap:.1%} above trigger")


if __name__ == "__main__":
    main()
