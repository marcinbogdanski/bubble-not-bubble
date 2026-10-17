# Independent cross-check: AI debt markets

*Review date and information cutoff: 2026-10-17. Reviewer: Codex / OpenAI, fresh context. Reviewed `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, `research/TEMPLATE.md`, and `research/macro/debt-markets.md`. All external sources below were accessed during this review on 2026-10-17. No changes to the research note.*

## Verdict

Mostly reliable on financing structures and arithmetic; revise before using it as a current credit-risk summary.
The main weaknesses are omitted September financing and customer advances, an uninformative mixed financing total, and unresolved bond-price versions—not demonstrated widespread defaults.
The evidence supports differentiated funding stress, but neither quantifies where aggregate losses concentrate nor establishes that profitable hyperscalers can self-fund their buildouts.

## Claim re-verification

Selected exactly 15 rows: **2, 6, 12, 16, 18, 21, 22, 23, 25, 28, 29, 30, 35, 39, 40**. These support the Summary's issuance corrections, size estimates, contractual protections, credit-stress comparison, and refinancing argument. Supporting inputs to row 40 were also checked without counting them as additional selected rows. Dollar figures are billions unless stated otherwise.

Grades follow the repository methodology. An issuer announcement is primary evidence of announced terms, not independent assurance of repayment. A forecast can be grade A as an accurately attributed forecast. An inaccessible source is a verification limitation, not proof that the claim is false.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 2 | Meta May 2026: $25 face/$24.91 net; 2031–2066; 4.55–6.45%; T+53–147bp | Same. The 10-Q distinguishes face issuance from cash proceeds; the pricing sheet confirms the maturity, coupon and spread endpoints. | [Meta Q2 10-Q, Note 8 and liquidity][meta]; [April 30 pricing sheet][meta26] | Yes | **A** |
| 6 | Alphabet June equity/preferred net proceeds $49.6; mandatory conversion May 2029 | Same aggregate proceeds; conversion is on/about **May 15, 2029**, unless earlier converted. This is equity financing, including preferred dividends and dilution, rather than bond principal. | [Alphabet Q2 10-Q, Note 11][goog] | Yes | **A** |
| 12 | Meta 84 + Alphabet 101.085 + Amazon 132.995 + Microsoft 46.136 + Oracle 130.105 = 494.321 | First three amounts reproduced directly. Oracle's 130.105 appears in an indexed SEC annual-report extract; its full document did not fetch. Microsoft's 46.136 could not be independently reproduced despite verifying the filing's existence. The five supplied numbers do sum to 494.321. | [Meta][meta]; [Alphabet][goog]; [Amazon][amzn]; [Oracle SEC indexed document][orclindex]; [Microsoft filing index][msftindex] | **Partial verification**, not a five-company certification | **A** for directly retrieved balances; **B** for the conditional sum. Original B is reasonable, but this review cannot clear the whole row. |
| 16 | Jupiter $18 loans; 89–91 cents; stalled syndication, September 18 | Same in Reuters' republication of the FT report, including Santander/Jefferies indications. No executed-trade record, loan agreement, or bank allocation register retrieved. | [Reuters/AOL, September 18][jupiter] | Yes, **as reporting only** | **C**, reported, unverified; Reuters repeating FT is not independent confirmation |
| 18 | Beignet/Hyperion $27.3 securities, PIMCO majority; Meta/Blue Owl 20/80; four-year initial leases; capped conditional support over first 16 operating years | Same. Counsel identifies the offering and majority investors; Meta specifies the ownership and residual-value mechanism. The guarantee is not a blanket guarantee of all bond payments. | [Investors' counsel][beignet]; [Meta transaction announcement][metajv] | Yes | **A** for disclosed structure; actual recovery remains unmeasured |
| 21 | October 15: Beignet <91, QTS <87, Hut Louisiana ~93/Texas ~91 | Accessible FT republication dated October 16 instead says **<92, <88, ~94/~92**, respectively. The cited Yahoo versions failed to fetch; the FT original exposed a subscription page. No primary dealer/TRACE observations retrieved. | [FT/BizNews republication][pricesalt]; [FT original][pricesft] | **Exact marks unresolved**; direction agrees. Different versions/timestamps could explain it. | **C** for attributed indicative prices; do not certify the note's precise marks or treat republication as a second independent source |
| 22 | CoreWeave gross 35.551; net recourse/non-recourse 31.405/3.663; DDTL 1.0/2.0 1.300/3.190, 15%/11%, March 2028/August 2030 | All reproduced in Note 10. Net amounts deduct issuance costs; effective rates are not necessarily contractual cash coupons. | [CoreWeave Q2 10-Q, Note 10][crwv] | Yes for June 30; not an October balance | **A** |
| 23 | DDTL 4.0 up to 8.5, A3/A(low), SOFR+225bp/~5.9%, March 2032; DDTL 5.5 2.6, SOFR+550bp, five-year debt/three-year average contracts | Same. Additional qualifications: 4.0 initially permits about **7.5**, increasing to 8.5 upon stabilization; 5.5 is **Ba2/BB+**, not investment grade. | [March 31 SEC release][crwv4]; [August 10 SEC release][crwv55] | Yes; material qualifications omitted | **A**, including issuer-reported facility ratings |
| 25 | Lambda up to 0.5 older facility; October 1 facility 1.008, 6.78%, Baa1/A(low), fully amortizing to May 2033, marketed to insurers | Same; final maturity **May 30, 2033**. New facility funds three deployments for **two investment-grade offtakers**, with draws linked to commissioning. Closing a delayed-draw commitment does not establish full funding. | [2024 issuer release][lambda24]; [October 1 issuer release][lambda26] | Yes | **A** for announced terms; insurer marketing does not identify final holdings |
| 28 | TeraWulf 3.2 secured notes due 2030; Google support starts with each lease, with payment/assumption alternatives | Same. Issuer is **WULF Compute LLC**; 7.75% notes mature October 15, 2030. Filing also describes a Google affiliate's undertaking to the collateral agent, tied to the recognition agreements' timing. | [TeraWulf Q2 10-Q, Notes 8 and 10, HTML equivalent of cited PDF][wulfhtml] | Yes; identify the subsidiary borrower | **A** |
| 29 | June 9 Anthropic transaction 35, Apollo/Blackstone, Fluidstack sites | Same announced initial AI XPV tranche. Release does not supply the funded balance, debt/equity breakdown, or all guarantee terms. | [Broadcom announcement][avgo] | Yes as transaction size; **not verified debt outstanding** | **A** for announcement only |
| 30 | CoreWeave CDS >1,000bp; approximately 63–64% cumulative five-year implied default probability | Reuters reports >1,000bp using LSEG data; its explainer gives **about 63%**. The cited Swedish 64% version was inaccessible. No vendor curve, recovery assumption, or contract identifier was retrieved. | [Reuters/Economic Times market report][cds]; [Reuters explainer][cdsex] | Main quote and 63% reproduced; 64% not independently cleared | **C** for the composite claim; a quoted model-implied probability is not an objective default forecast |
| 35 | September Baa 6.47% minus Aaa 6.03% = 0.44pp; October 15 HY OAS 3.23pp | Exactly reproduced from downloaded FRED CSV observations. **44bp** Baa–Aaa differential; **323bp** HY OAS. The former is a monthly yield-quality differential, not a matched-maturity OAS. | [FRED BAA/AAA CSV][fred]; [ICE/FRED HY CSV][fredhy] | Yes | **A** for observations; **B** for subtraction |
| 39 | S&P capex >1.3T **in** 2027; six hyperscalers negative FOCF in 2026/27 | Release says >1.3T **by** 2027; all six negative FOCF in 2026/27; recovery not projected until **2029**. Its six are Alphabet, Amazon, Microsoft, Meta, Oracle and SpaceX. | [S&P, August 27][sp] | Forecast attribution matches; retain source's “by” wording and disclose universe/recovery horizon | **A**, forecast, not an observed cash-flow result |
| 40 | 572.472 snapshot subtotal; 65.4 construction; 35 chip transaction; 50 later issuance; 722.872 extended | Arithmetic exactly matches. Project components reproduce 42.6. Corporate input verification inherits row 12's limitation. Construction includes a preliminary reported Vantage package. September CoreWeave issuance is missing from the later-flow map. | Rows above; [QTS counsel][qts]; [Hut results][hutq]; [Newmark phase 1][abilene1]/[phase 2][abilene2]; [Vantage report][vantage]; [Alphabet August terms][googaug]; [CoreWeave September 8-K][crwvsep] | **Arithmetic yes; current exposure total no** | **B** for arithmetic on verified primary inputs; **C** for mixed coverage/commitments. No grade makes it AI-only outstanding debt. |

**Retrieval limits.** Microsoft’s annual-report body failed through web fetch, direct HTTP, and Chrome (SEC access-denied page); its filing index was accessible. Oracle’s May annual-report body also failed, although search returned its primary-source principal schedule. Oracle’s newer August 10-Q fetched normally. Yahoo/FT price access limits and the inaccessible Swedish CDS version are disclosed above. FRED downloads succeeded via direct HTTP after web fetch failed. No unobserved market price or inaccessible filing value has been represented as newly verified.

## Arithmetic checks

Every explicit derived amount in **Analysis** is in its financing table. No numerical loss rate, debt-service coverage ratio, interest bill, or default probability is actually calculated in that section. I recalculated its amounts using decimal arithmetic:

| Analysis item | Recalculation, $B | Result |
|---|---|---|
| Corporate principal | 84 + 101.085 + 132.995 + 46.136 + 130.105 | **494.321**, correct conditional on the inputs; row 12 retrieval limits apply |
| Selected project securities | 27.3 + 4.6 + (3.25 + 4.25) + 3.2 | **42.600**, correct |
| Principal/securities subtotal | 494.321 + 35.551 + 42.600 | **572.472**, correct |
| Abilene component | 2.3 + 7.1 | **9.4**, correct; the two separate Newmark releases are necessary to support both phases |
| Construction package total | 9.4 + 38 + 18 | **65.4**, correct; does not demonstrate 65.4 of binding, still-outstanding commitments |
| Later Amazon/Alphabet USD issuance | 25 + 25 | **50**, correct; gross flow, not net debt change |
| Extended total | 572.472 + 65.4 + 35 + 50 | **722.872**, correct arithmetic; heterogeneous economic meaning |
| Summary rounding | 572.472 → 572.5; 722.872 → approximately 723 | Correct |

The project inputs are supported by [counsel for Beignet investors][beignet], [QTS purchasers' counsel][qts], [Hut's aggregate project-financing disclosure][hutq], and [WULF's principal balance][wulfhtml]. Amazon's subsequent issuance is disclosed in its [June 10-Q][amzn]; Alphabet's [August pricing sheet][googaug] contains fixed and floating tranches, both needed for its total.

Two additional reconciliations guard against apparent errors:

- **CoreWeave gross versus net:** 31.405 + 3.663 = 35.068; adding 0.427 + 0.056 of discounts/issuance costs gives **35.551**. The difference is explained, not missing debt. [Note 10][crwv]
- **Broad-credit comparison:** 6.47 − 6.03 = **0.44 percentage points = 44bp**; 3.23 percentage points = **323bp**. Comparing the two as identical credit-spread measures would be a definition error. [FRED yields][fred], [HY OAS][fredhy]

The arithmetic is not the problem with the extended total. Issuance flows may refinance existing principal, commitments may remain undrawn, and a transaction's capital can include equity. Adding these can describe selected financing announcements, but cannot measure outstanding credit, incremental exposure, or potential loss. Simply adding the newly identified September issue would make the old sum **727.072**, not a defensible October debt balance; repayments and subsequent draws would still be missing.

## Omissions

**1. Material new financing within the last 30 days: CoreWeave, September 22.** A primary 8-K confirms a **$4.2B** convertible issuance at **2.875%**, due **2033**, including the exercised purchaser option. Net proceeds before estimated expenses were **$4.137B**; capped calls cost **$0.5662B**, leaving approximately **$3.5708B** before those expenses for other uses. This is both additional borrowing and evidence that financing remained available. It must not be compared with straight-debt yields without accounting for the conversion option. [September 22 8-K][crwvsep] The June balance is legitimately dated, but selectively updating Amazon/Alphabet while omitting this transaction leaves the map unevenly current.

**2. A contract dispute within the last 30 days: Project Jupiter, September 24.** Reporting says Oracle sent a force-majeure notice; Oracle's quoted response maintained its planned schedule. The notice's actual terms and legal effect were not independently obtained. This should be labelled **reported, unverified (C)**, not treated as established rent cancellation or default. [Axios, September 24][jupnotice] On **October 13**, Oracle directly stated that Jupiter's scope had not changed beyond its April power-plan update—useful counterevidence, but no proof that financing or permitting risks disappeared. [Oracle announcement][juporacle] This is a concrete test of the note's otherwise abstract lease-commencement mechanism. Reports of continuing carry-cost obligations are another verification target; no authenticated contract was retrieved to resolve them.

**3. New primary research within the last 30 days: circular financing, October 1.** BIS authors find that **46.4% by value** of AI-to-AI investment deals in **2021–2025** also involved a commercial supply-chain relationship. This is a historical investment-deal statistic published recently, not a percentage of current AI debt. It strengthens the case that customer demand, financing and collateral support can fail together. Circularity can also secure scarce inputs, so it is not itself proof of fictitious demand. [BIS Bulletin 137][bis137]

**4. The current cash-flow cushion needs a source-based bridge.** Oracle's **September 10** results, outside the strict September 17–October 17 window but available before the note, show **$23.103B** operating cash flow, **$28.499B** capex and **−$5.396B** free cash flow for the August quarter. Operating cash flow included **$11.363B** of customer advances with a significant financing component. Removing that inflow gives an illustrative **−$16.759B** OCF-minus-capex figure, not Oracle's reported FCF. [Oracle results][orclresults] The August 10-Q explains that these advances produce interest expense and deferred revenue; it also records **$19.909B** net common-equity proceeds. [Oracle August 10-Q][orclq] This is a more informative account of funding than “profitable businesses provide a cushion,” while the equity raise is real loss-absorbing capital.

**5. Future lease burdens are omitted rather than separately displayed.** Meta disclosed **$278.99B** of leases not yet commenced at June 30 plus **$68B** signed in July. [Meta 10-Q][meta] Oracle disclosed **$288B** of additional leases not on its August balance sheet, expected to commence from fiscal Q2 2027 through fiscal 2029, for **15–19 years**. [Oracle August 10-Q][orclq] These undiscounted future obligations should not be added wholesale to project debt, but they matter to the tenant's ability to keep supporting outside borrowers. A separate contractual-obligations panel would preserve both facts: possible overlap and substantial economic obligations.

**6. Immediate liquidity and differences between facilities need more prominence.** CoreWeave's maturity schedule includes **$4.413B in the remaining part of 2026**, omitted from the note's selected 2027–2030 maturity presentation. [CoreWeave Note 10][crwv] DDTL 5.5's below-investment-grade ratings belong beside its shorter contracts. [August release][crwv55] Conversely, Lambda's October transaction has two investment-grade offtakers and draws linked to commissioning, strengthening the note's counterevidence against an indiscriminate financing shutdown. [Lambda release][lambda26]

**7. An older preliminary financing package is presented too firmly in the total.** The September 2025 Vantage report says the Wisconsin arrangements were still under discussion and pricing preliminary. [Bloomberg Línea][vantage] It supports a reported proposed package, not independent verification of today's final construction commitments. This matters to Summary bullet 3's wording even though the table already assigns grade C.

**8. Price discounts do not isolate credit risk.** The note correctly rejects equating marks with realized losses, but par discounts alone also combine interest-rate duration, credit, liquidity, amortization and other terms. The accessible FT version's different marks reinforce the need for a bond identifier and observation time. CDS contributes separate evidence of credit repricing, but there is still no documented portfolio-wide loss estimate. [FT republication][pricesalt], [Reuters CDS report][cds] “Tight aggregate spreads” should be qualified as a description of specified indicators, or supported with a historical benchmark.

## Summary-bullet assessment

| Bullet | Supported by its own evidence? | Usefulness and required correction |
|---|---|---|
| 1. Risk concentrated in construction/customer finance/residual values; hyperscaler cushion | **Partly.** Its transactions demonstrate these mechanisms, not the distribution of aggregate expected losses. Claim 39 itself qualifies the cushion. No cash-flow coverage analysis is supplied. | Too abstract: no figure/date and “concentrated” sounds measured. Replace with the dated funding example in edit 1. |
| 2. Meta net versus face; Alphabet equity not debt | **Yes.** Claims 2 and 6 support both corrections. | Concrete amounts, but missing transaction dates and overly editorial “cited.” Edit 2 makes it standalone. |
| 3. $572.5B/$723B perimeter | **Arithmetic yes; economic interpretation limited.** Caveats are welcome, but adding stocks, flows and provisional commitments still creates an attractive but non-comparable headline. | Has figures but no useful common measurement date. Keep the historical subtotal with verification caveats; display other categories separately (edit 3). |
| 4. Project vehicles, commencement/termination/guarantees determine who pays | **Yes**, notably claims 18, 19 and 28. The named hyperscaler is not automatically the note issuer or unconditional guarantor. | Too abstract: supply one identifiable transaction and its contract lengths (edit 4). |
| 5. October prices/CDS show selective stress, not realized losses | **Directionally yes.** Claims 21, 30, 31 and 35 support sector differentiation. Exact project prices need version reconciliation; a bond discount is not pure credit spread. | “October” is insufficiently precise. Use dated CDS and OAS observations; describe their definitions (edit 5). |
| 6. Insurer/pension participation, aggregate exposures unknown | **Yes as an evidence-limit statement.** Named participants support presence, not quantified holdings. CDPQ and BCI are institutional investment managers; do not imply every allocation is a pension's direct balance-sheet position. | Too abstract: identify the participants and deal dates; retain the absence of look-through (edit 6). |
| 7. Customer payments and collateral may fail together | **Yes as a reasoned risk hypothesis**, not a quantified finding that this is objectively the single largest risk. Claim 23 supplies a concrete example. | Too abstract: name the facility and contract/debt mismatch (edit 7). |

For bullet 6, I additionally checked [Blackstone's May 2024 announcement naming CDPQ][crwv24] and [Crusoe's announcement naming BCI and Liberty Mutual Investments][crusoe]. These verify participation; they do not identify today's ultimate holder allocations. The March 2026 CoreWeave release independently identifies insurance investors. [CoreWeave release][crwv4]

## Your assessment

This is evidence of a financing cycle becoming more dependent on external capital and enforceable customer commitments, with substantial differences between issuers and structures. The note is strongest on legal recourse, the distinction between capacity and drawn debt, and the limits of interpreting market marks; I agree that the evidence does not establish a systemic banking crisis or a realized default wave. I differ in emphasis: profitability alone is too reassuring when customer advances, equity issuance and future leases help fund the expansion, and the apparent diversification across corporate bonds, project vehicles and GPU lenders can conceal dependence on the same customers. The mixed total contributes less to that assessment than a borrower-by-borrower cash-flow and contractual-obligation map. Recent issuance and Lambda's protected structure remain important counterevidence: credit markets are differentiating, not simply closed. My concern is the durability and independence of the repayment sources, rather than the sheer size of the sum assembled here.

## Recommended edits

1. **Replace Summary bullet 1:** “Credit risk depends on construction delivery, customer payments and equipment resale values. Profitable operations provide support, but S&P's August 27, 2026 forecast expects all six covered hyperscalers to have negative free operating cash flow in 2026–2027, with recovery only in 2029.” Cite [S&P][sp]; label the second sentence a forecast. Avoid claiming a measured concentration of losses.

2. **Replace Summary bullet 2:** “Meta's May 2026 bond issue raised $25B face value and $24.91B net cash proceeds. Alphabet's June 2026 common-stock and mandatory-preferred offering raised $49.6B net; it is equity financing, with preferred conversion scheduled for May 2029.” Cite [Meta][meta] and [Alphabet][goog].

3. **Replace Summary bullet 3 and the extended-total emphasis:** “The note assembles approximately $572.5B of dated corporate and project principal/securities, mainly from May–June 2026 snapshots. Construction packages, announced chip-platform capital and subsequent issuance are shown separately because they are not comparable measures of outstanding debt.” Add a verification footnote for row 12, remove the bold $722.872B headline, and label the Vantage input “preliminary reported package; final commitment and draw status unverified.”

4. **Replace Summary bullet 4:** “Hyperion's 2025 structure illustrates the difference between project debt and tenant debt: Meta signed initial four-year leases and a conditional, capped residual-value guarantee covering the first 16 operating years. Those terms do not constitute an unlimited Meta guarantee of project bonds.” Cite [Meta's transaction announcement][metajv].

5. **Replace Summary bullet 5:** “On October 15, 2026, Reuters reported CoreWeave five-year CDS above 1,000bp and Oracle at 288bp, while the broad US high-yield OAS was 323bp. These differently constructed indicators suggest selective credit stress; they are neither realized losses nor directly comparable default probabilities.” Cite [Reuters][cds] and [FRED][fredhy]. In claim 21 and Signals, disclose both FT price versions with dates; withhold a single precise mark until reconciled.

6. **Replace Summary bullet 6:** “Institutional exposure is established: CDPQ participated in CoreWeave's May 2024 facility, and BCI and Liberty Mutual Investments joined Crusoe's March 2025 GPU financing. Current investor allocations, total insurer/pension exposure and banks' retained underwriting positions remain unquantified.” Cite [Blackstone][crwv24] and [Crusoe][crusoe].

7. **Replace Summary bullet 7:** “CoreWeave's August 2026 $2.6B DDTL 5.5 has roughly five-year debt against customer contracts averaging three years. Repayment therefore depends partly on renewals, replacement customers or collateral recovery after the initial contracts expire.” Cite [the August release][crwv55]. Add **Ba2/BB+** to claim 23; describe this as an illustrative risk mechanism, not a portfolio-wide loss forecast.

8. **Add the missing September financing and near-term maturity signal:** “On September 22, 2026, CoreWeave completed a $4.2B issue of 2.875% convertible notes due 2033. This is subsequent gross borrowing, not an updated net debt balance.” Cite [the 8-K][crwvsep]. Also add “CoreWeave remaining-2026 principal payments: $4.413B at June 30” to the maturity discussion and Signals. Do not omit convertible borrowing merely because equity is a possible settlement outcome.

9. **Add a cash-flow funding paragraph:** “Oracle's August 2026 quarter generated $23.103B of operating cash flow, including $11.363B of customer advances with a significant financing component, against $28.499B of capex. Reported free cash flow was −$5.396B. Customer funding improves near-term liquidity but should be distinguished from cash generated by services already delivered.” Cite [Oracle results][orclresults] and [its 10-Q][orclq]. Add a separate panel for the Meta and Oracle future lease commitments identified above, without adding them wholesale to project debt.

10. **Add the recent contractual and circularity evidence:** “September 24 reporting said Oracle sent a force-majeure notice for Project Jupiter; its contractual effect remains unverified, and Oracle maintained the project schedule. Oracle's October 13 release stated that project scope was unchanged beyond its April power-plan update.” Cite [Axios][jupnotice] and [Oracle][juporacle]. Then add: “BIS research published October 1 found that 46.4% by value of AI-to-AI investment deals in 2021–2025 also involved supplier-customer relationships, showing why contractual demand and financing cannot automatically be treated as independent.” Cite [BIS][bis137].

11. **Tighten definitions and verification status:** In claim 39 replace “in 2027” with the release's “by 2027,” name the six-company universe, and include the 2029 recovery assumption. In claim 35 label Baa–Aaa a “monthly yield differential,” separately from daily HY OAS. In claim 30 retain approximately 63% as the reproduced Reuters estimate and flag the inaccessible 64% version. In claim 12 record the uncompleted Microsoft check and Oracle full-document retrieval limitation instead of implying this review verified all five components. No numerical correction to the Analysis sums is warranted on arithmetic grounds.

[meta]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
[meta26]: https://www.sec.gov/Archives/edgar/data/1326801/000119312526197902/d148113dfwp.htm
[goog]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
[amzn]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[orclindex]: https://www.sec.gov/ixviewer/ix.html?doc=%2FArchives%2Fedgar%2Fdata%2F1341439%2F000119312526277521%2Forcl-20260531.htm
[msftindex]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm
[jupiter]: https://www.aol.com/articles/oracles-18-billion-data-center-220302000.html
[beignet]: https://www.cliffordchance.com/insights/thought_leadership/trends/2026/energy-and-resources-insights-2026.html
[metajv]: https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
[pricesalt]: https://www.biznews.com/global-investing/investors-dump-data-centre-bonds
[pricesft]: https://www.ft.com/content/678bcd31-6c2a-447b-a68c-ce6dec220bbc
[crwv]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
[crwv4]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex991.htm
[crwv55]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm
[lambda24]: https://markets.financialcontent.com/prnews/article/bizwire-2024-4-4-lambda-announces-500m-gpu-backed-facility-to-expand-cloud-for-ai
[lambda26]: https://lambda.ai/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
[wulfhtml]: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm
[avgo]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
[cds]: https://economictimes.indiatimes.com/tech/artificial-intelligence/ai-credit-default-swap-spreads-widen-sharply/articleshow/134958105.cms
[cdsex]: https://economictimes.indiatimes.com/markets/us-stocks/news/why-are-credit-default-swaps-unnerving-ai-investors/articleshow/134967395.cms
[fred]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA,AAA&cosd=2026-09-01&coed=2026-09-30
[fredhy]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-10-15&coed=2026-10-15
[sp]: https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says
[qts]: https://www.paulhastings.com/en-GB/news/paul-hastings-advises-the-initial-purchasers-on-qts-data-centers-usd4-6-billion-notes-offering
[hutq]: https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results
[abilene1]: https://www.nmrk.com/insights/press-releases/newmark-arranges-2-3-billion-construction-financing-for-206-mw-build-to-suit-data-center
[abilene2]: https://www.prnewswire.com/news-releases/newmark-facilitates-7-1-billion-construction-loan-to-develop-ai-data-center-302463532.html
[vantage]: https://www.bloomberglinea.com/negocios/bancos-alistan-deuda-por-us38000-millones-para-centros-de-datos-de-oracle/
[googaug]: https://www.sec.gov/Archives/edgar/data/1652044/000119312526338750/d159970dfwp.htm
[crwvsep]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm
[jupnotice]: https://www.axios.com/2026/09/24/oracle-force-majeure-blue-owl-openai
[juporacle]: https://www.oracle.com/news/announcement/project-jupiter-is-expected-to-generate-13-billion-in-economic-impact-2026-10-13/
[bis137]: https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms
[orclresults]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
[orclq]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
[crwv24]: https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/
[crusoe]: https://www.crusoe.ai/resources/newsroom/upper90-closes-usd225m-credit-facility-to-crusoe-to-expand-ai-cloud
