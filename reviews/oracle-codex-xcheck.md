# Oracle — independent Codex cross-check

*Review date and evidence cutoff: 2026-10-17. Reviewed `research/stack/oracle.md` against `report/methodology.md` and `tasks/RESEARCH_BRIEF.md`. USD billions unless stated otherwise. No changes to the research note.*

## Verdict

The central finding is supported: Oracle is profitable, but its infrastructure expansion requires outside funding and exposes it to execution and counterparty risk.
The 15 selected rows contain no material numerical transcription error; all Analysis calculations reconcile, but the funding illustration is not a complete liquidity forecast.
Revise the abstract Summary bullets, add October counterparty and permitting developments, and distinguish verified exposure from the judgment that Oracle is already “overextended.”

## Claim re-verification

Selection prioritizes the operating engine, cash deficit, customer financing, obligations, capital access and margin counterevidence on which the Summary and Analysis depend. “Matches” means the source supports the stated observation or management statement, not that management's forecast will occur. Dates below are observation dates; all retrievals were on 2026-10-17.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 2 | RPO conversion: 13% / 37% / 34% | 13% next 12 months; 37% months 13–36; 34% months 37–60, at August 31, 2026 | [10-Q, Note 1][Q] | Yes | A, management conversion estimate |
| 3 | OpenAI partnership >300 over five years; ratios 65.9% / 45.2% | >300 over five years; 300/455 = 65.934%; 300/664 = 45.181% | [OpenAI, September 23, 2025 announcement][O]; [FY26 Q1][E1]; [FY27 Q1][E5] | Yes; ratios are not customer shares | A announcement; B arithmetic; C if interpreted as a concentration proxy |
| 4 | OCI quarterly revenue/growth: 3.3/55%, 4.1/68%, 4.9/84%, 5.8/93%, 7.4/121%; FY26 18.1/77% | Same sequence, USD year-over-year growth | [FY26 Q1][E1], [Q2][E2], [Q3][E3], [Q4][E4], [FY27 Q1][E5] | Yes; OCI includes more than GPU rental | A |
| 5 | FY27 Q1 operating income 6.7; SaaS 4.2, +10% | GAAP operating income 6.728; SaaS rounds to 4.2, +10% | [September 10 release, income statement and highlights][E5] | Yes, rounding | A; does not isolate software or GPU profits |
| 8 | FCF −0.362, −9.967, −11.484, −1.873, −5.396; FY26 −23.686 | Same five standalone quarters; FY26 31.977−55.663 = −23.686 | [FY27 Q1 release, FCF table][E5] | Yes | A, explicitly published non-GAAP measure; B for independent reconstruction |
| 9 | Advances 11.363; manufacturer repayment 0.830; net outlay 17.966; adjusted OCF 11.740 | 28.499−11.363+0.830 = 17.966; 23.103−11.363 = 11.740 | [FY27 Q1 release, cash flows and net-outlay reconciliation][E5] | Yes; 0.830 is a **net financing outflow**, not necessarily gross repayments | A reported inputs/net outlay; B adjusted OCF |
| 10 | Borrowings 125.337; liquidity 37.077; net 88.260 | 7.625+117.712 = 125.337; 36.369+0.708 = 37.077; difference 88.260 | [10-Q, balance sheet][Q] | Yes; book borrowings, excluding leases | A components; B sums |
| 11 | Finance leases 9.185; operating leases 34.621; combined debt/leases 169.143; future leases 288, 15–19 years | Same; future leases expected to start FY27 Q2–FY29 | [10-Q, Note 6][Q] | Yes; distinguish recognized discounted liabilities from future contractual commitments | A inputs; B sum |
| 12 | May borrowings 129.541; liquidity 31.894; dividends 5.787; FY27/FY28 principal 7.210/10.145 | Same historical values and maturity schedule | [FY26 10-K, balance sheet, cash flows, Note 6][K] | Yes; historical dividends are an assumption when reused prospectively | A inputs; B liquidity sum |
| 16 | FY27 revenue ≥90; adjusted EPS 8.10; capex 90–95; net cash capex ≤70 | Same September 10, 2026 guidance | [Release][E5]; [Maxson's transcribed remarks][T] | Yes | A revenue/EPS statement; B capex statement from third-party transcript |
| 17 | CY26 raise 45–50; FY26 debt/equity 43/5; FY27 approximately 40 including ATM 20, completed in Q1 | Same plans; completion applies to the **20 ATM**, not the entire FY27 40 | [February plan][F]; [June release][E4]; [September release][E5] | Yes, but wording can imply too much funding is completed | A issuer statements; FY26 5 was mandatory convertible preferred equity |
| 18 | Prepaid/customer-supplied hardware portions 75 | 75 at FY26 year-end, combining both mechanisms | [June release, RPO discussion][E4] | Yes; not a cash receipt or an additional financing facility | A statement |
| 24 | S&P BBB/A-2 → BBB−/A-3, stable; July 9, 2026 | Same action in reporting | [Wisconsin reporting][R]; [Yahoo/Zacks][Z]; [S&P event page][SP] | Secondary corroboration only; S&P action text inaccessible | B; do not upgrade to A |
| 25 | Five-year CDS 288bp, +26bp overnight, October 15 | Same; Reuters identifies S&P Global Market Intelligence as the data provider | [Reuters/MarketScreener][C] | Yes to the dated Reuters report; underlying quote feed not independently obtained | B, not a current executable quote |
| 33 | Illustrative AI gross margin 35%; renewal premium 20%, mostly GPUs ≥4 years | Slide: 60 revenue, 39 costs, 21 gross profit, 35%; call repeats 20% renewal premium and age qualification | [Oracle analyst presentation][M]; [September call transcript][T] | Yes; illustration and selected renewals do not establish fleet-wide realized returns | A illustration; B transcribed management statement |

Retrieval limits: the 10-K and Magouyrk PDF were fetched directly after web extraction failed; the PDF's text was extracted locally. S&P's action page returned an access error, including a direct HTTP 403. Its own webinar page confirms a downgrade but does not establish the precise rating/date. The Zacks and some FT material was available as indexed text despite unsuccessful page opens. These limitations are not evidence that the claims are false. No primary CDS feed, private OpenAI contract, or audited standalone GPU income statement was obtained.

## Arithmetic checks

I recalculated every explicit derived quantity in Analysis, plus the table calculations that Analysis invokes. All equations below pass. The distinction is between correct arithmetic and adequate assumptions.

| Calculation | Independent result | Finding |
|---|---|---|
| FY26 quarterly OCF sum | 8.140+2.066+7.151+14.620 = 31.977 | Pass |
| FY26 quarterly capex sum | 8.502+12.033+18.635+16.493 = 55.663 | Pass |
| Five quarterly OCF−capex calculations | −0.362; −9.967; −11.484; −1.873; −5.396 | Pass |
| FY26 FCF, both methods | 31.977−55.663 = sum of first four quarterly FCFs = −23.686 | Pass |
| Q1 net capex outlay / OCF excluding specified advances | 17.966 / 11.740, as reconstructed in row 9 | Pass |
| Annualized adjusted OCF | 11.740×4 = 46.960 | Pass; C as an annual scenario, B as multiplication |
| FY27 funding need | 70−46.960+7.210+5.787 = 36.037 | Pass; before drawing opening liquidity |
| FY27 closing balance | 31.894+40−36.037 = 35.857 | Pass; conditional on the full raise |
| FY28 funding need | 70−46.960+10.145+5.787 = 38.972 | Pass |
| FY28 residual gap | 38.972−35.857 = 3.115 | Pass; assumes no liquidity floor |
| Stress capex midpoint | (90+95)/2 = 92.5 | Pass; FY27 guidance reused as an FY28 stress assumption |
| FY28 stress need / gap | 92.5−46.960+10.145+5.787 = 61.472; 61.472−35.857 = 25.615 | Pass |
| Opening liquidity, debt and lease sums | 31.289+0.605 = 31.894; row 10 totals correct; 125.337+9.185+34.621 = 169.143 | Pass |
| Illustrative backlog ratios | 65.934% / 45.181% → 65.9% / 45.2% | Pass; no measured concentration follows |
| Debt fair-value ratios used in securities discussion | 105.7/125.0 = 84.560%; 114.4/128.1 = 89.305% | Pass; not like-for-like bond total returns |
| Equity multiples used in securities discussion | 128.23/8.10 = 15.831×; 128.23/21 = 6.106× | Pass conditional on quoted price; distant adjusted EPS is not distributable cash |

Inputs: [quarterly cash tables][E5], [opening balances and maturities][K], [lease/debt disclosure][Q], [guidance transcript][T], [2025 EPS targets][D]. Yahoo price history did not open successfully; [StockAnalysis][P] independently displayed the same October 16 price, but that is not exchange verification. There is no additional numerical valuation model in Analysis to audit.

The gross/net funding explanation needs an explicit bridge: `(OCF−advances)−net outlay = OCF−gross capex−net manufacturer repayments`. Thus Q1 on the net-outlay basis is `11.740−17.966 = −6.226`, versus ordinary FCF of `−5.396`; the difference is the `0.830` financing outflow. The note recognizes the distinction but its “use either” wording can suggest equivalence without this adjustment. [Oracle reconciliation][E5]

The annual scenarios are explicitly conditional, so holding dividends and cash generation flat is not a transcription error. Nevertheless:

- A full-year model should roll forward from actual Q1 and separately track unrestricted cash, financing fees, dividends and finance-lease principal. The note already acknowledges several of these limitations; they should constrain the interpretation of its precise closing balances.
- Q1 cash dividends annualize to `1.565×4 = 6.260`, `0.473` above the scenario assumption. Substituting that run rate alone raises the two-year residual gap by `2×0.473 = 0.946`. This is a sensitivity, not guidance. [Cash-flow statement][E5]
- “External funding required” should mean the amount needed **to preserve opening liquidity**. Using cash or a revolver can meet a deficit without a new bond or equity issue. The FY28 scenario deliberately excludes a new raise; it is not evidence of a funding failure on that date.

## Omissions

**Recent developments searched: September 17–October 17, 2026.** The note already includes the September force-majeure story and October CDS stress. The following omissions materially sharpen or qualify that account:

1. **Jupiter permitting remains a live gate, with a new mitigation proposal.** On October 15 Oracle/YGI proposed a fuel-cell operating cap and roughly 35% lower projected permitted emissions, while asserting unchanged IT capacity. Its own statement calls the air-permit application pending. This is primary evidence for unresolved commissioning risk and an attempt to resolve it; neither a granted permit nor a proven loss of compute capacity. **A for the issuer's statement.** [October 15 release][J]

2. **Flood exposure and a subsequent schedule reaffirmation.** Oracle and STACK acknowledged flooding at Jupiter on September 30, stated that critical infrastructure was undamaged, and maintained the planned schedule. This updates the September 24 reporting and supplies direct counterevidence to an unqualified delay narrative. It does not independently establish the delivery date. **A as a joint statement.** [September 30 release][W]

3. **Power procurement has an explicit price.** Oracle's October 2 Point Beach proposal would absorb approximately $300m of rising energy costs and remains subject to Wisconsin commission approval. It shows both an attempt to obtain reliable power and an additional economic burden. The release does not establish an annual cost or incremental cost relative to the capex/operating model; do not simply add $300m to FY27 spending. **A announcement.** [October 2 release][B]

4. **OpenAI's latest reported revenue needs discussion.** FT reporting on October 8 put September annualized revenue near $50bn, versus previously circulated approximately $70bn; the discrepancy was attributed to grossing up partner sales for comparability. The private presentation was not obtained: **C, reported, unverified**. This is not proof of falling sales, a missed contractual payment or a $20bn cash shortfall. It does weaken arguments that equate headline customer revenue with readily available funds. Compare cash collections, operating costs, available financing and contractual payment milestones, not a five-year Oracle total with one year's revenue run rate. [FT report, indexed Yahoo republication][AIO]

Additional material omissions from the financial analysis:

- **Liquidity restrictions:** August restricted cash was about $2.6bn, outside reported cash equivalents. The net-debt calculation correctly excludes it; a cash-flow-to-liquidity bridge must also do so. **A.** [10-Q Note 1][Q]
- **Contractual rigidity:** unconditional purchase/other obligations totaled $34.150bn, including $6.176bn in FY28. Do not add these wholesale to capex or rent: map overlaps first. **A.** [10-Q Note 6][Q]
- **Preferred equity has a cost:** the FY26 equity financing was a 6.50% mandatory convertible issue. On $5bn liquidation preference, annual dividends are $0.325bn; settlement may use cash or shares, and automatic conversion is scheduled for January 15, 2029. This is different from ordinary common equity and matters for both cash needs and dilution. **A terms/B arithmetic.** [10-K Note 10][K]
- **Stronger contrary operating evidence:** management reported 97.9% utilization of its multi-tenant GPU fleet and more than $30bn of Q1 AI contracts without additional Oracle capital. Fleet selection and contract structure matter; neither proves consolidated returns. **B transcript/A contract announcement.** [Call][T], [release][E5]
- **An available primary source was missed:** the Magouyrk presentation directly contains the revised OCI outlook in row 14 and also states a 30–40% non-GAAP AI-infrastructure gross-margin range. That is stronger evidence of management's stated economics than the 35% example alone, though it still cannot reconcile the leaked margin to audited realized results. **A for presentation statements.** [Oracle slides][M]

## Summary-bullet assessment

| Bullet | Supported by the note's own evidence? | Clarity and needed treatment |
|---|---|---|
| 1 — profitable franchise cannot fund build | Broadly. Consolidated cash-flow evidence establishes the funding deficit; it does not separately measure the software franchise's cash contribution. | Too abstract: no period or magnitude. Use the dated consolidated comparison in edit 1. |
| 2 — negative FCF and advances | Yes. Rows 8–9 support the cash figures and financing interpretation. | Already concrete. Specify the amount and quarter of advances; avoid implying all ordinary deferred revenue is financing. |
| 3 — borrowings/net debt and leases | Yes. Rows 10–11 reconcile. | Add the balance-sheet date and quantify the future lease exposure; distinguish it from recorded debt. |
| 4 — OpenAI partnership and contract limits | Yes to the announcement. The precise contract rights are not established by the public announcement. | Add the announcement date. Prefer “not disclosed in the sources reviewed” to an exhaustive assertion about all public information. |
| 5 — alternative financing improves feasibility, not returns | Yes as an analytical inference from rows 17–18 and the project-financing discussion. | Too abstract: no scale, instrument cost or date. Edit 3 supplies an executed financing amount and a conditional plan. |
| 6 — observable credit stress | Yes, at secondary grade B. The note properly avoids turning CDS into proof of imminent default. | Add the observation/action dates; these are not live quotes or a fresh ratings affirmation. |
| 7 — OpenAI cash timing is largest uncertainty; Oracle is overextended | Partly. Counterparty and commissioning risks are supported. Their ranking as “largest,” and the unconditional characterization “overextended,” are judgments not demonstrated by a cash waterfall or contract review. | Too abstract and too categorical. Name the dated delivery gate and the conditional loss mechanism in edit 5. |

## Your assessment

Oracle presents a credible risk of capital earning inadequate returns, rather than evidence that an unprofitable operating business is already unable to meet its obligations. The note correctly distinguishes backlog from funded demand and developer debt from Oracle debt. I differ principally in how firmly I would label the company overextended: the record establishes large fixed commitments and reliance on capital access, but not a quantified inability to refinance or an expected project loss. Actual cloud growth, equity execution and customer-funded contracts are meaningful counterevidence. Conversely, pending permits, the cost of power, funding-instrument terms and uncertainty over the customer's cash generation deserve more weight than the note gives them. My conclusion is conditional financial fragility with unresolved project returns; the annual funding illustration is useful for sensitivity analysis, not a dated solvency conclusion.

## Recommended edits

1. **Replace Summary bullet 1:** “In FY2026, Oracle generated $31.977bn of operating cash but spent $55.663bn on capex: consolidated operations left a $23.686bn funding deficit before dividends and debt repayments.” Retain the existing results citation. This avoids attributing separately undisclosed cash generation to software.

2. **Date and quantify Summary bullets 3–4:** Replace bullet 3 with: “At August 31, 2026, Oracle had $125.337bn of borrowings, or $88.260bn after cash and securities, before leases; a further $288bn of uncommenced lease commitments extends its exposure beyond recorded debt.” Replace bullet 4's opening with: “OpenAI's September 23, 2025 announcement describes an Oracle partnership exceeding $300bn over five years.” End it with: “The underlying minimum purchases, termination rights and named customer share of RPO were not disclosed in the sources reviewed.” [Q], [O]

3. **Replace Summary bullet 5:** “Oracle completed its $20bn common-stock ATM program in Q1 FY2027; its approximately $40bn FY2027 financing plan includes that issuance, while customer prepayments and supplied hardware reduce Oracle's own funding requirement. These mechanisms improve fundability but do not establish investment returns.” In row 17, replace “completed in Q1” with “the $20bn ATM component completed in Q1”; describe FY26's $5bn equity as mandatory convertible preferred. [E4], [E5], [K]

4. **Date Summary bullet 6:** “Reuters reported five-year Oracle CDS at 288bp on October 15, 2026; secondary reports corroborate S&P's July 9 downgrade to BBB− with a stable outlook. These observations show credit stress, not imminent default.” Keep both claims at B. [C], [R], [Z]

5. **Replace Summary bullet 7:** “As of October 15, 2026, Jupiter's air-permit application remained pending. Oracle's exposure grows if commissioning or customer payments lag the equipment, lease and debt costs it must carry; public evidence does not quantify that timing gap or establish which risk is largest.” [J]

6. **Clarify the funding model immediately before its annual scenarios:** “The following is a flat-assumption sensitivity measured from May 31, 2026, not a forecast of unrestricted cash. Its funding requirement preserves opening liquidity. A usable forecast must incorporate actual Q1 flows, restricted cash, financing costs, common and preferred dividends, and finance-lease principal.” Add the exact reconciliation: “OCF excluding advances minus net capex outlay equals ordinary FCF minus net manufacturer-financing repayments.” Retain C for scenario outputs; classify pure arithmetic as B. [K], [Q], [E5]

7. **Add a dated paragraph to the delay discussion:** “On September 30, Oracle and STACK acknowledged flooding at Jupiter but reported no damage to critical infrastructure and reaffirmed the schedule. On October 15, Oracle/YGI proposed a fuel-cell operating cap intended to cut projected permitted emissions by about 35% without reducing IT capacity; the permit application remained pending. These are issuer statements, not independent confirmation of completion.” [W], [J]

8. **Add the missing counterparty update:** “On October 8, the FT reported that OpenAI's September annualized revenue was near $50bn, below the approximately $70bn previously circulated because partner revenue had been grossed up for comparison. This private-company figure is reported, unverified (C); it is neither collected cash nor evidence of a revenue collapse.” [AIO]

9. **Strengthen the margin and outlook sourcing:** Replace row 14's source with Oracle's Magouyrk presentation and its type/grade with “primary / A management outlook.” Add: “The October 16, 2025 slides also state 30–40% non-GAAP AI-infrastructure gross margins; the 35% six-year delivery example is illustrative, not a realized audited return.” Preserve the renewal evidence's narrower scope. [M]

10. **Add financing-cost and power qualifications:** “The $5bn preferred issue carries a 6.50% cumulative dividend, payable in cash or common shares, and mandatory conversion in January 2029; equity financing therefore has cash-cost or dilution consequences.” Add separately: “Oracle's October 2 Point Beach proposal would absorb approximately $300m of rising power costs, subject to regulatory approval; this is not an annual cost estimate.” [K], [B]

[Q]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
[K]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
[E1]: https://s23.q4cdn.com/440135859/files/doc_financials/2026/q1/1q26-pressrelease-September-final_.pdf
[E2]: https://investor.oracle.com/investor-news/news-details/2025/Oracle-Announces-Fiscal-Year-2026-Second-Quarter-Financial-Results/default.aspx
[E3]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Fiscal-Year-2026-Third-Quarter-Financial-Results/default.aspx
[E4]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/
[E5]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
[O]: https://openai.com/index/five-new-stargate-sites/
[T]: https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
[F]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-announces-Equity-and-Debt-Financing-Plan-for-Calendar-Year-2026/default.aspx
[R]: https://wiss.fm/news/2026/07/16/oracle-credit-rating-drops-amid-wisconsin-fight-over-data-center-credit-rules
[Z]: https://uk.finance.yahoo.com/news/oracles-credit-risk-nears-18-151000986.html
[SP]: https://www.spglobal.com/ratings/en/events/webinars/oracle-downgrade-explained
[C]: https://se.marketscreener.com/nyheter/cds-spreadar-inom-ai-vidgas-kraftigt-ce785dd3d980f124
[M]: https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-magouyrk.pdf
[D]: https://www.oracle.com/a/ocom/docs/corporate/financial-analyst-meeting-2025-kehring.pdf
[P]: https://stockanalysis.com/stocks/orcl/market-cap/
[J]: https://www.oracle.com/news/announcement/project-jupiter-microgrid-cuts-permitted-emissions-by-35-percent-2026-10-15/
[W]: https://www.oracle.com/news/announcement/project-jupiter-statement-on-southern-new-mexico-floods-2026-09-30/
[B]: https://www.oracle.com/news/announcement/oracle-announces-commitment-to-absorb-rising-point-beach-energy-costs-2026-10-02/
[AIO]: https://finance.yahoo.com/technology/ai/articles/openai-annualised-revenues-20bn-less-164234940.html
