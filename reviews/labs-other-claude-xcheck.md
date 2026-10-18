# Claude cross-check: frontier labs beyond OpenAI and Anthropic

*Review date and information cutoff: 2026-10-18. Reviewer: Claude (Opus). This is the first Claude review of a Codex-written note that was already corrected once after a Codex cross-check. I read report/methodology.md, tasks/RESEARCH_BRIEF.md, the note, its Codex review, the F5 and layer rows of forecasts/register.md, and the relevant rows of report/index.md and report/stack.md. Retrievals: 14 distinct URLs, which is within the 15-fetch cap. Four were SEC documents fetched with a generic User-Agent: the SpaceX 10-Q, the Q2 release, the EDGAR submissions index and the 2026-08-14 8-K. Ten were web pages, and Moonshot's page needed one extra request to follow a 301 redirect. I also ran 9 web searches, used only as leads. All sources were accessed 2026-10-18. No other file was edited.*

*Conflict check: the lead agent and I are both Anthropic models. This note covers other labs, and it does not rely on any Anthropic figure. Anthropic appears only in the title, as an exclusion. The 10-Q does not name SpaceX's cloud-services customers, so the note cannot be leaning on Anthropic through that channel either.*

## Verdict

The figures are accurate. All 12 re-verified rows match their primary sources, and every derived figure in the Analysis recomputes, including $30.98B, 58.75%, $9.08B, $13.329B and $0.784B.
Both Codex passes missed three things in primary filings: the **Cursor merger closed on 2026-08-14** (8-K); **Valor is a related party** (its founder sits on SpaceX's board); and xAI's own ~$5B of secured debt was **repaid in H1 2026** through SpaceX unsecured borrowing. The note still treats the first as open and leaves out the other two.
The Chinese-pricing section quotes cheap tiers and a stale 2025 Moonshot price. Current flagship rate cards show tiering and some price *increases*: Kimi K3 is $3/$15, and GLM-5.3 is up 40% on GLM-5. The neolab forecast row lists Cursor, which was acquired before the forecast origin.

## Claim re-verification

| Claim # | Note's value | My value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 2 | SpaceX AI Q2: revenue $2.561B, operating loss $1.257B, capex $15.828B, adj. EBITDA +$1.146B | Same four figures. Also: Q1 AI capex $7.723B, so **H1 AI capex is $23.551B against H1 AI revenue of $3.379B** | [Q2 release (8-K Ex.)](https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm), segment tables | Yes | A |
| 3 | Advertising $367M; solutions/infrastructure $2.194B; $1.6B incremental from cloud agreements; $14.1B contracted; 1.4 GW | Same. Revenue is "up 213% sequentially ... primarily driven by ... new Cloud Service Agreements". The 10-Q also gives company-wide backlog of $47.461B, of which $14.286B is deferred revenue | Release; [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm) Note 3 | Yes | A |
| 7 | Valor debt $2.039B current + $11.290B noncurrent = $13.329B, from three failed sale-leasebacks | Same. **Not in the note:** the balance sheet labels both lines "related party" (they were $455M + $4,052M = $4.507B at 2025-12-31). Valor's "founder, CEO and Chief Investment Officer ... Antonio Gracias, serves as one of the directors of the Company". Interest expense was $327M in Q2 and $513M in H1. The April 2026 transaction was entered by CTC Property, LLC, a SpaceX subsidiary | 10-Q balance sheet, Note 9, Note 17 | Yes; the note omits the related-party nature | A |
| 10 | Mistral Series D €3B at >€21B post-money, led by Samsung | "€3 billion", "post-money valuation of more than €21 billion", Samsung led, with EQT's Scaleup Europe Fund and PSG as co-leads. The page itself carries no date | [Mistral](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) | Yes | A |
| 12 | Prometheus $12B Series B, ~$41B valuation (A); $6.2B earlier round (C) | SparkLabs: "$12 billion Series B in June 2026", "a valuation of approximately $41 billion". It carries the disclaimer "Descriptions are each company's own ... Financing lines are as published." I did not re-check the $6.2B | [SparkLabs](https://www.sparklabsgroup.com/portfolio/prometheus) | Yes. A investor-published statement is fair, but it relays the company's own description | A statement / C total |
| 24 | DeepSeek Flash $0.15/$0.60 off-peak, $0.30/$1.20 peak | Same (model version DeepSeek-V4.1-Flash-1017). **Not in the note:** deepseek-v4-pro costs $0.66/$1.98 off-peak and $1.32/$3.96 peak. Peak hours are 01:00-04:00 and 06:00-10:00 UTC on weekdays | [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing/) | Yes, but only the cheapest tier is quoted | A |
| 25 | Moonshot K2 turbo $2.40→$1.15 input, $10→$8 output (2025-11) | That is history. **Current rate card: kimi-k3 $3.00 uncached input / $0.30 cached / $15.00 output**, 1M context; kimi-k2.6 $0.95/$4.00. K3 is 2.6× the input and 1.9× the output price of the K2 turbo the note cites | [Kimi platform pricing](https://platform.kimi.ai/docs/pricing/chat) | Stale; the current flagship price points the other way | A (current) |
| 26 | qwen3.6-plus "global" $0.276/$1.651 (≤256K) | Matches the "Global (Hong Kong)" listing. The International (Singapore) price is $0.50/$3.00. The page lists qwen3.6-plus under proprietary "Text generation - Qwen", **not under open source**. The flagship qwen3.8-max is $1.65/$4.951 (Global) and $2/$6 (International) | [Alibaba Model Studio](https://www.alibabacloud.com/help/en/model-studio/model-pricing) | Yes, but this is a proprietary model, and the price shown is the cheaper of two regional lists | A |
| 27 | GLM-5.3 $1.40/$4.40; GLM-5.3-Flash $0.15/$0.50 | Same. GLM-5 is $1.00/$3.20, so **the GLM-5.1 to 5.3 generation is +40% on input and +37.5% on output**. Cached-input storage is "Limited-time Free" | [Z.AI pricing](https://docs.z.ai/guides/overview/pricing) | Yes | A; % B |
| 31 | Cursor: SpaceX $60B acquisition agreement, "closing not established here" | **Closed.** 8-K Item 2.01: "on August 14, 2026 ... the Merger became effective". Consideration was 389,289,254 Class A shares at an implied $60.0B equity value (≈$154.13 per share), and Cursor is now a wholly owned subsidiary. The 10-Q adds a concurrent Cursor Compute Agreement (SpaceX supplies GPU capacity; the Q2 net amount was "not material") | [SpaceX 8-K, 2026-08-14](https://www.sec.gov/Archives/edgar/data/1181412/000162828026056945/spcx-20260814.htm); 10-Q Note 20 | **No: outdated by two months** | A |
| 41 | Mistral $830M limited-recourse financing; 13,800 GB300; seven banks | Same: Bpifrance, BNP Paribas, Crédit Agricole CIB, HSBC, La Banque Postale, MUFG, Natixis; site at Bruyères-le-Châtel; "Set to become operational in Q2 2026". The borrower, tenor and any guarantees are not stated | [Linklaters](https://www.linklaters.com/en/about-us/news-and-deals/deals/2026/march/linklaters-advises-seven-leading-global-banks) | Yes | A |
| 46 | Meta Q2: OCF $31.862B − capex $30.116B − lease principal $0.962B = FCF $0.784B | Same; "free cash flow was $784 million". 2026 capex guidance $130-145B including lease principal. The release does not mention MSL | [Meta Q2](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/) | Yes | A |

Also checked:
- **Row 6:** the 10-Q shows the June 2025 xAI debt is gone. At 2025-12-31 the xAI fixed-rate term loan was $995M, the floating-rate loan $995M and the 12.5% secured notes $3,000M, about $4.99B together; the X B-1/B-3 loans were $12.47B. All were repaid from a $20B SpaceX unsecured bridge loan, which was itself repaid from the $25B SpaceX notes. The loss on extinguishment was $1.526B.
- **Rows 9/47:** the $100B of cash and securities, $85.7B net IPO proceeds and $25B of bonds all match the release.
- **Row 29:** the MiniMax M3 standard tier at ≤512K is $0.30/$1.20. The badge says "Permanent 50% off", so it is not a promotion.
- **Row 34:** the Glean page title confirms "$300M ARR", but no date shows in the body text.

## Arithmetic checks

| Derived figure | Recalculation | Result |
|---|---|---|
| Core seven $9.08B | 2 + 2 + 2 + 1.1 + 1.03 + 0.65 + 0.30 | Pass |
| $28.28B / $30.98B | 9.08 + (6.2 + 12) + 1; + 0.6 + 2.1 | Pass |
| Prometheus 58.75%; ex-Prometheus $12.78B | 18.2 / 30.98 = 0.5875; 30.98 − 18.2 | Pass |
| Valor $13.329B | 2.039 + 11.290 | Pass. Related-party balance grew by **$8.822B** in H1 (from $4.507B) |
| Meta FCF $0.784B | 31.862 − 30.116 − 0.962 | Pass |
| AI adj. EBITDA $1.146B | −1.257 + 1.885 + 0.516 + 0.002 | Pass |
| Mistral >23.3× | >21 / 0.9 (both in €) | Pass; the denominator is a target and C |
| Glean 24×, Harvey <38.75×, Sierra 79×, TML 400× | 7.2/0.3; 15.5/0.4; 15.8/0.2; 40/0.1 | Pass; the date mismatches are already flagged |
| AMI ~$4.53B post | 3.5 + 1.03 | Pass |
| DeepSeek $5.576M | 2.788M h × $2 | Pass |
| Not in note: AI capex / revenue | Q2 15.828 / 2.561 = 6.2×; H1 23.551 / 3.379 = 7.0× | B |
| Not in note: implied Valor cost | Q2 interest 0.327 × 4 / 13.329 ≈ 9.8%. Approximate: the balance rose during Q2, so the true rate is higher | B/C |
| Not in note: SpaceX June raising vs cash | 85.7 + 25 = $110.7B raised in June, against $100B of cash and securities at June 30. $17.46B of X/xAI secured debt was refinanced | B |
| Not in note: Cursor exit multiple | 60 / 29.3 = 2.05× the Nov 2025 mark in nine months | B |

## Omissions

From primary filings the note cites but did not fully read (the 10-Q) or did not open (the 8-K):

1. **Cursor closed on 2026-08-14** (8-K). This removes the largest application company from the independent cohort. Its $60B all-stock exit, about 2× its November 2025 mark, is the strongest single piece of evidence against near-term down-round risk for top applications, and it makes Cursor an internal customer of xAI compute. From Q3 2026, Cursor's revenue (>$2B run-rate in February, C) is consolidated into SpaceX's AI segment. Q3 segment growth will therefore be partly inorganic.
2. **Valor is a related party.** Antonio Gracias, Valor's founder, CEO and CIO, is a SpaceX director. The $13.329B is related-party debt costing roughly 10%, and it grew $8.8B in six months. In a report whose method gives circular and insider financing a whole note, this matters more than the guarantee-boundary caveat the Codex pass added.
3. **xAI's secured debt was refinanced at the parent.** The ~$5B June 2025 xAI package (row 6) and $12.5B of X loans were repaid in H1 2026 through SpaceX unsecured debt (bridge, then IG notes). Two consequences follow. First, the note's open question of "a reconciled cumulative xAI debt-raised total" now has an answer for the balance sheet. Second, the creditor-recovery question for xAI is now mainly about the related-party Valor leases. External bondholders hold SpaceX unsecured paper, backed by $100B of cash against $38.4B of total debt principal.
4. **SpaceX non-cancellable commitments of $27.955B**, of which **$22.244B falls due in 2027**. These relate "primarily to ... AI infrastructure and third-party cloud capacity arrangements" (10-Q Note 16; company-wide figure). This is the most direct evidence in the note's perimeter on what a funding squeeze could and could not cut quickly.
5. **Current Chinese flagship prices** (rows 25 to 27 above). Kimi K3 at $3/$15 is a primary-source rate card and contradicts reading Moonshot as a price-cutter. GLM moved up a generation in price, and DeepSeek's Pro tier sits at 4.4× input and 3.3× output over Flash. Qwen's quoted prices are for proprietary hosted models.
6. **Lead only, not citable:** a secondary aggregator reports that AI21 Labs, a 2023 unicorn LLM lab, failed to close another major round and cut 60% of its staff on 2026-05-18 ([aiweekly](https://aiweekly.co/alerts/ai21-labs-slashes-60-of-staff-bets-all-on-maestro)). If primary reporting confirms it, it would be a second stress case besides Poolside. Grade D until traced.
7. **TML talks escalated:** reported talks now run from $40B up to a ~$50B valuation, with NVIDIA reportedly in for ~$2.5B (Bloomberg via Yahoo, The Information via TNW; C). No close was found. Co-founder Andrew Tulloch's departure to Meta was also reported. Neither changes the totals, and both belong in the TML row.

Checked and not found by the cutoff: a closed TML or Perplexity round, a new Glean round (a $12B "Series G" listing on one aggregator is unconfirmed and conflicts with other sources), and the release of Mistral Large 4 weights (reported due around 27 October).

## Summary-bullet assessment

1. **Meta FCF $0.784B (Q2 2026):** supported (A) and concrete. However, the bullet's subject is independent labs, and it gives no figure for them. It also leaves out the cohort's clearest observed outcome, Cursor's $60B exit.
2. **SpaceX AI Q2 figures:** supported (A) and concrete. Adding H1 capex of $23.55B against $3.38B of revenue would make the scale clearer.
3. **Valor $13.329B at 2026-06-30:** the figure is supported (A). The framing misses the material facts: the debt is related-party, and xAI's other debt was refinanced at the parent.
4. **$30.98B, 58.75% Prometheus:** supported, and the arithmetic is correct. It is concrete and correctly caveated.
5. **Mistral >€21B, >23.3× target ARR, $830M limited recourse:** supported. The €900M target is C, and the bullet should say "reported" before "€900m target" (it does). Concrete.
6. **Glean $300M ARR:** supported (A, although the date is not in the page body). Concrete. Cursor's internal models and its absorption into SpaceX make the double-counting point stronger.
7. **$9.08B subtotal; a freeze "could reduce training and new orders":** the conditional wording is defensible but underuses the note's own evidence (see below).

**Is "a funding winter would hit training and future orders first" supported?** Half of it is. *Future orders first* has two pieces of support in the note's own perimeter. Poolside's failed raise took its CoreWeave deal down with it (row 37, C): a not-yet-signed order died with the financing. And xAI's commitments are rigid in the short term: $22.2B of non-cancellable 2027 obligations, related-party lease debt, and fixed-fee cloud contracts it sells on to others. So the cuts that can happen fast are in uncommitted capacity. *Training first* (as opposed to inference) has no evidence: no lab in the register discloses its training/inference split, and several rent compute under multi-year contracts (Recursive with AWS for $410M; TML's 1 GW NVIDIA plan). The note's softened "no first-cut sequence is established" goes too far the other way. A supportable version is: "new, uncommitted capacity orders are cut first (Poolside, C); committed capacity transmits only through counterparty default; the training-versus-inference order is unknown."

## Your assessment

Outside OpenAI and Anthropic, nothing in this perimeter is comfortably profitable on the evidence. xAI loses $1.26B a quarter at the operating line and spends 6 to 7 times its revenue on capex. Mistral, Z.AI (26% gross margin) and MiniMax (18% gross margin, a $358M H1 loss) are all loss-making or thin-margin. The independent research labs mostly do not disclose revenue. But I would not call the layer overextended in the sense that matters for a bubble call: the financing has shifted toward strong balance sheets. xAI now sits inside a public SpaceX holding $100B of cash, having raised $110.7B in June. Its external secured debt was refinanced into IG unsecured paper, and the remaining $13.3B of leases is owed to a board-connected related party. Mistral's $830M GPU debt is limited-recourse, so its seven banks carry the risk of one asset rather than the whole company. Cursor and World Labs exited to strategic buyers at higher marks. **Who loses first:** venture and strategic equity in the pre-revenue research labs (SSI at $32B, TML at $12B moving to $40-50B, Reflection at $25B pre-money, Prometheus at ~$41B). Next come the counterparties that sell them compute under commitments: AWS, Google Cloud, NVIDIA as investor and licensor, and Valor. Public SpaceX shareholders absorb xAI's losses, and SpaceX bondholders are well covered. **Where I differ from the note.** It frames xAI's risk mainly as creditor recovery, but the filings show the real issue is related-party financing and shareholder dilution. The Cursor exit and up-rounds across the named cohort argue for *lower* near-term distress probabilities than the register carries. On Chinese pricing, the note's "open weights threaten rents" theme overstates commoditization: the cheap tiers are priced low, while the flagships now hold or raise prices.

## Front-page figures

| Page | Figure | From this note? | Still holds? |
|---|---|---|---|
| report/stack.md, frontier labs row | "$13.3B of Valor GPU financing inside SpaceX for xAI" | Yes (row 7) | **Holds** at 2026-06-30, but it should say "related-party", since Valor's founder is a SpaceX director |
| report/stack.md, neolabs row | "$31B of reproducible rounds by labs with little disclosed revenue" | Yes (row 22) | **The figure holds ($30.98B); the label does not.** The note says explicitly that it is not a low- or zero-revenue census: 58.75% is Prometheus, and Isomorphic is Alphabet-controlled with £55.2M of collaboration income |
| report/stack.md, neolabs row | "app margins thin and variable" | Yes (row 38) | **Weak.** The note establishes no comparable margins; there is only one Sacra estimate (Cursor, RU) |
| report/stack.md, neolabs row | "one reported failed raise (Poolside)" | Yes (row 37) | **Incomplete.** Poolside later reportedly raised $1B at $12B pre-money alongside a $6B NVIDIA licence (C) |
| report/stack.md, neolabs row | Loss order "Venture investors; then GPU demand for training" | Yes (row 39) | **Overstated.** Note-supported: new uncommitted orders first. Training versus inference is unknown |
| report/stack.md, neolabs row | Layer includes applications (Cursor) | Indirect | **Cursor has been a SpaceX subsidiary since 2026-08-14** |
| forecasts/register.md | Neolab row: SSI, TML, Reflection, Periodic, Mistral, Perplexity, **Cursor**, Harvey, Glean, Sierra at 25/45/65% | Yes | **The definition breaks:** Cursor was acquired before the 2026-10-17 origin, and "distressed sale" is undefined (the Reflection/NVIDIA hire-and-license talks would be ambiguous). On the level: every constituent with a known recent mark priced up or is in up-round talks (Mistral €11.7B→>€21B, Reflection $8B→$25B pre, Harvey $15.5B, Sierra >$15B, TML and Periodic talks). Only Glean (June 2025) and SSI (April 2025) have stale marks. Nothing in this note supports 25% at 6 months. My estimate: 15/35/55 |
| forecasts/register.md (cited on index.md) | F5 (OpenAI, Anthropic, xAI/SpaceX, Mistral, SSI, TML down round) at 10/20/35% | Partly | **The xAI branch is moot.** SpaceX listed on 2026-06-12, xAI is wholly owned and cannot close a priced primary round, and the "IPO below last mark" clause fired before origin, if at all. Mistral and TML are in up-rounds. So F5 is now essentially an OpenAI/Anthropic/SSI question, and this note gives no reason to raise it. 10/20/35 is defensible only on the strength of the OpenAI/Anthropic notes |
| report/index.md | Only "down round (F5)" | No figure | n/a |

## Recommended edits

1. **Row 31 (Cursor), replace the Value cell:** "Company revenue crossed $1bn annualized; $29.3bn valuation, $2.3bn round (2025-11-13); >$2bn February run-rate RU. **SpaceX completed the acquisition on 2026-08-14**: 389,289,254 Class A shares at an implied $60.0bn equity value; Cursor is a wholly owned subsidiary. A concurrent Cursor Compute Agreement has SpaceX supplying GPU capacity (Q2 net amount not material)." Source: [8-K 2026-08-14](https://www.sec.gov/Archives/edgar/data/1181412/000162828026056945/spcx-20260814.htm); 10-Q Note 20. Grade A. Delete "closing not established here" in the Analysis and in Signals.

2. **Row 6, append:** "Repaid in H1 2026: xAI fixed- and floating-rate term loans ($995m each) and 12.5% secured notes ($3,000m), plus X B-1/B-3 loans ($12,470m), from a $20bn SpaceX unsecured bridge loan later repaid with the $25bn SpaceX notes; loss on extinguishment $1,526m. 2026-06-30 debt principal: SpaceX notes $25,000m, X notes $27m, other financings $13,406m." Source: 10-Q Note 9. Grade A.

3. **Replace Summary bullet 3:** "At 2026-06-30 SpaceX recognized **$13.329bn of related-party Valor equipment-financing debt** (Valor's founder is a SpaceX director), up from $4.507bn at end-2025, with $327m of Q2 interest; xAI's own ~$5bn secured debt was repaid in H1 2026 through SpaceX unsecured borrowing (rows 6–7, 52)." Add the related-party facts to rows 7 and 52 with a 10-Q Note 17 citation, grade A.

4. **Add a claim row:** "SpaceX non-cancellable commitments $27.955bn at 2026-06-30, $22.244bn due in 2027, 'primarily related to ... AI infrastructure and third-party cloud capacity arrangements' (company-wide); backlog $47.461bn, of which $14.286bn deferred revenue." 10-Q Notes 3 and 16. Grade A.

5. **Row 25, replace the Value cell:** "Current rate card: kimi-k3 $3.00 uncached input / $0.30 cached / $15.00 output per million tokens, 1M context; kimi-k2.6 $0.95/$4.00. Historical: K2 turbo cut to $1.15/$8 on 2025-11-06. K3 claims ~2.5× scaling efficiency versus K2; full training dollars ND." Source: [Kimi pricing](https://platform.kimi.ai/docs/pricing/chat), as of 2026-10-18. Grade A.

6. **Rows 24, 26 and 27, append:** to row 24, "deepseek-v4-pro $0.66/$1.98 off-peak, $1.32/$3.96 peak; peak 01:00–04:00 and 06:00–10:00 UTC weekdays." To row 26, "qwen3.6-plus is listed as a proprietary model; International (Singapore) $0.50/$3.00; flagship qwen3.8-max $1.65/$4.951 Global, $2/$6 International." To row 27, "GLM-5 $1.00/$3.20, so the GLM-5.1–5.3 list price is +40%/+37.5%."

7. **Replace the first three sentences of the "Open weights threaten rents" paragraph:** "Chinese rate cards show tiering rather than uniform collapse. Flash tiers price at $0.15–0.30 input and $0.50–1.20 output per million tokens, while flagships list at $1.32/$3.96 (DeepSeek V4-Pro peak), $1.40/$4.40 (GLM-5.3, up about 40% on GLM-5) and $3/$15 (Kimi K3). Qwen's quoted Plus and Max prices are proprietary hosted models, so they bound open-weight competition only indirectly. DeepSeek's $5.576m official-run figure excludes prior research and is not an all-in training cost."

8. **Replace Summary bullet 7:** "The $9.08bn seven-lab subtotal (2025–26 rounds to 2026-10-17) measures equity exposure, not overvaluation. Evidence in the note supports **new, uncommitted capacity orders being cut first**: Poolside's failed raise took a CoreWeave deal with it (C). Committed capacity (for example, SpaceX's $22.2bn of 2027 non-cancellable commitments) transmits mainly through counterparty default. No lab discloses a training/inference split, so 'training first' is not established (C, author inference; rows 37, 39, new commitments row)."

9. **Add to Analysis ("Capital register"), new paragraph:** "Observed exits so far are at higher marks, not distress. Cursor sold to SpaceX for $60.0bn in stock on 2026-08-14, about 2.0× its November 2025 valuation, and World Labs agreed to an approximately $8.2bn AMD stock deal. Mistral (€11.7bn→>€21bn), Reflection ($8bn→$25bn pre-money) and Harvey ($15.5bn) all priced up. Glean (June 2025) and SSI (April 2025) have the stalest marks. Poolside's April stress (C) and the reported AI21 Labs restructuring (D, unverified) are the only distress cases found."

10. **Signals: add two rows.** (a) "SpaceX Q3 2026 AI segment: first quarter with Cursor consolidated from 2026-08-14; separate organic growth from acquired revenue." (b) "Valor related-party debt balance and interest: $13.329bn, $327m Q2 interest (2026-06-30)."

11. **TML row 14, append:** "Later reports of talks up to ~$50bn with NVIDIA ~$2.5bn (C; no close found by 2026-10-18); co-founder Andrew Tulloch reported departed to Meta (C)."

12. **Outside the note, for the lead to consider** (no files edited by me):
    - In report/stack.md, neolabs row, replace "$31B of reproducible rounds by labs with little disclosed revenue; app margins thin and variable; one reported failed raise (Poolside)" with "$31B of selected 2025–26 rounds (59% Prometheus), revenue mostly undisclosed; exits so far at higher marks (Cursor to SpaceX at $60B, 2× its Nov 2025 mark); one reported failed raise (Poolside, later refinanced, C)".
    - In the same row, replace "Venture investors; then GPU demand for training" with "Venture investors; then new compute orders and lessors".
    - In the frontier-labs row, write "$13.3B of related-party Valor GPU financing".
    - In the forecast register, replace Cursor in the neolab row (for example with Poolside or Cognition), define "distressed sale" (for example, consideration below the last priced primary round), and note that F5's xAI branch cannot trigger now that SpaceX is public. Consider 15/35/55 for the neolab row.
