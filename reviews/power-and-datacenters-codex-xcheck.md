# Independent cross-check: Power and datacenter real estate

*Review date and information cutoff: 2026-10-17. All linked sources accessed 2026-10-17. Reviewed against `report/methodology.md` and `tasks/RESEARCH_BRIEF.md`; original note unchanged.*

## Verdict

Mostly reliable numerically: 13 of 14 selected numerical rows match primary disclosures; claim 35 mislabels continuing-operations loss, while claim 40 remains an inference.
Materially incomplete on risk allocation and recent grid developments: supplier guarantees, PJM procurement delays, and October emergency measures deserve prominent treatment.
Retain the differentiated thesis, correct the accounting label, replace the abstract Summary, and avoid presenting a universal sequence of losses or announced budgets as deployed capital.

## Claim re-verification

I selected rows **1, 3, 4, 5, 7, 15, 25, 27, 29, 31, 35, 36, 38, 39 and 40** because they support the demand range, physical bottleneck, incumbent profitability, financing, capital-at-risk and downside arguments. This selection prioritizes the economic conclusions over individual campus specifications and nuclear procurement announcements. It is not a verification of all 40 rows.

**Grades apply to the precisely scoped claim:** A means a directly stated primary disclosure, including a company's forecast or estimate, not certainty that the forecast will happen. B covers arithmetic from primary figures. C applies to the author's unverified constraint estimate. D applies to a claim contradicted by the more specific financial statements. A primary forecast and a realized, independently measured outcome must not be conflated.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | US datacenters: 176 TWh / 4.4% in 2023; 325–580 TWh / 6.7–12% in 2028 | Identical. The first pair is a modeled historical estimate; the second is a projection, covering datacenters generally. | [DOE, 2024-12-20][lbnl] | Yes | A for the reported estimates |
| 3 | EPRI: 4.6–9.1% of US electricity by 2030 in 2024 scenarios; 9–17% in 2026 scenarios; 4–5% currently | Identical. The February 2026 FAQ locates the current baseline in **2024**, at 177–192 TWh; its 2030 scenarios are 380–790 TWh. “Currently” should be dated. | [EPRI's 2024 release][epri24]; [February 2026 FAQ, p. 1][epri26] | Yes; baseline date needs precision | A for the published scenarios |
| 4 | IEA: 945 TWh in 2030 in 2025 report; 485 TWh in 2025 → 950 TWh in 2030 in 2026 update | Identical. These are global, all-datacenter estimates/projections, not AI-only demand. | [IEA 2025 demand chapter][iea25]; [IEA 2026 executive summary][iea26] | Yes | A |
| 5 | PJM 2026/27: $329.17/MW-day, 134,311 MW; 2027/28: $333.44, 134,479 MW, shortfall 6,623 versus 6,517 MW; 2028/29: $325, shortfall 6,831 MW | All quoted values found. July 2026 release additionally states 138,318 MW auction procurement plus 10,864 MW FRR. The December 2025 release itself also contains a different 134,747 MW cleared total on p. 2; no reconciliation established. | [July 2025 release][pjm25a]; [December 2025 release, pp. 1–2][pjm25b]; [2025 annual report][pjmar]; [July 2026 release][pjm26] | Yes as attributed; underlying PJM discrepancy remains | A for each attributed disclosure; no single reconciled 2027/28 quantity |
| 7 | ERCOT requests >474 GW, approximately 90% datacenters, August 2026 | Governor's August 3 statement gives over 474 GW and approximately 90%. This verifies the government's description, not a project-by-project ERCOT queue audit. | [Texas Governor, 2026-08-03][txaudit] | Yes | A for official statement |
| 15 | GE Vernova: $176bn backlog; 116 GW gas backlog plus reservations; Q2 adjusted EBITDA margin 11.3%, Power 18.8% | Identical. The release explicitly splits 116 GW into **53 GW equipment backlog and 63 GW reservations**; Power's 18.8% is segment EBITDA margin. | [GE Vernova Q2 release, 2026-07-22][gev] | Yes; retain the metric labels and disclose the split | A |
| 25 | Onsite gas: 30–70% extra generation relative to load; 15–27 GW by 2030 | Identical IEA estimates. The 2030 range is mostly US deployment, not a committed project total. | [IEA 2026 executive summary][iea26] | Yes | A for IEA's estimates |
| 27 | TCEQ permit halt pending audit; October 19 compliance update, not expiry | Identical. September 21 directive also says state agencies should withhold related approvals pending required information and refers to both ERCOT and water-audit requirements. | [Governor's September 21 directive][txhalt], fetched directly after web-fetch timeout | Yes; scope is broader than the short table entry | A for directive; not proof of universal enforcement |
| 29 | Equinix Q2: revenue $2.625bn; operating income $665m; adjusted EBITDA margin 53%; stabilized cash-on-cash return 27% | Identical. Presentation gives $5.232bn trailing cash gross profit against $19.639bn gross PP&E for the stabilized pool. One-time xScale fees affect reported quarterly profitability. | [July 29 earnings release][eqix]; [Q2 presentation, pp. 5, 7, 10, 28][eqixdeck], fetched directly | Yes | A for disclosed measures; recomputed ratios B |
| 31 | DLR: 1,402 MW under development, 54% leased; total investment $20.180bn, DLR share $13.612bn; yield 11.5% | Identical after rounding. Yield is estimated **pre-tax stabilized cash yield**, based on expected investment and signed leases or market assumptions. | [Q2 financial supplement, p. 23 and footnotes][dlr] | Yes | A for disclosed estimates |
| 35 | PF1 400 MW leased / 250 MW live; Q1 FY2027 revenue $341.9m, common-stockholder net loss $221m, adjusted EBITDA $64.4m; debt $6.4bn | Other figures match; 250 MW is October 1, after the August 31 quarter-end. **Total common-stockholder loss is $237.082m: $221.028m continuing plus $16.054m discontinued operations.** The headline's abbreviated label is misleading. | [October 7 earnings exhibit][apldrelease]; [FY2027 Q1 10-Q, statements of operations][apldq]; [CoreWeave lease disclosure][apldlease] | **Partial: loss scope wrong** | A for corrected statements and other figures; D for $221m presented as total loss |
| 36 | Hyperion ~$27bn; Blue Owl funds 80%, Meta 20%; initial lease four years; capped residual guarantee first 16 operating years; PIMCO debt | Identical. The 80/20 split is ownership and pro-rata development funding responsibility, not a claim that the full budget was paid in cash at closing. | [Meta announcement, October 21 / updated November 14, 2025][meta] | Yes | A |
| 38 | Beacon Point $4.25bn, 6.129%, due 2042; River Bend $3.25bn, ~95% loan-to-cost, non-recourse | Identical. River Bend's coupon is 6.192%, with principal payments starting May 2028; its issuer describes the financing as fully amortizing over 16.5 years. | [Hut June 2026 10-Q, Note 9][hutq]; [issuer's May 6 release syndicated by Nasdaq][hutrelease] | Yes; amortization matters to the downside argument | A |
| 39 | $82bn = Hyperion $27bn + Abilene $15bn + Frontier/Lighthouse $40bn | $82bn arithmetic matches independently fetched announcements. They describe selected development budgets/plans with different financing perimeters, not a consolidated capital stock. | [Meta][meta]; [Crusoe, May 21, 2025][crusoe]; [DigitalBridge October 30, 2025 presentation, slides 7 and 23][dbrg] | Yes in table; Summary's “commitments” is too uniform | B for sum; A for component announcements |
| 40 | Power/commissioning binding regionally in 2026–28; chips co-constrained | TSMC on October 15 says assessed demand still exceeds supply after considering power and funding. Nvidia lists deployment risks. Neither quantifies a regional bottleneck ranking or establishes the full 2026–28 horizon. PJM and Texas evidence supports a narrower location-specific judgment. | [TSMC transcript, pp. 6 and 16][tsmc]; [Nvidia Q2 FY2027 10-Q][nvda]; [PJM][pjm26]; [Texas][txhalt] | Plausible inference, not directly verified fact | C for ranking/horizon; A only for management statements |

The EPRI 2024 report endpoint and some presentation/agency endpoints did not yield usable web-extracted content. I used EPRI's own syndicated release, direct PDF retrieval for Equinix, and direct HTML retrieval for Texas; I did not treat an inaccessible URL as corroboration. The Hut press release's extracted webpage omitted its body, so I used the issuer-authored Nasdaq syndication and the 10-Q. No secondary market-price claim was upgraded to A.

## Arithmetic checks

**Strict scope:** the Analysis section contains no explicit derived numerical figure or equation. After citation labels/URLs are removed, its only numeral-bearing sentence is the **2026–28** constraint judgment. That is a forecast horizon, not arithmetic. It would be misleading to claim to have checked calculations that do not appear there. I checked all actual computations supporting its qualitative comparisons and the adjacent capital/profitability claims as follows; added diagnostic ratios are identified as such.

| Check | Recalculation | Result and interpretation |
|---|---|---|
| Selected budgets, claim 39 | 27 + 15 + 40 = **$82bn** | Correct. Do not add financing proceeds, guarantees or leases to these budgets as if they were separate installed capital. [Component sources][dbrg] [and][crusoe] [Meta][meta] |
| IEA trajectory “barely changes” | (950 / 945 − 1) × 100 = **0.529%** | Correct characterization of the central 2030 endpoint. 950 / 485 − 1 = **95.88%**, consistent with approximately doubling over 2025–30. [IEA 2025][iea25], [2026][iea26] |
| EPRI scenarios are higher | Low endpoint 4.6% → 9%; high 9.1% → 17% | Direction correct. Do not describe the share ratios as a like-for-like electricity-volume revision: scenario construction, baselines and denominators differ. [EPRI 2024][epri24], [2026][epri26] |
| GE combined backlog/reservations | 53 + 63 = **116 GW**; reservations / combined = **54.31%** | Correct combined figure; the majority is reservations. The second calculation is my diagnostic, not an existing calculation in the note. [GE release][gev] |
| Equinix margins and stabilized return | 1,396 / 2,625 = **53.18%**; 665 / 2,625 = **25.33%**; 5,232 / 19,639 = **26.64%** | Supports rounded 53% adjusted EBITDA and 27% cash return. Operating margin is a separate diagnostic. The return numerator is trailing cash gross profit, not distributable cash after all overhead, maintenance and financing. [Release][eqix], [presentation][eqixdeck] |
| DLR budget totals | $5.161924bn + $15.017717bn = **$20.179641bn**; $4.086209bn + $9.526219bn = **$13.612428bn** | Both round correctly. Costs incurred and future costs are separate columns; do not call total expected investment already deployed. [Supplement p. 23][dlr] |
| APLD loss reconciliation | $221.028m + $16.054m = **$237.082m** | Correct total; the note omitted the discontinued-operations component from its loss label. [10-Q][apldq] |
| APLD delivery conversion | 250 / 400 = **62.5%** | A diagnostic of October 1 ready-for-service capacity relative to leased capacity, not actual utilization or the fraction earning rent throughout Q1. [Delivery][apldrelease], [lease][apldlease] |
| PJM cap change and conflicting shortfall | 325 / 333.44 − 1 = **−2.531%**; 6,623 − 6,517 = **106 MW** | Cap decline does not establish an improvement in adequacy. The source discrepancy cannot be resolved by arithmetic alone. [2026 release][pjm26], [2025 release][pjm25b], [annual report][pjmar] |
| Onsite redundancy | 1 GW load × (1 + 30–70%) = **1.3–1.7 GW generation** | Illustrates the IEA assumption. This is installed generation, not an implied 30–70% increase in annual consumption or a universally applicable campus design. [IEA][iea26] |

All recomputations are grade B. No arithmetic establishes an adequate return on capital: the note provides neither a matched project cash-flow model nor a project-specific discount rate. In particular, DLR's prospective yield and Equinix's historical cash return cannot be directly compared as investment spreads.

## Omissions

1. **Supplier credit support is a major missing exposure, not merely a hypothetical risk factor.** Nvidia's cited filing reports August 2026 guarantees capped at **$105bn** for OpenAI-related leases covering **4.25 GW** at SB Energy's Ohio PORTS campus. Obligations begin with lease commencement, expected first in fiscal 2029, and cover defined lease/power payments under specified defaults. This is conditional exposure, not current debt, campus cost or an expected loss. It nevertheless makes the financing map materially incomplete: demand risk can return to the chip supplier. **A; predates the last 30 days but was already in a cited source.** [Nvidia 10-Q, commitments and guarantees][nvda]

2. **September 29–30: the proposed near-term PJM reliability backstop was delayed.** FERC accepted the proposal for filing but suspended it for five months, effective **February 28, 2027**, subject to refund and further proceedings. PJM explicitly cancelled the planned September 30 start; that effective date is not a confirmed procurement date. Questions include cost allocation, transmission-owner exit rules and load-serving-entity collateral. These are directly relevant to who finances scarce capacity and who pays if large-load demand disappears. **A.** [FERC order, pp. 1, 9 and 85][rbporder]; [PJM September 30 statement][rbp]

3. **October 9: proposed mandatory early curtailment was not an established solution.** Commissioner Rosner's concurrence confirms rejection of most of PJM's interim-service filing and questions curtailing new loads before voluntary demand response and excluding them from capacity-market demand. This weakens any assumption that a ready regulatory mechanism already makes new datacenters absorb reliability risk. The concurrence is primary evidence of this rejection; I did not rely on an unread eLibrary attachment to characterize every surviving provision. **A for the action described; analytical implication is my inference.** [FERC concurrence, ER26-3515][iras]

4. **October 12–16: operational stress had already prompted an emergency order.** DOE Order 202-26-50 authorized exceptional generation measures, including datacenter backup generation as a last resort around an EEA 3 emergency. It applied **October 13–16**, so should not be described as still effective on October 17 without a renewal. PJM's application forecast approximately **111,500 MW** demand and **61,591 MW** generation outages; autumn maintenance and transmission outages matter, not just AI growth. Authorization is not proof that backup units ran or customers were disconnected. **A.** [DOE order, pp. 1–3 and 8–9][doeorder]

5. **September 24: there is a concrete counterweight to the bottleneck thesis.** DOE selected **31 projects in 26 states**, with **$1.9bn** prospective federal funding and **$3.35bn** recipient contributions, targeting over **23 GW** additional grid capacity through reconductoring and other upgrades. This is a prospective grid-capacity estimate, not commissioned generation or guaranteed capacity for a particular campus. Its omission makes the supply response appear more static than the evidence supports. **A for announcement/estimate.** [DOE SPARK announcement][spark]

6. **September 29: the queue-vetting mechanism became more concrete.** PJM reported a new review of large-load submissions, duplicate-request checks, contract-status information and an independent Charles River Associates assessment. It expected to explain adjustments in November before the January 2027 forecast. This supplies an actionable test of the speculative-demand thesis; it does not yet supply the size of a downward revision. **A.** [PJM forecasting update][vetting]

7. **October 7: Applied Digital's revenue mix materially changes the evidence of monetization.** The release separates **$183.5m tenant fit-out revenue** from **$65.8m base rent** and **$13.3m recoveries**. Total revenue therefore substantially reflects construction activity. The corrected loss is also not itself proof that stabilized campus rents are uneconomic. **A for components; interpretation is mine.** [Earnings exhibit, HPC Hosting and operating results][apldrelease]

8. **Contract protection cuts against a universal refinancing story.** Hut's River Bend financing is described as fully amortizing over **16.5 years**, and its rent obligations have a Google financial backstop. The notes themselves are not guaranteed by Google or the tenant. This distinction helps explain investment-grade financing at high loan-to-cost and reduces ordinary balloon-refinancing exposure if the project performs. It does not remove construction, payment or guarantor risk. **A.** [Issuer release][hutrelease]; [10-Q Note 9][hutq]

The note already discusses the September Texas halt, September Jupiter correspondence, and October bond repricing; these are not discoveries of this review. I found no primary evidence in this work that proves a sector-wide operating glut, a default on the quoted project bonds, or a single national bottleneck ranking. Nor did I independently verify bond trades or calculate expected credit losses. Those remain open rather than silently promoted to fact.

## Summary-bullet assessment

| Bullet | Supported by the note's own evidence? | Useful enough for a technical reader? | Required change |
|---|---|---|---|
| 1. Separate capital layer; regional energization and chips constrained | **Mostly.** PJM adequacy, Texas approvals and equipment constraints support location-specific limits; TSMC supports continued chip scarcity. They do not prove which constraint dominates each region throughout the stated horizon. | **No:** no location, magnitude or date. | Use a dated PJM shortfall and TSMC statement; replacement 1 below. |
| 2. Wide forecasts; speculative queues are not consumption | **Yes**, with a qualification: official request totals do not measure what fraction is speculative. | **No:** omits the forecast range and target year. | Give EPRI's dated scenario range; replacement 2. |
| 3. Profitable incumbents do not validate every campus | **Yes.** Disclosed profits support the first proposition; the second is a sound limitation, not evidence of specific bad projects. | **No:** readers need a margin and its period. | Anchor to GE and Equinix, retaining the fee caveat; replacement 3. |
| 4. Hyperscalers, utilities, REITs, funds and bondholders share risk | **Yes but materially incomplete.** Meta supports tenant recourse; supplier support is missing despite the cited Nvidia filing. | **No:** no transaction, exposure or date. | Add the supplier-guarantee example; replacement 4. |
| 5. $82bn “commitments”; consolidated stock unverified | **Partly.** The sum is correct, but the table correctly calls it announced budgets. Common enforceability and funded status have not been demonstrated. | **Partly:** it has a number, but no component list or vintage. | Say selected announced development budgets; replacement 5. |
| 6. Vulnerable projects; starts fall first, then refinancing/leases/residuals | **Mechanism plausible; ordering unsupported.** Financing spreads or valuation losses can precede cancellations. Contract design can defer rent losses and avoid a balloon maturity. | **No:** universal chronology, no concrete financing example. | Make it conditional and distinguish amortizing debt; replacement 6. |
| 7. Biggest uncertainty is signed capacity becoming paying energized demand | **Reasonable judgment, not a verified ranking.** The note lacks a common measure of commissioned, rent-commenced and actually used capacity. | **No:** no observable conversion measure or date. | Give PF1's delivery ratio and specify what it does not measure; replacement 7. |

## Your assessment

The evidence supports a sector with valuable scarce infrastructure and real incumbent earnings, alongside substantial exposure in unfinished or specialized developments; it does not by itself establish either a nationwide physical glut or adequate investment returns. I agree with the note's distinction between profitable equipment/colocation businesses and the economics of marginal campuses. I differ most on the financing map and timing: supplier-backed obligations create a more interconnected loss-bearing structure than the Summary acknowledges, while amortizing, credit-supported project debt can be less exposed to ordinary refinancing than the generic downside sequence suggests. Recent PJM decisions and emergency measures make execution and reliability concerns more immediate, but announced grid upgrades and better demand vetting can change the future scarcity picture. The decisive evidence is project-level rent commencement, durable tenant cash flow, enforceable support and the remaining cost to complete—not gross queue size or a mixed subtotal of announced construction budgets. The note needs a more measurable conclusion, not a reversal into an unsupported bubble verdict.

## Recommended edits

1. **Replace Summary bullet 1:** “PJM's July 2026 auction fell 6,831 MW short of its 2028/29 reliability requirement; TSMC still reported chip demand above supply on October 15, 2026. Power and chips can constrain different stages of deployment.” Cite [PJM][pjm26] and [TSMC][tsmc].

2. **Replace Summary bullet 2:** “EPRI's February 2026 scenarios put US datacenter electricity use at 9–17% of the national total by 2030. These are conditional projections; connection requests and announced campus MW are not measured consumption.” Cite [EPRI][epri26].

3. **Replace Summary bullet 3:** “In Q2 2026, GE Vernova reported an 11.3% adjusted EBITDA margin and Equinix $665m operating income, including one-time xScale fees. These profits do not establish the returns on unfinished campuses.” Cite [GE][gev] and [Equinix][eqix].

4. **Replace Summary bullet 4:** “Risk also reaches suppliers: Nvidia disclosed August 2026 guarantees capped at $105bn for OpenAI-related leases covering 4.25 GW in Ohio. These conditional obligations cover defined lease and power payments, not the campus's entire cost.” Cite [Nvidia][nvda].

5. **Replace Summary bullet 5:** “Selected 2025 announcements total $82bn of development budgets: Hyperion $27bn, Abilene $15bn, and Frontier/Lighthouse $40bn. They do not establish aggregate funded or deployed AI infrastructure capital.” Cite [Meta][meta], [Crusoe][crusoe] and [DigitalBridge][dbrg].

6. **Replace Summary bullet 6:** “A demand shortfall can impair unleased projects and residual values, but loss timing depends on contracts: Hut's May 2026 disclosure describes River Bend's $3.25bn debt as fully amortizing over 16.5 years, reducing ordinary maturity-refinancing exposure.” Cite [Hut's release][hutrelease]. Also replace the Analysis assertion that unused land and uncommitted phases absorb losses “first” with: “A demand shortfall can appear in financing prices, land values, cancelled starts or tenant concessions; the order depends on each project's funding and lease terms.”

7. **Replace Summary bullet 7:** “Track contracted capacity through delivery and rent commencement: Applied Digital reported 250 MW ready for service at Polaris Forge 1 on October 1, 2026, against 400 MW leased. That 62.5% delivery ratio does not measure utilization or collected rent.” Cite [delivery disclosure][apldrelease] and [lease disclosure][apldlease]; grade the ratio B.

8. **Correct claim 35's loss label and source:** Replace “common-stockholder net loss $221m” with “common-stockholder net loss $237.1m, comprising $221.0m from continuing and $16.1m from discontinued operations.” Cite the [FY2027 Q1 10-Q][apldq], rather than relying on the abbreviated release headline; grade A after correction. Keep the August 31 financial period separate from October 1 delivery.

9. **Add a dated PJM update to Analysis and Signals:** “On September 29, 2026, FERC suspended PJM's reliability-backstop proposal for five months, effective February 28, 2027; PJM cancelled its planned September 30 procurement start. On October 9, FERC rejected most of PJM's interim large-load service proposal. DOE subsequently authorized exceptional backup-generation measures for October 13–16. These actions show unresolved procurement, cost-allocation and operating-reliability issues; they do not prove datacenter-caused blackouts.” Cite the [backstop order][rbporder], [PJM statement][rbp], [FERC concurrence][iras] and [DOE order][doeorder].

10. **Add a concrete counterargument and forecast test:** “DOE's September 24, 2026 SPARK selections target over 23 GW of additional grid capacity through upgrades, supported by $1.9bn federal and $3.35bn recipient funding; these are prospective improvements. PJM's September 29 forecast review adds contract and duplicate-request checks, with load adjustments expected in November ahead of the January 2027 forecast.” Cite [DOE][spark] and [PJM][vetting].

11. **Make the Applied Digital profitability comparison economically interpretable:** Add: “Q1 FY2027 revenue included $183.5m of tenant fit-out services and $65.8m of base rent. Construction-service revenue should be separated from recurring rental income when evaluating debt service.” Cite the [earnings exhibit][apldrelease] and the [10-Q's segment and revenue discussion][apldq].

12. **Quantify the firm-order distinction in claim 15 and Signals:** Replace “116 GW gas equipment backlog plus slot reservations” with “53 GW gas equipment backlog plus 63 GW slot reservations, totaling 116 GW at June 30, 2026.” Cite [GE's release][gev]. Preserve the separate $176bn group-backlog figure and label Power's margin as segment EBITDA.

[lbnl]: https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
[epri24]: https://www.prnewswire.com/news-releases/epri-study-data-centers-could-consume-up-to-9-of-us-electricity-generation-by-2030-302157970.html
[epri26]: https://restservice.epri.com/publicattachment/96784
[iea25]: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
[iea26]: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
[pjm25a]: https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/
[pjm25b]: https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf
[pjmar]: https://services.pjm.com/annualreport2025/markets/
[pjm26]: https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf
[txaudit]: https://gov.texas.gov/news/post/governor-abbott-directs-comprehensive-data-center-audit
[txhalt]: https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits
[gev]: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gevpressrelease2q26.htm
[eqix]: https://investor.equinix.com/news-events/press-releases/detail/1114/equinix-reports-second-quarter-results-raises-2026
[eqixdeck]: https://d1io3yog0oux5.cloudfront.net/_1b9021a64126ce4a4888ccc1339fac81/equinix/db/2183/27054/earnings_presentation/Equinix+Q2+26+Earnings+Presentation+Final.pdf
[dlr]: https://investor.digitalrealty.com/static-files/678a7e32-514a-41c8-aebc-9492d513bf61
[apldrelease]: https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000057/apldq127earningsrelease.htm
[apldq]: https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000059/apld-20260831.htm
[apldlease]: https://ir.applieddigital.com/news-events/press-releases/detail/131/applied-digital-reports-fiscal-first-quarter-2026-results
[meta]: https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
[hutq]: https://www.sec.gov/Archives/edgar/data/1964789/000110465926090025/hut-20260630x10q.htm
[hutrelease]: https://www.nasdaq.com/press-release/hut-8-reports-first-quarter-2026-results-2026-05-06
[crusoe]: https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
[dbrg]: https://ir.digitalbridge.com/node/14786/html
[tsmc]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf
[nvda]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[rbporder]: https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9154/20260929-er26-3380-000.pdf
[rbp]: https://insidelines.pjm.com/ferc-accepts-pjm-reliability-backstop-proposal/
[iras]: https://www.ferc.gov/news-events/news/commissioner-rosners-concurrence-pjm-interconnection-llc-er26-3515-000
[doeorder]: https://www.energy.gov/documents/doe-order-no-202-26-50
[spark]: https://www.energy.gov/articles/energy-department-announces-speed-power-investments-across-26-states-lower-electricity
[vetting]: https://insidelines.pjm.com/pjm-kicks-off-annual-process-of-vetting-large-load-requests/
