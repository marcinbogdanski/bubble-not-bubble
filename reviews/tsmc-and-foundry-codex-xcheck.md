# Independent cross-check: TSMC and the foundry layer

*Reviewed 2026-10-17. Fresh-context Codex review of `research/stack/tsmc-and-foundry.md`; methodology and research brief read first. All external sources below were fetched or retrieved through web search on 2026-10-17. No subsequent information is used.*

## Verdict

The 15 selected claims match primary disclosures at the note's stated precision; no material numerical error overturns its profitability or liquidity conclusion.
The financing and overbuild analysis needs material additions: customer capacity deposits, purchase commitments, actual tax-credit inflows, and dated capacity/capex milestones.
Retain the qualified business assessment, reconcile the small cash-flow precision discrepancy, improve claim 16's sourcing/grade, and replace the abstract Summary bullets.

## Claim re-verification

Selection covers current earnings, AI exposure, investment, funding, concentration, overseas costs, historical downside and competitors. These are the 15 rows on which the Summary and Analysis most directly depend. A means a primary disclosure directly states the figure or management expectation; it does not validate a forecast. B means arithmetic from primary inputs. “Match” is a factual check, not endorsement of the accompanying inference.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | Q3 2026 revenue NT$1,494.24bn / US$46.72bn; +50.9% / +41.2% YoY | Same, quarter ended September 30, released October 15 | [Earnings release, p.1][S1] | Yes | A |
| 2 | Q3 gross / operating / net margin 66.4% / 58.7% / 51.1% | Same | [Earnings release, p.1][S1] | Yes | A |
| 4 | Q3 platform mix: HPC 68%, smartphone 21%, IoT 4%, automotive 4%, DCE 1%, other 2% | Same; denominator is net revenue | [Management report, p.2][S2] | Yes | A |
| 6 | FY2025 AI accelerators: high-teens percent of total revenue | Same; disclosed January 15, 2026 | [January call, p.5][S6] | Yes; not a current-quarter share | A |
| 11 | FY2026 capex initially US$52–56bn; July US$60–64bn, reiterated October | Same progression | [January, p.4][S6]; [July, p.4][S11]; [October, p.4][S4] | Yes | A, guidance only |
| 12 | Q3 CFO / capex / FCF / dividends: NT$919.77 / 443.21 / 476.56 / 155.59bn | Presentation matches exactly; statement inputs are 919.776 / 443.206 / 155.595bn, implying FCF 476.570bn | [Presentation, slide 7][S12]; [statement, p.4][S3] | Yes as reported; precision discrepancy below | A reported; B recalculated FCF |
| 13 | Jan–Sep CFO 2,402.117 less PP&E 1,289.971 = FCF NT$1,112.146bn | Same inputs and result | [Cash-flow statement, p.4][S3] | Yes | B result; A inputs |
| 16 | Debt ~NT$1,031.58bn; liquid assets less debt ~NT$2,985.40bn | Same; both totals also appear directly in management's debt-service table | [Management report, p.4][S2]; [presentation, slide 6][S12]; [statement, p.1][S3] | Yes | A if cited as reported totals; B for the note's independent calculation |
| 17 | FY2025 Customer A 19%, B 17%; combined 36%; unnamed | Same; 36% is the sum of rounded shares | [2025 Form 20-F, Note 39, printed F-82][S34] | Yes; original SEC exhibit fetch failed, company-hosted audited filing verifies it | A individual; B combined |
| 21 | US$2bn GF agreement; initial five years; Malta ramp H1 2028 | Same announced terms, October 8, 2026 | [GlobalFoundries announcement][S19] | Yes; agreement value is not disclosed TSMC capex or guaranteed offtake | A announcement |
| 22 | Overseas gross-margin dilution ~2 points in 2026, 3–4 later | Same; full-year 2026 versus the following few years | [October call, p.3][S4] | Yes | A guidance |
| 24 | N2-family annual capacity more than doubles in 2027 | Same expectation | [October call, p.5][S4] | Yes; capacity, not revenue or utilization | A guidance |
| 26 | Q2 2001 gross margin 19%, utilization 44%; operating profit/revenue NT$284m/26,298m = 1.08% | Same inputs; ratio 1.07993% | [Q2 2001 financial report, pp.1–2][S20] | Yes | A inputs; B ratio |
| 31 | Intel Foundry Q2 2026 revenue US$5.765bn, operating loss US$2.089bn, external revenue US$293m | Same; quarter ended June 27 | [Intel 10-Q, Intel Foundry Financial Performance][S24] | Yes; external growth primarily reflects Altera becoming external | A |
| 32 | Samsung Q2 Foundry earnings improved before incentive provisions; 2nm HPC engagements; no standalone financial totals | Same qualitative disclosure; no standalone Foundry revenue or profit in this release | [Samsung July 30 results, Foundry paragraph][S25] | Yes within this release; not proof no other disclosure exists | A statement; absence is bounded to the inspected release |

Claim 16 is conservatively graded, not falsely calculated. Replacing its indirect citation with the directly reported debt-service table makes its reported totals grade A. Conversely, claims 20 and 25's unsuccessful-search qualifications should be labelled coverage limitations, not substantive grade-C estimates of capacity or prices. Claim 35 remains an analytical judgment, not a primary fact merely because its inputs are primary.

## Arithmetic checks

The Analysis contains no standalone numerical equations. Its derived assertions refer back to the claims table. I checked every such calculation and numerical comparison, including the “room for dividends,” historical-margin and predominantly-internal-revenue inferences. Units below are NT$ billions unless stated otherwise; calculations were independently recomputed with decimal arithmetic.

| Calculation or inference | Independent check | Result |
|---|---|---|
| YTD FCF, claim 13 | 2,402.117 − 1,289.971 = **1,112.146** | Correct. Gross PP&E purchases; no asset-sale proceeds or dividends included. [S3] |
| Quarterly FCF, claim 12 | Presentation: 919.77 − 443.21 = **476.56**. Statement: 919.776 − 443.206 = **476.570** | Difference **0.010bn = NT$10m**. Source precision/presentation inconsistency, not a material error by the author. Do not silently mix the two series. [S3][S12] |
| Dividends affordable from residual cash | Q3: 476.570 − 155.595 = **320.975**. YTD: 1,112.146 − 440.853 = **671.293** | Supports the claim for the observed periods; these are residuals after PP&E and dividends, not total changes in cash. [S3] |
| Total debt and liquidity cushion | 818.38 + 213.198 = **1,031.578**; 4,016.98 − 1,031.578 = **2,985.402** | Rounds to the note's **1,031.58** and **2,985.40**. Matches management's totals. Other liabilities/commitments are not deducted. [S2][S3][S12] |
| Combined concentration | 19% + 17% = **36%** | Correct at disclosed rounded precision; not an exact customer-share measurement. [S34] |
| Dot-com operating margin | 284 / 26,298 × 100 = **1.07993%** | Correctly rounded to 1.08%. [S20] |
| Historical utilization versus gross-margin timing | Q2→Q3 2001 utilization **44→41%**, gross margin **19→25%** | Correct direction. The Q3 report expressly attributes improvement to mix and higher NT-dollar ASP; not solely a contractual price increase. [S20][S21] |
| Intel “overwhelmingly internal” | External share = 293 / 5,765 × 100 = **5.08%**; remainder **94.92%** | Supported. Segment operating loss/revenue is **−36.24%**, consistent with the filing's rounded −36%. [S24] |
| Arizona envelope versus annual capex | Cumulative US$165bn + additional US$100bn = **US$265bn** | Correct reconciliation of the July plan; no valid arithmetic adds this multiyear envelope to one year's global capex. [S11] |
| FY2025 FCF supporting the funding discussion | 2,274.98 − 1,272.41 = **1,002.57** | Confirmed in an alternative primary presentation after the cited management-report URL failed. [R1] |
| 2023 margin minima, claim 30 | Gross: min(56.3, 54.1, 54.3, 53.0) = **53.0%**; operating: min(45.5, 42.0, 41.7, 41.6) = **41.6%** | Both Q4, as claimed. [R2][R3][R4][R5] |

Additional completeness checks: the platform shares sum to **100%**; the leading-edge node subtotal is **8 + 33 + 28 + 10 = 79%**, with the full node distribution summing to **100%**. The claim-34 CSV has **33** observations. Its 2024 monthly values sum to **NT$2,894,307m**, exactly **NT$1m** below the published total; 2025 and Jan–Sep 2026 sums are **3,809,054m** and **3,898,727m**. I compared these inputs with the fetched monthly pages. No missing months or arithmetic defect found. [S1][S2][R6][R7][R8]

Two useful calculations missing from the Analysis: the July capex-range midpoint increased **14.81%** (62/54 − 1); the current range implies **46.70–56.48%** growth against FY2025's US$40.90bn. More immediately, US$60–64bn less reported YTD US$40.64bn leaves **US$19.36–23.36bn for Q4**, **39.88–68.79% above Q3's US$13.84bn**, if full-year guidance is met. These are grade-B implications, not new guidance. This is the appropriate forward check on “current capital spending.” [S6][S11][S2]

## Omissions

**Material evidence from September 18–October 17, 2026:**

- **Actual public-support cash, not just an award ceiling.** The October management report identifies investment-tax-credit receipts as the main source of a substantial investing inflow (exact insertion in edit 2). The note's statement that subsidy receipts are insufficiently disclosed misses information in its own source. This affects the explanation of cash accumulation; it does not contaminate CFO-minus-gross-capex FCF, because the inflow is classified in investing. [S2]
- **Timing of both expenditure and usable capacity.** The Q4 residual capex calculation above and the fab dates in edit 4 replace an undated overbuild mechanism with observable milestones. The important risk is demand at commissioning and subsequent loading, rather than merely the size of an announcement. [S2][S4]
- **Independent evidence of equipment scarcity.** ASML's October 14 release says planned 2027 and 2028 supply will not meet expected customer demand despite planned expansion. Edit 8 supplies exact wording. This is evidence against treating all announced fab capacity as promptly deliverable; it also shows correlated optimism extending into supplier investment. Neither company's order forecasts independently establish profitable end-user AI demand. [R9]
- **An additional US location remains exploratory.** October's Texas/Terafab discussions merit a monitored item, not inclusion in committed capacity (edit 9). [S4]
- **Demand outlook needs balance.** The October presentation forecasts approximately **44%** FY2026 US-dollar revenue growth. That is counterevidence to an already collapsing market, while leaving future returns unresolved. [S12] The note correctly mentions CPUs being excluded from the narrow accelerator definition, but its Summary still risks suggesting that the old accelerator share measures total present AI exposure.

**Older but still material omissions:**

- **Customers also finance reserved capacity.** The capacity-deposit balance and refund/receivable-offset treatment in edit 3 contradict any reading that reservations are uniformly costless or that funding comes only from profits, bonds and governments. They do not establish universal take-or-pay protection. [S34]
- **Purchase commitments limit cash's freedom of use.** The same edit adds contractual purchase obligations absent from the balance-sheet cushion. Compare dates carefully: year-end commitments cannot simply be subtracted from September liquidity, and expected operating inflows also matter. The note already disclaims subtracting all liabilities, so this is a missing funding analysis, not an arithmetical correction. [S34]
- **A stronger opposing profitability case exists.** In January management targeted through-cycle gross margin of at least **56%** and ROE in the **high twenties**. These are management targets, not a floor, but a fair adversarial note should explicitly test them against its historical stress argument. [S6]

I found no primary disclosure in this review that establishes a present foundry demand collapse or overturns the conclusion that TSMC is currently highly profitable. I also did not verify absolute current CoWoS monthly capacity, package-specific utilization, customer cancellation penalties, standalone Arizona returns or Samsung Foundry profit. These remain unknowns, not findings of absence.

## Summary-bullet assessment

| Bullet | Supported by the note's own evidence? | Technical usefulness and required change |
|---|---|---|
| 1: comfortably profitable, downstream returns unproven | **Yes.** Claims 1–3 directly support realized supplier earnings. The distinction from customer returns is sound. | Has figures but lacks a quarter. Insert **“In Q3 2026”** before the margin statement; retain the inference. |
| 2: operating cash exceeds spending; funding and first losses | **Yes for observed self-funding; incomplete funding description.** Claims 12–16 support liquidity. Equity is economically residual, but the exact sharing of a capacity shortfall depends on contracts and assistance. | **Too abstract: no figure or date.** Replace with edit 1; add edits 2–3 to the Analysis. |
| 3: HPC 68%, AI high teens | **Yes for the two disclosed metrics; qualify the interpretation.** The periods and definitions differ. The old accelerator share does not measure all current AI-linked demand. | Figures are useful, dates are vague. Use edit 6; do not calculate a current AI/non-AI split by subtraction. |
| 4: aggressive expansion, scarcity and future returns | **Directionally yes**, from claims 11, 19, 21 and 24. “Today's backlog” is not a quantified, contractually protected backlog in the evidence. | **Too abstract: no scale or date.** Replace with edit 4. |
| 5: overseas costs, subsidies, investment envelopes | **Yes**, chiefly claims 22–23 and 33, but public-support receipts deserve the missing detail above. Customer geography premiums are not quantified. | **Too abstract: no cost figure or horizon.** Replace with edit 5. |
| 6: Intel loss-making; Samsung unproven | **Yes**, from claims 31–32, with the correct warning against extrapolating TSMC economics. | **Too abstract: no loss figure or quarter.** Replace with edit 7. |
| 7: future demand risk, historical stress, Taiwan tail risk | **Supported as a qualitative risk judgment**, not as a measured probability or ranking of “biggest” risks. Claims 26–30 demonstrate cyclicality, and S34 describes Taiwan exposure. | **Too abstract: no historical scale/date or prospective checkpoint.** Replace with edit 10. |

## Your assessment

TSMC's observed operations and balance sheet support a low near-term funding-stress assessment, while its expansion leaves shareholders exposed to a later decline in utilization and investment returns. I agree with that central distinction and with treating Intel and Samsung separately. I differ from the note mainly in what deserves emphasis: current free cash flow is not the full expansion-funding story, customer advances and government receipts are economically relevant, and purchase commitments constrain flexibility. Overbuild should be assessed against dated commissioning and the remaining annual spending requirement, with tool scarcity as an opposing constraint. The narrow historical accelerator share is not a sufficient measure of today's AI sensitivity. Nothing checked here establishes that TSMC equity is cheaply priced, or that downstream AI investment earns its cost of capital; neither proposition follows from supplier profitability.

## Recommended edits

1. **Replace Summary bullet 2:** “In January–September 2026, TSMC generated NT$2,402.117bn of operating cash flow and spent NT$1,289.971bn on PP&E, leaving NT$1,112.146bn before dividends and NT$671.293bn after dividends. This supports low current funding stress; future factory returns remain shareholders' risk.” Add: “Meeting annual capex guidance would require US$19.36–23.36bn in Q4, versus US$13.84bn in Q3.” [S3][S2][S11]

2. **Add to the overseas/funding Analysis and narrow the claim that receipts are unknown:** “In Q3 2026, TSMC reported NT$198.74bn of other investing inflows, mainly attributable to US Treasury investment tax credits. This is not a separately disclosed tax-credit total or a CHIPS grant receipt; it is outside the operating-cash-flow-minus-capex calculation.” [S2]

3. **Add to the reservation and funding discussion:** “At December 31, 2025, customer capacity deposits were NT$189.858bn, with settlement by refund or receivable offset under agreed conditions. Capital and other purchase obligations were NT$1,534.575bn, including NT$1,220.393bn due within one year. These older balances show customer funding and spending commitments; they do not establish September 2026 balances or blanket cancellation protection.” [S34]

4. **Replace Summary bullet 4:** “TSMC guides to US$60–64bn of 2026 capex. Its October 15 plan places additional Tainan N3 production in H1 2027 and H1 2028 and Arizona fab 2 production in Q3 2027. Those commissioning dates make sustained demand and factory loading testable; absolute CoWoS capacity remains unverified.” [S11][S4]

5. **Replace Summary bullet 5:** “On October 15, TSMC expected overseas fabs to dilute 2026 gross margin by about 2 percentage points, widening to 3–4 points in following years. Its July US$265bn Arizona envelope is multiyear planned investment, not annual capex or a disclosed plant-level return.” [S4][S11]

6. **Replace Summary bullet 3:** “HPC supplied 68% of Q3 2026 revenue; narrowly defined AI accelerators supplied a high-teens share in FY2025. These are different periods and categories: neither figure establishes total current AI-linked revenue.” [S2][S6] Also date bullet 1 explicitly **Q3 2026**. [S1]

7. **Replace Summary bullet 6:** “Intel Foundry lost US$2.089bn on US$5.765bn segment revenue in Q2 2026, with only US$293m external revenue. Samsung's Q2 release describes Foundry improvement but supplies no standalone profit. Neither supports assigning TSMC's profitability to the whole foundry layer.” [S24][S25]

8. **Add opposing evidence to Conflicts:** “On October 14, ASML said planned 2027–2028 supply would fall short of customer demand; it plans 30% expansion in 2027 and is examining expansion beyond the previously indicated further 30% in 2028 for low-NA EUV and immersion DUV. Equipment scarcity can delay effective foundry supply.” [R9] Also add: “TSMC's January targets were at least 56% through-cycle gross margin and high-twenties ROE; these are management expectations to test, not guaranteed floors.” [S6]

9. **Add a contingent expansion signal:** “October 15: Texas evaluation and Terafab discussions remain exploratory; no final arrangement was announced, and TSMC requires operational control of the fab.” Do not count this as committed capacity. [S4]

10. **Replace Summary bullet 7:** “The investment risk is inadequate demand when new capacity becomes usable. Q2 2001 operating margin fell to 1.08% at 44% utilization; Q1 2009 operating margin was 3.1%. These illustrate fixed-cost downside, not a current break-even threshold. Taiwan disruption is a separate supply risk.” [S20][R10][S34]

11. **Reconcile source precision and improve grading:** Append to claim 12: “Presentation figures reproduced as published; the million-NT$ cash-flow statement implies Q3 FCF of NT$476.570bn, versus NT$476.56bn on the slide.” Cite claim 16 to S2's debt-service table and label its directly reported totals **A**, retaining **B** only if presented as the author's calculation. Describe claims 20 and 25's missing measurements as **not verified**, rather than giving the absence itself an evidentiary grade. [S3][S12][S2]

[S1]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/526b65af7305df2dde6b9ece6812b1fdf1e49f9b/3Q26%20EarningsRelease.pdf
[S2]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf
[S3]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/3a94d1034b9e6b22446b674f7aaf3d088a12a193/FS.pdf
[S4]: https://investor.tsmc.com/japanese/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf
[S6]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[S11]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[S12]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/9f58506f6f114f91cefbf86820cc63297b39b130/3Q26%20Presentation%20%28E%29.pdf
[S19]: https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/
[S20]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/english/2001/Q2/2q01fr.pdf
[S21]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/english/2001/Q3/3q01fr.pdf
[S24]: https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm
[S25]: https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results
[S34]: https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
[R1]: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000008/a4q25presentatione.htm
[R2]: https://pr.tsmc.com/schinese/news/3013
[R3]: https://pr.tsmc.com/system/files/newspdf/attachment/7809816e3f20b450e00a82f479cfc553c6f05138/2Q23%20%28E%29_with%20guidance_final_wmn.pdf
[R4]: https://pr.tsmc.com/english/news/3076
[R5]: https://pr.tsmc.com/english/news/3101
[R6]: https://investor.tsmc.com/chinese/monthly-revenue/2024
[R7]: https://investor.tsmc.com/english/monthly-revenue/2025
[R8]: https://investor.tsmc.com/english/monthly-revenue/2026
[R9]: https://investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026
[R10]: https://pr.tsmc.com/english/news/1548
