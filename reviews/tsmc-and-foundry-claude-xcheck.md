# Claude cross-check: TSMC and the foundry layer

*Reviewed 2026-10-18 by Claude (Anthropic), fresh context, as the second-vendor check of `research/stack/tsmc-and-foundry.md` (Codex-written, corrected once after `reviews/tsmc-and-foundry-codex-xcheck.md`). Methodology, research brief, note and prior review were read first. Fetch budget: 15 network fetches. Five direct downloads from investor.tsmc.com hit a Cloudflare challenge. The Q3 6-K, its exhibits and TSMC's submission index came from SEC EDGAR [E1][E2]. The Q3 and January transcripts, the Q3 management report and statements, the Q2 2001 report and the 2025 Form 20-F were retrieved by WebFetch and text-extracted locally [S4][S6][S2][S3][S20][S34]. The Q1 2009 release came from pr.tsmc.com [S26]. The note's S-numbers are reused below. Web searches (not counted as fetches) were used only as leads.*

## Verdict

The note's figures hold. All 12 load-bearing rows and 14 secondary rows match primary text, the arithmetic is right, and "comfortably profitable now, utilisation risk borne by shareholders" stands.
Both Codex passes missed the same primary evidence: management's own forward demand framing (AI-accelerator CAGR "mid-to-high-fifties %" for 2024–29, "probably will be higher"), its 15 October caution on consumer segments for 2027, and the capex lag ("looking for 2028-2029 supply"). The Form 20-F also shows capacity deposits falling 35% in 2025 and the largest customer rising from 12% to 19% of revenue.
Keep the assessment. Add these items, and move the overbuild test from "2027 commissioning" to 2028–29, when the 2026–28 capex wave delivers output. On stack.md, replace "after today's backlog ships": no backlog is disclosed.

## Claim re-verification

The 12 most load-bearing rows are below. Grades follow the methodology: A means directly stated in a primary source; B means primary inputs plus arithmetic.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | Q3 2026 revenue NT$1,494.24bn / US$46.72bn; +50.9% NT$, +41.2% US$ YoY | Same. Also +17.6% QoQ in NT$ and +16.2% in US$. The July–September monthly CSV rows sum to NT$1,494,243m, matching the release exactly | Q3 release [E2 a3q26e]; CSV | Yes | A |
| 2 | Gross / operating / net margin 66.4% / 58.7% / 51.1% | Same; gross margin −1.3pp QoQ, attributed to the N2 ramp; Q3 ROE 45.5% | Release [E2]; transcript p.2–3 [S4] | Yes | A |
| 4 | HPC 68% of Q3 net revenue | Same; HPC revenue +22% QoQ. 68% of US$46.72bn ≈ US$31.8bn (B) | Presentation slide 5 [E2]; transcript [S4] | Yes | A |
| 6 | AI accelerators high-teens % of FY2025 revenue | Same: "Revenue from AI accelerators accounted for high-teens percent of our total revenue in 2025" | January transcript p.5 [S6] | Yes. **Omitted:** the same passage raises the AI-accelerator forecast to "a mid-to-high-fifties % CAGR" for 2024–2029 and the long-term company CAGR to ~25% (US$). On 15 Oct Wei said "it probably will be higher" | A |
| 11 | FY2026 capex US$52–56bn (Jan), US$60–64bn (Jul), reiterated Oct | Jan and Oct confirmed; July not re-fetched (Codex confirmed it). **Omitted:** "CapEx dollars investment from 2026 to 2028 … significantly higher than the past three years" (US$101bn in 2023–25) | [S6] p.4; [S4] p.4 | Yes | A guidance |
| 13 | Jan–Sep CFO NT$2,402.117bn − PP&E NT$1,289.971bn = NT$1,112.146bn | Same (statement p.4; US$ convenience translation 75,671m / 40,637m) | [S3] | Yes | A inputs; B FCF |
| 16 | Interest-bearing debt NT$1,031.58bn; net cash reserves NT$2,985.40bn | Same, as directly reported in the management report debt table | [S2] p.4 | Yes | A |
| 22 | Overseas GM dilution ~2pp in 2026, 3–4pp later | 2026 "closer to 2%". The CFO pinned 3–4pp to "the second part of the five-year period", i.e. not 2027 automatically | [S4] p.3, Q&A | Yes; wording can be tighter (edit 7) | A guidance |
| 26 | Q2 2001: GM 19%, utilisation 44%, operating income NT$284m on NT$26,298m = 1.08% | Same; 284/26,298 = 1.0799%. Utilisation fell from 102% a year earlier and from 70% in Q1 2001 | [S20] p.1–2 | Yes | A inputs; B ratio |
| 29 | Q1 2009 GM 18.9%, operating margin 3.1% | Same; revenue NT$39.5bn, net income NT$1.56bn. "Utilisation below 40%" is not in this release, so it was not re-verified | [S26] | Yes for margins | A |
| 38 | Capacity deposits NT$189.858bn at 31 Dec 2025; refund/offset by mutual consent | Same. **Omitted trend:** NT$291.102bn at 31 Dec 2024, so −34.8% in a year of rising demand. Also omitted: "foundry customers generally do not place purchase orders far in advance" (Item 4) | [S34] F-57, Item 4 | Yes for the balance; the trend changes its interpretation | A |
| 40 | Q3 capex US$13.84bn; YTD US$40.64bn; implied Q4 US$19.36–23.36bn | Same (Q1 11.10, Q2 15.70, Q3 13.84). Q3 capex fell QoQ (NT$443.21bn vs NT$496.00bn), which flatters Q3 FCF | [S2] p.5; [S4] | Yes | A actuals; B implication |

Secondary rows also checked and matched: 3 (NT$763.06bn, +68.7%), 5 (node mix, 79% advanced), 9 (Q4 guide US$52.3–54.3bn, GM 65–67%, OM 56.5–58.5%; the transcript adds +14% QoQ and +58% YoY at the midpoint), 12 (slide: CFO 919.77, capex 443.21, FCF 476.56, dividends 155.59), 14 (cash and securities 4,016.98; equity 7,043.23; current ratio 2.6), 17 (Customer A 19%, B 17% in 2025), 24 (N2 capacity "more than double in 2027"), 36 (dividends YTD 440.853), 37 (NT$198.74bn "mainly attributable to U.S. Treasury Department Investment Tax Credits"), 39 (NT$1,534.575bn, of which 1,220.393bn within one year), 42 (Tainan N3 H1 2027, a second Tainan N3 fab H1 2028, Arizona fab 2 Q3 2027 "slightly ahead of our previous schedule"), 44 ("the fab got to be run by TSMC"), 45 (slide 9: "around 44%"), 46 ("56% and higher through the cycle … ROE of high-twenties percent"). No mismatches were found.

## Arithmetic checks

| Derived figure in note | Recalculation | Result |
|---|---|---|
| YTD FCF | 2,402.117 − 1,289.971 = 1,112.146 | Correct |
| YTD after dividends | 1,112.146 − 440.853 = 671.293 | Correct |
| Q3 FCF, statement vs slide | 919.776 − 443.206 = 476.570 vs 476.56 | Correct; NT$10m precision gap, properly disclosed |
| Q3 after dividends | 476.570 − 155.595 = 320.975 | Correct |
| Debt and net cash | 818.38 + 213.198 = 1,031.578; 4,016.98 − 1,031.58 = 2,985.40 | Correct; matches reported totals |
| Q4 implied capex | 60 − 40.64 = 19.36; 64 − 40.64 = 23.36; ÷13.84 → +39.88% / +68.79% | Correct |
| Capex guide growth | 62/54 − 1 = 14.81%; 60/40.9 − 1 = 46.70%; 64/40.9 − 1 = 56.48% | Correct |
| Concentration | 19 + 17 = 36% | Correct at rounded precision |
| 2001 margin | 284 / 26,298 = 1.0799% | Correct |
| CSV | 33 rows; 2024 sum 2,894,307 (published 2,894,308); 2025 3,809,054; Jan–Sep 2026 3,898,727, +41.1% vs Jan–Sep 2025 (2,762,964) | Correct |
| Investing inflow reconciliation | 198.74 − 22.32 (securities) − 3.87 (other financing) − 5.00 (FX) = 167.55, the slide's "Investments and others" | Consistent |

Useful derived figures absent from the note, all grade B from the primary inputs above:

- **Revenue is a year ahead of management's own long-term path.** FY2025 was US$122bn at +35.9%, so FY2024 was about US$89.8bn. "Around 44%" growth gives FY2026 of about US$175.7bn. A 25% CAGR from 2024 reaches US$175.3bn only in 2027 and US$274.0bn in 2029. If January's 25% CAGR held, 2027–29 growth would have to slow to about 16% a year while 2026–28 capex is "significantly higher". In practice, either management raises the long-term guide, which Wei signalled for AI, or capital intensity and returns deteriorate. This is the cleanest overbuild test the note can state.
- **Capital intensity.** US$60–64bn on about US$175.7bn of revenue is 34–36%, against 33.5% in FY2025 (40.9/122). FY2026 capex alone equals 59–63% of the entire 2023–25 total of US$101bn.
- **Depreciation is accelerating.** Q3 D&A was NT$220.20bn, +35.3% YoY and +10.9% QoQ, and 14.7% of Q3 revenue. January guided full-year depreciation to rise by a "high-teens percentage". This is the fixed-cost base that drove 2001 and 2009 margins down. [S2][S6]
- **Size of tax-credit receipts.** NT$198.74bn is 21.6% of Q3 CFO. At Q3's implied rate of NT$32.0 per US$ (443.21/13.84), it is about US$6.2bn in one quarter, comparable to the entire US$6.6bn CHIPS grant ceiling. Public support for Arizona runs mainly through tax credits, not grants. [S2][S33]
- **Dividend step-up.** The Q2 2026 dividend is NT$7.00 per share against the NT$6.00 paid in Q3 (155.595/25.932). That is about NT$181.5bn a quarter from January 2027, against Q3's FCF of NT$476.56bn. [E2 slide 10]
- **Concentration is rising.** Customer A grew from NT$352.3bn (12%) in 2024 to NT$727.0bn (19%) in 2025, +106%. Customer B fell from 25% (2023) to 22% to 17%. [S34 F-82]

## Omissions

From the last 30 days, all in primary sources the note already cites:

1. **Management's demand caution on 15 Oct.** "We continue to observe consumer and price-sensitive end market segments are being challenged due to the impact of rising component prices and more economic uncertainties. As such, we are being prudent in our business planning going into 2027." This is the strongest bearish statement on the call, and both passes omitted it. Smartphone is 21% of revenue; rising memory prices (the AI build crowding out consumer demand) is a cross-layer channel. [S4 p.3]
2. **Scale of the build.** "Nearly 20 fabs worldwide in progress … 13 leading edge and advanced packaging fabs in Taiwan over the next several years, and another five to six fabs overseas." Add also the Japan fab 2 on N3 in 2028, and A14 risk production in 2027 with volume in 2028. [S4 p.4]
3. **Forward AI growth guidance.** The AI-accelerator CAGR is "mid-to-high-fifties %" for 2024–29 (January). On 15 Oct Wei said: "we did not see any sign of slowdown whether it's high 50% CAGR, it doesn't matter, it probably will be higher." This is both the main bull anchor and the quantity an overbuild would falsify. The note gives only the backward FY2025 share. [S6 p.5][S4 p.6]
4. **Tool-price inflation.** The CFO said "The tool price inflation is real", covering tools, materials and labour. This interacts with ASML's supply-shortfall outlook: more capex dollars buy less capacity. [S4]
5. **2027 price increases (secondary, C).** Nikkei-sourced reports put base increases at 5–10% from January 2027, with premiums for overflow HPC orders (e.g. [T1]). Asked on 15 Oct, Wei did not deny it: pricing "depends on the market segment … location … technology" and "we will give our shareholders the maximum value". If true, part of 2027 revenue growth is price rather than volume, which flatters demand signals while capacity rises. Record this as reported and unverified. Claim 25's "no verified uniform increase" is correct but incomplete.

From primary filings the note opened but under-read:

6. **Capacity deposits are shrinking and contracts are short.** The deposit balance fell from NT$291.1bn to NT$189.9bn in 2025, and the 20-F says customers "generally do not place purchase orders far in advance". That cuts against the cross-check's framing that "customer deposits also fund capacity". At about 5% of 2025 revenue and falling, deposits are a minor offset. Utilisation risk sits squarely with TSMC shareholders, and the note's "loss sharing depends on customer contracts" overstates how much contracts protect TSMC. [S34 Item 4, F-57]
7. **Fixed-cost language.** "Semiconductor manufacturing facilities … are largely fixed cost assets … these costs do not decline when customer demand or our capacity utilization rates drop." This is direct primary support for the 2001/2009 analogy and should be cited beside it. [S34 Item 3]
8. **The capex lag sets the risk window.** Wei in January: "it takes … two to three years to build a new fab … the contribution to this year is almost none, and 2027, a little bit. So … we are looking for 2028-2029 supply, and we hope it's a time that the gap will be narrow." Combined with Wei's October comment, "I'm also very nervous about it … If we did not do it carefully, that will be a big disaster to TSMC for sure", this dates the test. The note quotes only "very nervous" and frames 2027 commissioning as the test. The material overbuild exposure is the 2028–29 output of the 2026–28 capex wave. [S6 pp.5, 9]
9. **Analyst question on funding and power.** Citi asked how TSMC reconciles capacity plans with "data center power availability, and also maybe funding recently". Wei answered that TSMC factors "CSPs, CapEx, data centers' build-out, financial, power supply" into its own judgement. This ties TSMC's demand directly to the hyperscaler and lab financing covered elsewhere in the report. It is useful for cross-layer linking but does not change the numbers. [S4 p.6]

Not omissions but limits: Intel's Q3 2026 10-Q is not yet out. Reports of a Tesla/Terafab 14A engagement with Intel are secondary leads only, and Wei separately confirmed Terafab talks with TSMC. Absolute CoWoS capacity remains unverified. Secondary reports (about 130k wafers per month at end-2026, doubling by 2028) are leads, grade C at best [T2]. Section 232 chip-tariff status in October could not be confirmed from primary sources.

## Summary-bullet assessment

| Bullet | Supported by note's evidence? | Concrete (figure + date)? | Comment |
|---|---|---|---|
| 1 Margins 66.4% / 58.7% | Yes [S1] | Yes, Q3 2026 | Fine |
| 2 Self-funding; Q4 capex step-up; loss sharing | Figures yes [S3][S2] | Yes | "Loss sharing depends on customer contracts and public support" overstates contractual protection given omission 6. Edit 2 |
| 3 HPC 68% vs FY2025 high-teens | Yes [S2][S6] | Yes | Accurate but backward-looking. Add the forward AI CAGR guidance (edit 3) |
| 4 Capex US$60–64bn; Tainan/Arizona dates | Yes [S4] | Yes | Omits the 2026–28 capex trajectory and the ~20 fabs in progress. The investment test is 2028–29 output, not only 2027 commissioning (edit 4) |
| 5 Overseas dilution ~2pp, then 3–4pp; US$265bn envelope | Yes [S4][S11] | Yes | "Following years" should be "later in the five-year period" (edit 7) |
| 6 Intel Foundry Q2 loss; Samsung | Yes [S24][S25] | Yes | Fine; refresh after Intel's Q3 10-Q |
| 7 2001 1.08% / 2009 3.1%; Taiwan | Yes [S20][S26][S34] | Yes for history; Taiwan has no figure | Add the 20-F fixed-cost sentence and "majority of net revenue derived from operations in the R.O.C." (edit 6) |

No bullet contains an unsupported figure. The gap is balance: the Summary has no forward-looking management number, bullish or bearish, although TSMC supplied both.

## Your assessment

TSMC is comfortably profitable, and its build is self-funded. YTD FCF after dividends is NT$671bn, net cash is NT$2,985bn, and Q4 is guided at +58% YoY. No financing channel through which it could be "overextended" exists today. Shareholders lose first if demand disappoints, and more completely than the note implies. Deposits are small and shrinking, orders are short-dated, and costs are "largely fixed". Equipment suppliers come second through deferrals, and creditors face no realistic risk. My main difference from the note is timing and framing. The note treats 2027 commissioning as the test. TSMC's own statements put the risk window in 2028–29, when the 2026–28 capex wave delivers output, and that is also the end of the AI-accelerator CAGR window management is underwriting. Revenue is already a year ahead of the 25% long-term path. Capital intensity is rising (34–36%), tool prices are inflating, depreciation is growing over 30% a year, and 2027 prices are reportedly rising. All of this makes current margins depend more on the AI build continuing than the 68% HPC share suggests. Management itself flagged consumer weakness and "prudent" 2027 planning. I would describe TSMC as the least fragile large AI-exposed balance sheet, with high operating leverage to a 2028–29 demand shortfall. Equity drawdown risk is real. Solvency risk is negligible.

## Front-page figures

| Page | Figure / statement | From this note? | Still holds? |
|---|---|---|---|
| index.md, Strongest arguments, Supply row | "TSMC says demand exceeds supply" (A) | Yes, [S4] 15 Oct: "far above our capability today to supply" | **Holds.** The page should pair it with the same call's caution on consumer segments for 2027 (edit 9) |
| stack.md, Foundry row | "66% gross, 59% operating margin" | Yes, Q3 66.4% / 58.7% | **Holds** (rounded); Q4 guide 65–67% / 56.5–58.5% |
| stack.md, Foundry row | "Operating cash flow; capex $60-64B fully covered" | Yes | **Holds** for YTD (OCF NT$2,402bn vs PP&E NT$1,290bn; positive after dividends). Q4 needs US$19.4–23.4bn |
| stack.md, Foundry row | "New leading-edge and CoWoS capacity arriving after today's backlog ships" | Derived from the old note wording | **Does not hold as worded.** No backlog is disclosed, and the 20-F says customers do not order far ahead. The Codex review already flagged this, and stack.md was not updated. Replace (edit 10) |
| stack.md, Foundry row | "AI accelerators were high-teens % of revenue in the last full year" | Yes, FY2025 | **Holds**; add the forward CAGR (edit 10) |
| stack.md, Foundry row | "Shareholders via utilisation; Taiwan is a separate tail" | Yes | **Holds**, and the 20-F fixed-cost and short-order language strengthens it |
| stack.md, "The shape of it" | "TSMC 59%" operating margin | Yes | **Holds** |
| Brief's list: revenue US$46.7bn (+41%), HPC 68%, 2001 1.08% at 44% utilisation, 2009 3.1%, Taiwan concentration | Not found on report/index.md or report/stack.md (grep, 2026-10-18). They appear in the note and, for HPC 68%, in signals/2026-10-18-market-views.md | Yes | **All verified as correct** against primary sources (claims 1, 4, 26, 29, S34) |

## Recommended edits

1. **Key claims, new row 47 (forward guidance):** "AI-accelerator revenue forecast | 'mid-to-high-fifties %' CAGR, 2024–2029 (narrow definition); company revenue ~25% CAGR (US$) over the same period; on Oct 15, 2026 Wei: 'it probably will be higher' | Jan 15 / Oct 15, 2026 | [January call, p.5][S6]; [October call, p.6][S4] | primary | A management forecast, not an outcome"
2. **Summary bullet 2, replace the last sentence** with: "Future factory returns remain at risk and sit mainly with shareholders: customer capacity deposits fell from NT$291.1bn to NT$189.9bn during 2025, and the 2025 Form 20-F says foundry customers 'generally do not place purchase orders far in advance'." [S34]
3. **Summary bullet 3, append:** "Management's forward view is far larger: in January it forecast a mid-to-high-fifties % CAGR in AI-accelerator revenue for 2024–29, and on October 15 Wei said it 'probably will be higher'." [S6][S4]
4. **Summary bullet 4, replace** with: "TSMC guides to US$60–64bn of 2026 capex (34–36% of the ~US$176bn implied by its ~44% growth outlook) and says 2026–28 capex will be 'significantly higher' than the US$101bn of 2023–25, with nearly 20 fabs in progress. New Tainan N3 output starts H1 2027 and H1 2028, Arizona fab 2 Q3 2027. In January Wei said new capex mainly serves '2028-2029 supply': that, not 2027, is when demand must absorb the build. Absolute CoWoS capacity remains unverified." [S4][S6]
5. **New Summary bullet after bullet 4:** "On October 15 management said consumer and price-sensitive segments 'are being challenged due to the impact of rising component prices' and that it is 'being prudent in our business planning going into 2027', while calling AI demand 'still far above our capability today to supply'." [S4]
6. **Summary bullet 7, append:** "The 2025 Form 20-F describes fabs as 'largely fixed cost assets' whose costs 'do not decline when … capacity utilization rates drop', and says the majority of net revenue derives from operations in Taiwan." [S34]
7. **Claim 22 and Summary bullet 5:** replace "widening to 3–4 points in following years" with "widening to 3–4 points in the second part of the five-year period, as more US fabs ramp". [S4]
8. **Analysis, "Current earnings and financing", replace** "Customer deposits also fund capacity: the December 31, 2025 balance was NT$189.858bn…" with: "Customer deposits are a small and shrinking offset: NT$189.858bn at December 31, 2025, down from NT$291.102bn a year earlier (−34.8%), settled by refund or receivable offset by mutual consent. Q3 2026 depreciation and amortisation was NT$220.20bn (+35.3% YoY; 14.7% of revenue), against January guidance of a high-teens % rise in 2026 depreciation; this is the fixed-cost base that drove the 2001 and 2009 troughs." Also add to the overseas paragraph: "At Q3's implied NT$32.0/US$, the NT$198.74bn tax-credit-related inflow is about US$6.2bn in one quarter, comparable to the whole US$6.6bn CHIPS grant ceiling." [S34][S2][S6][S33]
9. **Analysis, "Capacity and overbuild", add:** "Revenue is already a year ahead of management's January long-term path: FY2026 at ~US$175.7bn (US$122bn × 1.44) matches a 25% CAGR from 2024 (~US$89.8bn) only in 2027 (US$175.3bn). If that 25% path to 2029 (~US$274bn) held, 2027–29 growth would slow to ~16% a year while capex rises. Either guidance is raised or returns on the 2026–28 build fall; watch the January 2027 long-term outlook. The CFO also said 'tool price inflation is real.' Separately, Nikkei-sourced reports of 5–10% base price increases from January 2027 are reported, unverified (C); asked on October 15, Wei did not deny them." [S4][S6][T1] In Conflicts, extend the "nervous" quote with "If we did not do it carefully, that will be a big disaster to TSMC for sure." [S6]
10. **stack.md Foundry row (lead agent to apply; outside this note):** replace "New leading-edge and CoWoS capacity arriving after today's backlog ships; AI accelerators were high-teens % of revenue in the last full year" with "2026–28 capex 'significantly higher' than 2023–25's $101B, with output landing in 2028–29; management underwrites a mid-to-high-50s % AI-accelerator CAGR to 2029 (high-teens % of 2025 revenue); customer deposits fell 35% in 2025". In index.md's Supply row, consider "TSMC says AI demand exceeds supply, but is 'prudent' on 2027 consumer demand (A)".
11. **Signals table, add two rows:** "Long-term outlook revision | AI-accelerator CAGR mid-to-high 50s % (2024–29); company ~25% | Jan 2026 / Oct 2026 | [S6][S4] | A raise confirms demand; holding 25% implies ~16% a year in 2027–29 against rising capex". And: "Customer capacity deposits | NT$189.9bn, −35% YoY | Dec 31, 2025 | [S34] | Rising deposits mean customers share risk; falling deposits mean TSMC carries it."
12. **Sources:** add the SEC-hosted Q3 6-K [E2] as a mirror for S1/S12. TSMC's own URLs sit behind a Cloudflare challenge for scripted fetches, and EDGAR is reproducible.

[E1]: https://data.sec.gov/submissions/CIK0001046179.json
[E2]: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/0001046179-26-000726.txt
[S2]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf
[S3]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/3a94d1034b9e6b22446b674f7aaf3d088a12a193/FS.pdf
[S4]: https://investor.tsmc.com/japanese/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf
[S6]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[S11]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[S20]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/english/2001/Q2/2q01fr.pdf
[S26]: https://pr.tsmc.com/english/news/1548
[S33]: https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[S34]: https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
[T1]: https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes
[T2]: https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/
