# Forecast check, 2026-10-25 (first scoring check against the 16 October baselines)

*Checker: Claude subagent (lead's brief), 2026-10-25. Register vintage 0.9.
Prices: official closes through Friday **23 October 2026**, the last trading
day on or before 24 October (24 October 2026 is a Saturday). Observations
appended to [`data/forecast-observations.csv`](/data/forecast-observations.csv)
with `observation_date` 2026-10-23. No probabilities are changed here; the
lead decides.*

**Result: nothing resolved. Every question is open.** M1 97.02, M1a 99.09,
M1b 93.63 (100 at 16 October). The nearest market trigger is M1b, which
needs a further 35.9% fall. The week's damage came on 22 October, the day
after Meta's Q3 results: semiconductor equipment, GE Vernova, CoreWeave
and the smaller neoclouds fell 10-13%.

## Sources

| Series | Source | Grade |
|---|---|---|
| 20 equities (NVDA AVGO TSM ORCL CRWV AMD MU VRT ASML AMAT LRCX KLAC 8035.T 000660.KS 005930.KS MSFT GOOGL AMZN META NBIS) | Yahoo Finance spark, `https://query1.finance.yahoo.com/v8/finance/spark?symbols=NVDA,AVGO,TSM,ORCL,CRWV,AMD,MU,VRT,ASML,AMAT,LRCX,KLAC,8035.T,000660.KS,005930.KS,MSFT,GOOGL,AMZN,META,NBIS&range=1mo&interval=1d`, accessed 2026-10-25 | secondary, C |
| 9 equities (IREN CIFR WULF APLD CORZ HUT GEV EQIX DLR) | Yahoo Finance spark, `https://query1.finance.yahoo.com/v8/finance/spark?symbols=IREN,CIFR,WULF,APLD,CORZ,HUT,GEV,EQIX,DLR,%5ENDX&range=1mo&interval=1d`, accessed 2026-10-25 | secondary, C |
| NDX | Nasdaq official EOD, POST `https://indexes.nasdaq.com/Index/HistoryData` with `id=NDX&startDate=2026-10-01&endDate=2026-10-24&timeOfDay=EOD`, accessed 2026-10-25. The Yahoo ^NDX values agree to the cent | primary, A |
| CRWV, IREN cross-check | Nasdaq.com `https://api.nasdaq.com/api/quote/{CRWV,IREN}/historical?assetclass=stocks&fromdate=2026-10-15&todate=2026-10-24&limit=20` | secondary, B |
| Meta Q3 2026 | [Meta IR release, 21 Oct 2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) | primary, A |

Checks: the Yahoo 16 October closes equal all 29 frozen baselines exactly,
and the 19-20 October closes equal the rows already in
`data/ai-basket-performance.csv`.

## Index levels

Daily equal-weight rebalance, `I_t = I_prev × mean(P_t / P_prev)`, price
return. No corporate actions in the window.

| Date | M1 (8) | M1a chips (5) | M1b financing (3) | NDX (official) | NDX vs 2026 peak |
|---|---:|---:|---:|---:|---:|
| 16 Oct | 100.0000 | 100.0000 | 100.0000 | 29,187.55 | −6.52% |
| 19 Oct | 101.2729 | 101.9455 | 100.1520 | 29,529.34 | −5.43% |
| 20 Oct | 101.3792 | 101.7852 | 100.6948 | 29,490.28 | −5.55% |
| 21 Oct | 102.9865 | 103.9217 | 101.4292 | 29,822.52 | −4.49% |
| 22 Oct | 96.7763 | 98.1866 | 94.4484 | 28,958.69 | −7.26% |
| 23 Oct | **97.0201** | **99.0949** | **93.6265** | **28,957.53** | **−7.26%** |
| Trigger | ≤ 60 | ≤ 60 | ≤ 60 | ≤ 21,857.28 (0.70 × 31,224.69 peak of 6 Oct) | −30% |
| Further fall to trigger | −38.2% | −39.5% | −35.9% | −24.5% | |

M2: NVDA 210.96 × 24.1B shares (the 10-Q for the quarter ended 26 July is
still the latest filing) is a $5.08T market value. The trigger is a price
below $82.99, a further 60.7% fall.

## Constituent moves since 16 October

The trigger for each layer row is a close at or below 0.60 × the 16 October
close. M1 constituents are scored only through the index. The lowest
close covers 19-23 October.

| Ticker | Used in | Ccy | 16 Oct | 23 Oct | Change | Lowest close 19-23 Oct | Trigger (0.60x) | Further fall to trigger |
|---|---|---|---:|---:|---:|---:|---:|---:|
| NVDA | M1, M1a, accelerators | USD | 214.13 | 210.96 | −1.48% | 210.96 | 128.478 | −39.1% |
| AVGO | M1, M1a, accelerators | USD | 328.75 | 321.68 | −2.15% | 321.68 | 197.250 | −38.7% |
| TSM | M1, M1a, foundry | USD | 412.61 | 418.51 | +1.43% | 412.35 | 247.566 | −40.8% |
| ORCL | M1, M1b, Oracle | USD | 128.23 | 126.16 | −1.61% | 125.54 | 76.938 | −39.0% |
| CRWV | M1, M1b, neoclouds | USD | 61.39 | 54.235 | −11.65% | 54.235 | 36.834 | −32.1% |
| AMD | M1, M1a, accelerators | USD | 528.75 | 516.79 | −2.26% | 507.93 | 317.250 | −38.6% |
| MU | M1, M1a, memory | USD | 878.84 | 877.55 | −0.15% | 856.49 | 527.304 | −39.9% |
| VRT | M1, M1b, power | USD | 206.42 | 194.32 | −5.86% | 194.32 | 123.852 | −36.3% |
| ASML | equipment | USD | 1,641.52 | 1,571.80 | −4.25% | 1,560.54 | 984.912 | −37.3% |
| AMAT | equipment | USD | 409.29 | 377.24 | −7.83% | 375.58 | 245.574 | −34.9% |
| LRCX | equipment | USD | 263.94 | 230.10 | −12.82% | 230.10 | 158.364 | −31.2% |
| KLAC | equipment | USD | 165.74 | 145.61 | −12.15% | 145.61 | 99.444 | −31.7% |
| 8035.T | equipment | JPY | 10,630 | 9,458 | −11.03% | 9,450 | 6,378 | −32.6% |
| 000660.KS | memory | KRW | 1,272,000 | 1,277,000 | +0.39% | 1,223,000 | 763,200 | −40.2% |
| 005930.KS | memory | KRW | 215,500 | 215,500 | 0.00% | 211,500 | 129,300 | −40.0% |
| MSFT | hyperscalers | USD | 529.05 | 524.51 | −0.86% | 521.08 | 317.430 | −39.5% |
| GOOGL | hyperscalers | USD | 340.59 | 320.21 | −5.98% | 320.21 | 204.354 | −36.2% |
| AMZN | hyperscalers | USD | 250.00 | 248.00 | −0.80% | 248.00 | 150.000 | −39.5% |
| META | hyperscalers | USD | 709.33 | 642.62 | −9.40% | 642.62 | 425.598 | −33.8% |
| NBIS | neoclouds | USD | 165.47 | 158.74 | −4.07% | 158.74 | 99.282 | −37.5% |
| IREN | neoclouds | USD | 26.99 | 24.905 | −7.73% | 24.905 | 16.194 | −35.0% |
| CIFR | neoclouds | USD | 8.98 | 7.94 | −11.58% | 7.94 | 5.388 | −32.1% |
| WULF | neoclouds | USD | 11.68 | 11.32 | −3.08% | 11.32 | 7.008 | −38.1% |
| APLD | neoclouds | USD | 18.05 | 18.25 | +1.11% | 18.25 | 10.830 | −40.7% |
| CORZ | neoclouds | USD | 13.48 | 13.10 | −2.82% | 13.10 | 8.088 | −38.3% |
| HUT | neoclouds | USD | 67.75 | 61.23 | −9.62% | 61.23 | 40.650 | −33.6% |
| GEV | power | USD | 921.20 | 815.00 | −11.53% | 815.00 | 552.720 | −32.2% |
| EQIX | power | USD | 985.98 | 955.03 | −3.14% | 952.62 | 591.588 | −38.1% |
| DLR | power | USD | 175.97 | 172.37 | −2.05% | 170.94 | 105.582 | −38.7% |

The full daily path for every name is in the `note` field of its
observation row in the CSV.

## Question status

"Not located" means that no qualifying event appears in the repo signals
through 21 October or in the 25 October Grok scan
(`tasks/grok/2026-10-25-scan.md`, which is unverified leads). Within the
12-fetch budget I did not verify independently that such events are absent.

| ID | Status | Evidence |
|---|---|---|
| D1 | Open | No new OpenAI-basis revenue disclosure at two points. |
| D2 | Open | The latest readings (OpenAI ~$50B, Anthropic ~$65-67B) sum to about $117B, against a $200B threshold. A leaked Anthropic S-1 (Grok lead) is not a qualifying public disclosure until it is filed. |
| D3 | Open | No cloud segment reported in the window. Microsoft and Alphabet report on 28 Oct, Amazon on 29 Oct. |
| C1 | Open | It resolves on Q4 guidance, due by 2027-03-15. Meta's Q3 release gives no 2027 capex figure; it says only that revenue growth will stay strong "throughout 2027" and that Reality Labs losses will narrow to about $15B. I did not check the call transcript. |
| C2 | Open, and Meta moved the other way | Meta narrowed its 2026 capex range to **$135-145B from $130-145B**, so the midpoint rose from $137.5B to $140B (+1.8%). Only a cut of 10% or more counts. Q3 capex was $34.91B. MSFT, GOOGL and AMZN report 28-29 Oct. |
| C3 | Open | Nvidia's next release (Q3 FY2027) is due in late November. |
| C4 | Open | TSMC's October revenue is due around 10 Nov. No monthly release in the window. |
| P1 | Open | The first complete month inside the horizon is November. Archiving is not running (see caveats). The last OCPI H100 print in the repo is $3.12 (20 Oct). |
| P1b | Open | OCPI B200 printed $8.41-8.83 on 18-20 Oct, against a $4.50 threshold. |
| P2 | Open | No new public TrendForce assessment was checked. The 2026 peak is still unverified. |
| F1 | Open | No distressed event. CRWV fell 11.7% for the week. Leads (unverified): 5y CDS ~1,145bp and unsecured yields ~15-16%, within the range the register already uses. The cure window ends 28 Oct. |
| F2 | Open | No S&P, Moody's or Fitch action on Oracle located. ORCL −1.6%. |
| F3 | Open | No disclosed cancellation, deferral or reduction of $10B+ located. |
| F3b | Open | Same as F3. |
| F4 | Open | No distressed event located. A lead (IFR, 23 Oct) reports that datacenter IPOs were pulled and financing froze. That is stress, not an event. |
| F5 | Open | Nothing closed. Leads, unverified: OpenAI's round at $1.25T pre-money would be an *up* round on its last $852B, and Anthropic's IPO talk "under $1.5T" sits above its $965B Series H post-money. Neither is a down round on the reported terms. |
| M1 | Open | 97.02, with a low of 96.78 on 22 Oct. Trigger ≤ 60. |
| M1a | Open | 99.09, with a low of 98.19. |
| M1b | Open | 93.63, the low of the window. |
| M2 | Open | $5.08T. The trigger is below $2T. |
| M3 | Open | NDX is 7.26% below the 6 Oct peak, against a 30% trigger. The reference peak is unchanged. |
| Equipment | Open | Worst names: LRCX −12.8%, KLAC −12.2%, TEL −11.0%. All are at least 31% above the trigger. |
| Foundry | Open | TSM +1.4%. |
| Memory | Open | MU −0.2%, SK hynix +0.4%, Samsung 0.0%. |
| Accelerators | Open | NVDA −1.5%, AVGO −2.2%, AMD −2.3%. |
| Hyperscalers | Open | META −9.4% after its results, GOOGL −6.0%. |
| Oracle | Open | ORCL −1.6%. No credit event at Oracle or on Oracle-tenanted debt located. |
| Neoclouds | Open | CRWV −11.7%, CIFR −11.6%, HUT −9.6%, IREN −7.7%. None is within 32% of its trigger. No credit event located. Lead (unverified): Nebius signed a $3.5B 364-day Citi facility, which is ordinary financing. |
| Frontier labs | Open | No down round or 40% markdown (see F5). |
| Neolabs and applications | Open | No down round, shutdown or below-mark sale located. |
| Power and datacenter | Open | GEV −11.5%, VRT −5.9%. No $1B+ project-debt event located. |
| Headline, credit-led | Open | Conditional on M1, which is open. No distinct-obligor credit failures. |
| Headline, equity-led | Open | Conditional on M1, which is open. |

## Candidates for a probability revision (the 5-point rule)

Method, for transparency: each row's own register probability is treated
as a zero-drift barrier probability to set an implied volatility. The
starting distance is then moved from 0.60 to the 23 October distance. For
layer rows I give two versions: one using the average constituent distance
(the lower bound) and one using the closest name (the upper bound). This is
a mechanical mark-to-market. It is not fresh fundamental evidence, and a
one-week drop partly realises the bearish tilt the register already holds.

| Row | Register 6/12/24m | Mechanical re-mark | Suggested direction | Reason |
|---|---|---|---|---|
| **Equipment layer** | 15/30/45 | 25-29 / 41-45 / 55-58 | **Up, the largest move** | Three of five names fell 11-13% in one session (22 Oct), after Lam's September-quarter results (Grok lead: China and WFE commentary). Each now needs only a 31-33% fall. Read the Lam and KLA releases before revising. |
| **Power and datacenter** | 20/38/52 | 26-33 / 44-50 / 57-62 | **Up** | GEV −11.5% (needs −32%) and VRT −5.9%. The credit side (pulled datacenter IPOs, frozen financing; IFR lead) points the same way but is not an event. |
| **M1b** | 20/35/50 | 26 / 42 / 56 | **Up, about +5** | The index is down 6.4%, driven by CRWV (−11.7%) and VRT. Of the three indices this is the only one past the 5-point line. |
| **Neoclouds** | 65/78/85 | 69-73 / 81-83 / 87-89 | **Up, +4 to +8 at 6m** | CRWV, CIFR and HUT are each about 10-12% lower. Neocloud credit spreads are wide but still inside the range the register uses. Check after CoreWeave's cure window closes on 28 Oct. |
| Hyperscalers | 8/18/30 | 11-16 / 22-28 / 34-40 | Up, borderline (+3 to +8) | META −9.4% on negative FCF and a higher capex floor. Settle the META Class C adjustment rule (caveat 4) first. |
| M1 | 10/22/30 | 12 / 25 / 33 | Hold (+2-3) | Below the threshold. |
| M1a, M2, M3, foundry, memory, accelerators, Oracle | – | each within 2 points | Hold | Small moves. |
| C2 | 10/25/40 | – | Hold, or slightly down at 6m | Meta's guidance moved up, not down. The other three report next week, which is the real test. |
| F5 | 10/20/35 | – | Hold (watch) | If OpenAI's round closes at $1.25T pre-money and Anthropic prices its IPO above $965B, the 6m down-round path narrows. Both are unverified talks. |

Earnings on 28-29 Oct (MSFT, GOOGL, AMZN) and the FOMC on 27-28 Oct will
move D3, C2 and the hyperscaler row more than anything in this week's data
did. The lead may prefer to make one combined revision after 29 Oct.

## Data-quality caveats

1. **Date.** The brief said "Friday 24 October". In 2026, 24 October is a
   Saturday, so the observation date is Friday 23 October. The Tokyo and
   Seoul closes for 23 October are local sessions that ended before the US
   open.
2. **Grade.** The equity closes come from Yahoo (secondary, grade C, as in
   the existing basket CSV), not from exchange pages. They matched all 29
   frozen baselines and the existing 19-20 October rows exactly. NDX comes
   from Nasdaq's official EOD. Yahoo's API refused direct `curl` requests
   (HTTP 429), so I read it through a browser.
3. **Sub-penny closes.** CRWV (54.235) and IREN (24.905) show three-decimal
   23 October "Close/Last" values on both Yahoo and Nasdaq.com, with lower
   volume than earlier days. These may be last sales rather than
   closing-cross prints. That does not matter for any trigger, but re-pull
   them before using them for scoring.
4. **META corporate action.** Meta has declared a one-time stock dividend
   of one Class C share per Class A or B share. It depends on a charter
   amendment effective 19 January 2027. That is in effect a 2-for-1
   distribution inside the horizon. The register's "split- and
   spin-adjusted" rule needs a stated method before then: either scale
   the META history (and the 425.598 trigger) by the ex-date
   price-adjustment factor, or track META plus META Class C combined.
   Otherwise the hyperscaler row could trigger mechanically in January.
5. **P1/P1b archiving.** `scripts/archive-gpu-prices.sh` does not exist.
   `data/gpu-index-daily.csv` has no Silicon Data print since the 17
   October baseline, and its last OCPI row is 20 October. November is the
   first scoreable month. If daily SDH100RT archiving does not start by 1
   November, P1 November will fall back to the OCPI substitute or go void.
6. **M2 shares.** The figure still uses 24.1B shares from the 10-Q filed in
   August. Update it when Nvidia files its Q3 FY2027 10-Q (late November).
7. **Absence checks.** "Not located" statuses for the credit, rating and
   private-round questions rest on the repo signals through 21 October and
   an unverified Grok scan. A signals entry for 22-25 October would close
   that gap.
8. **CSV format.** The observation rows add five columns
   (`observation_date, observation_close, change_from_baseline_pct,
   trigger_level, distance_to_trigger_pct`) to the header. The 46 baseline
   rows are byte-identical and keep 10 fields, so the file is ragged:
   pandas and DictReader read it, and the missing fields come back empty.
