# Forecast register

*Vintage 0.8b, 2026-10-18. Horizons: 6 months (2027-04-17), 12 months
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
- Private-company questions (D1, D2, F3, F3b, F5, lab and neolab layers) resolve
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
- Baselines and observations are in `data/forecast-observations.csv`
  (29 closes verified; M1, M1a and M1b at 100 on 2026-10-16; M1 is already
  23.8% below its 2026 peak and M1b 43.4%, so the trigger at 60 means about
  −54% and −66% from peak).

## Demand and revenue

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| D1 | OpenAI's annualised revenue, as reported on its own accounting basis at two dated points, is lower at the later point. Corrections of basis (gross to net) and comparisons with targets do not count | 5% | 10% | 20% |
| D2 | Reported annualised revenue of OpenAI plus Anthropic, each on its own basis (exit-month run-rate or latest quarter times four, whichever the company or its reporter states; recorded in the observation ledger), with the two observations dated within 45 days of each other, sums to $200B or more. Current readings: OpenAI ~$50B net (end-September exit); Anthropic >$65B gross (July exit) or $67.2B (Q3 sales x4). Projections and targets do not count | 20% | 55% | 72% |
| D3 | Azure, Google Cloud or AWS reports a year-on-year growth rate (reported currency, company's restated segment) at least 10 points below the rate reported the previous quarter | 30% | 50% | 68% |

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
| P1 | The Silicon Data H100 rental index (SDH100RT, neocloud reading; $2.82 as of 2026-10-17, published each business day; both this series and OCPI must be archived daily in data/ because neither keeps a public history): the equal-weighted mean of each complete calendar month's official daily publications is below $1.50/GPU-hour for three consecutive months wholly inside the horizon, with at least 80% of scheduled publication days present and no interpolation. If a complete month is unavailable, the Ornn OCPI H100 series substitutes at $1.50 times the median OCPI/SDH100RT ratio over the preceding 90 overlapping days (at least 60 pairs), else void. Rule from the [GPU-pricing note](/research/macro/gpu-pricing-and-utilization). Caution: by October 2028 the H100 is about 5.5 years old, and today's 6.4-year-old A100 already prices at $1.53 on the same index in a market with no glut, so a Yes at 24 months is largely an age effect; read it together with P1b | 5% | 15% | 35% |
| P1b | The Ornn OCPI B200 monthly mean (September 2026: $7.245) is below $4.50 for three consecutive complete months inside the horizon; on 2027-10-17 the question rolls to the newest Nvidia GPU with at least 180 days of OCPI history, with Silicon Data's B200 index as fallback. P1 Yes with P1b No reads as ageing; both Yes reads as glut | 3% | 10% | 20% |
| P2 | TrendForce's DDR5 8GB SO-DIMM contract-price session average ($133 on 2026-08-31), observed at the final assessment of each calendar month, is at or below 70% of its highest calendar-2026 monthly observation in any later month published by the horizon. A fixed-product proxy for conventional DRAM; it excludes HBM. Rule from the [memory note](/research/stack/memory-hbm) | 5% | 20% | 45% |

## Credit and financing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| F1 | CoreWeave has a distressed credit event (definition above), or an acquisition of the company closes at consideration (cash plus stock at announcement value) below $40 per share split-adjusted. The acquisition branch is not a credit event and does not count toward the headline | 8% | 20% | 35% |
| F2 | Oracle's senior unsecured or issuer rating is below investment grade at any of S&P, Moody's or Fitch (S&P: BBB− stable as of 2026-10-17; Moody's Baa2 negative; Fitch BBB stable). In practice a one-notch S&P question: its triggers are adjusted leverage above 4.5x or no path to positive FOCF by FY2029, and its FY2027 forecast (mid-4x leverage, nearly −$42B FOCF) leaves limited headroom against both; agencies usually move to a negative outlook before cutting, and S&P went to stable only in July | 8% | 24% | 40% |
| F3 | OpenAI, or a counterparty in a filing or release, discloses the cancellation, a deferral of a year or more, or a reduction of a binding compute commitment, where the nominal amount cancelled, deferred or reduced is $10B or more (amendments to one contract aggregate). Supplier-side delivery delays, and slower incremental signings, do not count | 15% | 32% | 52% |
| F3b | The same as F3 for Anthropic (or a counterparty: Amazon, Google, Broadcom, Microsoft, a lessor). Below F3 because Anthropic's reported operating improvement and $65B Series H (which includes $15B of previously committed supplier funding) give a near-term cushion, while OpenAI's larger reported programme and burn outlook are offset by $122B of committed capital with at least $80B funded by 1 October; both companies' payment schedules and unrestricted cash are unknown, so the gap is judgmental. These questions concern disclosed binding amendments of $10B+, not insolvency; rigidity worsens liquidity but makes cancellation harder | 10% | 22% | 38% |
| F4 | A GPU-backed loan, datacenter project bond or AI-infrastructure SPV with $1B or more outstanding has a distressed credit event | 10% | 25% | 40% |
| F5 | OpenAI, Anthropic, xAI (or SpaceX in respect of xAI), Mistral, SSI or Thinking Machines closes a priced primary round at a lower fully diluted valuation than its previous priced primary round. IPOs below the last private mark count | 10% | 20% | 35% |

## Markets

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| M1a | Sub-basket of the five chip names in M1 (NVDA, AVGO, TSM, AMD, MU), same construction, closes at or below 60 | 6% | 14% | 25% |
| M1b | Sub-basket of the three financing-sensitive names in M1 (ORCL, CRWV, VRT), same construction, closes at or below 60 | 20% | 35% | 50% |
| M1 | An equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT, indexed to 100 at the 2026-10-16 close with daily rebalancing, closes at or below 60 | 10% | 22% | 30% |
| M2 | Nvidia's equity market value (closing price times shares outstanding per the latest 10-K or 10-Q as of that date, split-adjusted) is below $2T on any trading day | 3% | 8% | 18% |
| M3 | The Nasdaq-100 price index (NDX) closes 30% or more below its highest 2026 close recorded before that day (as of 2026-10-16 it is 6.5% below) | 8% | 16% | 26% |

## Layer impairment

Forward events only: a further 40% decline from the 2026-10-16 close for
any one named constituent, or a distressed credit event (definition above)
at any named constituent or on project debt tied to the layer. Already
observed 2026-peak drawdowns are listed for context and do not count.
Caution: "any one constituent" rows in layers with several volatile names
are largely volatility measures; the Claude review's zero-drift bootstrap
(realised volatility, no trend) gives CRWV alone 45/59/69 and MU alone
20/32/42, and the rows below sit near or above those baselines.

| Layer | Constituents | Observed 2026-peak drawdown to 10-16 | 6m | 12m | 24m |
|---|---|---|---|---|---|
| Equipment | ASML, AMAT, LRCX, KLAC, TEL (8035.T) | moderate | 15% | 30% | 45% |
| Foundry | TSM (Taiwan risk included) | moderate | 8% | 18% | 32% |
| Memory | MU, 000660.KS, 005930.KS | SK Hynix −56% | 25% | 40% | 52% |
| Accelerators | NVDA, AMD, AVGO | AVGO −32% | 20% | 37% | 52% |
| Hyperscalers | MSFT, GOOGL, AMZN, META | small | 8% | 18% | 30% |
| Oracle | ORCL equity; Oracle corporate or Oracle-tenanted project debt | −48% | 22% | 38% | 52% |
| Neoclouds | CRWV, NBIS, IREN, CIFR, WULF, APLD, CORZ, HUT; their debt | CRWV −56% | 65% | 78% | 85% |
| Frontier labs | OpenAI, Anthropic, xAI/SpaceX: a down round (F5 definition) or a reported markdown of 40%+ | n/a | 10% | 25% | 40% |
| Neolabs and applications | SSI, Thinking Machines, Reflection, Periodic, Mistral, Perplexity, Cursor, Harvey, Glean, Sierra: any down round, shutdown or distressed sale | n/a | 25% | 45% | 65% |
| Power and datacenter | VRT, GEV, EQIX, DLR equity; any datacenter project bond or loan of $1B+ whose tenant is an AI compute buyer (the F4 universe; this credit side overlaps the Oracle and neocloud rows, since a Jupiter-type loan or a CoreWeave landlord counts in both) | VRT −45% | 20% | 38% | 52% |

## Headlines

Two unwind patterns, both conditional on M1 (the basket falling 40%).
Distressed credit events are as defined above: not down rounds, rating
actions, deferrals or the F1 acquisition branch. Obligor groups: CoreWeave
and its SPVs; Oracle corporate; each other listed neocloud with its SPVs;
each project or GPU-backed debt vehicle of $1B+ grouped by sponsor. One
restructuring counts once; dealer marks below par are not events. The same
list defines the credit perimeter for F4 and the layer rows. "Distinct"
means separate obligors, not independent causes: one OpenAI or CoreWeave
failure can produce two qualifying events (Oracle-tenanted projects, or
CoreWeave's landlords whose notes are repaid from its rent), which is why
the two-or-more conditional is as high as it is.

Conditional tree given M1 (zero / one / two-or-more distinct credit
failures), rising with horizon because defaults lag equity falls (telecom's
came one to two years after the March 2000 peak):

| Horizon | P(M1) | zero | one | two+ | Credit-led unwind (M1 and two+) | Equity-led unwind (M1 and at most one) |
|---|---|---|---|---|---|---|
| 6m | 10% | 0.45 | 0.25 | 0.30 | 3% | 7% |
| 12m | 22% | 0.35 | 0.25 | 0.40 | 9% | 13% |
| 24m | 30% | 0.25 | 0.20 | 0.55 | 16% | 14% |

The equity-led row is the actual 2000 pattern (an equity bust with the
credit failures arriving later or not at all); the credit-led row is the
telecom 2001-02 pattern. Neither covers a slow disappointment without a
basket crash, which is the most likely way the boom under-delivers.

## Reasoning, in brief

- Supply-side disclosures still point to more capex in 2027 (ASML expects
  planned 2027-28 output below customer demand, with 2029-30 interest not
  yet accepted orders; Broadcom supply "secured" for FY2027-28; Microsoft
  and Amazon raising guidance), so C1 stays low.
- Drift: M1, M1a, M1b and M3 sit above a zero-drift bootstrap at realised
  volatility (M1 3/10/16; M3 1/4/11) and near a 1.5x-volatility stress
  (M1 13/21/27). The excess is a deliberate bearish tilt: rates rising into
  an energy shock, secondary unsecured yields above 15% for the weakest
  issuer, and payback arithmetic that needs revenue to keep growing at
  75-150% a year. The cycle would turn at the
  funding layer first; the credit questions carry the highest numbers.
- CoreWeave's CDS at 1,000-1,195bp maps to roughly 57-63% five-year
  risk-neutral default probability at 40% recovery and flat hazard, about
  8-10% at six months and 28-33% over two years; risk-neutral probabilities
  overstate real-world ones. F1 (8/20/35) tracks that path; its sale branch
  adds little at six months because a deal must close, and the DSCR test
  deferred to October 2027, the ATM and the cure rights cushion the near
  term. CoreWeave's own disclosure controls were not effective at 30 June
  2026 (10-Q), which lowers the weight on its management's operating claims. Covenant relief in December 2025
  and five-year loans against three-year contracts are the concrete risks.
- Oracle is one notch above junk with FY2026 FCF of −$23.7B and S&P's own
  FY2027 forecast leaving limited headroom against its downgrade triggers, but a stable outlook three
  months old, $37B of liquidity, no bond deal planned before January 2027
  and a working share-sale channel argue against a cut inside six months.
  The first sign of trouble would be Q2 FY2027 cash advances and
  customer-supplied hardware (mid-December) falling short of the $20-25B of
  annual capex offsets the funding plan assumes; $5-6B a quarter is that
  annual figure's average, not a demonstrated minimum.
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
- **Vintage 0.8b (2026-10-18)**: P1b (current-generation B200 companion
  to P1) added at 3/10/20 after the Claude cross-check of the GPU-pricing
  note; P1 timestamp wording and archive requirement fixed; no other
  changes.
- **Vintage 0.8a (2026-10-18)**: no changes; front page trimmed from
  2,250 to about 1,350 words with all figures and probabilities retained.
- **Vintage 0.8 (2026-10-18)**: no probability changes; closes the first
  Claude-side review round (one report review, five note cross-checks:
  OpenAI, demand side, Oracle, circular financing, debt markets) and the
  consistency sweep.
- **Vintage 0.7f (2026-10-18)**: no probability changes; wording fixes
  from the consistency sweep. Reconciliation: the following current values
  were set in vintage 0.2 without being itemised in its entry: D1 5/10/20
  (from 5/10/22), C2 10/25/40 (from 10/25/45), C3 2/10/30 (from 2/8/30),
  C4 3/10/25 (from 3/10/30), P2 5/20/45 (from 5/20/50), F4 10/25/40 (from
  10/25/45), and the layer rows equipment 15/30/45, foundry 8/18/32,
  hyperscalers 8/18/30, frontier labs 10/25/40 (all rebased from the
  40%-from-peak definitions). Cause at the time: the v0.1 review's
  forecast-by-forecast assessment.
- **Vintage 0.7e (2026-10-18)**: no probability changes; headline
  definition clarified (distinct obligors, shared roots) after the Claude
  cross-check of the circular-financing note.
- **Vintage 0.7d (2026-10-18)**: F2 lowered 12/28/42 to 8/24/40 after the
  Claude cross-check of the Oracle note (S&P triggers and outlook timing;
  Moody's and Fitch two notches above junk); no other changes.
- **Vintage 0.7a (2026-10-18)**: no probability changes; F3b rationale
  added and the private-company rule lists F3b, after the Codex check of
  the Claude review's Anthropic findings.
- **Vintage 0.7 (2026-10-18, after the Claude Opus review)**: headline
  split into credit-led (3/9/16) and equity-led (7/13/14) with a published
  conditional tree rising with horizon; M1 lowered 12/25/38 to 10/22/30 and
  M3 10/20/32 to 8/16/26 with the drift assumption stated; F1 lowered
  15/25/38 to 8/20/35 (sale branch cannot close in six months; CDS path);
  D2 raised 20/45/65 to 20/55/72 and D3 15/35/60 to 30/50/68 (Google Cloud's
  lumpy TPU-sales growth makes a 10-point deceleration easy); single-name
  layer rows recalibrated to the volatility baseline (neoclouds 65/78/85,
  memory 25/40/52, accelerators 20/37/52, Oracle 22/38/52); F3b (Anthropic
  twin of F3) added at 10/22/38; P1 age caveat added. Cause: the review's
  bootstrap and coherence analysis.
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
