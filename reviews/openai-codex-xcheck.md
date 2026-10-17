# OpenAI — independent Codex cross-check

*Evidence cutoff and source access: 2026-10-17. Reviewed `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, and `research/stack/openai.md`. Independent verification; no changes to the note.*

## Verdict

The central conclusion survives: substantial demand and financing coexist with unproven sustainable profitability and significant contingent supplier exposure.
The 15 selected rows largely reproduce their sources accurately, and every checked calculation is numerically correct; reported private figures remain unverified.
Revise the margin inference, growth baseline and inherited grades; add omitted liquidity, September adoption/pricing evidence, and concrete Summary wording.

## Claim re-verification

These 15 rows carry the demand, loss, funding and supplier-risk argument. “Matches” means the source supports the statement, not that a private financial leak has become an audited public fact. A applies to directly disclosed facts or announcements; forecasts remain forecasts. C means reported, unverified (RU). D applies to the contested plan. Primary filings were preferred, including better SEC sources where announcement pages were incomplete. All dates below precede the cutoff.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 3 | September ~$50bn annualised; previous $68–70bn gross partner basis; Q3 growth 77%, enterprise 107% | Same. CNBC identifies $68bn as including partners' gross revenue and reports both growth rates; Reuters says almost $50bn versus approaching $70bn. Neither supplies a public accounting reconciliation. | [CNBC, Oct 8][cnbc], [Reuters, Oct 8][sep-revenue] | Yes, as reporting. CNBC fetched directly after web-fetch failure. | **C, RU**, including growth rates |
| 5 | 2024 revenue $3.7bn, attributable loss $5.09bn; 2025 revenue $13.07bn, operating loss $20.92bn, attributable loss ~$38.5bn | Same; original reporter gives 2025 attributable loss $38.53bn. These are distinct from consolidated net loss and cash outflow. | [Original financial-document reporting, Jun 15][accounts]; [PYMNTS, Jun 17][q1] corroborates revenue and attributable losses | Yes. Original financial statements were not publicly authenticated by this review. | **C, RU**; reported audit/FT verification does not make our access primary |
| 6 | H1 2025 burn $2.5bn/revenue $4.3bn; FY2025 burn ~$8bn; Q1 2026 burn $3.7bn/revenue $5.7bn | Same numbers in the respective reports. FY2025 figure appears in a retrospective forecast-vintage table, not a fetched cash-flow statement. | [Reuters, Sep 30, 2025][h1]; [Decoder, Feb 21, 2026][decoder]; [PYMNTS, Jun 17][q1] | Yes, with a provenance qualification for full-year burn. | **C, RU** |
| 7 | Burn 2026/27/28/29: $25/$57/$85/$51bn; 2030 positive $39bn | Same sequence in the February forecast table. | [Decoder, Feb 21][decoder], attributing The Information | Yes; a forecast vintage, not realised spending. | **C, RU** |
| 8 | 2026–30 negative FCF $278bn; compute $856bn; revenue $840bn cumulative, $36bn→$350bn annually; July deck, reported Sep 18 | All financial figures reproduced by Reuters. Its accessible text does not establish the July deck date. The Information reports a finance employee's denial. | [Reuters, Sep 18][plan]; [The Information, Sep 18][dispute] | Figures match the report; underlying plan contested. July provenance not independently established here. | **D** for the contested plan; do not promote its derivatives to C |
| 9 | Adjusted gross margin 33% in 2025, 40% in 2024, 46% target; paid-user compute margin ~70% in Oct 2025 | Same reported metrics. Their definitions are not interchangeable. | [Decoder][decoder]; [Bloomberg, Dec 21, 2025][paid-margin] | Yes; accounting reconciliation missing. | **C, RU** |
| 13 | $122bn committed; $852bn post-money; ~$4.7bn undrawn revolver | All three directly stated at March 31 close. Commitment is not a cash-balance disclosure. | [OpenAI, Mar 31][round] | Yes. | **A** for announcement and facility status at close |
| 16 | Incremental $250bn Azure purchases; compute right of first refusal removed | Same, directly recorded in Microsoft's subsequent-event note for the October 28, 2025 agreement. | [Microsoft FY26 Q1 10-Q, note 17][azure] | Yes. Better primary source than relying on the abbreviated blog extract. | **A**; full contract/maturity schedule not disclosed |
| 19 | FY26 Microsoft revenue from OpenAI $24.1bn; receivable $6bn; $13bn commitment/$11.9bn funded; investment gain $6.5bn, chiefly dilution | Same. Revenue expressly includes revenue sharing. Gain chiefly reflects recapitalisation dilution, not OpenAI operating profit. | [Microsoft 10-K investment note][ms-investment]; [10-K indexed primary extract, note 3][ms-annual] | Yes. Full-document fetch blocked; investment note fetched and gain independently found in indexed SEC text. | **A** |
| 20 | Oracle 4.5GW; $300bn/~5 years starting 2027 | 4.5GW company-confirmed; dollar value, duration and start date reported from WSJ sources. No public contract found. | [OpenAI, Jul 22, 2025][oracle-capacity]; [Reuters, Sep 10][oracle-reuters]; [DCD, Sep 11][oracle-dcd] | Yes, with the note's primary/secondary distinction. | **A** capacity; **C, RU** financial terms |
| 21 | ≥10GW LOI, up to $100bn progressively, first GW H2 2026; subsequently $30bn finalised and $100bn unlikely | Original Nvidia announcement and Reuters account of Huang's March 4 remarks agree. “Finalised” is not proof of full cash receipt on that date. | [Nvidia, Sep 22, 2025][nv-loi]; [Reuters, Mar 4, 2026][huang] | Yes. | **A** original LOI; **B** for reported public remarks |
| 22 | $105bn guarantee cap; 4.25GW; 20-year leases; first phase FY2029; optional ~3.8GW | Same in note 10. Nine construction phases; coverage limited to defined lease/power obligations, contingent on delivery/default and subject to termination provisions. | [Nvidia July 26 10-Q, August subsequent event][nv-q] | Yes. FY2029 is Nvidia's fiscal year, not calendar 2029. | **A** |
| 28 | Amazon $28.7bn funded by June; $21.3bn subsequently; total $50bn | Same. Filing explicitly calls the later amount invested, not merely committed. | [Amazon June 30 10-Q, investment disclosure][amazon-q] | Yes; $28.7 + $21.3 = $50.0bn. | **A** components; **B** sum |
| 29 | Cerebras >$20bn deal, 750MW committed, 1.25GW optional; ~$1bn secured loan at 6%, service repayment; warrant | All supported. Loan funded in January; June outstanding balance was **$918.244m**, following $86.327m of non-cash offsets against $1,004.571m advanced. | [Cerebras Q1 release, Jun 23][cerebras-ir]; [Q2 10-Q, notes 3/10/12][cerebras-q] | Yes for original terms; add outstanding balance if presenting June exposure. | **A** |
| 36 | Final $10bn tranche; $30bn follow-on complete; $64.6bn cumulative/~13%; senior notes funded final tranche; bridge repaid/cancelled | Same, explicitly dated October 1. Senior-note funding refers to the final tranche; it does not describe the funding source of every prior investment. | [SoftBank, Oct 1][softbank] | Yes. | **A** |

No public primary accounts or investor deck were found to upgrade rows 3, 5–9 or Oracle's financial terms. Multiple articles repeating the same leak are not independent primary confirmation. The blocked Yahoo/Quartz page was replaced with the original reporter and accessible corroboration; this access limitation is not evidence that the note's figure is false.

## Arithmetic checks

The Analysis delegates its quantitative examples to claims 39–40 and refers to calculations in claims 2, 18, 27 and 28. I recomputed all of those, not just numerals printed inline. USD billions unless indicated.

| Derived figure | Independent calculation | Result / interpretation |
|---|---|---|
| March monthly revenue annualisation, claim 2 | 2 × 12 = 24 | Correct; a snapshot, not annual sales. [Source][round] |
| December OpenAI-related RPO, claim 18 | 625 × 45% = 281.25 | Correct rounding to ~$281bn. [Source][ms-q2] |
| Conditional June RPO concentration | 281.25 / 678 = 41.4823% | Correct rounding to 41.5%; no evidence the numerator was unchanged. [June call][ms-q4] |
| AWS total, claim 27 | 38 + 100 = 138 | Correct aggregate headline; different contract terms preclude a single implied annual bill. [Source][aws] |
| Amazon total, claim 28 | 28.7 + 21.3 = 50 | Correct; not additional to the round. [Source][amazon-q] |
| Oracle average, claim 39 | 300 / 5 = 60; 60 / 50 = 120% | Correct illustrative scale comparison. Neither a 2026 bill nor a payment schedule. [Reported terms][oracle-dcd], [run-rate][sep-revenue] |
| Gross-profit sensitivity, claim 39 | 50 × .33 = 16.5; 70 × .33 = 23.1 | Correct. Gross profit is not cash available for all corporate spending. [Inputs][decoder] |
| Training-only revenue hurdle, claim 39 | 32 / .33 = 96.9697 | Correct ~$97bn; assumes the cost sits outside this margin and both are comparable. [Inputs][decoder] |
| 2030 growth examples, claim 40 | 70 × 1.25⁴ = 170.8984; 70 × 1.5⁴ = 354.375 | Correct ~$171bn/$354bn; four growth intervals. $70bn is a hypothetical annual base, not the [reported exit run-rate target][target]. |
| Growth to $350bn, claim 40 | (350 / 70)^(1/4) − 1 = 49.5349% | Correct arithmetic, but does not describe the [reported plan's][plan] $36bn starting year. That path requires **76.58%** annual growth. |
| Valuation/run-rate, claim 40 | 852 / 50 = 17.04× | Correct; March post-money equity valuation divided by September annualised revenue. Not EV/sales or a trailing multiple. [Valuation][round], [revenue][sep-revenue] |

There is **no numerical correction to make to the existing calculations**. There are three interpretive corrections:

- The margin passage mixes periods and definitions. The leaked cost-of-revenue figures imply **(13.07 − 7.5) / 13.07 = 42.62%** for 2025 and **(3.7 − 2.65) / 3.7 = 28.38%** for 2024. These do not reconcile to claim 9. Treat this as an unresolved reporting-definition conflict, not proof either series is false. [Original reporting][accounts]
- The same February source forecasts future adjusted margins of **52–67%**. Holding training fixed, the hurdle becomes **$61.54bn–$47.76bn**. This sensitivity changes the inference; it is not a prediction that training stays fixed or that those margins arrive immediately. [Source][decoder]
- Claim 40's arithmetic is valid as a hypothetical, but its link to the disputed $350bn target inherits **D** uncertainty. The 25%/50% scenarios are author assumptions, not graded observations; the valuation/run-rate calculation retains C input uncertainty. A single C label obscures these differences.

## Omissions

**Liquidity is incompletely presented, although the note correctly rejects imminent-insolvency claims.** Its own Q1 source reports **$73bn cash and marketable securities at March 31, versus $40bn at December 31** (C, RU). This is the missing historical liquidity anchor. It cannot establish October unrestricted cash, and adding the entire subsequent round would double-count receipts already included. [PYMNTS][q1] Independently disclosed Amazon and SoftBank follow-on receipts establish at least **$80bn** funded across those two investors by October 1 (B arithmetic); that is stronger than a commitment-only framing but still not a cash balance. [Amazon][amazon-q], [SoftBank][softbank]

**A further October funding lead deserves a labelled follow-up:** Nvidia reportedly completed its $30bn pledge on October 1 (C, RU); no primary confirmation located. [The Information][nv-final] Keep that lead separate from the primary-confirmed $80bn, and do not add it on top of the March round.

**The latest primary adoption disclosure is missing.** OpenAI's **September 29 DevDay recap states 1.2bn weekly users**, substantially newer than the March observation in claim 32 (A for company statement). It does not disclose paid conversion, retention, comparable measurement methodology or profit. Nevertheless, the note should not say the latest global user total is wholly unavailable without recording this disclosure. [OpenAI][devday]

**Recent pricing changes make a static historical margin less informative.** The September 29 launch lists GPT-6.1 Sol at **$2/$10 per million input/output tokens**, versus Astra's $10/$50, with $0.10 cached input. The same day, OpenAI introduced **Pro 500 at $500/month**, with a premium speed tier and usage credits. These are primary facts about prices and product mix, not costs or realised ARPU. My inference: lower unit prices may expand usage or compress revenue per token; premium tiers may improve monetisation. Neither direction can be resolved from user growth alone. [Model launch][sol], [release notes][release]

**Execution risk is more concrete than “key-person risk.”** On September 28, OpenAI described training safety-case recommendations involving senior-leadership vetoes, pause controls and monitoring, with implementation ongoing. Earlier, its September 1 statement acknowledged delaying parts of Astra development/release while strengthening safeguards. This establishes a mechanism by which research spending need not turn into revenue on schedule; financial consequences are not quantified. [September 28 primary statement][safety], [September 1 primary statement][path-astra] Recent reporting about withholding GPT-6.1 Astra is a further lead, but I did not obtain a model-specific primary release decision and do not treat it as A evidence here.

**The financing analysis underuses contract detail.** Cerebras has already begun offsetting its loan through service billings, and the loan's security is a first-priority interest in a lockbox and related amounts, not a disclosed blanket claim on every company asset. Its customer service terms can be shorter than its data-center commitments. This sharpens who bears residual capacity and recovery risk. [Cerebras 10-Q][cerebras-q] Nvidia also discloses remedies including taking over leases, seeking replacement tenants or pursuing a sale. A guarantee cap therefore need not translate into an equally sized cash loss. [Nvidia 10-Q][nv-q]

The recent-event search covered September 17–October 17, with older evidence used to test existing claims. The largest recent funding and revenue stories are already represented in the note. I found no primary evidence in this review establishing an OpenAI-wide default or a funded new $30bn round. The omissions change the balance and specificity of the argument, rather than overturning it.

## Summary-bullet assessment

| Bullet | Supported by its own evidence? | Usefulness and required change |
|---|---|---|
| 1 — substantial demand, profitability unsupported | **Yes.** Distribution/revenue evidence and reported losses support both clauses. Absence of allocated segment accounts supports “unproven,” not proof that every segment loses money. | Too abstract: no date or scale. Use replacement 1 below. |
| 2 — September ~$50bn versus $68–70bn | **Yes, at C/RU confidence.** The correction and continued growth can coexist. | Already concrete; add **2026**, and keep “reported” attached to growth. Do not imply a primary gross/net reconciliation exists. |
| 3 — inference margins do not finance research/expansion | **Partly.** The reports support historical losses and a conditional funding gap. They do not establish a timeless result at today's product mix. | Too abstract and categorical. State the period and conditional nature; replacement 2. |
| 4 — $122bn/$852bn round; receipts differ | **Yes.** The source explicitly says committed capital; the note also identifies real receipts. | Quantified but undated, and excessively focused on the distinction without the known funded minimum. Replacement 3. |
| 5 — commitments overlap; Nvidia guarantee versus LOI | **Yes.** The note appropriately avoids summing cloud spend, chips and the umbrella plan. | Useful but omit neither the guarantee's August 2026 date nor its default contingency. Replacement 4. |
| 6 — nonprofit control and intersecting risks | **Control: yes. Risks: reasoned inference.** The [structure page][structure] directly confirms control; governance history does not quantify personal dependence or loss concentration. | Too compressed: governance and creditor exposure need separate concrete clauses. Replacement 5. |
| 7 — missing enforceable cash-payment schedule | **Yes as an identified evidence gap**, not as proof of inability to pay. | Useful question, but could specify a directly disclosed obligation and the missing liquidity bridge. Replacement 6. |

## Your assessment

OpenAI is a commercially substantial but financially opaque growth company whose buildout relies on external capital and on counterparties underwriting future demand. I agree with the note that the evidence establishes neither comfortable company-wide profitability nor imminent insolvency, and that overlapping construction headlines cannot certify a trillion-dollar enforceable liability. I differ in emphasis: disclosed funding receipts, reported historical liquidity and newer adoption evidence deserve as much prominence as burn projections; meanwhile, margin-definition conflicts and the annual-revenue versus exit-run-rate distinction make the claimed financing gap less mechanically demonstrable than the terse prose suggests. Supplier exposure is real, but its expected loss depends on delivery, contractual protections, recovery value and the ability to remarket capacity. The strongest bubble test is whether financed capacity earns durable returns after all costs, not whether current revenue is smaller than the arithmetic average of a future contract. The reviewed evidence supports substantial financing and execution risk; it does not support a precise failure probability or a definitive overvaluation finding.

## Recommended edits

1. **Replace Summary bullet 1 and update claim 32:** “At September 29, 2026, OpenAI reported 1.2bn weekly users. Demand is substantial, but public evidence does not establish profitability after research and corporate costs.” Add the DevDay source and retain the dated March subscriber observation. [Source][devday]

2. **Replace Summary bullet 3:** “The February 2026 forecast projected $25bn of 2026 cash burn despite positive inference margins; the later financial plan is disputed. Claim 39 illustrates a conditional funding gap.” In Analysis, explicitly reconcile the leaked cost-of-revenue margin with the adjusted metric, or state that reconciliation is unavailable; include the improved-margin sensitivity calculated above. [Historical accounts][accounts], [forecast source][decoder]

3. **Replace Summary bullet 4:** “On March 31, 2026, OpenAI announced $122bn committed at $852bn post-money. Amazon and SoftBank subsequently confirmed funding totalling at least $80bn within that round; October unrestricted cash is undisclosed.” Add the reported March cash/securities balance to the liquidity paragraph without double-counting receipts. [Round][round], [Amazon][amazon-q], [SoftBank][softbank], [cash report][q1]

4. **Replace Summary bullet 5:** “Cloud contracts, chip plans and Stargate overlap. Nvidia's August 2026 $105bn guarantee is contingent credit support; its September 2025 investment LOI is not cash available to OpenAI.” Preserve the detailed lease conditions in Analysis. [Guarantee][nv-q], [LOI][nv-loi]

5. **Replace Summary bullet 6:** “The Foundation controls OpenAI Group PBC. Financing risk extends to counterparties: Microsoft reported a $6bn OpenAI receivable at June 30, 2026, while suppliers also face capacity and guarantee exposure.” Keep key-person dependence explicitly labelled as inference in Analysis. [Structure][structure], [receivable][ms-investment]

6. **Replace Summary bullet 7:** “The unresolved financing question is when contracted purchases—including the $250bn incremental Azure commitment announced October 28, 2025—become payable, compared with cash collections and unrestricted funding.” [Microsoft filing][azure]

7. **Replace the claim 40 growth interpretation:** “The $70bn base is a hypothetical full-year revenue assumption. The disputed plan instead starts at $36bn in 2026; reaching $350bn in 2030 from that base requires 76.6% annual growth.” Split the grade cell: “author scenarios; C for valuation/run-rate inputs; D for the disputed plan target.” [Plan][plan], [exit target][target]

8. **Add a dated monetisation paragraph:** “On September 29, 2026, OpenAI introduced Pro 500 at $500/month and GPT-6.1 Sol at $2/$10 per million input/output tokens. These changes may alter revenue per customer and per token; realised margins are undisclosed.” Add the primary training-safety evidence to execution risks and monitor release delays separately from customer-demand cancellations. [Release notes][release], [pricing][sol], [safety statement][safety]

9. **Tighten source and balance precision:** cite Microsoft's investment-note HTML and indexed annual filing for claim 19, and its Q1 subsequent-event note for claim 16. Append to claim 29: “Original advance $1,004.571m; June 30 outstanding $918.244m after non-cash credits.” Label claim 6's full-year burn as retrospective reporting. [Microsoft][ms-investment], [Azure][azure], [Cerebras][cerebras-q]

[cnbc]: https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html
[sep-revenue]: https://uk.marketscreener.com/news/openai-s-september-annualized-revenue-nears-50-billion-less-than-previously-indicated-source-says-ce785ddfdf8bff23
[accounts]: https://www.wheresyoured.at/exclusive-openai-financials/
[q1]: https://www.pymnts.com/news/artificial-intelligence/2026/openai-ran-through-4-billion-dollars-q1/
[h1]: https://www.investing.com/news/stock-market-news/openais-firsthalf-revenue-rises-16-to-about-43-billion-the-information-reports-4262205
[decoder]: https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/
[plan]: https://www.marketscreener.com/news/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports-ce785adade89f226
[dispute]: https://www.theinformation.com/briefings/openai-said-forecast-nearly-280-billion-cash-burn-end-2030
[paid-margin]: https://www.bloomberg.com/news/articles/2025-12-21/openai-sees-better-margins-on-business-sales-report-says
[round]: https://openai.com/index/accelerating-the-next-phase-ai/
[azure]: https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm
[ms-investment]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R11.htm
[ms-annual]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm?aff_unique2=%2F&aff_unique3=t10tcKEC0&code=%2F&testcode=t10tcKEC0
[oracle-capacity]: https://openai.com/index/stargate-advances-with-partnership-with-oracle/
[oracle-reuters]: https://www.investing.com/news/stock-market-news/openai-oracle-sign-300-billion-computing-deal-wsj-reports-4234251
[oracle-dcd]: https://www.datacenterdynamics.com/en/news/openai-signs-300bn-cloud-deal-with-oracle-report/
[nv-loi]: https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership-to-Deploy-10-Gigawatts-of-NVIDIA-Systems/default.aspx
[huang]: https://www.investing.com/news/stock-market-news/nvidia-will-not-be-able-to-invest-100-billion-in-openai-due-to-ipo-ceo-jensen-says-4541937
[nv-q]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[amazon-q]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[cerebras-ir]: https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-strong-first-quarter-2026-results
[cerebras-q]: https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm
[softbank]: https://group.softbank/en/news/press/20261001
[ms-q2]: https://www.microsoft.com/en-us/Investor/events/FY-2026/earnings-fy-2026-q2
[ms-q4]: https://www.microsoft.com/en-us/Investor/events/FY-2026/earnings-fy-2026-q4
[aws]: https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment
[target]: https://ca.finance.yahoo.com/news/openai-expects-70-billion-annualized-014338719.html/
[nv-final]: https://www.theinformation.com/briefings/exclusive-nvidia-softbank-make-final-20-billion-investment-openais-last-round/
[devday]: https://openai.com/index/devday-2026-recap/
[sol]: https://openai.com/index/introducing-gpt-6-1-sol/
[release]: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
[safety]: https://openai.com/index/towards-safety-cases-for-frontier-ai-training/
[path-astra]: https://openai.com/index/path-to-astra/
[structure]: https://openai.com/our-structure/
