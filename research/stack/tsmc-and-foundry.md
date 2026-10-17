# TSMC and the foundry layer

*Last updated: 2026-10-17 · Status: draft · Author: Codex (OpenAI) · Reviewer: none; historical and peer figures independently checked by a same-vendor research agent*

## Summary

- TSMC manufactures and packages the silicon behind AI systems. Its current business is comfortably profitable: quarterly gross and operating margins are 66.4% and 58.7%, respectively. This is evidence of realized supplier profits, not proof of satisfactory returns for downstream AI buyers. [S1]
- Operating cash generation comfortably exceeds current capital spending. Expansion is supported principally by retained cash generation, supplemented by bonds and government assistance; shareholders bear the first economic loss from underused factories. [S3][S10]
- HPC supplies 68% of quarterly revenue, but HPC is broader than AI. The separately disclosed AI-accelerator share was high-teens percent for the last completed year. Treating all HPC revenue as AI materially exaggerates measured exposure. [S2][S6]
- Leading-edge and advanced-packaging expansion remains aggressive. Present scarcity supports investment, but new capacity must earn returns after today’s backlog has shipped. CoWoS capacity in absolute monthly units is not verified here.
- Overseas manufacturing diversifies supply but costs more. Subsidies and customer willingness to pay for geography matter to its economics; announced investment envelopes are not annual expenditures.
- Intel Foundry remains loss-making; Samsung does not disclose sufficient standalone Foundry financials to establish comfortable profitability. TSMC’s economics should not be assigned to the entire layer. [S24][S25]
- The biggest uncertainty is sustained economically justified AI demand when expanded capacity arrives. Historical utilization collapses nearly eliminated operating profit; Taiwan disruption is a separate, potentially much more severe tail risk.

## Key claims

All sources were accessed **2026-10-17**. TSMC periods are calendar periods; NT$ means New Taiwan dollars and US$ means US dollars. A grades on guidance establish what management said, not that the outcome will occur. Numerical observations in the accompanying CSV are individually sourced there.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Latest reported quarterly revenue | NT$1,494.24bn / US$46.72bn; YoY +50.9% in NT$, +41.2% in US$ | Q3 2026; released Oct 15 | [Release][S1] | primary | A |
| 2 | Gross / operating / net margin | 66.4% / 58.7% / 51.1% | Q3 2026 | [Release][S1] | primary | A |
| 3 | Profit attributable to parent shareholders | NT$763.06bn; +68.7% YoY | Q3 2026 | [Release][S1] | primary | A |
| 4 | Platform mix, net revenue | HPC 68%; smartphone 21%; IoT 4%; automotive 4%; digital consumer electronics 1%; other 2% | Q3 2026 | [Management report][S2] | primary | A |
| 5 | Node mix, wafer revenue | 2nm 8%; 3nm 33%; 5nm 28%; 7nm 10%; 16/20nm 6%; 28nm 6%; 40/45nm 2%; 65nm 4%; 90nm–0.13µm 1%; ≥0.15µm 2%; advanced subtotal 79% | Q3 2026 | [Management report][S2] | primary | A |
| 6 | AI accelerator share, narrower than HPC | High-teens percent of total revenue | FY2025 | [January call][S6] | primary | A |
| 7 | Latest monthly revenue | NT$511,857m; +54.6% YoY; August +53.3% YoY | September / August 2026 | [Monthly series][S9] | primary | A |
| 8 | Monthly-series published totals | 2024 NT$2,894,308m, +33.9%; 2025 NT$3,809,054m, +31.6%; Jan–Sep 2026 NT$3,898,727m, +41.1% | Respective periods | [2024][S7], [2025][S8], [2026][S9] | primary | A |
| 9 | Next-quarter guidance | Revenue US$52.3–54.3bn; gross margin 65–67%; operating margin 56.5–58.5% | Q4 2026 guidance, Oct 15 | [Release][S1] | primary | A |
| 10 | Actual capital expenditure / free cash flow | US$40.90bn / NT$1,002.57bn | FY2025 | [Year-end management report][S5] | primary | A |
| 11 | Annual capex guidance progression | US$52–56bn initially; US$60–64bn in July, reiterated October | FY2026 guidance | [January][S6], [July][S11], [October][S4] calls | primary | A |
| 12 | Quarterly cash generation and uses | CFO NT$919.77bn; capex NT$443.21bn; FCF NT$476.56bn; dividends NT$155.59bn | Q3 2026 | [Presentation][S12] | primary | A |
| 13 | Year-to-date cash generation | CFO NT$2,402.117bn less PP&E purchases NT$1,289.971bn = FCF NT$1,112.146bn | Jan–Sep 2026 | [Statements][S3]; subtraction | primary | B |
| 14 | Liquid assets / equity | Cash and marketable securities NT$4,016.98bn; equity NT$7,043.23bn; current ratio 2.6 | Sep 30, 2026 | [Presentation][S12] | primary | A |
| 15 | Interest-bearing debt components | Long-term NT$818.38bn; current bonds/loans NT$213.198bn | Sep 30, 2026 | [Presentation][S12], [statements][S3] | primary | A |
| 16 | Debt and liquidity cushion, derived | Debt approximately NT$1,031.58bn; liquid assets less debt approximately NT$2,985.40bn; does not deduct all liabilities | Sep 30, 2026 | [S12], [S3]; addition/subtraction | primary | B |
| 17 | Disclosed major-customer concentration | Customer A 19%, Customer B 17%; combined 36% derived. Identities withheld | FY2025 | [Audited consolidated report][S13] | primary | A individual; B combined |
| 18 | Named commercial relationships | Nvidia, Apple, AMD and Broadcom confirmed; their individual shares of TSMC sales not verified | Company disclosures available at cutoff | [Nvidia][S14], [Apple][S15], [AMD][S16], [Broadcom][S17] | primary | A relationships only |
| 19 | Documented CoWoS expansion baseline | July 2024 management statements: capacity more than doubled in 2024; aimed to double or more again in 2025; partly shared, version-specific tool sets | July 18, 2024 statement | [Call][S18] | primary | A statement; not subsequent actual |
| 20 | Current absolute CoWoS capacity/utilization | No verified monthly wafer-capacity or utilization number in retrieved primary disclosures | Oct 17, 2026 search cutoff | [Current call][S4], [packaging agreement][S19] | primary | C evidence-coverage limitation |
| 21 | US interposer expansion | US$2bn agreement; initial five-year term; Malta volume ramp expected H1 2028 | Oct 8, 2026 announcement | [GlobalFoundries][S19] | primary | A announced terms |
| 22 | Overseas gross-margin dilution outlook | Approximately 2 percentage points in 2026; 3–4 points later | Oct 15, 2026 | [Call][S4] | primary | A guidance |
| 23 | Arizona investment envelope | Additional US$100bn; cumulative US$265bn; schedule demand-dependent | July 16, 2026 | [Call][S11] | primary | A announced plan |
| 24 | Leading-edge capacity expansion | N2-family annual capacity expected to more than double in 2027 | Oct 15, 2026 | [Call][S4] | primary | A guidance |
| 25 | Pricing policy | Differentiated by technology, market and location; no verified uniform increase | Oct 15, 2026 | [Call][S4] | primary | A policy; C absence of uniform figure |
| 26 | Dot-com margin stress | Q2 gross margin 19%, utilization 44%; operating income NT$284m / revenue NT$26,298m = operating margin 1.08% | Q2 2001 | [Financial report][S20] | primary | A inputs; B ratio |
| 27 | Dot-com utilization trough | Q3 utilization 41%, gross margin 25%; Q4 utilization recovered to 50% | Q3 / Q4 2001 | [Q3 report][S21], [Q4 release][S22] | primary | A |
| 28 | Financial-crisis shock | Gross margin 31.3%; operating margin 18.6% | Q4 2008 | [Release][S23] | primary | A |
| 29 | Subsequent financial-crisis trough | Gross margin 18.9%; operating margin 3.1%; utilization below 40% | Q1 2009 | [Release][S26], [call][S27] | primary | A |
| 30 | Recent inventory downturn | FY2023 US$ revenue −8.7%; quarterly gross/operating margins Q1 56.3/45.5%, Q2 54.1/42.0%, Q3 54.3/41.7%, Q4 53.0/41.6%; both minima Q4 | 2023 | [Annual][S28], [Q1][S29], [Q2][S30], [Q3][S31], [Q4][S32] | primary | A figures; B minima |
| 31 | Intel Foundry economics | Revenue US$5.765bn; operating loss US$2.089bn; external revenue US$293m | Q2 2026 | [10-Q][S24] | primary | A |
| 32 | Samsung Foundry economics | Earnings improved before incentive provisions; standalone revenue/profit not supplied; 2nm HPC engagements expanding | Q2 2026 | [Samsung results][S25] | primary | A statement |
| 33 | US public support | Up to US$6.6bn direct CHIPS funding awarded, milestone-dependent; not all cash received | Nov 15, 2024 award | [Commerce][S33] | primary | A |
| 34 | Monthly rounding reconciliation | 2024 monthly sum NT$2,894,307m versus published total NT$2,894,308m: NT$1m difference; CSV has 33 reported months through Sep 2026 | Data retrieved Oct 17, 2026 | [S7]–[S9]; arithmetic | primary | B |
| 35 | Investment assessment | Comfortable current profitability; meaningful future overbuild risk; no demonstrated current financing crisis | Oct 17, 2026 | Analysis of [S1]–[S4], [S20]–[S32] | primary | C analytical judgement |

## Analysis

**Current earnings and financing.** Currency matters: NT$ and US$ revenue growth differ. Platform mix uses net revenue; node mix uses wafer revenue. [S1][S2]

The cash evidence is stronger than an EBITDA presentation: reported operating cash flow already exceeds purchases of property and equipment, leaving positive free cash flow and room for dividends. The year-to-date calculation is CFO minus gross PP&E purchases, without subtracting dividends or adding asset-sale proceeds. The liquidity cushion uses current and long-term interest-bearing debt, not merely the long-term bond balance. This is not a liquidation estimate or a deduction of all liabilities. These observations support a low current refinancing-pressure assessment. [S3][S12]

TSMC identifies operating cash and corporate bonds as funding sources for production investment. [S10] If demand disappoints, the immediate mechanisms are lower factory absorption, weaker cash generation and reduced returns on invested equity. Contractors and equipment suppliers face order deferrals; creditors bear losses only if deterioration ultimately overwhelms the company’s resources. Government grants transfer some construction risk to taxpayers, subject to award conditions. [S33] Public support does not guarantee plant profitability.

**Demand, customer concentration and pricing.** Customer relationships are documented independently of the anonymous concentration table: Nvidia describes Blackwell manufacturing at TSMC; Apple describes its Arizona chip supply; AMD confirms its manufacturing partnership; Broadcom identifies TSMC as an outsourced foundry. [S14]–[S17] The filings do not authorize assigning the anonymous shares to particular names. AMD and Broadcom may also transmit demand from overlapping cloud customers, so diversity of chip designers does not establish diversity of ultimate funding.

TSMC can benefit from either merchant GPUs or custom accelerators using its processes and packaging. A broad AI investment retreat would still hurt demand. Apple-related consumer demand offers some diversification but cannot be assumed to fill freed AI capacity immediately: process qualifications, designs and packaging requirements differ.

Pricing power is supported by high realized margins and scarcity, but neither proves unlimited price discretion. Revenue mix, currency, yield and utilization also influence profitability. The management report attributes the sequential gross-margin decline primarily to the initial N2 ramp, demonstrating that technological progress itself can impose a near-term cost. [S2] No customer-level contractual price schedule or blanket increase is established here.

**Capacity and overbuild.** CoWoS integrates logic and memory into advanced packages. Its economic constraint is useful packaged output, not just the number of wafer starts. TSMC’s earlier explanation emphasized differences among CoWoS versions and their equipment. [S18] Consequently, a capacity headline can overstate flexibility: tools serving one package architecture may not immediately relieve another bottleneck. Larger packages, yield losses and processing intensity also make a single wafer-count comparison an incomplete measure of economic capacity.

The GlobalFoundries agreement establishes an additional US interposer supply route, not an already operational expansion of completed CoWoS packages. [S19] Other packaging steps and customer qualification must also be available. The announced ramp date illustrates the lag between demand signals and usable output. It does not establish a take-or-pay obligation for the agreement’s full headline value; termination and minimum-volume protections were not disclosed in the announcement.

The strongest overbuild mechanism is synchronized expansion across foundries, packaging partners and downstream customers on correlated demand forecasts. Reservations motivated by scarcity can disappear once availability improves. Even if AI usage keeps increasing, cheaper inference, improved utilization of existing accelerators or slower monetization could reduce incremental chip purchases. Conversely, efficiency could expand affordable use sufficiently to sustain demand. Neither direction is settled by supplier revenue alone. This is an analytical risk assessment, not evidence that current orders are fictitious.

**Overseas economics and Taiwan.** Arizona’s cumulative investment envelope is a multiyear plan; adding it to annual global capex would double-count investment. [S11] Public assistance offsets some capital cost, but award ceilings are not current cash receipts. [S33] Local labor, supplier networks, construction and ramp efficiency determine whether geographic diversification earns acceptable returns. Overseas group-margin dilution is not the same thing as a disclosed Arizona standalone loss.

The annual filing locates most principal production facilities and revenue-generating operations in Taiwan and warns about military conflict, transportation disruption and trade restrictions. [S34] A blockade or prolonged infrastructure interruption could prevent production or delivery even if customer demand remains strong. Overseas capacity reduces exposure gradually; it cannot instantly reproduce the interconnected Taiwan manufacturing, supplier and engineering ecosystem. No invasion probability or assumption of normal operations during a disruption is supported here.

**What downturns demonstrate.** During the dot-com contraction, the low point for utilization followed the low point for gross margin. Better mix and pricing helped margins recover while factory loading still deteriorated. [S20][S21] TSMC also deferred expansion. Historical accounting scope and technology mix differ from today, so the episode demonstrates fixed-cost sensitivity rather than a reusable numerical stress-test formula.

The financial-crisis shock began in the late-2008 results, but the deeper margin and utilization trough came in early 2009. Calling the later figures “2008 utilization” would misdate the evidence. [S23][S26][S27] In the more recent inventory correction, TSMC retained much higher margins; its annual report nevertheless attributes pressure partly to lower utilization and the new-node ramp. [S28] The historical conclusion is survival with widely varying profitability, not an invariant margin floor. Today’s favorable product mix may cushion a contraction, but historical resilience does not guarantee that newly installed capacity earns its cost of capital.

**Other foundries.** Intel’s segment revenue is overwhelmingly internal manufacturing, so it is not comparable to TSMC’s external-customer revenue. Its filing also says external growth benefited from Altera’s reclassification following deconsolidation, while reduced period charges helped the operating-loss comparison. A revenue increase therefore does not by itself demonstrate competitive external foundry traction. [S24] Losses must be financed within Intel’s wider corporate funding structure; the disclosed segment has not demonstrated self-funding economics.

Samsung reports improving orders and expanding advanced-node engagements, which contradict any assumption that alternative suppliers cannot gain business. But its disclosure does not establish standalone Foundry profitability. [S25] Group or memory earnings cannot fill that gap. These alternatives could constrain TSMC pricing or attract geographically motivated demand, yet technology availability is insufficient: manufacturing yield, reliable delivery, packaging and customer qualification determine commercial substitutability.

## Conflicts and open questions

- **Management confidence versus overinvestment risk.** In October, Wei said demand was “still far above our capability today to supply.” [S4] In January he said, “I'm also very nervous about it,” while explaining checks with customers and cloud providers. [S6] Management also reports inspecting US datacenter construction and power readiness (primary, A). [S4] Such diligence supports capacity planning, but construction progress does not establish profitable end-user demand.
- **HPC versus AI.** TSMC excludes CPUs from its narrow accelerator definition because their ultimate application cannot reliably be separated. [S4] The disclosed accelerator share and HPC platform mix are different measurements and periods. A current, reconciled AI revenue bridge is missing.
- **Scarcity versus future surplus.** Expansion announcements and current demand are genuine evidence against an already collapsed market. They also create future supply risk. Exact installed CoWoS capacity, utilization by version and contractual cancellation protection remain unverified; media wafer estimates are not promoted to company facts.
- **Pricing and overseas costs.** Expansion costs and competitors limit margin extrapolation. Customer-specific US premiums, plant-level returns and subsidy receipts remain insufficiently disclosed.
- **Concentration and historical comparability.** Named customer revenue percentages, exact late-2008 utilization and the quarterly utilization series for 2023 were not verified. Anonymous customer letters can change ranking between annual presentations. A current break-even utilization threshold cannot responsibly be extrapolated from old troughs.
- **Scope limits.** Intel’s next results were scheduled after this cutoff; Samsung’s October preliminary announcement did not disclose Foundry economics. [S35][S36] The peer comparison therefore uses their latest detailed quarterly disclosures. This note assesses business and capacity risk, not whether any current share price already discounts those risks.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| Monthly sales growth | September +54.6% YoY; August +53.3% | Sep 2026 | [S9] | Persistent deceleration is more informative than a seasonal monthly dip; check currency effects. |
| HPC platform mix | 68% | Q3 2026 | [S2] | Indicates computing exposure, without treating all HPC as AI. |
| Leading-edge mix | Advanced nodes 79% of wafer revenue | Q3 2026 | [S2] | Tests whether new capacity supports high-value output. |
| Capex revisions | US$60–64bn guidance | Oct 2026 | [S4] | A cut alongside weaker sales/loading would be a stronger warning than either alone. |
| CoWoS supply announcements | GF interposer agreement; ramp expected H1 2028 | Oct 2026 | [S19] | Track commissioning and qualification, not just committed dollars. |
| Utilization commentary | Demand exceeds supply; numerical node/CoWoS rates unverified | Oct 2026 | [S4] | Watch for allocation relief, idle tools and order postponements. |
| Margins | Gross 66.4%; operating 58.7% | Q3 2026 | [S1] | Separate loading deterioration from predictable ramp costs. |
| Cash versus investment | Quarterly FCF NT$476.56bn | Q3 2026 | [S12] | Sustained deterioration would weaken the self-funding conclusion. |
| Overseas cost absorption | About 2 points of gross-margin dilution guided | FY2026 | [S4] | Tests whether diversification remains economically manageable. |
| Competitive profitability | Intel Foundry operating loss US$2.089bn; Samsung standalone profit unavailable | Q2 2026 | [S24][S25] | Distinguishes alternative capacity from commercially sustainable competition. |

## Sources

Full URLs are the link targets below; **every source accessed 2026-10-17**. Company-hosted call transcripts are primary evidence of management statements. The [monthly CSV](/data/tsmc-monthly-revenue.csv) preserves reported rounded values and omits unreported future months.

1. [S1 — TSMC, Q3 2026 earnings release][S1], published 2026-10-15.
2. [S2 — TSMC, Q3 2026 management report][S2], published 2026-10-15.
3. [S3 — TSMC, Q3 2026 condensed financial statements, unaudited][S3], published 2026-10-15.
4. [S4 — TSMC/LSEG, Q3 2026 earnings-call transcript][S4], call 2026-10-15.
5. [S5 — TSMC, Q4 2025 management report][S5], published 2026-01-15.
6. [S6 — TSMC/LSEG, Q4 2025 earnings-call transcript][S6], call 2026-01-15.
7. [S7 — TSMC, 2024 monthly revenue][S7], rolling monthly releases; completed January 2025.
8. [S8 — TSMC, 2025 monthly revenue][S8], rolling monthly releases; completed January 2026.
9. [S9 — TSMC, 2026 monthly revenue][S9], rolling monthly releases through 2026-10-08.
10. [S10 — TSMC, 2025 annual report, cash flow and investment sections][S10], published 2026; precise day not verified.
11. [S11 — TSMC/LSEG, Q2 2026 earnings-call transcript][S11], call 2026-07-16.
12. [S12 — TSMC, Q3 2026 earnings presentation][S12], published 2026-10-15.
13. [S13 — TSMC, 2025 consolidated financial report, major-customer note, SEC-hosted][S13], published 2026; precise filing day not verified.
14. [S14 — Nvidia, first US-produced Blackwell wafer][S14], published 2025-10-17.
15. [S15 — Apple, US manufacturing commitment and Arizona supply relationships][S15], published 2025-08-06.
16. [S16 — AMD, first TSMC N2 product-silicon milestone][S16], published 2025-04-14.
17. [S17 — Broadcom, FY2025 Form 10-K][S17], fiscal year ended 2025-11-02; filed December 2025.
18. [S18 — TSMC/LSEG, Q2 2024 earnings-call transcript][S18], call 2024-07-18.
19. [S19 — GlobalFoundries, US silicon-interposer manufacturing agreement][S19], published 2026-10-08.
20. [S20 — TSMC, Q2 2001 financial report][S20], published 2001-07-26.
21. [S21 — TSMC, Q3 2001 financial report][S21], published 2001-10-26.
22. [S22 — TSMC, Q4 2001 results][S22], published 2002-01-25.
23. [S23 — TSMC, Q4 2008 results][S23], published 2009-01-22.
24. [S24 — Intel, Q2 2026 Form 10-Q][S24], filed 2026-07-24; quarter ended 2026-06-27.
25. [S25 — Samsung Electronics, Q2 2026 results][S25], published 2026-07-30.
26. [S26 — TSMC, Q1 2009 results][S26], published 2009-04-30.
27. [S27 — TSMC, Q1 2009 earnings-call transcript][S27], call 2009-04-30.
28. [S28 — TSMC, 2023 annual report][S28], published 2024; precise day not verified.
29. [S29 — TSMC, Q1 2023 results][S29], published 2023-04-20.
30. [S30 — TSMC, Q2 2023 results][S30], published 2023-07-20.
31. [S31 — TSMC, Q3 2023 results][S31], published 2023-10-19.
32. [S32 — TSMC, Q4 2023 results][S32], published 2024-01-18.
33. [S33 — US Department of Commerce, final TSMC Arizona CHIPS award][S33], published 2024-11-15.
34. [S34 — TSMC, 2025 Form 20-F, risk factors][S34], filed 2026-04-16.
35. [S35 — Intel, notice of Q3 2026 reporting date][S35], published 2026-10-06.
36. [S36 — Samsung Electronics, Q3 2026 preliminary guidance][S36], published 2026-10-08.

[S1]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/526b65af7305df2dde6b9ece6812b1fdf1e49f9b/3Q26%20EarningsRelease.pdf
[S2]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf
[S3]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2026-10/3a94d1034b9e6b22446b674f7aaf3d088a12a193/FS.pdf
[S4]: https://investor.tsmc.com/japanese/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf
[S5]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/a920e9c2e3879f198dc700d041344229e7ffb438/4Q25%20Management%20Report.pdf
[S6]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[S7]: https://investor.tsmc.com/chinese/monthly-revenue/2024
[S8]: https://investor.tsmc.com/english/monthly-revenue/2025
[S9]: https://investor.tsmc.com/english/monthly-revenue/2026
[S10]: https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20Annual%20Report.E.pdf
[S11]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[S12]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/9f58506f6f114f91cefbf86820cc63297b39b130/3Q26%20Presentation%20%28E%29.pdf
[S13]: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[S14]: https://blogs.nvidia.com/blog/tsmc-blackwell-manufacturing/
[S15]: https://www.apple.com/newsroom/2025/08/apple-increases-us-commitment-to-600-billion-usd-announces-ambitious-program/
[S16]: https://ir.amd.com/news-events/press-releases/detail/1245/amd-achieves-first-tsmc-n2-product-silicon-milestone
[S17]: https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm
[S18]: https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[S19]: https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/
[S20]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/english/2001/Q2/2q01fr.pdf
[S21]: https://investor.tsmc.com/english/encrypt/files/encrypt_file/english/2001/Q3/3q01fr.pdf
[S22]: https://pr.tsmc.com/english/news/2404
[S23]: https://pr.tsmc.com/english/news/1532
[S24]: https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm
[S25]: https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results
[S26]: https://pr.tsmc.com/english/news/1548
[S27]: https://investor.tsmc.com/schinese/encrypt/files/encrypt_file/english/2009/Q1/09Q1%20Conf%20Call-Transcript.pdf
[S28]: https://investor.tsmc.com/static/annualReports/2023/english/index.html
[S29]: https://pr.tsmc.com/schinese/news/3013
[S30]: https://investor.tsmc.com/schinese/quarterly-results/2023/q2
[S31]: https://pr.tsmc.com/english/news/3076
[S32]: https://pr.tsmc.com/english/news/3101
[S33]: https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[S34]: https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
[S35]: https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-reports-third-quarter-2026-financial-results.html
[S36]: https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026
