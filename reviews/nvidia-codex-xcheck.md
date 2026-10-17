# NVIDIA — independent Codex cross-check

*As of and sources accessed: 2026-10-17. Reviewed `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, `research/stack/nvidia.md`, and its quarterly CSV. Only this review was changed. No git commands were run.*

## Verdict

The core profitability figures and financing exposures verify, but the note needs material corrections before publication.
Its weakest conclusions confuse future demand with current funding dependence, gross commitments with losses, and a conditional valuation scenario with cheapness.
It also misses September financing and capital-return developments; retain the risk thesis, correct the arithmetic and accounting, and rewrite the affected Summary bullets.

## Claim re-verification

These are the 15 rows most directly supporting profitability, liquidity, financing dependence, customer concentration, and valuation. Dollars are billions unless marked otherwise. A grade on guidance verifies management's statement, not its eventual realization. I located NVIDIA's own hosted corrected call transcript, allowing the relevant transcript claims to be upgraded from B to A. “Qualified” identifies a scope, accounting, or freshness problem rather than a fabricated number.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | Q2 FY27 revenue $96,221m; +106% y/y, +18% q/q | $96,221m; calculated growth 105.85% and 17.90%; quarter ended July 26 | [Q2 release][pr] | Yes | A figures; B calculations |
| 2 | DC $89,023m; Hyperscale $48,710m; ACIE $40,313m | Same; components sum exactly. Prior periods were recast. | [Q2 CFO commentary][cfo] | Yes | A |
| 4 | Q3 $108bn ±2%; GM 74% ±50bp; no China DC compute | Same; guidance, not actual revenue | [Q2 release][pr] | Yes | A |
| 5 | Preliminary FY2028 growth ~70%; supply constrained through FY2028 | Same, including preliminary qualification | [Company-hosted transcript, p.7][call] | Yes | A for outlook |
| 6 | GM 71–72% Q4; 72–73% FY2028 | Same; recovery also assumes price increases taking effect in Q1 | [Company-hosted transcript, p.7][call] | Yes; causal explanation incomplete | A for outlook |
| 9 | Q2 one customer 16%; H1 16/15/13%; historical Q2 23/16%, FY26 22/14%, FY25 12/11/11% | All percentages match; different reporting periods are not a common concentration series | [Q2 10-Q, Note 15][q]; [FY26 10-K][k] | Yes | A |
| 12 | AR $63.1bn; DSO 60 versus 45; terms 90 days–one year | $63.059bn; same DSO and terms. Q1 commentary had already warned its unusually low DSO would normalize. | [Q2 CFO][cfo]; [10-Q, Note 7][q]; [Q1 CFO][q1cfo] | Yes; missing baseline context | A |
| 15 | Supply $279bn vs $119bn/$95.2bn/$45.8bn; $92/$87/$88bn due through FY29 | Current total and schedule match. July 2025's $45.8bn included non-inventory obligations, including cloud agreements; unlike current supply-only total. | [Q2 CFO][cfo]; [Q1 CFO][q1cfo]; [Q4 CFO][q4cfo]; [Q2 FY26 CFO][oldcfo] | Qualified: historical scope changes | A disclosures; B only for comparable arithmetic |
| 17 | $105bn guarantee; 4.25 GW; nine phases from FY29; optional ~3.8 GW; $150–200bn/generation | All match. It is a conditional residual-value guarantee; potential chip revenue is management's scenario. | [August 17 8-K, Item 1.01][guar]; [Q2 CFO][cfo] | Yes; loss interpretation incomplete | A for terms and stated scenario |
| 18 | Equity $99bn; $25bn committed; purchases $42.4bn; gains $23.7bn | $42.783bn + $4.957bn + $47.898bn + ~$3.3bn ≈ $99bn; purchases $42.404bn; gains $23.707bn | [10-Q, Notes 5–6, cash flows][q] | Yes; carrying value ≠ cash invested | A; B component sum |
| 19 | Nearly $50bn invested in labs; supported labs ~quarter of next year's business; circularity acknowledged; no loans | Statements verified. Quarter share is FY2028 total-company demand; it is not current DC revenue or an audited loss-funded share. | [Company-hosted transcript, pp.5–6][call] | Yes as attributed statements | A; downstream demand estimate C at best |
| 23 | CoreWeave Q2 revenue $2.575bn; loss $626m; interest $640m; debt ~$35.1bn; equity $5bn; liabilities $72bn; backlog ~$104bn; A/B 36/26%; all GPUs NVIDIA | Revenue/loss match; interest is **net**. Debt carrying value $35.068bn versus $35.551bn gross; equity $5.024bn; liabilities $72.046bn. Backlog, customer shares and GPU statement match. | [CoreWeave 10-Q][crwv]; [results release][crwvpr] | Yes with accounting labels | A; B debt addition |
| 26 | Cash/debt securities $56.6bn; new notes $25bn; outstanding $33.5bn; CP $25bn undrawn; buybacks $19.7bn/94m; returns ~$26bn; authorization ~$99bn; dividend $0.25 | July values match; debt carrying amount $33.366bn. September 28 update: **$235bn authorization remaining**, after $150bn addition. | [10-Q, Notes 9/12][q]; [September announcement][buyback] | Historical yes; stale as current authorization | A |
| 27 | Q2 OCF/FCF $24.1/$21.3bn; Q1 $50.3/$48.6bn; TTM FCF $126.9bn | $24.077/$21.341bn; $50.344/$48.554bn; TTM $126.886bn | [Q2 release][pr]; [Q4 release][q4pr]; [Q3 release][q3pr] | Yes | A quarters; B TTM |
| 31 | $214.13 × 24.1bn ≈ $5.16tn; sales $303bn; GAAP NI $192.9bn; adjusted NI $170.8bn; P/E 26.8/30.2; P/S 17; P/FCF 40.7; forward P/E 17.7 | Price matches October 16. All arithmetic reproduces, but adjusted TTM mixes accounting bases. Quote provider itself shows 24.15bn shares, ~$5.17tn and EPS-based P/E 27.08. Forward 17.70 is provider consensus, not company guidance. | [Quote][quote]; [10-Q cover][q]; [Q2][pr], [Q4][q4pr], [Q3][q3pr] releases; [Q1 CFO][q1cfo] | Qualified: stale share-count approximation and mixed adjusted earnings | B price/derived GAAP ratios; no clean B for mixed adjusted TTM |

## Arithmetic checks

The calculations below cover the derived numerical assertions throughout Analysis, including estimates embedded in prose. Correct arithmetic does not validate assumptions or convert an estimate into a disclosure. Primary quarterly inputs were checked against the releases above; additional comparison inputs are linked below.

| Analysis calculation | Independent result and assessment |
|---|---|
| Starting $26.0bn quarter; “ten quarters ago” | Q1 FY25 to Q2 FY27 is **nine elapsed quarters**, ten observations inclusive. Revenue is 3.69 times the starting figure. The CSV itself contradicts the elapsed-period wording. |
| GM held at 73–75% except H20 | Not literally: Q2 FY26 was **72.4%** GAAP, independently confirmed in the current release's comparative column. Q1 FY25 was also outside the stated range in the CSV. Say “around the mid-70s, apart from export-related charges and transition effects.” |
| Net income, investment gains, earnings measure | $59.688bn/$96.221bn = **62.03%**; $53.954bn/$96.221bn = **56.07%**. Gains are pretax; subtracting them directly from after-tax income would be wrong. $53.954bn is adjusted **net income**, not operating income; GAAP operating income is $63.734bn. [Q2 release][pr] |
| Supply schedule and increase | $92+$87+$88 = **$267bn**, 95.70% of $279bn, through FY2029 (about 2½ years from July 2026). $279−$119 = $160bn, **134.45%** increase. Much is future procurement, not already prepaid cash. |
| DSO and operating cash flow | DSO +15 days, +33.33%; OCF $24.077/$50.344−1 = **−52.18%**. “Halved” is fair. Receivables are an important cause, but CFO commentary also cites other working capital and cash taxes. [Q2 CFO][cfo] |
| Guarantee “almost twice cash” | $105/$56.586 = **1.86×**; all guarantees $108.5/$56.586 = **1.92×**. Denominator includes debt securities, not just cash. Numerator is a contingent multi-year maximum, not money due now. |
| AR concentration; Taiwan; hyperscale share; ACIE growth | 22+14+13+11+10 = **70%**; $27.0/$96.221 ≈ **28.1%**; $48.710/$89.023 = **54.72%**; $40.313/$16.928−1 = **138.14%**. Arithmetic passes; these are different classifications, not a look-through funding map. |
| CoreWeave placement and customer concentration | ~23m × $87.20 = **$2.0056bn**, consistent with rounded $2bn; 36+26 = **62%**. Its substantial leverage does not show that all neocloud purchases are debt-financed. [CoreWeave 10-Q][crwv] |
| Equity/investment totals | $42.8+$5.0+$47.9+$3.3 = **$99.0bn** rounded. Nearly $50bn in labs is a subset, not additive. $99+$25 = $124bn mixes existing carrying value with unfunded commitments; do not call it cash spent. |
| Groq total; Hugging Face funding status | $13.0+$2.9 = **$15.9bn**, arithmetic passes. A signed acquisition's ~$11.9bn consideration cannot be treated as cash already spent merely by putting it next to historical licence payments; claim 30 itself says signed. |
| FY2027 estimate; FY2028 revenue; supported-lab dollars | H1 $177.837bn + Q3 $108bn requires **$114.163bn Q4** (+5.71% q/q) to reach $400bn. $400×1.70 = **$680bn**, not $690bn. $690bn requires FY27 $405.882bn and Q4 $120.045bn (+11.15%). Either scenario is plausible as an assumption; specify one. A quarter of $680–690bn is **$170–172.5bn**. Neither is company dollar guidance. |
| Equity/FCF and guarantee/FCF | $50/$126.886 = **39.41%**; $105/$126.886 = **82.75%**. “Fraction” and 83% pass. They compare a cumulative investment or multi-year maximum with one trailing year's flow, not a funding schedule. |
| Broadcom relative size and annualization | $16.7/$89.023 = **18.76%**; $21.7/$89.023 = **24.38%**. “Roughly a quarter” uses Broadcom's future guide against NVIDIA's completed quarter. Annualizing yields $66.8bn actual / $86.8bn guided versus $356.092bn NVIDIA; multiplying by four fixes no period mismatch. Broadcom includes AI networking; AMD DC includes CPUs. [Broadcom release][avgo]; [AMD release][amd] |
| Competitors “growing faster” | AMD DC **107% < NVIDIA DC 117%**; only faster than NVIDIA total-company 106%. Broadcom AI 221% is faster. The Summary's AMD comparison uses unlike denominators. [AMD][amd]; [NVIDIA][pr]; [Broadcom][avgo] |
| H100 rates “roughly halved”; reserved +40% | Pairing range endpoints $2.8/$6−1 = **−53.3%**, $4.2/$10−1 = **−58%**; midpoint $3.5/$8−1 = **−56.25%**. Rough wording is arithmetically plausible, but vendor/contract comparability is unestablished. Reserved +40% has no numerator, denominator or direct cited SemiAnalysis observation; not reproducible. |
| Cisco growth, sales multiple, earnings multiple | $18.928/$12.173−1 = **55.49%**; $555/$18.928 = **29.32×**; $555/$2.668 = **208.02×**. Pass using the note's peak-cap assumption. FY2000 financials postdate the peak; these are not contemporaneous trailing multiples. [Cisco FY2000 10-K][cisco] |
| Cisco drawdowns | $8.12/$80.06−1 = **−89.86%** through the stated October 2002 low. An 84% drawdown implies **$12.81**. No dated 13-month endpoint is supplied in Analysis, so that separate historical claim is not established by the displayed prices. |
| Trailing NVIDIA totals | Revenue: 57.006+68.127+81.615+96.221 = **$302.969bn**. GAAP NI: 31.910+42.960+58.321+59.688 = **$192.879bn**. DC: 51.215+62.314+75.246+89.023 = **$277.798bn**. FCF: 22.089+34.902+48.554+21.341 = **$126.886bn**. Pass, using disclosed quarters; $1m rounding inconsistencies versus half-year tables are immaterial. |
| Market capitalization and multiples | $214.13×24.1 = **$5,160.533bn**; /302.969 = **17.03× sales**; /192.879 = **26.76× GAAP earnings**; /126.886 = **40.67× FCF**. Pass as an approximation using August's rounded share count. Forward 17.7× cannot be reconstructed without the provider's earnings horizon/basis. |
| Adjusted TTM earnings/multiple | 31.767+39.552+45.548+53.954 = **$170.821bn**; multiple **30.21×**. Sum passes but accounting comparability fails: FY26 excluded SBC, FY27 includes it. Q4 FY26 on the restated basis is **$38.969bn**, not $39.552bn. Do not invent a precise comparable TTM until Q3 is similarly reconciled. [Q4 release][q4pr]; [Q1 CFO][q1cfo] |
| Five-year return scenario | $5,160bn×1.1^5/25 = **$332.409bn earnings**; /.55 = **$604.380bn revenue**. Arithmetic passes with rounding. Assumes constant shares, no interim distributions, 25× terminal P/E and 55% net margin. It is a scenario, not an inference of uniquely priced expectations. At 40% margin the same earnings need **$831.023bn revenue**; at 20× exit P/E and 55% margin they need **$755.476bn**. |
| “Current level” can be a plateau | Q2 revenue annualized is **$384.884bn**. Reaching $604.380bn needs **57.03%** growth from that run-rate, or **99.49%** above TTM. The proposed plateau is a higher future level, not the current level. |
| Hyperscale/ACIE TTM approximation | 55%×277.798 = **$152.789bn**; 45% = **$125.009bn**. Last three disclosed quarters' weighted hyperscale share is **55.42%**, so ~55% is a reasonable scenario proxy, not an observed four-quarter split. |
| Blended debt-funded estimate | Low: .55×.20 + .45×.40 = **29.00%**. High: .55×.30 + .45×.55 = **41.25%**. Correct range is **29–41.25%**, conditional on unsupported allocation assumptions. The note's 25–40% does not reproduce. |
| Lab-funded estimate/floor | **25–35% is not calculable from the disclosed inputs.** Management's next-year total-business share is neither a current-period lower bound nor the fraction funded from losses. Adding profitable hyperscalers' internal model training to “entities with no profits” is a category error. Revenue, operating cash flow, equity and debt cannot be assigned to specific GPU purchases from these disclosures. |
| Loss-order totals; debt versus returns | $105+$3.5 = **$108.5bn**, passes. $33.5/(19.732+6.047) = **1.30×** one quarter's cash returns, broadly the same scale, but $33.5bn is total face debt and $25bn is new issuance. Combining guarantees, procurement and take-or-pay into a loss number would double-count economics and ignore recoveries. |

## Omissions

1. **September 25: actual convertible-debt participation.** Nscale announced a $3.36bn financing, consisting of $2.36bn initially and a **$1bn NVIDIA commitment expected to fund in mid-November 2026**. Notes convert automatically at its IPO, into non-voting shares for NVIDIA. This is a material update to the note's equity-versus-loans framing: convertible loan notes exist alongside the take-or-pay model. It is not evidence that the $1bn was already funded. **A, company statement.** [Nscale announcement][nscale]

2. **September 28: much larger discretionary capital returns.** NVIDIA added $150bn of authorization, leaving $235bn, with execution expected through FY2028. This strengthens the capital-allocation question and demonstrates a substantial discretionary lever if conditions deteriorate. Authorization is not debt or a binding cash outflow. **A, company statement.** [NVIDIA announcement][buyback]

3. **September 21 SB Energy S-1/A: $3bn backing and project execution risk.** The prospectus distinguishes **$1.5bn prepaid August 17 at 90% of the IPO price** from **$1.5bn conditional concurrent placement at the IPO price**. Neither belongs in July's balance sheet. It also describes OpenAI as not investment-grade and warns planned gas generation is not yet financed, constructed or contracted. This adds correlated developer/tenant exposure and a delivery constraint to the chip-demand thesis. Do not blindly add the new amounts to July commitments without a roll-forward. **A, filed terms/disclosures.** The web reader failed on this long filing; I fetched the SEC HTML directly and checked the cover, concurrent-placement section and risk factors. [SB Energy amended prospectus][sb]

4. **The guarantee has material protections.** Recovery from reletting/sale offsets the guaranteed minimum; NVIDIA has lease/remedy choices, OpenAI reimbursement rights, and specified termination events including a satisfactory credit rating. Ready-for-service conditions precede effectiveness. These reduce or defer exposure but do not ensure recovery during a correlated AI downturn. The same capacity scarcity that supports prices could prevent sites becoming operational; “fungible compute” is not proof that an Ohio shell retains its financing value. **A for terms; economic implications are my interpretation.** [August 17 8-K][guar]

5. **RPO exists, and other funding flows cut both ways.** The statement that NVIDIA reports no RPO is false: **$3.2bn** for contracts longer than one year. It is not comprehensive chip backlog. The filing also discloses customer advances, while existing public equity holdings have sale restrictions; treating all investments as readily available liquidity would be wrong. These are offsets/qualifications to a one-way supplier-credit narrative. **A.** [10-Q, Notes 5/7][q]

6. **A named OpenAI financing round is missing.** OpenAI's February 27 announcement identifies **$30bn of NVIDIA investment** in its $110bn round, plus 3 GW inference and 2 GW training capacity on Vera Rubin. This is more informative than leaving all funding under the older up-to-$100bn LOI unknown. It does not establish that the full LOI was funded, or its relationship to every later agreement. **A for company announcement.** [OpenAI announcement][openai] An October 1 report says NVIDIA completed its final $10bn installment; **reported, unverified, C**, not primary-confirmed here. [The Information][installment]

7. **Bear/bull evidence should not be selectively framed.** Q1 DSO benefited from early payments; normalization was flagged before Q2. Margin recovery assumes pricing actions, not only cheaper memory. AMD's 107% DC growth trails NVIDIA DC's 117%, and its primary release verifies the Anthropic partnership without a crypto blog. S&P's June upgrade to **AA/stable** is counterevidence to near-term NVIDIA distress, although it predates the Ohio guarantee and must not be presented as a post-guarantee endorsement. [Q1 CFO][q1cfo]; [transcript][call]; [AMD][amd]; [S&P rating action][sp]

8. **Loss seniority is not a cross-company chronology.** Lab equity can lose value while secured creditors remain protected; guarantees may shield some lenders and shift losses to NVIDIA. NVIDIA equity can reprice before any default. Demand weakness can damage customer capex returns while today's supplier P&L remains profitable. Thus “no overbuild question inside Nvidia's own P&L” and an ordered universal loss waterfall are too categorical. This is analysis, not an additional disclosed fact.

The last-30-day search covered September 17–October 17 inclusive, NVIDIA releases/filings, partner financing and credit developments. The three primary-confirmed September changes above materially affect this note. The October OpenAI installment remains a reporting lead. I did not establish a new NVIDIA rating downgrade/default in that window; that is a search limitation, not proof none occurred. Later earnings were not substituted for the July quarter.

## Summary-bullet assessment

1. **Profitability: supported, with valuation-period qualifications.** Headline revenue, margins and trailing cash generation verify. Forward growth is an expectation. The quarter's net margin should not silently become a durable operating-margin assumption.
2. **Balance-sheet change: substantially supported, incomplete.** The increases and caps verify. “First $25bn of senior notes” should mean this issuance, not NVIDIA's first borrowing. Add the September developments and distinguish conditional maximum exposure from debt due.
3. **Circularity: statement supported; numerical extrapolation unsupported.** Management's acknowledgement and future share verify. Neither current 25–35% lab funding nor the asserted minimum dependence on capital-market-financed losses follows. The debt range also fails its own arithmetic.
4. **Concentration: disclosed figures supported; identity inference overstated.** Hyperscale ratio verifies. The unnamed lab may plausibly be OpenAI, but the disclosure does not identify it. Direct channel concentration does not mathematically establish a higher ultimate-customer concentration.
5. **Margins/competition/China: partly supported.** Margin guidance verifies. AMD is not growing faster on a DC-to-DC basis. “China effectively zero” must refer to restricted DC compute/forward assumptions, not NVIDIA's entire China-related revenue; the note's own claim 29 gives substantial revenue by Chinese customer headquarters.
6. **Cisco/valuation: conditional comparison supported; cheapness inference not supported.** The broad GAAP multiple contrast holds on the selected dates. Adjusted TTM is inconsistent; Cisco financials are hindsight denominators. Capital-market dependence across all end demand is not quantified, and procurement commitments are not all prepayments. A lower P/E than Cisco does not establish fair value.
7. **Biggest uncertainty: valid question, unsupported present-tense proportion.** Financing durability is central. “Now a quarter to a third” borrows a future forecast and unverified estimate. Keep the uncertainty; remove the supposed measured current share and separate commitment caps from expected losses.

## Your assessment

NVIDIA is comfortably profitable today and is not shown by this evidence to be financially distressed. Its risk is increasingly a combination of chip-cycle exposure, investment concentration and contractual support for customers whose infrastructure plans outgrow their own financing capacity. I agree with the note that this makes customer funding durability central, but differ from its confident estimate of current loss-funded demand, its inference of inexpensive valuation, and its fixed sequence of losers. In a downturn, speculative customer equity and NVIDIA's own valuation can fall first; who ultimately absorbs contractual losses depends on collateral, recourse, lease recovery and guarantee triggers, with some lenders protected by NVIDIA rather than losing before it. The missing September transactions reinforce the financing concern, while guarantee protections, discretionary buybacks and strong operating earnings argue against equating gross commitments with imminent insolvency. The appropriate conclusion is a highly profitable supplier taking growing, correlated financing risk—not a demonstrated current solvency crisis or a demonstrated bargain.

## Recommended edits

1. **Replace the conclusion of Analysis (d), and its Summary 3/7 echoes:** “Applying assumed debt-financed shares of 20–30% to hyperscale and 40–55% to ACIE at a 55/45 mix yields 29–41.25%. This is a scenario, not a measured funding share. Current revenue ultimately financed by loss-making labs cannot be quantified from these disclosures; management's supported-lab share refers to FY2028 total-company demand.”

2. **Add the September financing update:** “Nscale announced a $1bn NVIDIA commitment to convertible loan notes on September 25, expected to fund in mid-November 2026. SB Energy's September 21 prospectus discloses $1.5bn prepaid by NVIDIA on August 17 at 90% of the IPO price and a separate $1.5bn placement conditional on the IPO at its offer price.” [Nscale][nscale]; [SB Energy][sb]

3. **Update claim 26 and the capital-allocation analysis:** “On September 28, NVIDIA increased repurchase authorization by $150bn, leaving $235bn, which it expects to execute through FY2028. This is discretionary authorization, not a debt obligation.” [NVIDIA][buyback]

4. **Replace the guarantee characterization:** “The $105bn Ohio cap is conditional residual-value support, phased with service readiness, reduced by recoveries and scheduled lease payments, with termination provisions and reimbursement rights. Gross cap, expected loss and near-term cash demand are different measures.” Also identify the additional $3.5bn when using the $108.5bn combined cap. [8-K][guar]; [CFO][cfo]

5. **Correct the visibility paragraph:** “NVIDIA discloses $3.2bn of RPO for contracts longer than one year. This limited measure does not establish that its supply commitments are matched by firm chip orders.” [10-Q, Note 7][q]

6. **Remove the comparable-adjusted-TTM claim pending reconciliation:** “The $170.8bn sum mixes FY2026 measures excluding SBC with FY2027 measures including SBC; its 30.2× multiple is not a consistently defined adjusted P/E.” Replace “operating earnings” with “adjusted net income” for the $54bn quarterly figure. [Q4 release][q4pr]; [Q1 CFO][q1cfo]

7. **Make the valuation scenario explicit:** “Assuming $400bn FY2027 revenue, 70% growth implies $680bn FY2028 revenue and a 25% share implies $170bn. At constant shares, a 10% five-year price return and 25× terminal earnings require about $332bn net income, or $604bn revenue at a 55% net margin. These assumptions describe a scenario, not a conclusion that the stock is cheap; the required revenue is above today's run-rate.”

8. **Correct Summary 5's peer comparison:** “AMD DC revenue grew 107%, below NVIDIA DC's 117%; Broadcom AI semiconductor revenue grew 221%. These businesses differ in CPU, accelerator and networking mix.” Limit the China statement to DC compute. [AMD][amd]; [NVIDIA][pr]; [Broadcom][avgo]

9. **Repair dates, baselines and cash terminology:** Use “nine quarters earlier”; note the 72.4% Q2 FY26 margin; describe the OCF fall as 52% with working-capital and cash-tax effects; label $33.5bn total face debt versus $25bn new issuance; label July 2025 commitments as a broader category; replace “pre-paid years ahead” with “committed to future procurement.” [Q2 release][pr]; [Q2 CFO][cfo]; [Q2 FY26 CFO][oldcfo]

10. **Replace the categorical loss waterfall:** “Equity valuations can fall before defaults. Ultimate losses depend on each contract's seniority, collateral, recourse and guarantees; NVIDIA support can protect lenders and transfer losses to NVIDIA. Procurement obligations, cloud commitments, investment carrying values and guarantee caps must not be added as if each were an immediate loss.”

11. **Add the named OpenAI round and qualify identification:** “OpenAI announced $30bn of NVIDIA investment in its February 2026 financing. This does not establish funding of the entire earlier up-to-$100bn LOI.” Change the unnamed-lab identification to “possibly OpenAI; not identified in this disclosure.” [OpenAI][openai]

12. **Improve source/grade discipline:** Cite the company-hosted call for claims 5/6/19 and grade A for what management said; cite AMD's own results for the verified financials; grade estimates C and label them as scenarios. Keep Cisco multiples explicitly based on subsequently reported FY2000 results; remove the 84%-in-13-months and reserved-H100 +40% statements until the dated underlying observations are supplied.

[pr]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm
[cfo]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
[q]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[k]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[q1cfo]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm
[q4cfo]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm
[oldcfo]: https://www.sec.gov/Archives/edgar/data/1045810/000104581025000207/q2fy26cfocommentary.htm
[q4pr]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm
[q3pr]: https://www.sec.gov/Archives/edgar/data/1045810/000104581025000228/q3fy26pr.htm
[call]: https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
[guar]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
[crwv]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
[crwvpr]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
[quote]: https://stockanalysis.com/stocks/nvda/
[avgo]: https://www.sec.gov/Archives/edgar/data/1730168/000173016826000076/avgo-08022026x8kxex99.htm
[amd]: https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results
[cisco]: https://www.sec.gov/Archives/edgar/data/858877/000109581100003692/f65797e10-k.txt
[sb]: https://www.sec.gov/Archives/edgar/data/2133037/000162828026062846/sbenergy-sx1a2.htm
[nscale]: https://www.nscale.com/press-releases/pre-ipo-convertible-financing
[buyback]: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-a-150-Billion-Share-Repurchase-Authorization-Increase/default.aspx
[openai]: https://openai.com/index/scaling-ai-for-everyone/
[installment]: https://www.theinformation.com/briefings/exclusive-nvidia-softbank-make-final-20-billion-investment-openais-last-round/
[sp]: https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101690859
