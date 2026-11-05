# Forecast register

*Vintage 0.10, 2026-11-05. Horizons: 6 months (2027-04-17), 12 months
(2027-10-17), 24 months (2028-10-17). Rules in
[Methodology](/report/methodology). Probabilities are the lead agent's
estimates after the research notes and a red-team review of vintage
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
  listings for ADRs where named; local currency otherwise), adjusted for
  splits, stock dividends and spin-offs (Meta's one-for-one Class C
  distribution (charter change effective 19 January 2027; payment date not yet set) is treated as a two-for-one
  split: the 16 October baseline is halved from that date), price return. M1 and the layer thresholds are measured from
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
  (29 closes verified; M1, M1a and M1b at 100 on 2026-10-16). On
  2026-11-05 they closed at 82.3, 82.1 and 82.1, so each needs a further
  27% fall to reach 60.

## Demand and revenue

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| D1 | OpenAI's annualised revenue, as reported on its own accounting basis at two dated points, is lower at the later point. Corrections of basis (gross to net) and comparisons with targets do not count | 5% | 10% | 20% |
| D2 | Reported annualised revenue of OpenAI plus Anthropic, each on its own basis (a company- or reporter-stated exit-month run-rate, or the latest publicly disclosed quarterly revenue times four, computed here; basis and date recorded in the observation ledger), with the two observations dated within 45 days of each other, sums to $200B or more. Current readings: OpenAI ~$50B net (end-September exit); Anthropic $67.8B (filed Q3 revenue x4). Projections and targets do not count | 20% | 55% | 72% |
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
| P1 | The Silicon Data H100 rental index (SDH100RT, neocloud reading; $2.82 as of 2026-10-17, published each business day; both this series and OCPI must be archived daily in data/ because Silicon Data keeps no public history and OCPI only a rolling three months): the equal-weighted mean of each complete calendar month's official daily publications is below $1.50/GPU-hour for three consecutive months wholly inside the horizon, with at least 80% of scheduled business-day publications present as fresh prints (no carried-forward, interpolated or disruption-flagged values). If a complete month is unavailable, the Ornn OCPI H100 series substitutes at $1.50 times the median OCPI/SDH100RT ratio over the preceding 90 overlapping days (at least 60 pairs), else void. Rule from the [GPU-pricing note](/research/macro/gpu-pricing-and-utilization). Caution: by October 2028 the H100 is about 5.5 years old, and today's 6.4-year-old A100 already prices at $1.53 on the same index, so a Yes at 24 months is largely an age effect; read it together with P1b | 5% | 15% | 35% |
| P1b | The Ornn OCPI B200 monthly mean (September 2026: $7.245) is below $4.50 for three consecutive complete months inside the horizon, each month with at least 80% fresh calendar-day coverage (no carried-forward or interpolated prints); on 2027-10-17 the 24-month reference rolls to the newest Nvidia datacenter GPU with at least 180 days of OCPI history, its threshold reset to 62% of its 2027-Q3 monthly mean; Silicon Data's B200 index is the fallback, calibrated on at least 60 fresh overlapping days. P1 Yes with P1b No reads as ageing; both Yes reads as glut | 3% | 10% | 20% |
| P2 | TrendForce's DDR5 8GB SO-DIMM contract-price session average ($133 on 2026-08-31), observed at the final assessment of each calendar month, is at or below 70% of its highest calendar-2026 monthly observation in any later month published by the horizon. A fixed-product proxy for conventional DRAM; it excludes HBM. Rule from the [memory note](/research/stack/memory-hbm) | 5% | 20% | 45% |

## Credit and financing

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| F1 | CoreWeave has a distressed credit event (definition above), or an acquisition of the company closes at consideration (cash plus stock at announcement value) below $40 per share split-adjusted. The acquisition branch is not a credit event and does not count toward the headline | 10% | 22% | 35% |
| F2 | Oracle's senior unsecured or issuer rating is below investment grade at any of S&P, Moody's or Fitch (S&P: BBB− stable as of 2026-10-17; Moody's Baa2 negative; Fitch BBB stable). In practice a one-notch S&P question: its triggers are adjusted leverage above 4.5x or no path to positive FOCF by FY2029, and its FY2027 forecast (mid-4x leverage, nearly −$42B FOCF) leaves limited headroom against both; agencies usually move to a negative outlook before cutting, and S&P went to stable only in July | 8% | 24% | 40% |
| F3 | OpenAI, or a counterparty in a filing or release, discloses the cancellation, a deferral of a year or more, or a reduction of a binding compute commitment, where the nominal amount cancelled, deferred or reduced is $10B or more (amendments to one contract aggregate). Supplier-side delivery delays, and slower incremental signings, do not count | 17% | 37% | 57% |
| F3b | The same as F3 for Anthropic (or a counterparty: Amazon, Google, Microsoft, Broadcom, SpaceXAI, a lessor). The S-1/A's $895.4B total identifies the arrangements to watch; inclusion alone does not make a conditional arrangement an effective binding obligation. These questions concern disclosed amendments of $10B+, not insolvency; rigid terms worsen liquidity but make cancellation harder | 12% | 30% | 48% |
| F4 | A GPU-backed loan, datacenter project bond or AI-infrastructure SPV with $1B or more outstanding has a distressed credit event | 13% | 30% | 45% |
| F5 | OpenAI, Anthropic, Mistral, SSI or Thinking Machines closes a priced primary round at a lower fully diluted valuation than its previous priced primary round. IPOs below the last private mark count. (xAI removed: it is inside listed SpaceX, so no private round can occur) | 15% | 27% | 40% |

For F3 and F3b alike, a disclosed exercise of a contractual termination
right over an effective binding commitment of $10B or more counts as a
cancellation. An unexercised option, an unmet commencement condition
without such a commitment, or a supplier-side delivery delay does not.

## Markets

| ID | Question | 6m | 12m | 24m |
|---|---|---|---|---|
| M1a | Sub-basket of the five chip names in M1 (NVDA, AVGO, TSM, AMD, MU), same construction, closes at or below 60 | 21% | 34% | 46% |
| M1b | Sub-basket of the three financing-sensitive names in M1 (ORCL, CRWV, VRT), same construction, closes at or below 60 | 40% | 53% | 63% |
| M1 | An equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT, indexed to 100 at the 2026-10-16 close with daily rebalancing, closes at or below 60 | 24% | 37% | 47% |
| M2 | Nvidia's equity market value (closing price times shares outstanding per the latest 10-K or 10-Q as of that date, split-adjusted) is below $2T on any trading day | 3% | 8% | 18% |
| M3 | The Nasdaq-100 price index (NDX) closes 30% or more below its highest 2026 close recorded before that day (as of 2026-11-05 it is 14.7% below) | 12% | 25% | 38% |

## Layer impairment

Forward events only: a further 40% decline from the 2026-10-16 close for
any one named constituent, or a distressed credit event (definition above)
at any named constituent or on project debt tied to the layer. Already
observed 2026-peak drawdowns are listed for context and do not count.
Caution: "any one constituent" rows in layers with several volatile names
are largely volatility measures: at the origin a no-view bootstrap (realised
volatility, no trend; [public-markets](/research/macro/public-markets))
now gives CRWV alone 79/86/90, MU alone 61/72/81 and any of the three
accelerator names 58/74/85. Several names sit within 3-22% of their
triggers, so the equity rows mostly measure distance to trigger. The
equipment, hyperscaler and neocloud rows are judgements: their full
constituent sets are not in the simulation.

| Layer | Constituents | Closest name on 11-05: fall since 10-16, further fall to trigger | 6m | 12m | 24m |
|---|---|---|---|---|---|
| Equipment | ASML, AMAT, LRCX, KLAC, TEL (8035.T) | LRCX −29.8%, −14.5% | 55% | 68% | 76% |
| Foundry | TSM (Taiwan risk included) | TSM −14.4%, −29.9% | 12% | 25% | 38% |
| Memory | MU, 000660.KS, 005930.KS | MU −25.3%, −19.7% | 60% | 71% | 79% |
| Accelerators | NVDA, AMD, AVGO | AMD −23.5%, −21.6% | 55% | 71% | 81% |
| Hyperscalers | MSFT, GOOGL, AMZN, META | GOOGL −17.0%, −27.7% | 13% | 24% | 35% |
| Oracle | ORCL equity; Oracle corporate or Oracle-tenanted project debt | ORCL −10.2%, −33.2% | 32% | 48% | 60% |
| Neoclouds | CRWV, NBIS, IREN, CIFR, WULF, APLD, CORZ, HUT; their debt | CIFR −38.2%, −2.9% | 90% | 94% | 96% |
| Frontier labs | OpenAI, Anthropic, xAI/SpaceX: a down round (F5 definition) or a reported markdown of 40%+ | n/a | 15% | 30% | 43% |
| Neolabs and applications | SSI, Thinking Machines, Reflection, Periodic, Mistral, Perplexity, Harvey, Glean, Sierra (Cursor removed: acquired by SpaceX on 2026-08-14, before the origin): any down round, shutdown, or sale at a price below the last priced round | n/a | 15% | 35% | 55% |
| Power and datacenter | VRT, GEV, EQIX, DLR equity; any datacenter project bond or loan of $1B+ whose tenant is an AI compute buyer (the F4 universe; this credit side overlaps the Oracle and neocloud rows, since a Jupiter-type loan or a CoreWeave landlord counts in both) | GEV −16.4%, −28.3% | 38% | 54% | 66% |

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
failures), rising with horizon because defaults lag equity falls (WorldCom
filed in July 2002, over two years after the March 2000 peak):

| Horizon | P(M1) | zero | one | two+ | Credit-led unwind (M1 and two+) | Equity-led unwind (M1 and at most one) |
|---|---|---|---|---|---|---|
| 6m | 24% | 0.55 | 0.25 | 0.20 | 5% | 19% |
| 12m | 37% | 0.42 | 0.25 | 0.33 | 12% | 25% |
| 24m | 47% | 0.30 | 0.20 | 0.50 | 23% | 24% |

The equity-led row is the actual 2000 pattern (an equity bust with the
credit failures arriving later or not at all); the credit-led row is the
telecom pattern that ended in the 2002 bankruptcies. Neither covers a slow disappointment without a
basket crash. On 5 November the tree moved toward zero and one failure: the
fall so far has run through equities on a political shock with no credit
event, so an M1 reached from 82 is less likely to arrive with two failures
than one reached from 100. The tree is a judgement, not a measurement.

## What drives the numbers

For the market rows there are two reference runs from the 5 November levels
(`process/baseline.py`: ten-day block bootstrap of daily returns since March
2025, daily rebalancing, 20,000 paths): one with no drift, one with +10% a
year. Our rows sit between them. M3's run fixes the 6 October peak; the rule
allows a higher later peak. The other rows are judgements with evidence on
each side; no baseline is measured for them. Drivers link to the note that
holds the figure, its date and its source. To ask a conditional question,
change a driver and re-judge the row.

| Forecast | Reference (6/12/24m) | Pushes up | Pushes down |
|---|---|---|---|
| M1 24/37/47 | No drift 26/40/52; +10% drift 23/34/44 | Existing restrictions and new proposals against data-centre building: a Texas permit halt since September, moratorium positions of three governors-elect, 40 of 41 local contests ([power](/research/macro/power-and-datacenters)). Funding costs more: Oracle's notes carry 7.0-8.65% coupons, Meta sold preferred and forward equity ([debt-markets](/research/macro/debt-markets)). Payback needs revenue growth of 78-157% a year ([unit economics](/research/theory/ai-unit-economics)) | Demand accelerated: Azure +48%, Google Cloud +103%, AWS +39% ([Microsoft](/research/stack/microsoft), [Alphabet](/research/stack/alphabet), [Amazon](/research/stack/amazon)). Anthropic's filed Q3 revenue was $17.0B ([Anthropic](/research/stack/anthropic)). OCPI B200 rents averaged $8.50 in October against $7.25 in September ([GPU pricing](/research/macro/gpu-pricing-and-utilization)). The 10-year yield fell to 4.84% ([rates](/research/macro/rates-sovereign-geopolitics)) |
| M1a 21/34/46 | No drift 23/38/52; +10% drift 20/32/42 | AMD and Micron are already 23-25% down; about 600,000 H200s reportedly await import approval in Hong Kong (C, [Nvidia](/research/stack/nvidia)) | SK Hynix has over half of 2027-28 capacity under long-term agreements and earned an 80% operating margin in Q3 ([memory](/research/stack/memory-hbm)); AMD guides Q4 revenue to $17B ([AMD](/research/stack/amd-broadcom-custom-silicon)) |
| M1b 40/53/63 | No drift 40/54/64; +10% drift 37/49/58 | CoreWeave's reported CDS at 1,165bp, its 2032 notes as low as 74.75 cents, its shares at $43.66 ([CoreWeave](/research/stack/coreweave)) | Oracle raised its full $20B ([Oracle](/research/stack/oracle)); Vertiv's organic orders grew more than 100% ([power](/research/macro/power-and-datacenters)) |
| F1 10/22/35 | At 1,165bp, flat hazard and 40% recovery: about 9/18/32% risk-neutral, which overstates real-world risk | The 2032 notes' spread touched 1,200bp; a weaker share price makes equity funding more dilutive; June's schedule put $4.4B of principal in H2 2026 and $6.2B in 2027; disclosure controls were ineffective at 30 June ([CoreWeave](/research/stack/coreweave)) | No qualifying event; the first debt-service test on DDTL 3.0 is 31 October 2027; management expects backlog to withstand policy changes; Microsoft did not say which suppliers delivered late. F1 also counts an acquisition below $40, which CDS does not |
| F2 8/24/40 | None | New notes priced 240-335bp over Treasuries, between the BB (206bp) and single-B (363bp) index spreads, though durations and conventions differ; the plan needs about $110B from vendors and customers (inferred, C); FY2026 free cash flow −$23.7B ([Oracle](/research/stack/oracle)) | $10B of new equity, which Moody's reportedly called key to keeping Baa2 (C); the note's liquidity scenario covers FY2027; all three agencies rated the new notes investment grade |
| F3 17/37/57 | None | Funding target reportedly cut from $30B to $20B at a desired $1.25T, first close expected below $20B (C); Microsoft's receivable from OpenAI rose to $7.2B; the February plan needs more funding during 2028 ([OpenAI](/research/stack/openai)) | Amazon completed its $50B investment; net annualised revenue is reportedly about $50B (C); take-or-pay terms are hard to amend |
| F3b 12/30/48 | None | Filed commitments of $895.4B, about 13 times annualised Q3 revenue; $69.8B expected within twelve months of 30 September; $213.8B has termination rights or commencement conditions; enforcement against policy-breaching customers can cut revenue; some rent starts before capacity is usable ([Anthropic](/research/stack/anthropic)) | $131.8B of cash and investments; nine-month operating cash flow of $6.6B, though management expects significant cash use ahead; the $63B structure finances leased equipment, not lab cash; $5.0B of extra short-term compute in Q3 shows a capacity gap then |
| Credit-led 5/12/23 | P(M1) times 0.20/0.33/0.50 | F4 rising; one shared shock can cause separate distressed events at a tenant and its landlord (the same restructuring counts once) | No credit event so far; Oracle, Meta, Microsoft and Alphabet funded in the window |
| Equity-led 19/25/24 | P(M1) times 0.80/0.67/0.50 | As M1 | As M1 |

The other rows, in one line each:

- **D1, D2**: no new OpenAI revenue print. Anthropic's filed Q3 revenue
  times four is $67.8B (our calculation, not a reported run-rate), which
  leaves $132B to reach $200B.
- **D3**: Azure's next-quarter guide is 49-50% in constant currency and
  Amazon projects AWS above 40% in 2027-28; neither rules out a ten-point
  quarterly fall in reported growth, and Google Cloud's hardware sales add
  volatility. Held.
- **C1, C2**: Amazon and Alphabet expect higher 2027 capex and S&P
  forecasts it for Meta. Microsoft's calendar-2026 trim was about 3%, below
  C2's 10%. Restrictions and proposals can affect guidance before they take
  effect.
- **C3, C4, P2**: no new print; Nvidia reports on 17 November, TSMC on 10
  November.
- **P1, P1b**: October monthly means rose, while the B200 eased 2.8% from
  26 October to 4 November. Neither is near three months below threshold.
- **F4**: the $63B Anthropic structure, a conditional $40B SpaceX lease and
  negative outlooks on Meta's project notes widen the exposure; IREN delayed
  its revenue target and $6B of its FY2027 funding depends on markets; IREN,
  HUT and CIFR shares are 32-38% below 16 October. Closed refinancings and
  the absence of any distressed event restrain the near term.
- **F5**: an Anthropic IPO counts if it closes at a comparable fully diluted
  valuation below the $965B Series H mark. A debut in the week of 16
  November is reported, unverified; the filing is unpriced.
- **M2**: distance to trigger (Nvidia needs a further 54%).

**How much is price and how much is view.** The market rows carry no
bearish tilt: they sit between the no-drift and +10%-drift runs. This
corrects the record. The baselines used since 18 October (M1 3/10/16 at the
origin) were too low, because that calculation gave too little weight to
the last ten days of its sample, a sell-off. Re-run correctly, the origin
baseline is 7/18/30, so the original M1 of 10/22/30 was at the no-view
level, not 7-14 points above it as earlier vintages said. The rise since is
almost all distance: the baskets now need 27% instead of 40%.

**Why credit did not rise as much as equity.** Reporting links the sell-off
mainly to policy uncertainty, and Oracle, Meta, Microsoft and Alphabet
arranged financing in the window. That shows selective access, not a
freeze; it does not show that credit was calm on 5 November, for which no
broad spread print exists yet. CoreWeave's marks show stress, and IREN's
after-close results add execution and funding risk.

**What would move the rows next.** CoreWeave's Q3 report on 10 November
(principal paid from operations, any covenant amendment); Nvidia on 17
November; the Anthropic IPO price; Oracle's Q2 offsets in mid-December;
state action on data centres; the calendar-2027 capex guides.

## History

- **Vintage 0.1 (2026-10-17, before review)**: D1 5/10/22; D2 10/45/70;
  D3 15/35/60; C1 7; C2 10/25/45; C3 2/8/30; C4 3/10/30; P1 5/15/35;
  P2 5/20/50; F1 8/20/38; F2 20/40/55; F3 20/40/60; F4 10/25/45;
  F5 10/25/45; M1 (40% below 2026 peak) 25/40/55; M2 3/8/18; M3 12/25/40;
  layers (40% below 2026 peak) equipment 10/20/35, foundry 8/15/30, memory
  10/25/50, accelerators 10/25/40, hyperscalers 5/12/25, Oracle 25/40/55,
  neoclouds 35/50/65, labs 15/30/50, neolabs 25/45/65, power 15/30/45;
  headline (M1 plus two of F1-F5) 15/30/45.
- **Vintage 0.9.1 (2026-10-25)**: M1b raised 20/35/50 to 25/40/55: the
  sub-basket closed at 93.6 on 23 October, a 6.4% move toward the trigger
  that re-marks the row by about 5 points (mark-to-market, no new
  information about the names). All other rows held: Meta's negative Q3
  free cash flow and cash-below-debt position lean the hyperscaler row up
  by 2-3 points, below the revision threshold; Lam's results read as a
  repricing rather than new demand information, so the equipment row holds
  despite the 11-13% fall; CoreWeave and Oracle CDS tightened from their
  15-19 October peaks. A combined revision follows the 28-29 October
  results.
- **Check 2026-10-23 closes (run 2026-10-25)**: nothing resolved. M1 97.0,
  M1a 99.1, M1b 93.6; NDX 7.3% below its 6 October peak. Meta's narrowed
  capex guide does not count under C2. Stock-dividend rule added for Meta's
  Class C.
- **Check 2026-10-21**: no probability changes and nothing resolved; the
  week's facts were stress or proposals, not qualifying events.
- **Vintage 0.9 (2026-10-18)**: no probability changes; P1/P1b coverage
  rules tightened; final consistency sweep applied. Reconciliation: F5
  moved from 10/25/45 (vintage 0.1) to 10/20/35 in vintage 0.2 without its
  numerical outcome being itemised there.
- **Vintage 0.8c (2026-10-18)**: neolab layer lowered 25/45/65 to
  15/35/55 and Cursor removed from its cohort (acquired before the origin),
  "distressed sale" defined; xAI removed from F5 (inside listed SpaceX);
  after the Claude cross-check of the other-labs note.
- **Vintage 0.8b (2026-10-18)**: P1b (current-generation B200 companion
  to P1) added at 3/10/20 after the Claude cross-check of the GPU-pricing
  note; P1 timestamp wording and archive requirement fixed; no other
  changes.
- **Vintages 0.8 and 0.8a (2026-10-18)**: no probability changes.
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
  definition clarified (distinct obligors, shared roots).
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
- **Wording check (2026-11-05)**: every figure on this page was traced to
  the research notes after they were cut to current state. Eight wordings
  were corrected to match the notes (Anthropic's July run-rate, Broadcom
  supply years, the telecom default timing, the Meta distribution date, the
  Anthropic year-end range, two P1 remarks). No probability changed.
- **Vintage 0.10 (2026-11-05)**: the combined revision deferred from 25
  October. Window: Microsoft, Alphabet and Amazon results, Anthropic's
  S-1/A, Oracle's and Meta's financings, the Fed's hold, the 3 November
  midterms and the sell-off of 5 November (Nasdaq-100 −6.4%; M1 from 108.9
  on 28 October to 82.3). Reviewed by Codex gpt-6-astra before publication.
  - Baseline corrected. The 18 October bootstrap under-weighted the final
    days of its sample; re-run, the origin baselines are M1 7/18/30, M1a
    6/15/28, M1b 20/33/46, M3 4/13/29 (published then: 3/10/16, 1/5/10,
    16/27/37, 1/4/11). From 5 November: 26/40/52, 23/38/52, 40/54/64,
    15/32/48 with no drift; 23/34/44, 20/32/42, 37/49/58, 10/20/29 with +10%
    a year. Earlier statements of a 7-14 point bearish tilt are withdrawn.
  - Market rows, set between the two runs: M1 10/22/30 to 24/37/47, M1a
    6/14/25 to 21/34/46, M1b 25/40/55 to 40/53/63, M3 8/16/26 to 12/25/38.
  - Layers, mostly distance to trigger: equipment 15/30/45 to 55/68/76,
    foundry 8/18/32 to 12/25/38, memory 25/40/52 to 60/71/79, accelerators
    20/37/52 to 55/71/81, hyperscalers 8/18/30 to 13/24/35, Oracle 22/38/52
    to 32/48/60, neoclouds 65/78/85 to 90/94/96 (CIFR 2.9% from its
    trigger), power 20/38/52 to 38/54/66. Frontier labs 10/25/40 to
    15/30/43. Equipment, hyperscalers and neoclouds are provisional: their
    constituent sets are not simulated.
  - F1 8/20/35 to 10/22/35: reported credit marks and a weaker share price;
    kept near the CDS-implied path.
  - F3 15/32/52 to 17/37/57: smaller reported funding target, offset by
    Amazon's completed investment.
  - F3b 10/22/38 to 12/30/48: filed payment obligations, contractual exits
    and expected cash use, offset by cash and operating cash flow. Rule
    revision, applied to F3 and F3b alike: exercising a termination right
    over an effective binding commitment of $10B+ counts.
  - F4 10/25/40 to 13/30/45: more vehicles, Meta-project outlooks, IREN.
    F5 10/20/35 to 15/27/40: an IPO price would be set in a weaker market.
  - Conditional tree: 6m 0.45/0.25/0.30 to 0.55/0.25/0.20; 12m
    0.35/0.25/0.40 to 0.42/0.25/0.33; 24m 0.25/0.20/0.55 to 0.30/0.20/0.50
    (judgement). Credit-led 3/9/16 to 5/12/23; equity-led 7/13/14 to
    19/25/24.
  - D2 rule revision: this register may annualise a disclosed quarter for
    either lab. Held: D1, D2, D3, C1-C4, P1, P1b, P2, F2, M2, neolabs.
  - "Reasoning, in brief" replaced by the drivers table.
