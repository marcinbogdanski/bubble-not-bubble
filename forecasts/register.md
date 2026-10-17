# Forecast register

*Vintage 0.6, 2026-10-18. Horizons: 6 months (2027-04-17), 12 months
(2027-10-17), 24 months (2028-10-17). Rules in
[Methodology](/report/methodology). Probabilities are the lead agent's
estimates after the research notes and the
[red-team review](/reviews/2026-10-17-codex-redteam-report) of vintage
0.1, whose numbers are preserved in History. Revisions are appended, never
overwritten. The 24-month numbers carry wide error bars.*

## Resolution rules

- Forecast origin: 2026-10-17 00:00 UTC. An event counts if it occurs after
  the origin and is publicly disclosed by the horizon date (disclosure date
  governs). Source hierarchy: company filings and releases, then Reuters,
  Bloomberg, FT, WSJ, CNBC, The Information. Question-specific rules take
  precedence over these general rules.
- Private-company questions (D1, D2, F3, F5, lab and neolab layers) resolve
  on qualifying public disclosure; if none appears by the horizon the answer
  is No. A later disclosure of an earlier event does not reopen a resolved
  question.
- Price questions use official closing prices on the primary listing (US
  listings for ADRs where named; local currency otherwise), split- and
  spin-adjusted, price return. M1 and the layer thresholds are measured from
  the 2026-10-16 close; M2 is an absolute level; M3 is measured from the
  highest 2026 close before the test day. Corporate actions: a cash
  acquisition fixes that constituent at the deal value from closing; a
  bankruptcy or delisting after a qualifying fall fixes it at the last
  close; a resolved Yes is never voided by a later delisting.
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
| D2 | Reported annualised revenue of OpenAI plus Anthropic, each on its own basis (exit-month run-rate or latest quarter times four, whichever the company or its reporter states; recorded in the observation ledger), with the two observations dated within 45 days of each other, sums to $200B or more. Current readings: OpenAI ~$50B net (end-September exit); Anthropic >$65B gross (July exit) or $67.2B (Q3 sales x4). Projections and targets do not count | 20% | 45% | 65% |
| D3 | Azure, Google Cloud or AWS reports a year-on-year growth rate (reported currency, company's restated segment) at least 10 points below the rate reported the previous quarter | 15% | 35% | 60% |

## Capex and supply

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| C1 | The first calendar-2027 capex guidance midpoints from Alphabet, Amazon and Meta (given with Q4 2026 results, by 2027-03-15), plus Microsoft's stated expectation for calendar 2027 if quantified, sum to less than those companies' calendar-2026 capex on the same basis each company uses. Pure accounting reclassifications are adjusted out; a company that gives no quantified figure is excluded; void if fewer than three companies qualify | 7% | 7% | 7% |
| C2 | Any of Microsoft, Alphabet, Amazon or Meta reduces its current-year capex guidance midpoint by 10% or more versus its prior guidance for the same year, excluding reclassifications | 10% | 25% | 40% |
| C3 | Nvidia reports a year-on-year decline in Data Center segment revenue (company's restated comparable basis) in any quarterly release published by the horizon | 2% | 10% | 30% |
| C4 | TSMC's monthly NT$ revenue release shows year-on-year declines for three consecutive months, all published by the horizon | 3% | 10% | 25% |

## Pricing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| P1 | The Silicon Data H100 rental index (SDH100RT, neocloud reading; $2.82 displayed on access 2026-10-17, no fixing timestamp): the equal-weighted mean of each complete calendar month's official daily publications is below $1.50/GPU-hour for three consecutive months wholly inside the horizon, with at least 80% of scheduled publication days present and no interpolation. If a complete month is unavailable, the Ornn OCPI H100 series substitutes at $1.50 times the median OCPI/SDH100RT ratio over the preceding 90 overlapping days (at least 60 pairs), else void. Rule from the [GPU-pricing note](/research/macro/gpu-pricing-and-utilization) | 5% | 15% | 35% |
| P2 | TrendForce's DDR5 8GB SO-DIMM contract-price session average ($133 on 2026-08-31), observed at the final assessment of each calendar month, is at or below 70% of its highest calendar-2026 monthly observation in any later month published by the horizon. A fixed-product proxy for conventional DRAM; it excludes HBM. Rule from the [memory note](/research/stack/memory-hbm) | 5% | 20% | 45% |

## Credit and financing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| F1 | CoreWeave has a distressed credit event (definition above), or an acquisition of the company closes at consideration (cash plus stock at announcement value) below $40 per share split-adjusted. The acquisition branch is not a credit event and does not count toward the headline | 15% | 25% | 38% |
| F2 | Oracle's senior unsecured or issuer rating is below investment grade at any of S&P, Moody's or Fitch (S&P: BBB− as of 2026-10-17) | 12% | 28% | 42% |
| F3 | OpenAI, or a counterparty in a filing or release, discloses the cancellation, a deferral of a year or more, or a reduction of a binding compute commitment, where the nominal amount cancelled, deferred or reduced is $10B or more (amendments to one contract aggregate). Supplier-side delivery delays, and slower incremental signings, do not count | 15% | 32% | 52% |
| F4 | A GPU-backed loan, datacenter project bond or AI-infrastructure SPV with $1B or more outstanding has a distressed credit event | 10% | 25% | 40% |
| F5 | OpenAI, Anthropic, xAI (or SpaceX in respect of xAI), Mistral, SSI or Thinking Machines closes a priced primary round at a lower fully diluted valuation than its previous priced primary round. IPOs below the last private mark count | 10% | 20% | 35% |

## Markets

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| M1a | Sub-basket of the five chip names in M1 (NVDA, AVGO, TSM, AMD, MU), same construction, closes at or below 60 | 6% | 14% | 25% |
| M1b | Sub-basket of the three credit-sensitive names in M1 (ORCL, CRWV, VRT), same construction, closes at or below 60 | 20% | 35% | 50% |
| M1 | An equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT, indexed to 100 at the 2026-10-16 close with daily rebalancing, closes at or below 60 | 12% | 25% | 38% |
| M2 | Nvidia's equity market value (closing price times shares outstanding per the latest 10-K or 10-Q as of that date, split-adjusted) is below $2T on any trading day | 3% | 8% | 18% |
| M3 | The Nasdaq-100 price index (NDX) closes 30% or more below its highest 2026 close recorded before that day (as of 2026-10-16 it is 6.5% below) | 10% | 20% | 32% |

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
| Power and datacenter | VRT, GEV, EQIX, DLR equity; any datacenter project bond or loan of $1B+ whose tenant is an AI compute buyer (the F4 universe) | VRT −45% | 20% | 38% | 52% |

## Headline

A 2000-style unwind: M1 resolves yes **and** distressed credit events
(definition above; not down rounds, rating actions, deferrals or the F1
acquisition branch) occur at two distinct obligor groups among {CoreWeave
and its SPVs; Oracle corporate; each other listed neocloud with its SPVs;
each project or GPU-backed debt vehicle of $1B+ grouped by sponsor}. One
restructuring counts once. Dealer marks below par are not events. The same
obligor-group list defines the credit perimeter for F4 and the layer rows.
This measures one severe outcome, not every way the boom could disappoint.

| 6m | 12m | 24m |
|---|---|---|
| 6% | 13% | 20% |

Implied probability of two distinct credit failures given the basket event:
50% / 52% / 53%. The scenario tree behind that: multiple compression alone
(no credit failure) is the most likely basket-crash path; one large failure
(CoreWeave or Oracle) next; two or more distinct failures requires the
take-or-pay contracts to fail at more than one counterparty.

## Reasoning, in brief

- Supply-side disclosures still point to more capex in 2027 (ASML capacity
  sold through 2028, Broadcom supply "secured" for FY2027-28, Microsoft and
  Amazon raising guidance), so C1 stays low. The cycle would turn at the
  funding layer first; the credit questions carry the highest numbers.
- CoreWeave's CDS at 1,000-1,195bp maps to roughly 57-63% five-year
  risk-neutral default probability at 40% recovery and flat hazard, or
  28-33% over two years; risk-neutral probabilities overstate real-world
  ones. F1 at 35% also includes a non-distressed sale below $40, so it is
  not a CDS-derived number. Covenant relief in December 2025
  and five-year loans against three-year contracts are the concrete risks.
- Oracle is one notch above junk with FY2026 FCF of −$23.7B, but a stable
  S&P outlook, $20B of equity raised, customer advances and legacy earnings
  argue for a slower path; F2 sits below the vintage-0.1 number.
- D2: the reported targets (OpenAI $70B+ by year-end; an outside
  expectation of $100-110B for Anthropic) sum to roughly $170-180B, not
  $200B, so a Yes needs growth beyond stated targets; at recent growth rates
  that is plausible within 12 months but not implied.
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
- **Vintage 0.6 (2026-10-18)**: no probability changes; market comparison
  added on the front page (Polymarket 6.9%/16.5%, CoreWeave CDS-implied
  path, Goldman capex path); no matched market exists for any question.
- **Vintage 0.5 (2026-10-18, after third red-team)**: F1 raised 10/20/35
  to 15/25/38 (the $40 sale branch needs only a 35% fall from the baseline;
  unsecured market shut); F3 lowered 20/40/60 to 15/32/52 (a binding $10B+
  cut is a specific legal event; operator and funding evidence argues
  against it near term); M1 split into M1a chips and M1b credit-sensitive
  sub-baskets at 6/14/25 and 20/35/50 for transparency about what drives
  M1; D2 basis, C1 coverage, F3 aggregation and the credit perimeter
  defined; headline unchanged.
- **Vintage 0.4 (2026-10-17)**: no probability changes; all 26 notes now
  cross-checked and corrected; baselines frozen in
  `data/forecast-observations.csv` (29 closes verified; the P2 2026 peak
  could not be verified publicly).
- **Vintage 0.3 (2026-10-17, after second red-team)**: headline restricted
  to distressed credit events at distinct obligor groups (down rounds,
  rating actions and the F1 acquisition branch excluded), 8/18/30 to
  6/13/20; power layer widened to the F4 universe and raised 12/25/40 to
  20/38/52; D2 reasoning corrected and 20/50/72 to 20/45/65; general rules
  gained an origin timestamp, disclosure-date convention, private-company
  No-by-default, and corporate-action handling; P1 fallback aligned with the
  GPU-pricing note; F1 acquisition branch labelled; correction: Broadcom
  (−32%) had not crossed the old 40% threshold.
- **Vintage 0.2a (2026-10-17)**: P1 and P2 definitions adopted from the
  GPU-pricing and memory notes; probabilities unchanged.
- **Vintage 0.2 (2026-10-17, after red-team)**: every question rewritten
  with a resolution rule; price questions rebased to the 2026-10-16 close
  because Oracle (−48%), CoreWeave (−56%), SK Hynix (−56%) and Vertiv
  (−45%) had already passed the old 40%-from-peak threshold (Broadcom, at
  −32%, had not);
  F1/F4 restricted to distressed events; headline redefined to two distinct
  obligors; D2 raised, F2 and F5 lowered, M3 lowered, per the review's
  reasoning. Cause: review findings on definitions and already-observed
  drawdowns.
