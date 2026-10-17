# China — independent Codex cross-check

*Review date and information cutoff: 2026-10-17. Reviewed methodology, research brief, template and `research/macro/china.md`. Only this review was written; no git commands were run.*

## Verdict

Mostly verified, but material revisions are needed: the 15 selected rows largely reproduce their sources, while ByteDance's denied 2025 budget requires grade D.  
No arithmetic error found; cash-flow definitions and Tencent's compute prepayments materially qualify the financing interpretation.  
Missing debt financing, disclosed AI segment losses/profits, and September–October model/software releases make the Summary less current and less discriminating than the evidence permits.

## Claim re-verification

These 15 rows support the spending, financing, model economics, domestic substitution and geopolitical arguments. All linked sources below were fetched on **2026-10-17**. A means a primary disclosure is verified, not that a forecast, benchmark or commercial outcome was independently validated. “Match” distinguishes numerical agreement from a complete and current characterization. Unselected rows are not thereby certified.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | At least RMB380bn over three years; later increase, no replacement total | Same: February 24, 2025 commitment; September 29 announcement says investment will exceed it without quantifying the revision. | [Alibaba commitment][commitment]; [Apsara 2025][apsara25] | Yes; absence of a replacement total is scoped to sources checked. | A for announcements |
| 3 | FY2026 RMB126.063bn; March quarter 26.887bn; June quarter 67.678bn vs 38.676bn | All four match. Fiscal year ends March 31. June 2025 comparator also appears in Alibaba's presentation, p.3. | [FY2026 results][baba-fy]; [June 2026 SEC exhibit][baba-q]; [issuer presentation, third-party mirror][baba25-slides] | Yes. Original June PDF failed retrieval; used SEC replacement. | A; comparator is issuer-authored material on a mirror |
| 4 | June OCF RMB22.945bn; FCF −44.670bn; AI Cloud and Compute revenue 48.4bn, +45% | 22.945; −44.670; exact segment revenue 48.437bn, +45%. | [June results, financial highlights and segment results][baba-q] | Yes. This segment is not exclusively AI revenue. | A |
| 5 | HK$80bn gross equity placement completed August 26; proceeds for AI infrastructure | Same; 710m shares at HK$112.70. Intended net allocations are HK$47.871bn and HK$31.914bn. | [Completion announcement][placement] | Yes; intended use, not evidence funds have already been spent. | A |
| 7 | Tencent June cash capex RMB59.3bn; OCF 52.7bn; FCF −13.8bn; IFRS operating profit 67.3bn; net cash 58.2bn | Same rounded values; exact profit 67.276bn and net cash 58.191bn. Release also reports FCF excluding compute prepayments of **+37.6bn**. | [Tencent Q2 release, pp.1–2, 5–6][tencent-q] | Yes, but important qualification underweighted. | A |
| 10 | ByteDance 2025 budget >RMB150bn; possible 2026 US$70bn capex backed partly by roughly US$50bn 2025 profit; C | Reports contain those figures. **The 2025 Reuters article also records ByteDance's explicit rejection of the anonymously sourced spending information.** May 2026 amounts are preliminary, anonymous-source estimates. | [Reuters, January 23, 2025][byte25]; [Bloomberg/The Edge, May 27, 2026][byte26] | Numbers match reporting; omitted denial changes grade. No primary budget/accounts found. | **D for contested 2025 budget; C for 2026 capex/profit** |
| 11 | 2.788m H800 hours × US$2 = US$5.576m; prior research excluded | Same, Table 1: 2.664m pretraining + 0.119m context extension + 0.005m post-training hours. | [DeepSeek-V3 report, Table 1][v3] | Yes; assumed rental-equivalent cost, not total R&D expenditure. | A for reported estimate; B for recomputation |
| 12 | R1 specified stages: 147,000 H800 hours / US$294,000; inherited V3 excluded | Same, Supplementary Table 4: 101K R1-Zero + 5K data creation + 41K R1, priced at US$2/hour. Earlier A100 experiments are discussed separately. | [Nature supplement, §2.4.4 and Table 4, printed pp.26–27][r1] | Yes; does not establish all-in development cost. | A for disclosure; B for recomputation |
| 13 | April V4 preview; independent V4-family post-training on Ascend; original pretraining mix unknown | Historical claims match. SLAI T-Rex reports 34.22% MFU and 2.93× its baseline. **Current status has advanced to V4.1-Flash-1017 on October 17.** | [V4 announcement][v4]; [SLAI T-Rex v3][trex]; [DeepSeek changelog][ds-log] | Historical match, materially stale as a current model description. No complete original hardware mix verified. | A for releases and authors' reported experiment |
| 16 | 950DT Q4 2026; HiZQ 2.0 144GB, 4TB/s; domestic volume unproved | Same in Huawei's September 2025 roadmap. | [Huawei keynote, Ascend 950DT passage][huawei25] | Yes as a roadmap. It supplies neither qualified shipment volume nor manufacturing yield. | A for advertised specifications/schedule |
| 22 | Singapore international Qwen3.8-Max US$2/6; Qwen3.7-Plus US$0.40/1.60, input ≤256K, before promotions | Same list prices per million input/output tokens. Plus has a temporary 20% discount; larger contexts use another tier. | [Alibaba Cloud pricing, Singapore/International tables][qwen-price] | Yes, with region, token tier and promotion caveats retained. | A |
| 28 | H200 case-by-case licences; China restrictions; shipments <1% of latest Data Center revenue; US$0.4bn charge; 25% tariff borne by Nvidia | Same; **charge covers the first half of FY2027**, while the <1% revenue observation is for the latest quarter ended July 26, 2026. Nvidia says it cannot pass the tariff to customers. | [Nvidia 10-Q, printed pp.27, 37][nvda]; [BIS January 13 policy][bis-h200] | Yes numerically; clarify mixed periods within row. | A |
| 31 | MOFCOM No.48: 40 proposed technologies, 23 AI; comments October 16–November 15; registration starts immediately | Same. Registration also covers exports already started but unfinished and specified changes to foreign ownership/control. | [Announcement 48, §§I–III][mofcom48] | Yes. Distinguish registration now from catalogue restrictions proposed. | A |
| 32 | Public-domain/open-source exclusion; facilitated licensing for new open-source transfers; API/app/SaaS exclusion | Substantively matches the announcement/Q&A. API/app/SaaS exclusions and overseas deployment treatment describe the **proposed final regime**; they are not proof it is already in force. | [Announcement 48][mofcom48]; [official Q&A][mofcom-qa] | Qualified match; proposal/effective-date wording needs tightening. | A as statement of proposed scope |
| 34 | Majority of TSMC principal production facilities and operating revenue remain in Taiwan | Filing says majority of principal production facilities are in the ROC and majority of net revenue derives from operations there; distinct from customer location. | [TSMC 2025 20-F, printed p.5][tsmc] | Yes in substance; use filing's “net revenue from operations” terminology. | A |

## Arithmetic checks

The Analysis contains **no explicit new numerical calculation**: it refers to the claim-table values and draws qualitative implications. I therefore checked every numerical relationship underlying those implications, plus the table's explicit training-cost and half-year derivations. Monetary arithmetic below uses billions of RMB unless stated otherwise. Recomputations are grade B.

| Relationship | Recalculation and finding |
|---|---|
| V3 official training | (2,664K + 119K + 5K) = 2,788K hours; × US$2 = US$5.576m. Correct. [Table 1][v3] |
| R1 selected stages | (101K + 5K + 41K) = 147K hours; × US$2 = US$294K. Correct on rounded table inputs. Do not describe this as all development or add the whole V3 figure to it as an audited R1 budget. [Table 4][r1] |
| Alibaba cash deficit versus FCF | 22.945 − 67.678 = **−44.733**, not reported FCF. Correct FCF bridge: 22.945 − 67.660 + 0.045 = **−44.670**; eligible capex and merchant-deposit adjustment differ. This is a definition difference, not a note arithmetic error. [FCF reconciliation][baba-q] |
| Alibaba cloud growth | 48.437 / 33.418 − 1 = **44.9428%**, rounding to 45%. Use recast segment comparatives. [Segment results][baba-q] |
| Tencent half-year capex | 31.936 + 52.784 = **84.720**, correct. [Interim report, p.14][tencent-ir] |
| Tencent FCF | 52.7 − 59.3 − 5.0 media content − 2.2 leases = **−13.8**. Compute-prepayment effect is 37.6 − (−13.8) = **51.4**. Do not subtract prepayments again: they already depress OCF. [Release p.2][tencent-q] |
| Baidu consolidated FCF | 3.436 − 11.390 = **−7.954**, correct. Do not mix these consolidated values with the separate ex-iQIYI columns. [Cash-flow table][baidu-q] |
| Spending exceeds operating cash | Alibaba's gap is 44.733; Tencent cash-capex gap 6.6; Baidu gap 7.954. All three comparisons hold for the June quarter, not necessarily a normalized year or AI-only operations. |

There is no numerical conversion of component dies into delivered accelerators in the Analysis, no purported aggregate “China AI capex,” no currency conversion, and no numerical conflict probability to audit. These are appropriate exclusions. The new Tencent offering's RMB96.3bn half-year **cash payments** are not a correction to RMB84.720bn reported capex: the two documents expressly use different measures. [October offering extract, p.48][tencent-offer]

## Omissions

The recent-information search focused on **September 18–October 17, 2026**, with older items included where material. These findings change the financing mix, profit allocation or strength of substitution evidence; none alone proves a bubble.

- **Debt is already concrete, not merely a hypothetical loss channel.** Tencent announced bond pricing on October 14, with issuance expected October 21, for general corporate purposes. This is a primary-source addition to the financing analysis, not proof that every dollar funds AI. See exact amounts in recommended edit 4. Its October 12 offering extract also supplies the cash-capex measure discussed above. [Pricing announcement][tencent-bonds]; [offering extract][tencent-offer]
- **Important older financing lead:** Reuters reported a US$29.6bn unsecured ByteDance facility on September 4, with an initial three-year term and extension options. General corporate purposes were communicated to lenders; AI/offshore-project allocations come from anonymous sources. It remains **reported, unverified, C**, not a verified drawdown. It substantially changes the note's profit-financed framing even though a complete financing schedule remains unavailable. [Reuters][byte-loan]
- **Recent private-lab financing lead:** October 6 reporting says DeepSeek expects a round exceeding RMB80bn, with a possible higher total. Completion was expected during October, not established by the article. Include as **reported, unverified, C**; do not turn it into cash already raised or an audited budget. A search of official DeepSeek news did not establish closing. [Reuters][ds-funding]
- **Cash burn is not the only observable economic result.** Alibaba separately discloses profitable AI cloud and loss-making AI labs/apps, while Tencent gives a prepayment-adjusted cash-flow counterfactual. These distinguish build timing from recurring losses. The note's blanket “provider margins remain unknown” should be narrowed to standalone inference and investment-cohort returns; segment operating results do exist. Exact additions are in edits 2–3. [Alibaba segment results][baba-q]; [Tencent release][tencent-q]
- **September 30 software evidence is stronger than a roadmap.** DeepSeek's own TileKernels repository adds an Ascend backend; FlashMLA documents Ascend sparse-attention inference kernels. This is direct evidence of porting work, not independent verification of end-to-end cost, reliability or shipped capacity. It strengthens the substitution argument and weakens an undifferentiated claim that software remains a fixed barrier. [TileKernels][tilekernels]; [FlashMLA technical note][flashmla]
- **Current DeepSeek economics have moved beyond the April preview.** V4.1-Flash launched September 10; its October 17 update retains API prices while the vendor claims shorter outputs and runtimes. The launch describes reduced KV-cache HBM demand, which is not the same as reducing all memory needs. Lower prices may therefore reflect efficiency as well as rent destruction. **Source conflict:** the launch page planned to route V4-Pro requests away, but the current official changelog explicitly retains V4-Pro service after September 14. Huawei Cloud's separate September 22 retirement notice applies to its own service, not every host. [Launch][v41]; [current changelog][ds-log]; [Huawei notice][huawei-retirement]
- **Domestic competition is broader than Ascend.** Alibaba's September 22 keynote introduces Zhenwu V900 and advertises 3× predecessor performance and clusters up to 500,000 cards. These are **A as vendor claims**, not measured delivered capacity. Huawei's September 19 ecosystem announcement adds public compute access and programming support. Both matter to the substitution pathway; neither resolves HBM manufacturing or utilization. [Alibaba keynote][apsara26]; [Huawei ecosystem update][huawei26]
- **October 16 policy is already present, not an omission.** The missing nuance is that restricted-technology overseas deployment remains within the proposed controls, with facilitation for own-cloud deployment; general API delivery is treated differently. Avoid reading the exclusions as unrestricted transfer of all weights or infrastructure know-how. [Official Q&A][mofcom-qa]

## Summary-bullet assessment

| Bullet | Supported by its own evidence? | Specificity and required change |
|---|---|---|
| 1 — demand, model rents, geopolitics | **Partly.** Demand and policy exposure have observations. “Competes away model rents” implies a realized causal effect not demonstrated by tariff samples. The Analysis itself admits this. | No number/date; too abstract. Replace with edit 8's first bullet and make rent pressure conditional. |
| 2 — profitability and cash shortfall | **Yes for June-quarter group cash flows; incomplete as economic diagnosis.** Existing-business profitability is supported, but timing and segment outcomes matter. | No date/figure; too abstract. Use edit 8's second bullet, together with edits 2–4 in Analysis. |
| 3 — Alibaba commitment versus ByteDance | **Alibaba supported; comparison unsafe without annualization and aligned scope.** ByteDance's annual scenario versus Alibaba's multiyear floor is not a like-for-like “much larger” comparison. | Has a figure but no announcement date. Replace with edit 8's third bullet; record the denial under edit 1. |
| 4 — DeepSeek cost boundaries | **Supported.** Correct distinction between run cost, inherited base training and broader research. | No actual costs or dates, despite being the central factual point. Edit 8 supplies both. |
| 5 — Ascend alternative and constraints | **Directionally supported, too categorical on constraints.** A post-training paper and proposed site do not establish inference economics; yields/packaging lack quantified evidence in the note. | No figure/date. Update with dated released software; describe shipment and cost limitations as unresolved questions. |
| 6 — open weights and prices | **Mechanism supported; realized rent destruction not established.** Its own caveats and Tencent pricing commentary prevent a universal conclusion. | No figure/date. Use a correctly scoped tariff example and distinguish an offer from successful substitution. |
| 7 — Taiwan | **Supported as a conditional supply-risk mechanism and an epistemic limit.** Neither a stock index nor daily military counts identifies invasion probability. | Useful but unanchored. Add the 2025 filing date reference; retain the refusal to infer a probability. |

## Your assessment

China is a credible source of both compute demand and competitive pressure, but the note's evidence supports a differentiated investment-risk story more strongly than a general inference-margin-collapse story. I agree that development-cost headlines do not establish all-in model economics, and that Taiwan creates systemic supply exposure without a defensible numerical invasion probability. I differ in putting more weight on observable cloud profitability, application losses and procurement timing, while assigning more financing exposure to debt holders than the note currently conveys. Recent released Ascend software strengthens the practical substitution case; it does not establish manufacturing autonomy or profitable deployment at scale. The defensible conclusion is rising and uneven capital-at-risk, with inadequate evidence on utilization, incremental returns and security valuation to declare a China-wide AI bubble.

## Recommended edits

1. **Split row 10 and correct the grade/conflict.** Replace the 2025 portion with: “Reuters reported a 2025 capex budget above RMB150bn on January 23, 2025; ByteDance explicitly rejected the anonymously sourced spending information. Contested, grade D.” Keep the May 2026 US$70bn scenario and US$50bn profit estimate at C, reported and unverified. [Reuters][byte25]; [Bloomberg][byte26]

2. **Add the missing profit allocation to Analysis:** “In the June 2026 quarter, Alibaba reported adjusted EBITA of RMB5.628bn in AI Cloud and Compute Services and a loss of RMB13.861bn in AI Labs and Applications. These segment results distinguish profitable infrastructure services from application/model investment losses; standalone inference margins and investment-cohort returns remain undisclosed.” [Alibaba results][baba-q]

3. **Replace the vague Tencent prepayment qualification:** “Tencent's Q2 2026 FCF was −RMB13.8bn, but management reports +RMB37.6bn excluding compute prepayments. Procurement timing explains the sign reversal; the cash commitment and delivery/utilization risks remain.” Retain the company's FCF reconciliation, including content and leases. [Tencent release][tencent-q]

4. **Add actual financing developments:** “On October 14, 2026, Tencent announced pricing of US$1.8bn and CNY26bn of notes for general corporate purposes, with issuance expected October 21. Separately, Reuters reported a US$29.6bn unsecured ByteDance loan in September and a prospective DeepSeek funding round above RMB80bn on October 6; both private-company reports remain unverified, grade C.” [Tencent announcement][tencent-bonds]; [ByteDance report][byte-loan]; [DeepSeek report][ds-funding]

5. **Update row 13 and domestic-supply Analysis:** “DeepSeek's current Flash model was updated to V4.1-Flash-1017 on October 17, 2026, with API pricing unchanged. On September 30, DeepSeek released Ascend support in TileKernels and Ascend inference kernels in FlashMLA. These releases demonstrate concrete software adaptation, not full original pretraining on Huawei or verified cost parity.” [Changelog][ds-log]; [TileKernels][tilekernels]; [FlashMLA][flashmla]

6. **Add the other major domestic supplier:** “Alibaba introduced Zhenwu V900 on September 22, 2026, advertising 3× predecessor performance and clusters of up to 500,000 cards. These vendor specifications broaden the domestic-substitution scenario; accepted shipment volumes and comparable workload economics remain unverified.” [Alibaba keynote][apsara26]

7. **Correct scope labels without changing matching figures.** In row 28 replace “US$0.4bn charge” with “US$0.4bn H200 charge in the first half of FY2027”; in row 32 begin “Under the proposed revised catalogue and official explanatory Q&A…” and add “temporary pre-export registration is already effective.” Preserve the distinction between restricted-technology overseas deployment and API/app/SaaS services. [Nvidia filing][nvda]; [MOFCOM notice][mofcom48]; [Q&A][mofcom-qa]

8. **Replace all seven Summary bullets with these concrete sentences, in order:**

   - “Alibaba spent RMB67.678bn in the June 2026 quarter, demonstrating accelerating infrastructure demand; Chinese model pricing creates competitive pressure, but this note does not measure its effect on Western margins.” [Alibaba results][baba-q]
   - “In the June 2026 quarter, cash capex exceeded operating cash at Alibaba, Tencent and Baidu; Tencent's FCF would nevertheless have been positive excluding compute prepayments, so the shortfall is not by itself evidence of unprofitable steady-state operations.” [Alibaba results][baba-q]; [Tencent release][tencent-q]; [Baidu results][baidu-q]
   - “Alibaba announced a minimum RMB380bn three-year infrastructure programme in February 2025 and an unquantified increase that September; ByteDance's reported US$70bn annual 2026 scenario remains unverified and is not directly comparable.” [Alibaba commitment][commitment]; [Apsara 2025][apsara25]; [Bloomberg][byte26]
   - “DeepSeek disclosed US$5.576m of V3 official-run compute in its February 2025 report revision and US$294,000 for specified R1 stages in September 2025; neither is an all-in development budget.” [V3 report][v3]; [R1 supplement][r1]
   - “DeepSeek released Ascend inference software on September 30, 2026, strengthening domestic substitution; qualified HBM volumes, manufacturing yields and comparable cost per successful task remain unverified.” [TileKernels][tilekernels]; [FlashMLA][flashmla]
   - “On October 17, 2026, Qwen3.7-Plus listed Singapore international input/output prices of US$0.40/1.60 per million tokens for inputs up to 256K, before promotions; cheap offers and open weights do not establish provider returns or universal workload substitution.” [Pricing][qwen-price]
   - “TSMC's 2025 annual filing places most principal production facilities and operating-origin net revenue in Taiwan, leaving systemic disruption exposure; neither equity prices nor military counts identifies an invasion probability.” [TSMC filing][tsmc]

9. **Carry the new evidence into the existing claim table and signals, without inventing totals.** Add separately graded rows for Tencent bond pricing, the reported ByteDance loan and DeepSeek round, Alibaba's two segment results, and the dated software/model releases. Track bond issuance on October 21 and private-round closing separately from announcements. Keep Tencent's RMB96.3bn half-year cash-payment measure distinct from its RMB84.720bn reported capex. [Offering extract][tencent-offer]; [interim report][tencent-ir]

[commitment]: https://www.alibabagroup.com/en-US/document-1830678592242057216
[apsara25]: https://home.alibabagroup.com/en-US/document-1911884625546838016
[baba-fy]: https://www.sec.gov/Archives/edgar/data/1577552/000110465926060224/tm2614494d1_ex99-1.htm
[baba-q]: https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm
[baba25-slides]: https://s3-2.valuesense.io/IR_presentations/BABA/Investor_presentations/BABA_Q1_2026.pdf
[placement]: https://www.alibabagroup.com/en-US/document-2029365886510432256
[tencent-q]: https://www.tencent.com/wp-content/uploads/2026/08/Tencent-Announces-2026-Second-Quarter-Results.pdf
[tencent-ir]: https://www.tencent.com/wp-content/uploads/2026/08/E700_IR.pdf
[byte25]: https://www.investing.com/news/stock-market-news/exclusivebytedance-plans-20-billion-capex-in-2025-mostly-on-ai-sources-say-3826261?ampMode=1
[byte26]: https://theedgemalaysia.com/node/805120
[v3]: https://arxiv.org/html/2412.19437v2
[r1]: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-09422-z/MediaObjects/41586_2025_9422_MOESM1_ESM.pdf
[v4]: https://deepseek.com/en/news/v4-preview/
[trex]: https://arxiv.org/abs/2607.20145v3
[huawei25]: https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech
[qwen-price]: https://www.alibabacloud.com/help/en/model-studio/model-pricing
[nvda]: https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf
[bis-h200]: https://media.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china
[mofcom48]: https://www.mofcom.gov.cn/zcfb/dwmygl/art/2026/art_61446ab4beee4f63973d4d0ab3097648.html
[mofcom-qa]: https://www.mofcom.gov.cn/zwgk/zcjd/art/2026/art_b11d5c1e9374421e93e85dc87eba6e38.html
[tsmc]: https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
[baidu-q]: https://ir.baidu.com/news-releases/news-release-details/baidu-announces-second-quarter-2026-results
[tencent-offer]: https://www.tencent.com/wp-content/uploads/2026/10/E700_Launch-Announcement.pdf
[tencent-bonds]: https://www.tencent.com/wp-content/uploads/2026/10/E700_Pricing-Announcement.pdf
[byte-loan]: https://www.investing.com/news/stock-market-news/bytedance-secures-296-billion-loan-in-ai-push-sources-say-4889439
[ds-funding]: https://www.investing.com/news/economy-news/deepseek-set-to-net-over-12-billion-in-new-fundraising-source-says-4933887
[tilekernels]: https://github.com/deepseek-ai/TileKernels
[flashmla]: https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20260930-ascend-prefill-deep-dive.md
[v41]: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
[ds-log]: https://api-docs.deepseek.com/updates/
[huawei-retirement]: https://www.huaweicloud.com/intl/en-us/notice/20260922173926811.html
[apsara26]: https://home.alibabagroup.com/en-US/document-2039431633571938304
[huawei26]: https://www.huawei.com/en/news/2026/9/hc-agentic-thinkpro-pto-cann
