# Independent cross-check (Claude): Meta

*Review date: 2026-10-18. Reviewer: Claude (Anthropic), fresh context, first second-vendor check. Reviewed: `research/stack/meta.md` (last updated 2026-10-17, written by Codex and corrected once after the Codex cross-check in `reviews/meta-codex-xcheck.md`). Every external source below was accessed on 2026-10-18. Figures are in USD billions unless stated otherwise.*

## Verdict

All 12 load-bearing rows I re-checked match their primary sources, and the core arithmetic is correct. The front-page figures taken from this note still hold, although two of them need qualifying.
Both vendors missed one thing. The FY2025 H2/H1 cash-flow ratio that the Codex review added (+$4.7B to +$19.7B FY FCF) is inflated by a one-off drop in cash taxes in H2 2025. With cash taxes adjusted, the upside is about +$13.9B. A guidance-based check gives −$8.5B to +$10.1B. In every scenario, 2026 FCF fails to cover dividends plus RSU tax withholding.
The note also omits several items: Q3 results due on 21 October; $81.65B of commitments due in 2027; the scope of GEM's evidence (per-surface uplifts of 1.6–5.8%, a model trained on "several thousand" GPUs); management's statement about compute-resale offers; and the El Paso SPV bond pricing. Accept the note once the edits below are made.

## Claim re-verification

| Claim # | Note's value | My value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 10 | Q2'26 capex / OCF / FCF 31.078 / 31.862 / 0.784 | Purchases of P&E 30.116 + finance-lease principal 0.962 = 31.078. OCF 64.088 (H1) − 32.226 (Q1) = 31.862. FCF 0.784 is printed in the release | [Q2 release][Q2], [10-Q][Q2Q] | Yes | A (FCF as printed); B (capex sum) |
| 11 | FY2025 capex / OCF / FCF 72.215 / 115.800 / 43.585; FY2024 39.225 / 91.328 / 52.103 | 69.691 + 2.524 = 72.215; OCF 115.800; FCF 43.585. 2024: 37.256 + 1.969 = 39.225; 91.328; 52.103 | [FY25 release][FY25] | Yes | A / B |
| 12 | 2026 capex guidance 115–135 → 125–145 → 130–145, reaffirmed in August; no numerical 2027 guidance | January 115–135. July 130–145, "narrowed from our prior outlook of $125–145 billion". August: "Otherwise, the guidance ranges provided in our July earnings release remain unchanged". July call: "we aren't providing a specific outlook for 2027 CapEx", and plans are "geared towards maximizing 2026 and 2027 capacity" | [FY25][FY25], [Q2][Q2], [call][CALL], [Aug statement][LEGAL] | Yes. The note leaves out the 2027 capacity-maximisation wording and the July expense guidance ($165–169B, FY OI above 2025, Q3 revenue $61–64B) | A |
| 13 | H1'26 OCF 64.088, capex 50.918, FCF 13.170 | 64.088; 49.113 + 1.805 = 50.918; 13.170 | [10-Q cash-flow statement][Q2Q] | Yes | A inputs; B |
| 14 | Cash and securities 90.260; debt 83.664; escrow 10.80 restricted | 90.26; long-term debt 83.664 (face 84.000); 10.80 of money-market funds reclassified to restricted cash, release expected 2028–2030; no financial covenants on the Notes | [10-Q][Q2Q] | Yes | A |
| 17 | Q2 revenue 60.801; ads 59.363 (+27%, +26% cc); FoA OI 23.394; RL −4.619; OI 18.775 | All the same. Total revenue +28% reported, +27% constant currency. OI fell 8% year on year (the 10-Q states this; the note does not) | [Q2][Q2], [10-Q MD&A][Q2Q] | Yes | A; B ratios |
| 18 | GEM: Oct 13, 2026, +18.9% conversions, +12% CTR "across surfaces/objectives" | The figures are correct but cover "over the past year". The same post gives per-surface uplifts of **5.8% / 4.1% / 1.6%** (Facebook / Instagram / off-site) "for targeted users", and says GEM "trains at LLM scale on several thousand of the latest-generation GPUs". The post gives no baseline, no test design and no revenue figure | [GEM 2026][GEM26] | Figures match; scope is understated | A as company measurement |
| 19 | Advantage+ over 75 annual revenue run-rate | "reaching over $75 billion in annual revenue run-rate this quarter". The same call also claims +8.3% ad clicks and +15.7% conversions on Facebook from ranking advances | [call][CALL] | Yes | A (management claim) |
| 24 | Hyperion RVG ~28 (declining); equity 2.92; max exposure 46.03; unconsolidated; no RVG liability | All the same. Max exposure was **45.95 at Dec 2025**, so it is flat. It is made up of equity, lease commitments, estimated future funding and the maximum RVG threshold. RVG payment = shortfall of fair value below threshold, "if certain other conditions are met" | [10-Q Note 5][Q2Q] | Yes | A |
| 28 | Uncommenced leases 278.99; July +68; commitments 349.31; contingent 14.72 | All the same. The July leases commence in **2027 and 2028 with 18–20 year terms**. Of the commitments, **53.52 is due in 2026 and 81.65 in 2027**. I did not re-open the March figure (182.88); Codex checked it | [10-Q Note 9][Q2Q] | Yes; the note omits the timing | A |
| 36 | Close $709.33 (Oct 16); 2.547506225bn shares; 1,807.0; 47.7×; 2.1% | Table close 709.33 (the header shows 709.42). Shares 2,205,128,509 A + 342,377,716 B as of July 24 | [price][PRICE], [10-Q cover][Q2Q] | Yes | B (vendor price) |
| 37 | Settlement ~18 over 10 years, 12.7 allocated / 5.3 conditional; ~10 Q3 accrual outside July expense guidance | All the same. The conditional 30% depends on YouTube and TikTok adopting matching measures and payments. Meta's page also lists a **non-algorithmic default feed option** for teens, which the note does not mention | [Meta statement][LEGAL] | Yes | A (attributed). I did not re-open Illinois's 17.1 |

I also confirmed these rows against the 10-Q: claim 16 (Q2 impressions +14%, price per ad +12%), claim 31 (SBC 13.690 in the H1 cash-flow statement; the RSU-only table shows 13.626, with the difference being options; unrecognised RSU expense 79.79), and claim 44 (legal 2.40, severance 1.18 for about 8,000 employees).

## Arithmetic checks

| Calculation | Recalculation | Result |
|---|---|---|
| Flat-H2 FY FCF | 2 × 64.088 − [145, 130] = −16.824 / −1.824 | Correct |
| Seasonal FY FCF (claim 41) | H2'25 OCF 115.800 − 49.587 = 66.213; ratio 1.335289; 64.088 × ratio = 85.576; FY FCF +4.664 / +19.664 | Arithmetic correct, **assumption flawed (see below)** |
| Break-even and H2-only thresholds (claims 42–43) | 130/145 − 64.088 = 65.912 / 80.912 (+2.8% / +26.3%); 79.082 / 94.082 (+23.4% / +46.8%) | Correct |
| TTM FCF, equity value, multiple | 43.585 + 13.170 − 18.883 = 37.872; 709.33 × 2.547506 = 1,807.02; ÷ 37.872 = 47.71×; yield 2.10% | Correct |
| Legal and severance add-back | 18.775 + 2.40 + 1.18 = 22.355; ÷ 60.801 = 36.77%; vs Q2'25 OI 20.441 = +9.4% (management says +9%) | Correct |
| Ratios | Ads/revenue 97.63%; capex/revenue 51.11%; capex/OCF 97.54% | Correct |
| Selected-outflow residual | 13.170 − 8.704 − 2.699 = 1.767 | Correct |

**The seasonal ratio is inflated by cash taxes (new; both prior passes missed this).** Cash paid for income taxes was 5.544 in H1'25 and 7.578 for FY2025, so H2'25 was **2.034**. That fall came after the July 2025 OBBBA, and the 10-K says the OBBBA "had a significant impact on our tax obligations". H1'26 cash taxes were already low at **1.999**. As a result, the 1.335× ratio carries a tax benefit that has already been banked in H1'26. On a pre-tax-cash basis the ratio is (66.213 + 2.034) / (49.587 + 5.544) = **1.2379×**. That gives H2'26 OCF of (64.088 + 1.999) × 1.2379 − 1.999 = **79.81**, and FY FCF of **−1.10 to +13.90** at capex of 145 to 130. Sources: [10-K][K25], [10-Q][Q2Q]. Grade B.

**Guidance-based cross-check (new).** Q3'25 revenue = 200.966 − 89.830 − 59.893 = 51.243. The Q3'26 guide of $61–64B is +19.0% to +24.9%. Apply the same growth to Q4, so H2 revenue is 132.3–138.8, and use the H1'26 OCF margin (54.72%). H2 OCF comes out at 72.4–76.0, and FY FCF at **−8.5 to +10.1**. This is an illustration, not a forecast. Grade B.

**Owner outflows (new, robust across all scenarios).** Run H1's RSU withholding (8.704) and dividends (2.699) at the same rate for the full year: 22.81. FY FCF minus that is **−39.6 to −8.9** across the full range of sensitivities. In other words, 2026 dividends plus equity-award tax withholding need external funding (the $24.91B May notes) whatever the H2 outcome. This conclusion does not depend on which seasonal assumption is used.

**Hyperion exposure breakdown.** 46.03 ≈ RVG ~28 + leases 12.31 + equity 2.92 + estimated future funding ≈ 2.8 (the residual). Only the ~12.3 lease component can overlap with the $279B of uncommenced leases. This is my arithmetic; "approximately $28 billion" is rounded.

## Omissions

1. **Q3 2026 results on 21 October 2026, after the close** ([Meta notice][Q3D]). These replace the June-based FCF, the lease and commitment balances, and the H2 sensitivities, and may bring a first 2027 capex comment. The note's Signals table should flag the date, and the front-page Meta figures should be refreshed on 21–22 October.
2. **The 2027 rigidity is under-stated.** $81.65B of the non-cancellable commitments fall due in 2027. The $68B of July leases commence in 2027–28, with 18–20 year terms. Management says plans are "geared towards maximizing 2026 and 2027 capacity". These matter more for the "who loses if demand disappoints" question than the 2026 FCF sign does. Over the 18-month horizon, they make a 2027 capex cut harder. [10-Q][Q2Q], [call][CALL]
3. **The scope of the GEM evidence.** The note highlights the 18.9% / 12% headline. The same post gives per-surface uplifts of 5.8% / 4.1% / 1.6% for targeted users, and describes GEM training on "several thousand" GPUs. This evidence is about a model that uses a small fraction of a $130–145B build. It supports "AI improves ads". It says little about the frontier/MSL share of the capex. Both earlier passes accepted the headline. [GEM 2026][GEM26]
4. **Compute resale has been stated, not only reported.** On the July call, management listed "potentially selling compute directly". It said Meta has "quite a number of offers at a meaningful premium over what we paid for the compute", while preferring to sell "intelligence". Separately, the NYT reported (via [Engadget][ENG], 17 July) early talks to lease Anthropic up to $10B of compute over two years. No signed deal turned up in my searches through 18 October. This cuts both ways. It is a hedge against stranded capacity. It is also an admission that capacity may run ahead of Meta's own demand. The note's "no separately reported cloud earnings base" is literally true but leaves this out. Statement: A. Talks: C, reported, unverified.
5. **The cost of SPV capital is rising.** Search results (Bloomberg via Advisor Perspectives, 24 and 28 July; Capacity, 24 July) report that the El Paso notes (Sopaipilla Investor LLC, ~$12.3–12.55B, due 2048) were marketed at about T+287.5bp. One report gives a final yield near 7.5%. S&P (preliminary A+) and Fitch (AA−(EXP)) ratings are also reported. Meta's own 2036 notes priced at 5.25% in April. I could not fetch a pricing record: final size, coupon and closing are **reported, unverified (C)**. If confirmed, this would settle the note's "El Paso closing not verified" point. It also means the market charges a clear premium for Meta-backed off-balance-sheet structures. [Capacity][CAP]
6. **Accrued capex ran ahead of cash.** Property and equipment sitting in payables and accruals rose from 9.331 (Dec 2025) to **19.502** (June 2026). On an accrual basis, H1 spending was about $10B above cash capex. Guidance is on a cash basis, so this does not change the FY sensitivity. It does mean H1 FCF of 13.170 flatters the pace of the build. H1 D&A was also up 49.9% year on year (12.355 vs 8.242), so the earnings drag is already arriving. [10-Q][Q2Q]
7. **Minor items.** In H1 Meta issued options on 20M shares at a weighted-average strike of **$2,788** with market conditions, about 3.9× the October 16 price; the unrecognised expense is only $0.47B. This shows what pay is now tied to, not a material cost. Q2 OI fell 8% year on year as reported, and the Summary does not say so.

## Summary-bullet assessment

| Bullet | Supported? | Concrete? | Assessment |
|---|---|---|---|
| 1 Ads 97.6%, FoA OI $23.394B, no cloud base | Yes | Yes | Accurate. Add the July compute-resale statement so "no cloud base" is not read as "no resale optionality". |
| 2 FY FCF −16.8 to −1.8 flat; +4.7 to +19.7 seasonal | Arithmetic yes; the seasonal assumption is flawed | Yes | Replace the upper case with the tax-adjusted −1.1 to +13.9. Add the robust finding that FCF does not cover dividends plus withholding in any scenario. |
| 3 GEM +18.9% / +12% | Yes as company claims | Yes | Overstates the scope. Add the "over the past year" period, the per-surface 5.8 / 4.1 / 1.6% and the several-thousand-GPU scale. |
| 4 Hyperion $46.03B max exposure; $27.3B Beignet | Yes | Yes | Fine. Optionally add the composition (RVG ~28 dominates) and that the figure is flat from Dec 2025. |
| 5 $278.99B leases + $68B July | Yes | Yes | Add that $81.65B of commitments fall due in 2027 and that the July leases start in 2027–28. That is the flexibility point. |
| 6 47.7× TTM FCF on Oct 16 | Yes | Yes | Fine. Note that Q3 results on 21 October will move the TTM denominator. |

## Your assessment

Meta's core business is comfortably profitable. In H1 2026 it generated $64B of operating cash, FoA earned $23.4B in Q2, it holds $90B of liquidity against $84B of covenant-free debt, and it is rated AA−. At the corporate level it is not overextended. The investment programme, though, has outrun self-funding. 2026 capex roughly equals operating cash flow. My sensitivities put FY FCF between about −$17B and +$14B, with the central cases near zero to +$10B. In every case, dividends and RSU withholding are debt-funded, and 2027 is locked in by $81.65B of commitments due that year plus 18–20 year leases starting in 2027–28. If the AI payoff disappoints, Meta shareholders lose first, through multiple compression at a 2.1% trailing FCF yield. Next come holders of the long SPV paper, through mark-to-market rather than default (Beignet reported near 91 cents; El Paso reportedly priced near junk-like yields). The external SPV equity holders (Blue Owl, BlackRock funds) come after that, but only if Meta walks away and the RVG shortfall payments fall short. Corporate bondholders are well covered. I differ from the note in three ways. First, I treat its upside FCF case as about $6B too generous. Second, I read the ad evidence as solid for "AI improves ad ranking" but nearly silent on the frontier/MSL share of capex. Third, I give more weight to 2027 rigidity and to management's own statement that it could resell compute. That statement is both the main hedge against stranded capacity and the clearest sign that capacity may run ahead of Meta's own demand.

## Front-page figures

`report/index.md` currently cites no Meta-specific figures. The figures below appear in `report/stack.md`. I did not find the −$17B to +$20B sensitivity on either page as of this review.

| Page / line | Figure | Still holds? | Comment |
|---|---|---|---|
| stack.md L20, L39 | Meta Q2 FCF $0.8B; "fell below $1B in a quarter" | Yes | 0.784. Superseded by Q3 results on 21 Oct. |
| stack.md L20, L73 | $279B uncommenced leases + $68B signed in July | Yes | Add "commencing 2027–28". |
| stack.md L20 | "the $46B Hyperion maximum exposure overlaps these" | Partly | Only the ~$12.3B lease component can overlap. The ~$28B RVG and ~$5.7B of equity and funding do not. |
| stack.md L73 | $349B non-cancellable commitments | Yes | $81.65B due in 2027 is the most decision-relevant slice. |
| stack.md L20, L73 | Meta $90B cash and securities | Yes | 90.26, excluding $10.80B restricted escrow; vs $84.0B debt face value. |
| stack.md L25 | RVG threshold ~$28B "roughly covers" $27.3B Hyperion bonds, so bondholders depend mainly on Meta's credit | Yes, with caveats | The threshold declines over time. Payment equals any fair-value shortfall, only on non-renewal or termination and "if certain other conditions are met". It is not a debt guarantee. |
| stack.md L73 | "ad metrics support AI-driven monetisation" | Directionally yes | Ads +27%, impressions +14%, price +12% (Q2). GEM figures are company measurements without baselines; per-surface uplifts are 1.6–5.8%. |
| (if used anywhere) | FY FCF −$17B to +$20B | No | Use −$17B to +$14B (flat-H2 low to cash-tax-adjusted seasonal high), until Q3 results. |

## Recommended edits

1. **Summary bullet 2, replace with:** "Against 2026 capex guidance of $130–145bn, repeating H1 operating cash flow in H2 implies FY FCF of −$16.8bn to −$1.8bn. Applying the FY2025 H2/H1 OCF ratio after removing the post-OBBBA fall in cash taxes (H1'25 $5.5bn, H2'25 $2.0bn) implies −$1.1bn to +$13.9bn. Scaling H2 revenue by the Q3 guide ($61–64bn) at H1's OCF margin implies −$8.5bn to +$10.1bn. In every case FY FCF falls short of dividends plus RSU tax withholding (~$22.8bn at the H1 rate), so that gap is funded by debt. These are sensitivities, not forecasts. Q3 results on October 21, 2026 will resolve half of H2." Cite [S6], [S8], [S10], [S23].
2. **Claim 41, add to the Value column:** "Unadjusted ratio is inflated by H2'25 cash taxes of 2.034 vs H1'25 5.544 (FY 7.578, 10-K); H1'26 cash taxes 1.999. Pre-tax-cash ratio 1.2379× gives H2 OCF 79.81 and FY FCF −1.10 to +13.90." Change the Summary and Signals rows to match.
3. **Summary bullet 3, replace with:** "On October 13, 2026, Meta reported that GEM delivered 18.9% conversion and 12% CTR improvements over the past year across ad surfaces, and 5.8%, 4.1% and 1.6% conversion uplifts on Facebook, Instagram and off-site for targeted users. GEM trains on 'several thousand' latest-generation GPUs. These company measurements, with no baseline or revenue bridge, support ad-ranking gains but say little about the frontier-model share of the $130–145bn build." Update claim 18 to match.
4. **Summary bullet 5, append:** "Of June's $349.31bn of non-cancellable commitments, $81.65bn is due in 2027, and the July leases commence in 2027–28 with 18–20 year terms. Management says plans are 'geared towards maximizing 2026 and 2027 capacity', so a 2027 cut would face contractual friction." Add a claim row citing [S10] and [S11].
5. **Analysis, "Scope and cash economics", add:** "On the July 29 call, management listed 'potentially selling compute directly' among enterprise opportunities and said Meta had 'quite a number of offers at a meaningful premium over what we paid for the compute'. The NYT reported on July 17 early talks to lease Anthropic up to $10bn of compute over two years (reported, unverified; no signed deal found through October 18). Resale optionality reduces stranded-capacity risk but also signals capacity that may exceed Meta's own near-term demand." Grade A for the call, C for the talks.
6. **Claim 29 / Financing paragraph, replace "Final closing was not independently verified" with:** "Bloomberg-syndicated reports (July 24–28) describe Sopaipilla Investor LLC notes of about $12.3–12.55bn due 2048, marketed at about T+287.5bp, with one report giving a ~7.5% yield and preliminary S&P A+ / Fitch AA−(EXP) ratings. Meta's own April 2036 notes priced at 5.25%. Reported, unverified (C) pending a pricing record." Add El Paso yield to Signals.
7. **Signals table, add rows:** "Q3 2026 results | due October 21, 2026, after close | [Q3 notice] | Replaces June figures and H2 sensitivities; first 2027 capex signal" and "2027 commitments | $81.65bn due 2027 | June 2026 | [S10] | Tests capex flexibility".
8. **Analysis, add after the funding paragraph:** "Property and equipment in payables and accruals rose from $9.33bn (December 2025) to $19.50bn (June 2026), so accrual-basis H1 investment ran roughly $10bn ahead of cash capex. H1 D&A rose 49.9% to $12.36bn." Grade A inputs, B difference.
9. **Financing paragraph, add the exposure breakdown:** "The $46.03bn maximum exposure (flat from $45.95bn in December 2025) is roughly the ~$28bn RVG threshold plus $12.31bn of leases, $2.92bn of equity and ~$2.8bn of estimated future funding (residual). Only the lease component can overlap with uncommenced leases." Then change `report/stack.md` L20 from "(the $46B Hyperion maximum exposure overlaps these)" to "(about $12B of the $46B Hyperion maximum exposure is lease commitments that overlap these; the ~$28B residual-value guarantee does not)".
10. **Settlement paragraph, add:** "Meta's own description also includes a non-algorithmic feed as a default option for teens in participating states, which bears directly on recommendation-driven engagement." Cite [S27].
11. **Summary bullet 1, append:** "Q2 operating income fell 8% year on year as reported (+9% excluding $2.40bn of legal charges and $1.18bn of severance)." Cite [S8] and [S11].

[Q2]: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/
[FY25]: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx
[Q2Q]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
[K25]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[CALL]: https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf
[GEM26]: https://engineering.fb.com/2026/10/13/ml-applications/generative-ads-model-gem-scaling-frontier-ads-ai/
[LEGAL]: https://about.fb.com/news/2026/08/agreement-with-state-attorneys-general-supporting-teens/
[PRICE]: https://chartexchange.com/symbol/nasdaq-meta/historical/
[Q3D]: https://s21.q4cdn.com/399680738/files/doc_news/Meta-to-Announce-Third-Quarter-2026-Results-2026.pdf
[ENG]: https://www.engadget.com/2217904/meta-is-reportedly-considering-a-multibillion-dollar-data-center-deal-with-anthropic/
[CAP]: https://capacityglobal.com/news/metas-12bn-el-paso-bond-exposes-ai-debt-repricing/
