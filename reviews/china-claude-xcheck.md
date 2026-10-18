# China: independent Claude cross-check

*Review date: 2026-10-18. Reviewer: Claude (Anthropic), first Claude reviewer of `research/macro/china.md` (Codex-written, corrected once after `reviews/china-codex-xcheck.md`) and `data/china-hyperscaler-capex.csv`. 14 fetches used (one, the TSMC 20-F, was blocked by Cloudflare). Only this file was written. No git commands were run.*

## Verdict

The figures hold. All 14 re-verified rows match their primary sources and the Analysis has no arithmetic errors. The weak points are framing and omissions, not numbers.
Both Codex passes left out public evidence that answers the note's own open questions: OpenRouter's token and spend shares by lab origin, MiniMax's HKEX interim results, Alibaba's disclosed AI-related revenue (RMB12.4bn), Tencent's RMB88.7bn one-quarter fall in net cash and its new-AI-products loss, and CXMT's 10% DRAM share. Codex also gave Tencent's "+RMB37.6bn FCF excluding prepayments" more comfort than it deserves.
The conclusion that China is a margin competitor but not yet a demand substitute is supported, and the omitted evidence supports it more strongly than the note does. Nothing here changes report/index.md. The stack.md China and Taiwan figures still hold.

## Claim re-verification

All sources were fetched on 2026-10-18. Grade A means a primary disclosure was verified. It does not mean delivery or an audit.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | At least RMB380bn over three years, announced 2025-02-24; later increase unquantified | "at least RMB 380 billion ($53 billion) … over the next three years … exceeds Alibaba's total AI and cloud spending over the past decade". A search found no replacement total for the September 2025 increase | [Alibaba, 2025-02-24][baba380]; [Bloomberg, 2025-09-24][bbg-apsara] | Yes | A |
| 3 | June-quarter capex RMB67.678bn vs RMB38.676bn | RMB67,678m (US$9,975m), **+75%** y/y. Alibaba attributes the rise to "fluctuations in procurement cycles, increase in CPU-compute capacity driven by anticipated growing customer adoption of AI agents, and higher pricing of a broad range of chip components" | [Alibaba June-quarter release, SEC Ex. 99.1][baba-q] | Yes on figures. The note leaves out the company's own three-part explanation, which weakens Summary bullet 1's "demonstrating accelerating infrastructure demand" | A |
| 4 | OCF RMB22.945bn; FCF −RMB44.670bn; AI Cloud and Compute revenue RMB48.437bn, +45% | Same. The same release also gives **AI-related product revenue of RMB12.376bn**, the 12th consecutive quarter of triple-digit growth | [baba-q] | Yes. The AI-related revenue figure is omitted | A |
| 42 / 43 | AI Cloud adjusted EBITA +RMB5.628bn; AI Labs and Applications −RMB13.861bn | +5,628 (vs +2,419) and −13,861 (vs −3,224). Group adjusted EBITA −30%, net income −75% y/y | [baba-q], segment EBITA table | Yes | A |
| 6 | Tencent capex: June quarter RMB52.784bn vs 19.107bn; March quarter 31.936bn; first half 84.720bn | 52,784 / 19,107 / 31,936 in the results table; "up 176% YoY" | [Tencent Q2 release, pp.1, 6][tencent-q] | Yes | A |
| 7 | Cash capex RMB59.3bn; OCF 52.7bn; FCF −13.8bn; IFRS operating profit 67.3bn; net cash 58.2bn | Same. **Net cash was RMB146,860m at 31 March 2026 and RMB58,191m at 30 June.** Non-current prepayments, deposits and other assets rose from RMB24.5bn to RMB91.2bn (Dec 2025 → Jun 2026) | [tencent-q], pp.1–2, 6–7 | Yes. The quarterly net-cash fall is omitted | A |
| 44 | FCF ex-compute prepayments +RMB37.6bn | Same, quoted as management's counterfactual. The release also gives non-IFRS operating profit of RMB75.6bn against **RMB86.1bn "excluding New AI Products"** (Hy, Yuanbao, CodeBuddy, WorkBuddy, Xiaowei) | [tencent-q], p.1–2 | Yes. The AI-products drag is omitted | A |
| 11 | 2.788m H800 hours × US$2 = US$5.576m; excludes prior research | Table 1: 2,664K + 119K + 5K = 2,788K hours, US$5.576m, "excluding the costs associated with prior research and ablation experiments"; 2,048-GPU H800 cluster | [DeepSeek-V3 report v2][v3] | Yes | A |
| 50 | TileKernels Ascend backend, 2026-09-30 | Same date. The same Python APIs run on Nvidia GPUs and Huawei NPUs. **Requires "Ascend 950 NPU" and CANN 9.2.0+.** Training on Ascend is not claimed. No comparison with Nvidia | [TileKernels][tilekernels] | Yes | A |
| 51 | FlashMLA Ascend sparse-attention prefill and decode kernels | Dated 2026-09-30. DeepSeek "open-sourced its inference infrastructure and core components for the Huawei Ascend platform". On Ascend 950 it claims **410 TFLOPS prefill (~95% of peak) and 360 TFLOPS decode (~83%)** on V4.1 workloads. No production-deployment or Nvidia comparison | [FlashMLA note][flashmla] | Yes. The performance claims are omitted | A as vendor claim |
| 20 | CXMT G5 DRAM mass production; no qualified HBM | Not re-fetched. Counterpoint's DRAM table puts **CXMT at 10% of DRAM revenue in Q2 2026 (4% Q2 2025, 5/8/8% in the quarters between)**. CXMT does not appear in the HBM share table | [Counterpoint, Sep 2026][cp] | Row consistent but incomplete. The share figure, already carried in `research/stack/memory-hbm.md` row 56, is absent here | C (analyst estimate) |
| 22 | Qwen3.8-Max US$2/6; Qwen3.7-Plus US$0.40/1.60 ≤256K, Singapore, before promotions | Same. Plus carries a "Limited-time 20% off". The 256K–1M tier is US$1.2/4.8. Beijing-region prices are lower: Plus US$0.276/1.101, Max US$1.65/4.951. Page updated 2026-10-15 | [Alibaba Cloud pricing][qwen] | Yes | A |
| 31 | MOFCOM/MOST No.48: 40 technologies, 23 AI; comments 16 Oct–15 Nov; registration effective on announcement | 40 = 23 AI ("large models, agents, compute clusters, information processing") + 5 biomedicine + 12 photovoltaics. Registration runs from the announcement until the revised catalogue takes effect. The page gives no prohibited/restricted split and no compute or parameter thresholds (they sit in Attachment 1) | [MOFCOM No.48][mofcom48] | Yes. Agrees with the signals log, which also says the 14/26 split and thresholds were not established | A |
| 34 | Majority of TSMC principal production facilities and net revenue from operations in Taiwan | **Not re-fetched**: the 20-F URL returned a Cloudflare challenge. The same statement was verified against the same 20-F (S34) in `reviews/tsmc-and-foundry-claude-xcheck.md` | [TSMC 2025 20-F][tsmc] | Accepted on the sibling verification | A (second-hand) |
| 49 | DeepSeek round >RMB80bn, expected to close in October; reported, unverified | Same (US$11.93bn in the body). It also says **Tencent and CATL committed among the largest amounts**, the July kickoff targeted a **RMB500bn (~US$74bn) valuation**, there was an earlier maiden round of ~US$7.4bn, and the money is a "war chest … ahead of a domestic IPO". A search found no closing announcement | [Reuters via Investing.com, 2026-10-06][ds-round] | Numbers match. The investors, valuation and earlier round are omitted | C |

Not re-fetched, with no reason to doubt them: rows 8–9 (Baidu), 12 (R1 US$294k), 13, 26–28, 36–39. The equipment shares in rows 36–39 match `research/stack/semiconductor-equipment.md` rows 5, 14, 26–28.

## Arithmetic checks

Monetary figures are RMB billions unless stated. Where a figure is my own derivation it is grade B.

| Relationship | Recalculation | Finding |
|---|---|---|
| Alibaba capex growth | 67.678 / 38.676 − 1 = 74.99% | Correct (75%) |
| Alibaba cloud growth | 48.437 / 33.418 − 1 = 44.94% | Correct (45%) |
| Alibaba OCF − capex vs FCF | 22.945 − 67.678 = −44.733; 22.945 − 67.660 + 0.045 = −44.670 | Correct (claim 46) |
| Tencent capex growth, half-year | 52.784 / 19.107 − 1 = 176.3%; 31.936 + 52.784 = 84.720 | Correct |
| Tencent FCF bridge | 52.7 − 59.3 − 5.0 − 2.2 = −13.8; prepayment effect 37.6 + 13.8 = 51.4 | Correct (claim 45) |
| Baidu FCF | 3.436 − 11.390 = −7.954 | Correct (inputs from the note) |
| DeepSeek V3 / R1 | 2,788K × $2 = $5.576m; 147K × $2 = $294K | Correct |
| DeepSeek round in USD | 80 / 6.7848 = US$11.8bn at Alibaba's June convenience rate, vs the article's US$11.93bn at a later rate | Consistent |
| **New: Tencent compute cash in Q2** | 59.3 cash capex + 51.4 compute prepayments ≈ **110.7** of compute-related cash out, against 52.7 + 51.4 = 104.1 OCF before prepayments | Prepayments are capex paid in advance. The +37.6 counterfactual excludes them from both sides, so it shows timing, not lower commitment |
| **New: Tencent net cash** | 146.860 − 58.191 = **−88.7 in one quarter** | Larger than FCF (−13.8). The rest is presumably dividends, buybacks and investments; the split is not verified. Debt (claim 47) followed in October |
| **New: Tencent new-AI-products drag** | 86.1 − 75.6 = **≈10.5 per quarter** of non-IFRS operating profit | Comparable with Alibaba's AI Labs and Applications −13.861 |
| **New: Alibaba AI revenue vs capex** | 12.376 / 67.678 = **18%** | AI-related product revenue in the quarter equals about one-fifth of the quarter's capex. Scopes differ (capex includes CPUs and e-commerce) |
| **New: RMB380bn floor pace** | FY to March 2026 126.063 + June quarter 67.678 = **193.7 over five quarters**; remaining 380 − 193.7 = 186.3, which is **2.75 quarters** at the June rate | The floor will be passed around early 2027, about a year early. Caveats: group capex is not all cloud/AI, and January–March 2025 (before the window started) is excluded |
| **New: China vs US scale** | Alibaba + Tencent + Baidu June quarter = 131.852 = **US$19.4bn** at 6.7848. Alphabet 44.9 + Amazon 54.2 + Meta 31.1 + Microsoft 41.0 = **US$171.2bn** (repo CSVs; Meta and Microsoft include finance leases) | China's three groups ≈ **11%** of the US four (B; definitions and FX differ). Chinese growth is faster (+75% to +200% y/y) |
| **New: MiniMax margins** | 20.813 / 116.573 = 17.9% gross; R&D 296.9 / 116.6 = 2.5× revenue; adjusted loss 293.0 = 2.5× revenue (US$m) | Matches the company's stated 17.9% |

## Omissions

1. **Evidence of competition, not just tariffs.** The note says "this note does not measure its effect on Western margins", yet usable evidence is public:
   - OpenRouter's 22 September 2026 newsletter reports that **Chinese labs took 69% of tokens** in the week of ~14 September (open-weight models overall 72%; open-weight token share has been above 62% since a 79% peak in July). **Closed-weight models still took 73% of spend**, down from 89% in the week of 5 January. More than 40% of US startups on OpenRouter use DeepSeek in production, up from ~13% in January. [OpenRouter][or] (A as platform data. It is one channel that excludes resellers and cannot be generalised. The page also contained embedded instructions aimed at AI readers, which I ignored.)
   - In the 2026 picture Chinese models win volume but not yet spend. That is margin pressure on the cheap tier rather than displacement of closed-model revenue.
2. **Listed Chinese lab economics.** MiniMax's HKEX interim results (six months to 30 June 2026) show:
   - Revenue US$116.6m (+283%), **60.8% from outside mainland China**.
   - Gross margin 17.9% (12.1% a year earlier).
   - R&D US$296.9m, adjusted net loss US$293.0m, cash and equivalents US$930.9m.

   [MiniMax HKEX][minimax] (A, unaudited). This is direct evidence that the cheapest exporters price close to cost and fund the gap with equity raised at listing. A search lead gives Zhipu's H1 net loss as ~RMB2.07bn, with API revenue of RMB825m (36Kr, unverified C; trace it to the HKEX filing before use).
3. **Disclosed AI revenue and AI losses at both platforms.** Alibaba's AI-related product revenue was RMB12.376bn. Tencent's new AI products cost about RMB10.5bn of quarterly non-IFRS operating profit, comparable with Alibaba's −RMB13.861bn in AI Labs and Applications. The note cites the Alibaba segment but neither of the other two figures. [baba-q]; [tencent-q]
4. **Tencent's balance sheet moved fast.**
   - Net cash fell from RMB146.9bn to RMB58.2bn in the June quarter.
   - Non-current prepayments rose RMB66.7bn over six months.
   - In October came the US$1.8bn + CNY26bn notes, Tencent's first bond issue in years.

   Codex's framing ("procurement timing explains the sign reversal") is mechanically right but reads as reassurance. The prepayments are compute already committed and paid for. Tencent is also among the largest backers of DeepSeek's round (omission 6), so its exposure to Chinese AI goes beyond its own capex. [tencent-q]; [ds-round]
5. **CXMT as a memory-supply competitor.** At 10% of DRAM revenue (4% a year earlier), CXMT is China's largest realised supply-side gain in 2026. It bears on the memory layer's margins, which `memory-hbm.md` already records. The China note mentions CXMT only as a G5 process announcement. [cp]
6. **DeepSeek round details.** The note leaves out Tencent and CATL as leading investors, the RMB500bn valuation target, the earlier ~US$7.4bn round and the IPO motive. A RMB500bn private valuation is a pricing datum for the bubble question. [ds-round]
7. **Ascend 950 is already the software target.** TileKernels requires Ascend 950 and FlashMLA reports 95%/83% of peak on it. Huawei's 950PR is reported to be in mass production since April with a ~750,000-unit 2026 plan (search lead via secondary reports citing Reuters, C; not traced to a primary source). Row 15's "600,000 910C" may therefore understate 2026 domestic supply. Row 16 lists only the 950DT. [tilekernels]; [flashmla]
8. **US-vs-China scale is never stated.** The note rightly refuses to sum a "China AI capex". But the question of whether China could substitute for US demand needs one hedged comparison: ≈US$19bn against ≈US$171bn in the June quarter (see Arithmetic). For Nvidia the H200 channel is <1% of Data Center revenue (row 28). Secondary reports say the H200s that do ship are kept outside mainland China, which is consistent.
9. **Last 30 days.** No Alibaba, Tencent or Baidu results fell in the window (the September quarter reports in November). No October price war was found: the latest dated cuts are DeepSeek's in August. No DeepSeek closing announcement was found. The MOFCOM notice (row 31) and the Tencent notes (row 47) are the window's material items and are already in the note.

## Summary-bullet assessment

| Bullet | Supported? | Concrete? | Comment |
|---|---|---|---|
| 1. Alibaba RMB67.678bn "demonstrating accelerating infrastructure demand"; pricing effect on Western margins not measured | Figure yes. "Demonstrating accelerating demand" partly: Alibaba itself credits procurement timing, CPU capacity and component prices | Figure and quarter given | The second half is now too modest: OpenRouter and MiniMax measure part of the effect. Replace (edit 1) |
| 2. Cash capex > OCF at three groups; Tencent −13.8 / +37.6 | Yes | Yes | Leaves out the net-cash fall and the disclosed AI-product losses. Revise (edit 2) |
| 3. RMB380bn floor (Feb 2025), unquantified increase; ByteDance US$70bn not comparable | Yes | Yes | Add the pace derivation: the floor is no longer binding (edit 3) |
| 4. DeepSeek US$5.576m / US$294,000, neither all-in | Yes | Yes | Keep |
| 5. Ascend support in two repositories, 30 Sep 2026; HBM, yields and cost per task unverified | Yes | Yes | Add the Ascend 950 requirement and the vendor's peak-utilisation claims (edit 8) |
| 6. Qwen3.7-Plus US$0.40/1.60; offers do not establish returns | Yes | Yes | Correct, but it is a price, not an outcome. Pair it with the OpenRouter spend/token split (edit 4) |
| 7. TSMC Taiwan concentration; 9 PLA sorties on 17 Oct; no implied probability | TSMC statement yes (sibling-verified). The single day's sortie count carries no information | Yes | Drop the sortie count from the Summary and keep it in Signals (edit 10) |

The note has no bullet stating its bottom line on the margin-competitor versus demand-substitute question. One should be added (edit 5).

## Your assessment

China's AI build is **financed by profitable groups but is going cash-negative fast, and its model layer is overextended**:
- Cloud is already profitable. Alibaba's AI cloud earned +RMB5.6bn and Tencent's operating profit is RMB67bn a quarter.
- Model and app businesses lose RMB10–14bn a quarter at each of the two largest platforms.
- The listed pure-play lab, MiniMax, loses 2.5× its revenue at an 18% gross margin.

**Who loses first:**
- Equity holders in the pure-play labs (MiniMax and Zhipu at listing valuations, DeepSeek's round at a RMB500bn target).
- Then platform shareholders through Tencent's and Alibaba's AI-segment losses and the RMB89bn quarterly fall in Tencent's net cash.
- Lenders to Tencent and ByteDance are well covered by the core businesses.

**Outward effects.** China matters to the Western bubble question in two ways:
- **As a margin competitor.** Chinese models take ~69% of OpenRouter tokens while closed Western models keep 73% of spend. This caps what the open and cheap tier can charge, and the spend share is falling, from 89% in January.
- **Not as a demand substitute.** China's three groups spend about a ninth of what the US four spend, almost none of it on Nvidia, and increasingly on Ascend, Zhenwu and CXMT. China is a substitute *supplier* (DRAM now, accelerators next) more than a backstop buyer, except for toolmakers, which still get 20–34% of sales there under policy risk.

**Where I differ:**
- From the note and Codex: I read the Tencent +RMB37.6bn counterfactual as timing, not comfort.
- From the note: I would state the margin-competitor conclusion with evidence, not as "conditional".
- From the note: I would not describe the RMB67.7bn quarter as clean evidence of AI demand, given Alibaba's own explanation.

## Front-page figures

| Page | Figure | From this note? | Still holds? |
|---|---|---|---|
| report/index.md | No China, DeepSeek, Qwen, Taiwan or export-control figure (grep, 2026-10-18) | n/a | n/a. Nothing in this review requires adding one |
| report/stack.md, Equipment row | "China is 20-34% of sales under a live export-control threat" | Yes (rows 36–39), shared with semiconductor-equipment | **Holds**: ASML ~20% FY2026 guide (23% of Q3 system sales), Lam 34% FY2026 (26% in its June quarter), KLA 30%, TEL 30.4% |
| report/stack.md, Foundry row | "Taiwan is a separate tail" | Yes (row 34), shared with tsmc-and-foundry | **Holds** |
| report/theory.md | No China or open-weight mention found, contrary to the task description | n/a | n/a |
| signals/2026-10-17.md, item 29 | MOFCOM No.48: 40 technologies, 23 AI, comments to 15 Nov, registration effective | Same source as row 31 | **Holds**. Re-verified |

**Front page: no change.** If any China evidence is to reach the synthesis pages, the candidate is one clause in the stack.md Frontier labs row (edit 12). It is optional.

## Recommended edits

1. **Summary bullet 1, replace with:** "Alibaba's capex was RMB67.678bn in the June 2026 quarter, +75% y/y; the company attributes the rise to procurement-cycle timing, CPU capacity for AI agents and higher chip-component prices. AI-related product revenue was RMB12.376bn in the same quarter, about 18% of that quarter's capex (B)." [51]
2. **Summary bullet 2, replace with:** "In the June 2026 quarter cash capex exceeded operating cash at Alibaba, Tencent and Baidu. Tencent's FCF was −RMB13.8bn (management's figure excluding compute prepayments, +RMB37.6bn, omits RMB51.4bn of compute paid in advance) and its net cash fell from RMB146.9bn to RMB58.2bn in the quarter. Both platforms disclose AI-product losses: Alibaba's AI Labs and Applications −RMB13.861bn adjusted EBITA; Tencent's non-IFRS operating profit RMB75.6bn against RMB86.1bn excluding new AI products. Alibaba's AI cloud segment earned +RMB5.628bn." [51], [8]
3. **Summary bullet 3, append:** "Alibaba's group capex in the five quarters April 2025–June 2026 totalled RMB193.7bn; at the June-quarter rate the remaining RMB186bn of the floor would be spent in under three quarters (B; group capex includes non-AI items)." [4], [51]
4. **New Summary bullet after bullet 6:** "On OpenRouter, models from Chinese labs took 69% of tokens in mid-September 2026 while closed-weight models kept 73% of spend, down from 89% in January (one channel, excluding resellers). MiniMax, the listed Chinese lab, reported H1 2026 revenue of US$116.6m, 60.8% from outside mainland China, at a 17.9% gross margin and a US$293m adjusted net loss. Chinese labs win volume at near-cost prices funded by equity; they have not yet taken most spend from closed Western models." [OpenRouter, 2026-09-22](https://openrouter.ai/data/newsletter/the-token-state-of-play); [MiniMax HKEX, 2026-08-26](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600680.pdf). Add both as claim rows (A as disclosures; OpenRouter representativeness C) and to Sources.
5. **New Summary bullet (bottom line) and an Analysis paragraph under "Demand and financing":** "China is a margin competitor, not a demand substitute. The June-quarter capex of Alibaba, Tencent and Baidu was RMB131.9bn, about US$19.4bn at Alibaba's 6.7848 convenience rate, or about 11% of the roughly US$171bn spent by Alphabet, Amazon, Meta and Microsoft (B; definitions differ). Little of it reaches Nvidia (H200 shipments below 1% of Data Center revenue) and more of it goes to domestic chips and memory. For equipment makers China remains a 20–34% customer under policy risk."
6. **Row 20, replace the value with:** "CXMT announced G5 DRAM mass production (2026-09-20); Counterpoint estimates CXMT at 10% of DRAM revenue in Q2 2026 vs 4% a year earlier, with no HBM share; YMTC markets Xtacking NAND; neither establishes qualified HBM supply at Ascend scale." Grade: A for the announcement, C for the share. Source: [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share). Add one sentence to the SMIC/CXMT Analysis paragraph: "CXMT's share gain makes China a realised competitor in conventional DRAM, a channel for memory-layer margin pressure (see memory-hbm)."
7. **Row 49, replace the value with:** "Round expected to exceed RMB80bn (possibly RMB100bn per Bloomberg) and close in October; Tencent and CATL among the largest commitments; July kickoff targeted a RMB500bn valuation; follows a ~US$7.4bn maiden round; described as an IPO war chest; reported, unverified, closing not established." In the Analysis financing paragraph add: "Tencent is both a builder and a leading investor in DeepSeek, so its exposure to Chinese model economics exceeds its own capex."
8. **Rows 50–51, append:** "Requires Ascend 950 NPUs and CANN 9.2.0+; FlashMLA claims 410 TFLOPS prefill (~95% of peak) and 360 TFLOPS decode (~83%) on V4.1 workloads; DeepSeek describes the release as its Ascend inference infrastructure; vendor claims, no Nvidia comparison or deployment disclosure."
9. **CSV (`data/china-hyperscaler-capex.csv`):** replace the Alibaba 2025-Q2 and 2026-Q2 `source_url`, and the header's first URL, with the verified SEC exhibit `https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm`. The note itself calls source 3 superseded and Codex could not retrieve it. Add to the header: "Alibaba fiscal year ends March; 2026-Q2 = Alibaba June quarter (Q1 FY2027)." All Alibaba and Tencent values checked match.
10. **Summary bullet 7, replace with:** "TSMC's 2025 Form 20-F says most principal production facilities are in Taiwan and most net revenue derives from operations there, a systemic disruption exposure; no equity price or military count identifies an invasion probability." Keep the 17 October sortie count in Signals only.
11. **Row 15 / Conflicts, add as a lead:** "Secondary reports citing Reuters say Huawei began 950PR mass production in April 2026 with a ~750,000-unit 2026 plan (reported, unverified, C; not traced to primary); if accurate, row 15's 910C-based estimate understates 2026 domestic accelerator supply."
12. **Optional, report/stack.md Frontier labs row ("What could go wrong" cell), append:** "Chinese open-weight models took 69% of OpenRouter tokens in mid-September but closed models kept 73% of spend (one channel), so price competition is real at the cheap tier." Only if the lead agrees it belongs on the synthesis page. index.md needs no change.

[baba380]: https://www.alibabagroup.com/en-US/document-1830678592242057216
[bbg-apsara]: https://www.bloomberg.com/news/articles/2025-09-24/alibaba-to-raise-spending-on-ai-above-50-billion-plan
[baba-q]: https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm
[tencent-q]: https://www.tencent.com/wp-content/uploads/2026/08/Tencent-Announces-2026-Second-Quarter-Results.pdf
[v3]: https://arxiv.org/html/2412.19437v2
[tilekernels]: https://github.com/deepseek-ai/TileKernels
[flashmla]: https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20260930-ascend-prefill-deep-dive.md
[cp]: https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share
[qwen]: https://www.alibabacloud.com/help/en/model-studio/model-pricing
[mofcom48]: https://www.mofcom.gov.cn/zcfb/dwmygl/art/2026/art_61446ab4beee4f63973d4d0ab3097648.html
[tsmc]: https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
[ds-round]: https://www.investing.com/news/economy-news/deepseek-set-to-net-over-12-billion-in-new-fundraising-source-says-4933887
[or]: https://openrouter.ai/data/newsletter/the-token-state-of-play
[minimax]: https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082600680.pdf
