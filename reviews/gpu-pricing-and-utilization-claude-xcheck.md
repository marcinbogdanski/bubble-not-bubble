# Claude cross-check: GPU pricing, utilization and residual value

*Review date: 2026-10-18. Reviewer: Claude (Anthropic), fresh context, first second-vendor review of a Codex-written note already corrected once after a Codex cross-check. 15 fetches, all accessed 2026-10-18. Scope: [the note](/research/macro/gpu-pricing-and-utilization), [data/gpu-rental-prices.csv](/data/gpu-rental-prices.csv), the figures the front page, stack page, theory page and register take from it, and the P1 forecast. No other file was edited.*

## Verdict

The note's numbers hold: all 12 re-verified rows match at their stated dates. Every derived figure in Analysis recomputes, and the CSV's 364 OCPI rows reproduce the published monthly means.
Both Codex passes missed three things. OCPI's H200 level is an outlier: it sits above CoreWeave's own on-demand list price and runs 81% above Silicon Data. The note shows CoreWeave's 59% adjusted EBITDA margin but not its −2% GAAP operating margin, nor depreciation at 54% of revenue. And P1 is mostly a test of the H100's age: today's A100, at 6.4 years, already prices at P1's $1.50 threshold on Silicon Data's own index.
Two pages have gone stale. The stack page still says "connected clusters are scarce", wording the note withdrew. The theory page says the $1.84 A100 figure "could not be reproduced"; it now reproduces. P1 needs a resolvability fix, because neither index keeps a public history beyond 90 days. It also needs a current-generation companion question.

## Claim re-verification

Units are USD/GPU-hour unless stated. "Match" means the source reproduces at the note's stated date.

| Claim # | Note's value | My value (2026-10-18 access) | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | Silicon Data H100 $2.82, H200 $3.51, B200 $6.12, B300 $7.01, A100 $1.53; weekly +6.4/+6.0/+7.0/+0.9/−3.2%; "no settlement stamp" | Same values and weekly changes. **The dedicated SDH100RT page is dated "As of Oct 17, 2026"** and says the index is "published every business day". The portal offers "90-day historical pricing", portal-only. The FAQ on the same page has a stale, undated "$2.53". | [Silicon index](https://www.silicondata.com/products/silicon-index), [SDH100RT page](https://www.silicondata.com/products/silicon-index/h100) | Values yes. The freshness caveat is now wrong for H100. | A (H100 print dated); C for other GPUs on the summary panel |
| 3 | OCPI Oct 16: H100 $2.74, H200 $6.34, B200 $8.12, A100 $0.94 | Same. Oct 17: $2.78 / $6.39 / $8.48 / $0.97. The API labels history `"access":"public-3mo"`, a rolling 92 days (2026-07-18 to 2026-10-17). | Ornn index-history APIs ([H100](https://data.ornn.com/api/public-index/gpu/H100%20SXM/index-history), [B200](https://data.ornn.com/api/public-index/gpu/B200/index-history), H200, A100 SXM4) | Yes | A prints; C representativeness. **H200 level D**: see Omission 1 |
| 4 | H100 $3.21 → $3.13 → $2.74; day −12.5%, week −1.8%, month +4.6% | Same. The 30-day change flips from +4.6% (Oct 16) to −2.5% (Oct 17) on a one-day shift of base date. The daily log-return SD over 92 days is 4.6%. | H100 API | Yes | A prices; B changes |
| 5 | Monthly means: H100 Sep $2.8293 vs Oct-to-16 $2.8306; H200 $4.8803/$5.7475; B200 $7.2450/$7.6925; A100 $0.9997/$0.9269 | All reproduce, from both the API and the CSV. Oct 1–17: H100 $2.8276, H200 $5.7853, B200 $7.7388, A100 $0.9294. | APIs; CSV | Yes | B |
| 9 | CoreWeave NA per GPU: H100 $6.155/$2.46375, H200 $6.305/$2.61625, B200 $8.60/$4.26375, B300 spot $4.48, A100 $2.70/$1.20625 | Node prices unchanged ($49.24/$19.71, $50.44/$20.93, $68.80/$34.11, $35.84, $21.60/$9.65). The note omits the **GB200 NVL72 4-GPU instance at $42.00 on-demand, i.e. $10.50/GPU-hour**. | [CoreWeave pricing](https://www.coreweave.com/pricing) | Yes | A quotes; B division |
| 16/49 | SemiAnalysis 1-year H100: $1.45–1.95 (Oct 2025) → $2.00–2.70 (Mar 2026) → $2.10–2.70 (Apr); 25% prepay | Ranges reproduce. The note omits the publisher's **composite**, which was flat at $2.80–2.84 from Oct 2025 to Mar 2026 (Jul 2025 $2.79), down from $6.62 in 2H 2023. A middle-term column reads "Sold Out" for Feb–Apr 2026. The text-extracted table lost its column alignment, so the term mapping is uncertain. | [SemiAnalysis dashboard](https://gpu-index.semianalysis.com/) | Yes, but the context is incomplete | C |
| 18 | CoreWeave Q2: adjusted EBITDA margin 59%, net loss $626m | Same ($1,510m / $2,575m = 58.6%). The same exhibit shows a **GAAP operating loss of $49m (−2%)**, **D&A of $1,393m (54.1% of revenue)**, net interest of $640m, and adjusted operating income of $128m (5%). | [Q2 exhibit, SEC](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm) | Yes | A |
| 20 | 3–6-month contracts at ~$40m/MW-year, Sep 17 | Same, "annualized revenue divided by power required to service the related clusters". **No GPU generation is named.** The release adds >$25bn of net new commitments and contracted power rising from 3.7 to 4.2 GW. | [CoreWeave Sep 17 release](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx) | Yes | A |
| 26 | Prior A100 median $1.84 not reproduced; fetched $1.79 (page dated Oct 2, 48 providers) | **Both URLs** (`/gpus/nvidia-a100` and `/reference/cloud-gpu/nvidia-a100`) now show **$1.84 on-demand median, "As of October 18, 2026", 47 providers (40 with priced on-demand configs)**. Spot median is $1.19 and reserved $1.67. The median pools 40GB/80GB and PCIe/SXM. | [GetDeploying](https://getdeploying.com/gpus/nvidia-a100), [alt URL](https://getdeploying.com/reference/cloud-gpu/nvidia-a100) | The discrepancy is explained: a daily-updated page caught on different dates, not an error. | C (mixed-variant listing median) |
| 41 | Nebius Oct posted: H100 $4.50, H200 $5.40, B200 $8.50, B300 $9.50; preemptible from $0.79/$0.99 | Same current levels. Old columns and the "effective Oct 1" text are not visible, as Codex found. The page also says "up to 35% less" for multi-month reservations. | [Nebius prices](https://nebius.com/prices) | Yes for current levels | A levels; B historical change |
| 38/40 | P1 rule: SDH100RT complete-month equal-weight mean < $1.50 for 3 months, ≥80% of scheduled publication days, OCPI fallback with 90-day overlap | The rule's inputs exist, but **neither series has a public archive**. SDH100RT history is portal-only (90 days, paid; trial 7 days). OCPI public history is a rolling three months. "Scheduled publication days" means business days for Silicon Data and calendar days for OCPI (31 August observations). | Silicon pages above; Ornn API `access` field | The rule is well formed but **not resolvable retrospectively** from public sources | D (rule design) |
| Theory page / ai-unit-economics row 24 | GB200 NVL72 $0.19 vs H100 $0.42 per 1M tokens, MiniMax M2.7, "FP8" | Same at **91 tok/s/user** (2,725.1 vs 771.8 tok/s/chip). At 50 tok/s/user the costs are $0.060 vs $0.192 (3.2×). Cost tier: "Owning at Large Hyperscaler Volume", **TCO $1.86 vs $1.17 per chip-hour**, from a July 2026 pricing survey. Values are "interpolated from real benchmark data". **The config panel shows FP4 while the summary says fp8**, and no software version or run date is given. | [InferenceX compare](https://inferencex.semianalysis.com/compare/minimax-m27-gb200-vs-h100) | Yes for the figures; the precision label is unresolved | A published measurements; C cost economics |

## Arithmetic checks

Every derived figure in the note recomputes:

- The CoreWeave proxy: 2.575 × 4 / 1,500 = $6.867m/MW-year, which gives $0.9994/H100-hour at 1.275 kW.
- The Nebius B200 illustration: $4.081–5.101/hour at 1.7875 kW.
- The CoreWeave node divisions: all nine reproduce.
- The B200 spot discount: 50.4%.
- The OCPI daily changes: −12.46%, −1.79% and +4.58%.
- The SemiAnalysis rise: 2.35 / 1.70 = +38.2%.
- The register baseline: 2.83 / 1.86 = +52.2%.
- IREN: 9.7 / 5 / 200 = $9.7m/MW-year.
- Nebius increases: 4.50 / 3.85 = +16.9%, 5.40 / 4.50 = +20.0%, 8.50 / 7.15 = +18.9%, 9.50 / 7.85 = +21.0%.
- Convertible: 3.6445 − 0.4988 = 3.1457bn.
- SF Compute: 0.063 × 60 = 3.78.
- CSV records: 4,495 lines − 3 comment lines − 1 header = 4,491.

The checks below are new derivations in this review. They affect interpretation, not the note's arithmetic.

| Calculation | Result | Use |
|---|---|---|
| P1 distance | 1.50 / 2.82 − 1 = **−46.8%** needed on SDH100RT | Scale of the move P1 needs |
| Front-page "B200 +15% in 30 days" | 8.12 / 7.03 (Sep 16) − 1 = +15.5%. But B200 was **$8.14 on Sep 29**, so Oct 16 ≈ Sep 29 (−0.2%). The trough was $7.33 on Oct 12, and Oct 17 is $8.48 (+19.4% on 30 days). Monthly means: Aug $6.14 → Sep $7.25 (+18.0%) → Oct-to-17 $7.74 (+6.8%). | The 30-day figure depends heavily on the chosen endpoint. The monthly means are the robust statement of the B200 firming. |
| OCPI / Silicon Data on the same dates | H100 0.97; A100 0.61; B200 1.33; **H200 1.81** | The indices agree on H100 only. The P1 fallback ratio is GPU-specific and could drift down as H100 ages, as the A100's 0.61 suggests. |
| H200 / H100 price ratio | OCPI **2.31**; Silicon 1.24; CoreWeave list 1.02; Nebius 1.20; Hyperstack 1.25 | OCPI's H200 is an outlier against every other source |
| OCPI transaction / CoreWeave on-demand list | B200 0.94; H200 1.01; H100 0.45; A100 0.35 | Realized rents sit near list for newer chips and far below list for older ones: a discount that grows with chip age |
| Benchmark cost basis | 0.190 × 9.810M tok/hr = $1.864; 0.421 × 2.778M = $1.170/chip-hour, matching the stated TCO | The $0.19/$0.42 figures are ownership costs, not rents |
| Same benchmark at market rents | H100 at OCPI $2.74 → $0.99/M. GB200 at CoreWeave list $10.50 → $1.07/M. Both at CoreWeave list: H100 $2.22/M vs GB200 $1.07/M (2.07×) | On a same-provider list basis the 2.2× gap survives. Against H100 transaction prices it nearly closes, because the market already prices the older chip down. These are mixed bases, so the result is illustrative (C). |
| H100 rent vs hyperscaler TCO | 2.74 / 1.17 = 2.34× today; P1's $1.50 is only 1.28× that TCO | P1's threshold sits just above SemiAnalysis's estimated ownership cost. That is a sensible economic anchor, but note it is new-purchase TCO, not the sunk cost of 2023-vintage fleets. |
| CoreWeave depreciation weight | D&A 1,393 / 2,575 = 54.1% of revenue. If all D&A were six-year GPU equipment moved to four years, it would add $696m a quarter (upper bound). | The useful-life question decides whether CoreWeave makes or loses money |
| Age analog | SemiAnalysis H100 composite $6.62 (2H 2023) → $2.80 (Mar 2026), −57.7%. A100 (launched 2020) today: Silicon $1.53, OCPI $0.94 = 54% / 34% of H100 | An aged generation already trades at or below P1's level without a glut |

## Omissions

1. **OCPI's H200 level is implausible against list prices (same-vendor blind spot).** OCPI H200 was $6.34 on Oct 16 and $6.39 on Oct 17. That is above CoreWeave's on-demand list ($6.305), above Nebius after its increase ($5.40) and above Hyperstack ($3.99). It is 81% above Silicon Data ($3.51). On OCPI an H200 rents at 2.31× an H100; four other sources put the ratio at 1.02–1.25×. A transaction index clearing above most posted on-demand prices points to a thin or unusual contributor mix. The note's "H200 firmer" conclusion, and its 17.8% month-on-month mean rise, rest mostly on this series. Silicon Data's weekly +6.0% supports the direction; the size of the move is unverified. Both Codex passes reproduced the print and accepted the level.

2. **The GAAP operating line is missing from the profitability bullet.** The same exhibit the note cites shows a −2% GAAP operating margin, depreciation at 54% of revenue and interest at 25% of revenue. This is the most direct primary evidence on whether GPU rental earns its depreciation, and it ties the note to its own useful-life section. "59% adjusted EBITDA" next to only "net loss" undersells how thin the operating line is.

3. **Publisher-level context omitted from SemiAnalysis.** The H100 composite sat at $2.80–2.84 throughout Oct 2025–Mar 2026 while the 1-year range rose. The "recovery" is in term contracts, not the composite. A middle-term column shows "Sold Out" for Feb–Apr 2026, which is the one direct availability observation in the evidence set. The composite's 2H 2023 → 2025 decline (−58%) is also the best public measure of an H100 aging path.

4. **Realized-sale appraisal omitted (last 30 days).** American Compute's October 2026 Rack Report (data through August) gives a typical realized sale of **$14,250 per used H100 SXM** (25th percentile $13,200; "limited sample"). It values an HGX H100 node at $195,000 and puts dealer asks at 1.16× realized prices. Its June 2026 residual report projects H100 value at **5–7% of list in 2028** on a conservative basis (7–14% moderate). The note cites only this vendor's index level (75). This is a vendor appraisal, grade C/D, but it is the only completed-sale-based H100 figure and the only dated residual path. It bears directly on P1's age caveat. [American Compute H100 appraisal](https://www.amcompute.com/appraisals/h100).

5. **Discount to list by vintage is a cleaner signal than any single index.** OCPI realized prices as a share of CoreWeave's on-demand list: B200 0.94, H100 0.45, A100 0.35. A glut would show as newer chips falling away from list; aging shows as older chips doing so. The note has all the inputs but does not compute this.

6. **Resolution infrastructure for P1.** Silicon Data publishes only business days and keeps history behind a paid portal. OCPI's public API holds a rolling three months. Unless the project archives both series daily from now, P1 and its fallback cannot be scored. The note says "capture the daily series prospectively" but nothing schedules it. Separately, the register's phrase "no fixing timestamp" is now inaccurate for H100.

7. **GB200 NVL72 per-GPU list ($10.50) and the benchmark basis.** The theory page's GB200-vs-H100 token-cost claim uses hyperscaler-volume ownership TCO, at one interactivity point, with interpolated values and an unresolved precision label (FP4 vs fp8). None of the pages states this. At market rents the per-token advantage is much smaller (see Arithmetic).

8. **CoreWeave's Sep 17 release names no GPU generation.** The $40m/MW figure cannot be used as evidence about H100 or A100 economics. It is consistent with new-generation scarcity only.

No primary filing in the last 30 days contradicts the note's segmented-pricing conclusion. The Sep 30 Rubin deployment and Sep 18 convertible were already added after the Codex review.

## Summary-bullet assessment

| # | Supported? | Concrete? | Comment |
|---|---|---|---|
| 1 | Yes | Yes (date, $/MW, spot price) | Add that the $40m/MW release names no GPU generation |
| 2 | Yes | Yes | Replace "display" with the dated "As of Oct 17, 2026" SDH100RT reading. Add that the indices agree on H100 (OCPI/SD 0.97) but diverge on H200 (1.81) and B200 (1.33) |
| 3 | Mostly | Yes | The H100 and A100 statements hold. The H200 magnitude rests on an outlier level (Omission 1) and needs a caveat |
| 4 | Yes | Partly | Add the GAAP operating margin of −2% and D&A at 54% of revenue. Without them the bullet reads more comfortable than the exhibit |
| 5 | Partly | Yes | The 1-year survey rise is real, but the same publisher's composite was flat at about $2.82. Add the realized-sale appraisal and its 2028 residual path |
| 6 | Yes | Yes | Fine |

## Your assessment

GPU rental is segmented by age. It is not uniformly firm. The newest chips (B200, B300 and, with caveats, H200) clear close to list and rose about 18% month on month into September. The H100 has been flat at about $2.80–2.84 since mid-2025 on the SemiAnalysis composite, consistent with Silicon Data and OCPI today. The A100 is at 35% of list and falling about 7% a month. None of this shows a glut, and the evidence is consistent with the note's segmented-pricing view. Where I differ is on comfort. The best primary evidence on profitability is CoreWeave's GAAP line: an operating margin of −2% even with 59% adjusted EBITDA and a six-year depreciation life, with depreciation absorbing 54% of revenue. Any shortening of real economic life, which the A100's discount to list and American Compute's projected 5–14% residual by 2028 both point toward, falls straight through to losses.

Who loses first:
1. Equity in levered neoclouds whose 2023–24 H100 fleets reprice at renewal. Their contract cash flows protect them until then.
2. GPU-collateral lenders, if realized sale prices (about $14k per H100 today) follow the projected residual path.
3. NVIDIA, through capacity backstops, before hyperscalers.

The note is right that rents alone cannot tell us more. My main difference is that its comfort from "H200 and B200 firmer" leans on one index's H200 level, which I would not trust.

## Front-page figures

| Page | Figure | Still holds? | Note |
|---|---|---|---|
| register P1 | SDH100RT $2.82 "displayed on access 2026-10-17, no fixing timestamp" | $2.82 holds. **"No fixing timestamp" no longer holds**: the page is dated "As of Oct 17, 2026" | Business-day publication |
| register P1 | Definition (complete-month mean < $1.50 × 3, ≥80% coverage, OCPI fallback) | Well formed, but **not resolvable without a project archive** | Both public windows are ≤90 days |
| register P1 | Caveat: by Oct 2028 the H100 is ~5.5 years old, a Yes is "partly an age effect" | **Understated** | Today's A100, at 6.4 years, is at $1.53 on Silicon's own neocloud index, at the threshold, in a non-glut market |
| index (signals/U3) | OCPI H100 $2.74 (Oct 16); monthly means flat $2.83 vs $2.83 | Yes ($2.8306 vs $2.8293; Oct-to-17 $2.8276; Oct 17 print $2.78) | Daily SD 4.6%: quote the means, not daily prints |
| index Supply row | "B200 rents +15% in 30 days" (A/B) | Holds at Oct 16 (+15.5%; +19.4% at Oct 17) but **depends on the endpoint**: Oct 16 equals the Sep 29 level | Use the monthly means |
| note/signals | H200 and B200 firmer, A100 softer ($0.94) | B200 and A100 yes ($0.97 on Oct 17). H200 direction yes, **level doubtful** | See Omission 1 |
| note signals | CoreWeave B200 spot $4.26 vs on-demand $8.60 | Yes | |
| theory | A100 "$1.84 median; pricing note found $1.79 on 2 October and could not reproduce" | **$1.84 now reproduces (Oct 18, both URLs)**, so the "could not reproduce" clause is stale | A mixed 40/80GB listing median; the transaction index is $0.94 |
| theory | GB200 $0.19 vs H100 $0.42 per 1M tokens (MiniMax M2.7, FP8) | Figures hold at 91 tok/s/user | Ownership TCO basis, interpolated values, FP4/fp8 label conflict; should say so |
| stack | "connected clusters are scarce while standalone GPU-hours stay cheap" | **No.** The note replaced this with segmented pricing after the Codex review | Replace (edit 10) |
| index unknowns | "H100 monthly index (P1, age test by 2028)" | Yes as a pointer | Becomes accurate once P1b exists |

## Recommended edits

1. **Note row 1, Summary 2, Signals "P1 benchmark".** Replace "no settlement stamp" / "settlement date absent" with: "SDH100RT $2.82, dated 'As of Oct 17, 2026' on the index page; published every business day; history is portal-only (90 days). The summary panel's other GPUs carry no date."

2. **Note Summary 3 and row 3, and add a Conflicts paragraph.** Append to Summary 3: "OCPI's H200 level is an outlier: $6.34 on Oct 16 is above CoreWeave's on-demand list ($6.305) and Nebius's ($5.40), and 81% above Silicon Data's $3.51. The H200 rise is directionally supported (Silicon +6.0% on the week) but its size is unverified." Grade the OCPI H200 level D for market representativeness.

3. **Note Summary 4 and row 18.** Replace the first sentence with: "CoreWeave's Q2 2026 adjusted EBITDA margin was 59%, but its GAAP operating margin was −2% ($49m loss), with depreciation at 54% of revenue ($1,393m) and net interest of $640m; net loss $626m." Add a row: GAAP operating loss $49m, D&A $1,393m, interest $640m, Q2 2026, A.

4. **Note Summary 5 and row 16.** Append: "The same publisher's H100 composite was flat at $2.80–2.84 from October 2025 to March 2026, down from $6.62 in 2H 2023; the rise is in 1-year terms, not the composite." Add a row for the "Sold Out" middle-term observations (Feb–Apr 2026, C, column mapping uncertain).

5. **Note, new row and Depreciation paragraph.** Add: "American Compute's October 2026 Rack Report (data through August) puts a typical realized used H100 SXM sale at $14,250 (25th percentile $13,200; limited sample) and an HGX H100 node at $195,000. Its June 2026 residual report projects 5–7% of list in 2028 (conservative) and 7–14% (moderate). Vendor appraisal, C." [Source](https://www.amcompute.com/appraisals/h100).

6. **Note row 26 and Conflicts.** Replace with: "GetDeploying's A100 on-demand median is $1.84 as of October 18, 2026 (47 providers, 40 with priced on-demand configs; spot $1.19). The $1.79 figure came from the same daily-updated page dated October 2. The median pools 40GB/80GB and PCIe/SXM; OCPI A100 SXM4 transactions were $0.94–0.97 on Oct 16–17."

7. **Note, new Signals row: "Realized discount to list by generation".** Current value: "OCPI ÷ CoreWeave on-demand: B200 0.94, H200 1.01, H100 0.45, A100 0.35 (Oct 16/17)". Why it matters: "Glut shows as new-generation ratios falling; aging shows only in old-generation ratios."

8. **Register P1 text.** Replace "($2.82 displayed on access 2026-10-17, no fixing timestamp)" with "($2.82 as of 2026-10-17; published business days; history portal-only)". Add: "Scheduled publication days are Silicon Data business days. The project archives SDH100RT and OCPI H100 daily from 2026-10-18 in data/; days missing from the archive count as missing." Then add a scheduled daily capture task so the archive actually exists.

9. **Register P1 caveat.** Replace "Caution: by October 2028 the H100 is about 5.5 years old, so a Yes at 24 months is partly an age effect, not glut evidence on its own" with: "Caution: this is mainly an aging question at 24 months. The A100, at 6.4 years in October 2026, already prices at $1.53 on Silicon Data's neocloud index (OCPI $0.94) without a glut. The H100 composite fell 58% between 2H 2023 and mid-2025. A vendor appraisal projects H100 residuals of 5–14% of list by 2028. A P1 Yes counts as glut evidence only together with P1b." I would leave 5/15/35: aging makes 35% plausible at 24 months, and the 46.8% fall needed by 12 months has no aging precedent at the H100's current flat rate.

10. **Report stack.md, Compute market line.** Replace "connected clusters are scarce while standalone GPU-hours stay cheap" with: "rents are segmented by generation: B200 near list and rising, H100 flat at ~$2.82 for a year, A100 at about a third of list; the three public indices measure different products and cannot be spliced."

11. **Report index.md, Supply bull cell.** Replace "B200 rents +15% in 30 days (A/B)" with: "B200 rent monthly means $6.14 Aug → $7.25 Sep → $7.74 Oct-to-17, while H100 is flat at $2.83 (Ornn OCPI, A/B)".

12. **Report theory.md, GPU-life sentence.** Replace "(an aggregator quoted $1.84/hr median; the pricing note found $1.79 on 2 October and could not reproduce the earlier figure)" with "(Ornn's transaction index $0.94 on 16 October, about a third of CoreWeave's list; listing medians are near $1.84)". Replace "on one published benchmark (MiniMax M2.7, FP8) a GB200 serves tokens at $0.19 per million against $0.42 on an H100" with "on one published benchmark (MiniMax M2.7, interpolated, at 91 tokens/s per user, on SemiAnalysis's hyperscaler ownership cost), a GB200 serves tokens at $0.19 per million against $0.42 on an H100; at market rents the gap is much smaller because the H100 already rents at a discount".

13. **Register, add P1b (current-generation companion).**

    > **P1b.** The Ornn OCPI B200 index's equal-weighted mean of each complete calendar month's daily publications is below $4.50/GPU-hour for three consecutive months wholly inside the horizon. The threshold is 62% of September 2026's $7.245, a fall of 38%. At least 80% of calendar days must be present, with no interpolation, and carried-forward or disruption-flagged prints are excluded. For the 24-month horizon the reference series rolls on 2027-10-17 to the newest Nvidia data-centre GPU with at least 180 days of OCPI history, at 62% of its 2027-Q3 mean. If OCPI is unavailable for a complete month, Silicon Data SDB200RT ($6.12 on 2026-10-17) substitutes, scaled by the median OCPI/SDB200RT ratio over the preceding 90 overlapping days (at least 60 pairs); otherwise void. Interpretation: P1 Yes with P1b No is an aging effect; both Yes is glut evidence.

    Indicative reviewer probabilities: 3% / 10% / 20%. These are judgement (D), set below P1 because B200 has no aging tailwind at 6–12 months. The roll keeps the 24-month question on a current generation instead of a 3.75-year-old B200.
