# Forecast register

*Forecast date: 2026-10-17 · Horizons: 6 months (2027-04-17), 12 months
(2027-10-17), 24 months (2028-10-17) · Rules in
[Methodology](/report/methodology). Probabilities are the lead agent's
estimates after reading the research notes; each revision will be appended
to the History section with its cause. The 24-month numbers carry wide error
bars and should be read as "more likely than not" or "less likely than not"
rather than as precise.*

## How to read this

Each question resolves yes or no by the horizon date from the stated source.
"Reported" means a report by Reuters, Bloomberg, FT, WSJ, CNBC or The
Information, or a company statement. Probabilities are cumulative: the
12-month number includes the 6-month one.

## Demand and revenue

| ID | Question | Resolves by | 6m | 12m | 24m |
|---|---|---|---|---|---|
| D1 | OpenAI's reported annualised revenue is lower than the prior reported figure at any point (a reported decline in run-rate) | Reported figure | 5% | 10% | 22% |
| D2 | Combined reported annualised revenue of OpenAI and Anthropic reaches $200B (on each company's own basis; currently ~$50B net and ~$65-74B gross) | Reported figures | 10% | 45% | 70% |
| D3 | Microsoft Azure, Google Cloud or AWS reports year-on-year growth more than 10 points below its prior-quarter growth in any quarter | 10-Q / earnings release | 15% | 35% | 60% |

## Capex and supply

| ID | Question | Resolves by | 6m | 12m | 24m |
|---|---|---|---|---|---|
| C1 | The first 2027 capex guidance from Microsoft, Alphabet, Amazon and Meta combined (given with Q4 2026 results, Jan-Feb 2027) is below their 2026 actual capex | Earnings calls | 7% | 7% | 7% |
| C2 | Any of the four cuts its current-year capex guidance by 10% or more in a quarterly report | Earnings release / call | 10% | 25% | 45% |
| C3 | Nvidia reports a year-on-year decline in data-center revenue in any quarter | 10-Q / release | 2% | 8% | 30% |
| C4 | TSMC reports year-on-year declines in monthly revenue for three consecutive months | TSMC monthly release | 3% | 10% | 30% |

## Pricing

| ID | Question | Resolves by | 6m | 12m | 24m |
|---|---|---|---|---|---|
| P1 | The Silicon Data H100 neo-cloud index (or successor named in the GPU-pricing note) averages below $1.50/GPU-hour for three consecutive months (was $2.83 on 2026-10-16) | Index | 5% | 15% | 35% |
| P2 | Contract DRAM prices (TrendForce) fall 30% or more from their 2026 peak | TrendForce | 5% | 20% | 50% |

## Credit and financing

| ID | Question | Resolves by | 6m | 12m | 24m |
|---|---|---|---|---|---|
| F1 | CoreWeave misses an interest or principal payment, restructures or exchanges any debt, or agrees to be acquired below its $40 IPO price | 8-K / reported | 8% | 20% | 38% |
| F2 | Oracle's senior unsecured rating is cut below investment grade by any of S&P, Moody's or Fitch (S&P is at BBB−) | Rating action | 20% | 40% | 55% |
| F3 | OpenAI, or a counterparty's filing, discloses the cancellation, deferral of a year or more, or reduction of a compute commitment of $10B or more | Reported / filing | 20% | 40% | 60% |
| F4 | A GPU-backed loan, datacenter project bond or AI-infrastructure SPV of $1B or more defaults or is restructured | Reported / filing | 10% | 25% | 45% |
| F5 | A frontier lab (OpenAI, Anthropic, xAI, Mistral, SSI, Thinking Machines) raises a priced round at a lower valuation than its previous one | Reported | 10% | 25% | 45% |

## Markets

| ID | Question | Resolves by | 6m | 12m | 24m |
|---|---|---|---|---|---|
| M1 | An equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT closes 40% or more below its 2026 peak (basket defined in data/ai-basket-performance.csv once the public-markets note lands) | Closing prices | 25% | 40% | 55% |
| M2 | Nvidia's market capitalisation closes below $2T (from $5.2T) | Closing price | 3% | 8% | 18% |
| M3 | The Nasdaq-100 closes 30% or more below its 2026 peak | Closing price | 12% | 25% | 40% |

## Layer impairment summaries

Probability that capital deployed in the layer is materially impaired within
the horizon: a 40%+ equity drawdown from the 2026 peak for the layer's main
listed names, or a loss to creditors, or (for private companies) a valuation
markdown of 40%+ or a down round.

| Layer | 6m | 12m | 24m | Main driver |
|---|---|---|---|---|
| Equipment (ASML etc.) | 10% | 20% | 35% | Order cancellations if hyperscaler capex slows; valuation at ~42x |
| Foundry (TSMC) | 8% | 15% | 30% | Utilisation of N2/CoWoS; Taiwan tail separately |
| Memory (HBM) | 10% | 25% | 50% | Cyclicality; 2027 capacity arriving together |
| Accelerators (Nvidia, AMD, Broadcom) | 10% | 25% | 40% | Lab and neocloud funding; margin compression; guarantees |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | 5% | 12% | 25% | Depreciation and lease costs reaching earnings; OpenAI exposure at Microsoft |
| Oracle | 25% | 40% | 55% | Negative FCF, OpenAI concentration, rating one notch above junk |
| Neoclouds (CoreWeave and others) | 35% | 50% | 65% | Refinancing at distressed yields; 2027-29 contract renewals |
| Frontier labs (OpenAI, Anthropic, xAI) | 15% | 30% | 50% | Commitments vs revenue; dependence on supplier and sovereign capital |
| Neolabs and applications | 25% | 45% | 65% | Funding winter; thin margins |
| Power and datacenter real estate | 15% | 30% | 45% | Single-tenant project bonds already below par; tenant deferrals |

## Headline

Probability of a 2000-style unwind, defined as M1 (basket −40%) together
with at least two of F1-F5 occurring:

| 6m | 12m | 24m |
|---|---|---|
| 15% | 30% | 45% |

## Reasoning, in brief

- The capex side is still accelerating on every primary disclosure (ASML
  capacity sold out to 2028, Broadcom supply "secured" for FY2027-28,
  Microsoft and Amazon raising guidance), so a 2027 capex cut (C1) is
  unlikely. The cycle turns at the funding layer first, which is why the
  credit questions carry the highest probabilities.
- CoreWeave's CDS implies roughly a 64% five-year default probability on a
  standard model; F1 at 38% over two years is somewhat below the
  market-implied path because contracted cash flows cover interest 2.4x and
  the secured loans amortise from specific contracts. The risk is
  refinancing, not coverage.
- Oracle is one notch from junk with FCF of −$24B a year and a backlog
  dominated by a customer whose revenue is a tenth of its commitments; F2 is
  the most likely single event in the register.
- The labs are growing fast enough that a revenue decline (D1) is unlikely
  within a year; a down round (F5) is more likely to come from xAI or a
  neolab than from OpenAI or Anthropic.
- Market questions are driven as much by rates as by AI: the Fed is hiking
  into 3.7% inflation with the 10-year above 5%, which is the Dalio "pin",
  and CAPE at 40.6 leaves little cushion.

## History

- 2026-10-17: initial estimates, lead agent (Claude Fable 5.1), before
  external review. Open items: GPU-pricing, memory, Alphabet, power,
  public-markets and rates notes still pending; red-team review pending.
