"""No-view baseline for the market forecasts.

    uv run --with numpy python process/baseline.py

Ten-day block bootstrap of demeaned daily log returns (zero drift), 20,000
paths, daily-rebalanced baskets, touch rule as in forecasts/register.md.
Horizons are trading days left to the register's fixed dates. Before a run,
set the current levels below from data/forecast-observations.csv.
"""
import csv, sys, numpy as np
rows = [r for r in csv.reader(l for l in open('data/ai-basket-performance.csv') if not l.startswith('#'))][1:]
px = {}
for d, tk, c in rows: px.setdefault(tk, {})[d] = float(c)
M1 = ['NVDA','AVGO','TSM','ORCL','CRWV','AMD','MU','VRT']; M1a = ['NVDA','AVGO','TSM','AMD','MU']; M1b = ['ORCL','CRWV','VRT']
start, end = '2025-03-28', '2026-11-05'
dates = sorted(d for d in px['NVDA'] if start <= d <= end and all(d in px[t] for t in M1 + ['^NDX']))
names = M1 + ['^NDX']
R = np.array([[np.log(px[t][dates[i]] / px[t][dates[i-1]]) for t in names] for i in range(1, len(dates))])
print('sessions', len(R), dates[0], dates[-1], 'ann vol', {t: round(float(R[:, j].std() * 252 ** .5), 2) for j, t in enumerate(names)})
R = R - R.mean(axis=0)
rng = np.random.default_rng(7); N, B = 20000, 10
H = {'6m': 112, '12m': 238, '24m': 490}; T = max(H.values())
def paths(scale):
    nb = T // B + 1
    starts = rng.integers(0, len(R), size=(N, nb))            # circular blocks: every day equally likely
    idx = ((starts[:, :, None] + np.arange(B)[None, None, :]) % len(R)).reshape(N, -1)[:, :T]
    return R[idx] * scale                                  # N x T x names
def touch(level_paths, barrier):
    hit = np.minimum.accumulate(level_paths, axis=1) <= barrier
    return {k: round(100 * float(hit[:, h - 1].mean()), 1) for k, h in H.items()}
# Three runs: zero drift; zero drift at 1.5x volatility; +10% a year log drift.
for scale, drift in ((1.0, 0.0), (1.5, 0.0), (1.0, 0.10)):
    r = paths(scale) + drift / 252; simple = np.exp(r) - 1
    out = {}
    for label, members, lvl in [('M1', M1, 82.26), ('M1a', M1a, 82.08), ('M1b', M1b, 82.14)]:
        j = [names.index(m) for m in members]
        basket = lvl * np.cumprod(1 + simple[:, :, j].mean(axis=2), axis=1)   # daily rebalanced
        out[label] = touch(basket, 60.0)
    ndx = 26629.81 * np.exp(np.cumsum(r[:, :, names.index('^NDX')], axis=1))
    out['M3'] = touch(ndx, 0.70 * 31224.69)
    single = {}
    for tk in ['CRWV', 'MU', 'ORCL', 'NVDA', 'AMD', 'AVGO', 'TSM', 'VRT']:
        last, base = px[tk][dates[-1]], None
        base = base or px[tk]['2026-10-16']
        lv = last * np.exp(np.cumsum(r[:, :, names.index(tk)], axis=1))
        out[tk + ' -40% from 10-16'] = touch(lv, 0.6 * base); single[tk] = np.minimum.accumulate(lv, axis=1) <= 0.6 * base
    union = single['NVDA'] | single['AMD'] | single['AVGO']
    out['Accelerators: any of NVDA, AMD, AVGO'] = {k: round(100 * float(union[:, h - 1].mean()), 1) for k, h in H.items()}
    print(f'volatility x{scale}, drift {drift:+.0%} a year'); [print('  ', k, v) for k, v in out.items()]
