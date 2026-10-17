# Forecast register

*Vintage 0.2, 2026-10-17. Horizons: 6 months (2027-04-17), 12 months
(2027-10-17), 24 months (2028-10-17). Rules in
[Methodology](/report/methodology). Probabilities are the lead agent's
estimates after the research notes and the
[red-team review](/reviews/2026-10-17-codex-redteam-report) of vintage
0.1, whose numbers are preserved in History. Revisions are appended, never
overwritten. The 24-month numbers carry wide error bars.*

## Resolution rules

- Only information publicly released by the horizon date counts. Source
  hierarchy: company filings and releases, then Reuters, Bloomberg, FT,
  WSJ, CNBC, The Information. Silence is not evidence either way.
- Price questions use official closing prices from the named exchange, split-
  and spin-adjusted, price return. Baselines are the 2026-10-16 close.
- "Distressed credit event" means a missed payment beyond any grace period,
  a distressed exchange or restructuring in which creditors take a
  concession, a bankruptcy filing, or a sale of the company or of the
  collateral under creditor pressure. Ordinary refinancing, amendments
  without concessions and voluntary buybacks do not count.
- A question becomes void if the series or disclosure it depends on ceases
  to exist; this is recorded, not scored.
- Observations and their archived copies go in `data/forecast-observations.csv`
  (to be created at first resolution check).

## Demand and revenue

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| D1 | OpenAI's annualised revenue, as reported on its own accounting basis at two dated points, is lower at the later point. Corrections of basis (gross to net) and comparisons with targets do not count | 5% | 10% | 20% |
| D2 | Contemporaneously reported annualised revenue of OpenAI plus Anthropic, each on its own basis (currently ~$50B net and ~$65-67B gross), sums to $200B or more. Projections and targets do not count | 20% | 50% | 72% |
| D3 | Azure, Google Cloud or AWS reports a year-on-year growth rate (reported currency, company's restated segment) at least 10 points below the rate reported the previous quarter | 15% | 35% | 60% |

## Capex and supply

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| C1 | The first calendar-2027 capex guidance midpoints from Alphabet, Amazon and Meta (given with Q4 2026 results), plus Microsoft's stated expectation for calendar 2027 if quantified, sum to less than those companies' calendar-2026 capex on the same basis each company uses. Pure accounting reclassifications are adjusted out; a company that gives no quantified figure is excluded | 7% | 7% | 7% |
| C2 | Any of Microsoft, Alphabet, Amazon or Meta reduces its current-year capex guidance midpoint by 10% or more versus its prior guidance for the same year, excluding reclassifications | 10% | 25% | 40% |
| C3 | Nvidia reports a year-on-year decline in Data Center segment revenue (company's restated comparable basis) in any quarterly release published by the horizon | 2% | 10% | 30% |
| C4 | TSMC's monthly NT$ revenue release shows year-on-year declines for three consecutive months, all published by the horizon | 3% | 10% | 25% |

## Pricing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| P1 | *Provisional until the GPU-pricing note names the series.* The Silicon Data H100 neo-cloud index (daily, portal.silicondata.com; $2.83 on 2026-10-16) averages below $1.50/GPU-hour for three consecutive calendar months | 5% | 15% | 35% |
| P2 | *Provisional until the memory note names the series.* TrendForce's quarterly conventional server DRAM contract price index falls 30% or more from its 2026 peak | 5% | 20% | 45% |

## Credit and financing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| F1 | CoreWeave has a distressed credit event (definition above) or is acquired for consideration below $40 per share split-adjusted | 10% | 20% | 35% |
| F2 | Oracle's senior unsecured or issuer rating is below investment grade at any of S&P, Moody's or Fitch (S&P: BBB− as of 2026-10-17) | 12% | 28% | 42% |
| F3 | OpenAI, or a counterparty in a filing or release, discloses the cancellation, a deferral of a year or more, or a reduction of a binding compute commitment, where the amount cancelled, deferred or reduced is $10B or more. Supplier-side delivery delays do not count | 20% | 40% | 60% |
| F4 | A GPU-backed loan, datacenter project bond or AI-infrastructure SPV with $1B or more outstanding has a distressed credit event | 10% | 25% | 40% |
| F5 | OpenAI, Anthropic, xAI (or SpaceX in respect of xAI), Mistral, SSI or Thinking Machines closes a priced primary round at a lower fully diluted valuation than its previous priced primary round. IPOs below the last private mark count | 10% | 20% | 35% |

## Markets

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| M1 | An equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT, indexed to 100 at the 2026-10-16 close with daily rebalancing, closes at or below 60 | 12% | 25% | 38% |
| M2 | Nvidia's equity market value (closing price times shares outstanding per the latest 10-Q cover) is below $2T on any trading day | 3% | 8% | 18% |
| M3 | The Nasdaq-100 price index closes 30% or more below its highest 2026 close (as of 2026-10-16 it is 6.5% below) | 10% | 20% | 32% |

## Layer impairment

Forward events only: a further 40% decline from the 2026-10-16 close for
any one named constituent, or a distressed credit event (definition above)
at any named constituent or on project debt tied to the layer. Already
observed 2026-peak drawdowns are listed for context and do not count.

| Layer | Constituents | Observed 2026-peak drawdown to 10-16 | 6m | 12m | 24m |
|---|---|---|---|---|---|
| Equipment | ASML, AMAT, LRCX, KLAC, TEL (8035.T) | moderate | 15% | 30% | 45% |
| Foundry | TSM (Taiwan risk included) | moderate | 8% | 18% | 32% |
| Memory | MU, 000660.KS, 005930.KS | SK Hynix −56% | 12% | 28% | 45% |
| Accelerators | NVDA, AMD, AVGO | AVGO −32% | 15% | 30% | 45% |
| Hyperscalers | MSFT, GOOGL, AMZN, META | small | 8% | 18% | 30% |
| Oracle | ORCL equity; Oracle corporate or Oracle-tenanted project debt | −48% | 15% | 30% | 45% |
| Neoclouds | CRWV, NBIS, IREN, CIFR, WULF, APLD, CORZ, HUT; their debt | CRWV −56% | 40% | 55% | 70% |
| Frontier labs | OpenAI, Anthropic, xAI/SpaceX: a down round (F5 definition) or a reported markdown of 40%+ | n/a | 10% | 25% | 40% |
| Neolabs and applications | SSI, Thinking Machines, Reflection, Periodic, Mistral, Perplexity, Cursor, Harvey, Glean, Sierra: any down round, shutdown or distressed sale | n/a | 25% | 45% | 65% |
| Power and datacenter | VRT, GEV, EQIX, DLR equity; any datacenter project bond or loan of $1B+ | VRT −45% | 12% | 25% | 40% |

## Headline

A 2000-style unwind: M1 resolves yes **and** distressed credit events occur
at two distinct obligors among {CoreWeave, Oracle, any other neocloud, any
$1B+ project or GPU-backed debt, any frontier lab (F5)}. One restructuring
counts once.

| 6m | 12m | 24m |
|---|---|---|
| 8% | 18% | 30% |

## Reasoning, in brief

- Supply-side disclosures still point to more capex in 2027 (ASML capacity
  sold through 2028, Broadcom supply "secured" for FY2027-28, Microsoft and
  Amazon raising guidance), so C1 stays low. The cycle would turn at the
  funding layer first; the credit questions carry the highest numbers.
- CoreWeave's CDS at 1,000-1,195bp maps to roughly 57-64% five-year
  risk-neutral default probability on simple models, about 34% over two
  years at constant hazard; risk-neutral probabilities overstate real-world
  ones, and F1 at 35% is near that path. Covenant relief in December 2025
  and five-year loans against three-year contracts are the concrete risks.
- Oracle is one notch above junk with FY2026 FCF of −$23.7B, but a stable
  S&P outlook, $20B of equity raised, customer advances and legacy earnings
  argue for a slower path; F2 sits below the vintage-0.1 number.
- D2 is higher than in vintage 0.1 because both labs' reported targets
  (OpenAI $70B+ by year-end, Anthropic above $100B) would already sum past
  $200B; those targets are grade C.
- Market questions are driven as much by rates as by AI. The Fed hiked in
  September into 3.7% CPI; the 10-year is above 5% though it fell during the
  week of 10-17 October.

## History

- **Vintage 0.1 (2026-10-17, before review)**: D1 5/10/22; D2 10/45/70;
  D3 15/35/60; C1 7; C2 10/25/45; C3 2/8/30; C4 3/10/30; P1 5/15/35;
  P2 5/20/50; F1 8/20/38; F2 20/40/55; F3 20/40/60; F4 10/25/45;
  F5 10/25/45; M1 (40% below 2026 peak) 25/40/55; M2 3/8/18; M3 12/25/40;
  layers (40% below 2026 peak) equipment 10/20/35, foundry 8/15/30, memory
  10/25/50, accelerators 10/25/40, hyperscalers 5/12/25, Oracle 25/40/55,
  neoclouds 35/50/65, labs 15/30/50, neolabs 25/45/65, power 15/30/45;
  headline (M1 plus two of F1-F5) 15/30/45.
- **Vintage 0.2 (2026-10-17, after red-team)**: every question rewritten
  with a resolution rule; price questions rebased to the 2026-10-16 close
  because Oracle (−48%), CoreWeave (−56%), SK Hynix (−56%), Vertiv (−45%)
  and Broadcom (−32%) had already passed the old 40%-from-peak threshold;
  F1/F4 restricted to distressed events; headline redefined to two distinct
  obligors; D2 raised, F2 and F5 lowered, M3 lowered, per the review's
  reasoning. Cause: review findings on definitions and already-observed
  drawdowns.
