# Independent cross-check: AI demand

*Review date: 2026-10-17. Fresh-context Codex review of `research/macro/demand-side.md`; methodology and research brief read. All external sources below were fetched or attempted on this date. Only this review was written; no git commands were run.*

## Verdict

Revise before publication: most checked disclosures match, but they do not validate the headline market-size reconstruction.
The claimed 2028 shortfall against a “combined-cohort requirement” is unsupported: the cited model explicitly disclaims that interpretation.
Retain “real demand, uncertain payback,” add omitted recent counterevidence, and distinguish assumptions, reported private financials and verified observations.

## Claim re-verification

I selected these 15 rows because they support the market-size estimate, accounting warning, cloud monetization, adoption, realized value, retention and payback conclusion. “Matches” means the cited statement was found, not that a forecast came true or private accounts were audited. A applies to a directly observed primary statement within its stated scope; C remains appropriate for private financial reporting and market estimates. D remains appropriate for the note's unsupported allocations. Internal CSV agreement is not independent verification.

| Claim # | Note's value | My value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | OpenAI ~$50bn net annualized; ~$70bn gross equivalent, end-September | Same reported amounts and accounting distinction. No primary September accounts located. | [Axios, Oct 8][axios]; earlier primary revenue anchor: [OpenAI, Mar 31][openai-march] | Yes, secondary report only | **C** for latest figures; do not promote to A |
| 2 | Anthropic ~$65bn July / ~$74bn latest run-rate; Q3 $16.8bn; Q2 $11.5bn; 2025 $4.6bn | All appear in cited report. $74bn is attributed to SemiAnalysis, not a company disclosure. Earlier company statement: run-rate exceeded $47bn in May. | [Euronews, Oct 15][anthropic-report]; [Anthropic, May 28][anthropic-primary] | Yes as reporting; different provenance within row | **C** for reported financials/estimate; **A** only for separately dated company statement |
| 4 | Microsoft AI >$37bn run-rate, +123%; M365 Copilot >30m paid seats | Same; AI metric in Apr 29 call for March quarter, seats in Jul 29 release for June year-end. | [FY26 Q3 call][ms-q3]; [FY26 Q4 SEC release][ms-q4] | Yes; mixed observation dates correctly separable | **A**, company metrics, not AI-only audited segment revenue |
| 5 | Google Cloud Q2 revenue $24.768bn, +82%; operating income $8.814bn | Same; 81.80% growth rounds to 82%. Segment includes TPU-system product sales as well as services; shared AI R&D sits partly outside segment. | [Alphabet Q2 SEC release][google] | Yes; scope caveat should include hardware | **A** for segment disclosures |
| 6 | AWS AI >$25bn annual run-rate; total AWS growth 36.7% | Both stated in Q2 release. AI and chips are separately named businesses; their run-rates must not be added without overlap information. | [Amazon Q2 release][amazon] | Yes | **A**, company-defined AI run-rate |
| 8 | Menlo 2025 enterprise GenAI $37bn; apps $19bn; excludes inference/model serving and embedded features | Same. Methodology uses 495 US enterprise AI decision-makers surveyed Nov 7–25, 2025 plus a market-sizing model. | [Menlo report and methodology][menlo] | Yes as an estimate, not a transaction census | **C** for market size; **A** for what methodology states |
| 11 | Census 23.8% current, SE 0.41pp; 27.7% expected, Sep 21–Oct 4; May 19.8%; wording changed Nov 2025 | Independently confirmed May 19.8% and wording change. Browser download page confirms Oct 8 release covers through Oct 4. Could not retrieve October national values: API fetch failed, direct HTTP returned 403, browser API navigation was blocked; workbook HTTP also returned 403. | [Census explanation][census-story]; [release/download page][census-download]; [attempted API][census-api] | **Partial; October values and SE not independently reproduced** | **A** for verified May/wording/release metadata. October claim remains unverified in this review; access failure alone does not justify regrading it as false or tertiary |
| 12 | Ramp September adoption 55.9%; Anthropic 43.8%; OpenAI 40.6%; +0.62pp overall; flat Aug–Sep token spend | Same. | [Ramp October index][ramp] | Yes, sample only | **A**, provider's observed sample |
| 13 | Ramp top 1% accounts for 80% of lab spend; $9,568 per employee, −3.1% versus July $9,873 | Same; also +11.7% month-on-month. Source warns this small cohort is volatile and revised. | [Ramp October index][ramp] | Yes; omitted rebound matters | **A**, sample only; global extrapolation would be D |
| 21 | Customer service: +15% resolved issues/hour; 5,172 agents | Same in Nov 6, 2024 revision; staggered introduction, not a universal productivity estimate. | [Authors' arXiv abstract][service-study] | Yes | **A**, studied setting |
| 27 | Annual-plan 12-month retention 21.1% AI / 30.7% non-AI; monthly 6.1% / 9.5%; first-year revenue/payer $30.16 / $21.37 | All match. Revenue/payer figures are **medians**; these app benchmarks do not measure enterprise contract renewals or margins. | [RevenueCat 2026 report][revenuecat] | Yes; specify medians and population | **A**, sample statistics |
| 32 | Gartner through-2030 cumulative requirement $8.5tn at 12% ROIC; attributable revenue ≤$3.6tn; owners earn <half | Same stated forecast. The revenue bound is for enterprise/consumer revenue **attributable to AI data centers**, not all economic benefits of AI. | [Gartner, Oct 14][gartner] | Yes as forecast; underlying model not reconstructed | **A** that Gartner states it, not A evidence of a realized shortfall |
| 33 | ~$300–470bn annual requirement for 2026 cohort; ~$535–850bn for combined 2024–26 cohorts | Recalculation: $295.34–467.85bn for an assumed $750bn **new** cohort; $535.56–848.37bn for an assumed $1.36tn **new** cohort. Current source expressly rejects treating this as previously deployed cohorts' remaining requirements. | [Current unit-economics worked model][unit-model]; primary boundary checks: [Microsoft][ms-q4], [Alphabet][google] | Rounded numbers broadly match; **cohort attribution does not** | **D** as an empirical payback claim; conditional calculation is reproducible, assumptions unverified |
| 38 | Gross $78bn/$225bn; overlap −$23bn/−$45bn; final $55bn/$180bn, 2025/26 | Same sums in CSV. No primary evidence establishes segment allocations or overlap amounts. Source anchors do not yield these values without additional assumptions. | [Project CSV][csv]; [Menlo][menlo], [Microsoft][ms-q3], [Amazon][amazon] | Arithmetic yes; end-user market size **not verified** | **D** |
| 39 | Bear 130/170/210; base 180/300/480; bull 230/440/800; cumulative 510/960/1,470 ($bn, 2026–28) | Same paths and sums. They imply 2026–28 annualized growth of 27.1%, 63.3% and 86.5%, respectively. No external source validates these chosen paths. | [Project CSV][csv]; [Gartner][gartner] provides a differently scoped external scenario, not validation | Arithmetic yes; scenario assumptions only | **D** |

For row 11, the original author's claim of API access is not a substitute for my own verification. I have not invented a replacement October value. This is a specific remaining verification gap, not evidence that the quoted numbers are wrong.

## Arithmetic checks

I recalculated all numerical derivations used in Analysis, including its referenced reconstruction/capture rows, and checked all 18 annual infrastructure-capture cells in the CSV. There is no addition or multiplication error in those cells. The principal problems are definitions and inference.

| Derivation | Independent calculation | Result |
|---|---|---|
| 2025 reconstruction | 20 + 30 + 23 + 5 = 78; 78 − 23 = **55** | Correct conditional on assumed inputs |
| 2026 reconstruction | 90 + 75 + 50 + 10 = 225; 225 − 45 = **180** | Correct conditional on assumed inputs |
| Cumulative 2026–28 revenue | 130 + 170 + 210 = **510**; 180 + 300 + 480 = **960**; 230 + 440 + 800 = **1,470** | Correct |
| 2028 infrastructure capture | 210 × (40%, 60%) = **84–126**; 480 × (40%, 60%) = **192–288**; 800 × (40%, 60%) = **320–480** | Correct; gross owner revenue before costs, not cash profit |
| ChatGPT subscriber/weekly-user quotient | 50 / 900 = **5.56%** | Rounded correctly; lower-bound counts with different populations do not establish a conversion rate. [Primary disclosure][openai-march] |
| NANDA funnel denominator observation | If the table's 5% implemented and 20% piloted share a base, 5 / 20 = **25%** | Supports the denominator caution; not a measured 95% pilot failure rate. Conditional arithmetic only; this report was not among the 15 re-verified rows |
| Ramp July comparison | (9,568 / 9,873 − 1) × 100 = **−3.089%** | Correct rounding to −3.1%. [Ramp][ramp] |
| Cloud growth cross-check | (24.768 / 13.624 − 1) × 100 = **81.797%** | Correct rounding to 82%. [Alphabet][google] |

The imported capital-recovery calculation is `R = [(2K/3)/A(10%, L) + (K/3)/A(10%, 15)] / 0.5`, with `A(r,n) = [1 − (1+r)^−n]/r`. For equipment lives of six and three years it gives the row-33 values above. The long-lived tranche lasts 15 years; the combined revenue is not required forever. Applying the same fresh-cohort formula to historical spending ignores earlier recoveries, remaining lives and commissioning dates. The source also does not identify all assumed capital as AI-only. Thus **480 < 535.56 is true arithmetic but not evidence of an actual 2028 capital-payback deficit**. [Worked model][unit-model]

The Goldman comparison is numerically correct but narrowly conditional: $800bn × 60% = $480bn exceeds the reported $417bn infrastructure hurdle by $63bn; $417bn / $800bn = **52.125%** is the necessary capture rate. At 40%, it falls short. The bank's original model was not obtained; the result cannot be generalized across capital bases or later buildout. [Cited secondary summary][goldman-summary]

Sequoia's $600bn heuristic includes a margin for the compute buyer; JPMorgan's $650bn is an investment-return requirement; Bain's $2tn concerns 2030. Treating these as different comparisons is appropriate, but merely matching the revenue layer does not reconcile capital vintages or cash-flow timing. Gartner's cumulative through-2030 comparison cannot be resolved using one year of 2028 revenue. [Sequoia][sequoia], [JPMorgan][jpm], [Bain][bain], [Gartner][gartner]

Two material, unstated assumptions deserve visibility. The overlap deduction falls from **29.49%** of gross layer sales in 2025 to **20.00%** in 2026 without a transaction bridge. The base path requires **66.7%** growth in 2027 and **60.0%** in 2028; “production deployments expand” is not a quantitative derivation of that growth. These are sensitivity choices, not arithmetic mistakes. [CSV][csv]

## Omissions

The recent-information search covered September 17–October 17, 2026, with earlier primary disclosures used where they improve the evidence hierarchy. These are the material additions, not a claim of exhaustive coverage.

- **The cited October spending source contains its own counterevidence.** Ramp reports an early-October AI-spend peak 1.5% above August. Its rebound and revision warning qualify the note's emphasis on persistent weakness; they do not invalidate the August–September observation. [Ramp][ramp]
- **A different billing panel contradicts a broad spending-stall interpretation.** CloudZero's October 13 report, updated October 14, follows 422 same-store customer organizations: median AI share of cloud bills rose from 2.66% in August to 3.02% in September. Separately, its survey says 87% plan larger FY2027 AI budgets, but only 10% characterize funding as net-new. This supports expanding demand and budget substitution simultaneously. Shares are not absolute dollar growth, and neither panel represents the entire economy. Grade A for sample statements. [CloudZero][cloudzero]
- **Reported lab profitability is omitted from a source already used for revenue.** The October 15 Anthropic report also describes a second consecutive adjusted-profit quarter, positive free cash flow on the reported adjusted basis and an 11% operating margin. Definitions and primary accounts remain unavailable. This is C-grade counterevidence to blanket cash-burn assumptions, not proof of GAAP profitability or sustainable financing. [Euronews][anthropic-report]
- **Debt exposure already exists; it is not only a later stage.** CoreWeave completed $4.2bn of 2.875% convertible senior unsecured notes on September 22, maturing in 2033. Creditors bear risk while equity financing remains available; priority and guarantees govern ultimate recovery. The note's loss sequence is too categorical. Grade A for debt terms; loss implications are analytical. [SEC 8-K][coreweave]
- **Earlier, better primary anchors are missing from the reconstruction.** OpenAI disclosed $2bn monthly revenue in March; Anthropic disclosed the May milestone in the claim table above. These support scale but cannot authenticate later leaks. OpenAI's September 8 update also reports over 1bn weekly users and 2.5m businesses—newer adoption evidence, without a comparable new paid-subscriber denominator. [OpenAI March][openai-march], [Anthropic May][anthropic-primary], [OpenAI September][openai-sept]
- **The model lacks an operational boundary for final demand.** It admits that training purchases may have no end customer but deducts only one lump-sum “overlap.” Removing double-counted supplier invoices is different from excluding externally financed training purchases or subsidy-funded consumption. Conversely, internal AI cost savings and incremental advertising cash flow can fund owned infrastructure without appearing as separately sold AI products. A narrow AI-product numerator cannot settle the return on broad corporate capex. This is a boundary objection, not an invented estimate of omitted benefits. [CSV][csv], [worked model][unit-model]
- **The internal dependency has already been corrected.** The current unit-economics note disclaims both the combined-cohort interpretation and the unsupported tokens-to-dollars inference. The demand note's Conflicts paragraph describing the older version is now stale. [Current source][unit-model]

## Summary-bullet assessment

1. **“Demand is real; capital payback remains unproven … $55bn/$180bn.” Partly supported.** The first sentence follows from the verified disclosures and unresolved economics. The totals are declared judgments but lack a reproducible derivation from sales to allocations to eliminations. A $130–230bn band is not evidence that the actual market falls within it. This bullet has figures and dates; its problem is evidential status. Use edit 1.
2. **“Lab run-rates require accounting reconciliation …” Supported as reported evidence.** Appropriate caution and C grades. However, the Anthropic figures are a dated sequence with different provenance, not a statistical range. Add dates and distinguish the outside estimate. Use edit 10.
3. **“Microsoft, AWS and Google disclose substantial monetization …” Supported, but too abstract.** No figure or date, despite strong company disclosures. It also leaves the reader unable to distinguish an AI run-rate from quarterly total-cloud sales. Use the concrete sentence in edit 3.
4. **“Adoption is broadening … 23.8% versus 55.9% … wording explain[s] much …” Partly supported.** Different populations and measures make direct comparison invalid; the note does not quantitatively establish what explains “much” of the gap. The October Census figures remain unreproduced in this review. This bullet already has figures but needs dates, a narrower explanation and resolution of the verification gap. Use edit 4.
5. **“Productivity gains exist … App margins and retention vary sharply.” Directionally supported, but too abstract.** The studies and app data support heterogeneity, not a measured economy-wide conversion from saved time to cash margins. No number or date makes it useful to a technical reader. Use edit 5; do not generalize consumer subscription retention to enterprise software.
6. **“Profitable incumbent franchises … Equity bears initial losses …” Partly supported and too abstract.** Company profits and funding announcements support the financing mechanism, but the note has no specific financing example in its Summary. Debt can be exposed immediately, and contractual loss allocation is not a universal chronological sequence. Use edit 6.
7. **“The base path reaches $480bn … falls short of … combined-cohort requirement.” Unsupported as an empirical conclusion.** The scenario figure is reproducible; its comparison benchmark is misidentified. Capture is important, but the note has not established that it is the single largest uncertainty relative to market size, asset scope, remaining lives, costs and funding. Replace the bullet as in edit 2.

## Your assessment

The evidence supports substantial paid AI demand and considerable uncertainty about who captures enough cash to earn a return. I differ from the note principally in refusing to turn its uncalibrated market reconstruction and a misidentified capital-recovery model into a measured payback gap. The note is careful about run-rates, overlapping sales and sample limitations, and most checked quoted values survive. Its balance is weaker: recent spending rebounds and reported adjusted lab profitability deserve the same visibility as spending softness and retention concerns. Neither those additions nor the existing bear evidence establish aggregate profitability. The next useful analytical step is a company- and cohort-specific bridge from external customer receipts to supplier payments, operating costs and dated capital recovery, with internally realized benefits treated explicitly. Until that exists, the revenue paths are illustrative stress scenarios, and “real demand, uncertain payback” is the defensible conclusion.

## Recommended edits

1. **Relabel the headline reconstruction and expose the missing bridge.** Replace Summary bullet 1 with: “Paid AI demand is substantial, but capital payback remains unproven. Our illustrative AI-product spending assumptions are $55bn for 2025 and $180bn for 2026, with $130–230bn used for 2026 scenarios; these are not independently measured market totals.” In Analysis add: “The segment allocations and $23bn/$45bn overlap deductions are judgmental inputs, not outputs of a verified invoice-level reconstruction.” To upgrade them, show company sales by period, gross/net treatment, app/compute allocation and each elimination. Retain D grades until then. [CSV][csv]

2. **Correct row 33, Summary bullet 7 and the payback paragraph together.** Replace row 33's value with: “Hypothetical new-cohort model: $750bn capital requires $295–468bn annual revenue; $1.36tn requires $536–848bn, assuming 3–6-year equipment life, 15-year long-lived infrastructure, 50% owner EBITDA margin and 10% discount rate; not an estimate for actual 2024–26 cohorts.” Replace Summary bullet 7 with: “The illustrative base path assumes $480bn of end-user revenue in 2028 and $192–288bn of infrastructure revenue at 40–60% capture. Comparison with a hypothetical capital-recovery model does not establish the actual buildout's payback gap.” In Analysis replace the first two payback-comparison sentences with: “The base scenario is numerically below the hypothetical $1.36tn new-cohort requirement, but the asset populations, revenue boundaries and recovery schedules are not matched.” [Worked model][unit-model]

3. **Give Summary bullet 3 concrete, correctly scoped numbers.** Replace it with: “Microsoft reported an AI run-rate above $37bn for the March 2026 quarter; AWS reported above $25bn for Q2. Google Cloud recorded $24.768bn in Q2 revenue, including non-AI services and TPU hardware; these overlapping measures cannot be summed as end-user AI demand.” [Microsoft][ms-q3], [Amazon][amazon], [Alphabet][google]

4. **Remove the unsupported explanation of the adoption gap and finish the Census check.** Replace Summary bullet 4's second sentence with: “Census measures employer businesses' reported AI use; Ramp measures payments among its customers, so their rates are not directly comparable.” Date the figures Sep 21–Oct 4 and September 2026 respectively. Before presenting the October Census value as independently reviewed, reproduce the national current/expected-use rows and SE from the API or workbook; this review could verify only release metadata and the older baseline. [Census][census-download], [Census wording][census-story]

5. **Make Summary bullet 5 measurable.** Replace it with: “A November 2024 study found 15% more issues resolved per hour among 5,172 support agents. RevenueCat's 2026 sample reports 12-month annual-plan retention of 21.1% for AI apps versus 30.7% for non-AI apps; neither result establishes enterprise-wide cash returns.” Add “median” before the row-27 first-year revenue/payer figures. [Study][service-study], [RevenueCat][revenuecat]

6. **Replace the abstract financing bullet and categorical loss sequence.** Replace Summary bullet 6 with: “Anthropic announced $65bn of funding in May 2026; CoreWeave issued $4.2bn of convertible senior unsecured debt in September. Both equity and debt finance the buildout; loss allocation depends on leverage, guarantees and contracts, while audited standalone lab profitability remains unresolved.” [Anthropic][anthropic-primary], [SEC][coreweave]

7. **Balance the Ramp passage and signal.** Append: “September top-cohort spending rebounded, and early-October spending reached a new high; the small-cohort estimates are volatile and revised.” Keep the August–September observation explicitly dated. [Ramp][ramp]

8. **Add the omitted lab profitability counterevidence.** In Conflicts add: “October reporting describes Anthropic's second consecutive adjusted-profit quarter and an 11% operating margin; the figures remain reported, unverified, with no public reconciliation establishing GAAP profitability or durable free cash flow.” Grade C. [Euronews][anthropic-report]

9. **Add a recent independent spending-panel comparison.** In Analysis add: “CloudZero's October 2026 panel reports rising median AI share of cloud bills in September, while its separate finance survey points mainly to budget reallocation. This challenges extrapolating one panel's spending stall to the whole market.” Include the dated observations specified under Omissions, their separate populations and the distinction between spend share and spend dollars. [CloudZero][cloudzero]

10. **Update provenance and stale dependencies.** In row 2 and Summary bullet 2, replace “$65–74bn” with “a reported ~$65bn July run-rate and an outside ~$74bn estimate cited on October 15.” Add the primary lab anchors and newer September OpenAI adoption disclosure identified above, without substituting them for verified September financials. Replace the stale unit-economics Conflicts bullet with: “The current unit-economics note rejects a combined historical-cohort payback interpretation; the demand scenarios therefore do not quantify an observed funding or return deficit.” [Anthropic report][anthropic-report], [Anthropic primary][anthropic-primary], [OpenAI March][openai-march], [OpenAI September][openai-sept], [unit-economics][unit-model]

[axios]: https://www.axios.com/2026/10/08/openai-50-billion-arr-anthropic-revenue-accounting
[anthropic-report]: https://www.euronews.com/2026/10/15/anthropic-revenue-jumps-46-to-168bn-as-ai-firm-eyes-record-2-trillion-ipo-valuation
[anthropic-primary]: https://www.anthropic.com/news/series-h
[openai-march]: https://openai.com/index/accelerating-the-next-phase-ai/
[openai-sept]: https://openai.com/index/the-work-now-within-reach/
[ms-q3]: https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3
[ms-q4]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm
[google]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[amazon]: https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
[menlo]: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
[census-story]: https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
[census-download]: https://www.census.gov/hfp/btos/data_downloads
[census-api]: https://www.census.gov/hfp/btos/api/periods/110/data
[ramp]: https://ramp.com/data/ai-index-oct-2026
[service-study]: https://arxiv.org/abs/2304.11771
[revenuecat]: https://www.revenuecat.com/state-of-subscription-apps
[gartner]: https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030
[unit-model]: ../research/theory/ai-unit-economics.md
[csv]: ../data/ai-revenue-estimates.csv
[goldman-summary]: https://advisoranalyst.com/2026/10/15/ai-capex-required-revenues-and-what-the-market-is-actually-pricing.html/
[sequoia]: https://www.sequoiacap.com/article/ais-600b-question/
[jpm]: https://am.jpmorgan.com/au/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/evaluating-ai/
[bain]: https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/
[cloudzero]: https://www.cloudzero.com/blog/ai-economics-pulse-october-2026/
[coreweave]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm
