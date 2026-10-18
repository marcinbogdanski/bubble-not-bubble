# OpenAI: independent Claude cross-check

*Reviewer: Claude (Opus 5.5), fresh context, first non-OpenAI reviewer of this note. Evidence cutoff and access date: 2026-10-18. Reviewed `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, `research/stack/openai.md` (version of 2026-10-17, after the Codex cross-check) and `reviews/openai-codex-xcheck.md`. I made 13 fetches (two returned HTTP 403) plus web searches. I did not edit the note.*

## Verdict

The figures in the note are accurate: all 12 re-verified rows match their sources and every calculation is numerically correct. The two problems are dating and basis: claim 4 is misdated, and the basis of the run-rate figures is unclear.
The real problem is balance. After two OpenAI-model passes the note piles up caveats in OpenAI's favour and leaves out the most direct funding-gap evidence: every new burn forecast has been worse than the last, the plan reportedly runs out of cash in 2028, the CFO reportedly warned about compute payments, and Anthropic's quarterly revenue has overtaken OpenAI's.
The central conclusion survives (real demand, unproven economics, contingent supplier exposure, no evidence of imminent default). But the Summary should state how large the gap is, in dollars and dates, and the $70bn/49.5% growth scenario should be replaced.

## Claim re-verification

These are the 12 rows the Summary and Analysis lean on most. "Your value" is what I found in my own fetch or search this session. Where the primary page blocked me, I say so and rely on the corroboration shown.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 3 | Sep run-rate ~$50bn; earlier $68–70bn includes partners' gross revenue; Q3 growth 77%, enterprise 107% | Reuters (Oct 8): "almost $50bn". The August "approaching $70bn" figure came from "an attempt to produce a direct comparison with figures from rival Anthropic". OpenAI, unlike Anthropic, does not count sales made through cloud partners. The 77%/107% growth rates trace only to CNBC (403 for me; secondary relay confirms). The FT says OpenAI's *direct* revenue grew >70% in Q3. Basis check: Q2 revenue of $6.7bn (≈$26.8bn annualised) × 1.77 ≈ $50bn, which is consistent with the growth being on the same direct basis. | [Reuters via MarketScreener][r-oct8]; [CNBC relay][cnbc-relay] | Yes. The $70bn was a pro-forma comparison basis, not a downward revision of OpenAI's own figure. | C (RU) |
| 4 | Year-end run-rate ≥$70bn; ≥$30bn raise at $1.4tn pre-money; "Oct 8, 2026" | The $30bn-at-$1.4tn talks were first reported **Sep 29** (Reuters citing Bloomberg): "not including the money raised", early stage, MGX up to $10bn. That report said the run-rate was "nearing $70bn, up more than 70% since the start of the third quarter". The ≥$70bn year-end target was reported **Oct 9** (Bloomberg). That report does not say which basis the target uses. | [Reuters, Sep 29][r-sep29]; [Bloomberg via Investing, Oct 9][b-oct9] | Figures match; **date wrong** for the funding talks. Earlier, Sep 18 Reuters/FT reported talks at ~$1.2tn. | C (RU) |
| 5 | 2024 revenue $3.7bn, attributable loss $5.09bn; 2025 revenue $13.07bn, operating loss $20.92bn, attributable loss $38.53bn | Same. The note leaves out: 2025 **consolidated net loss $60.35bn**, including a $41.55bn fair-value change on convertible interests and warrants; 2024 operating loss $8.78bn; 2025 R&D $19.18bn (147% of revenue); total 2025 costs $34bn. The source reports end-2025 assets of "just over $50bn, with almost half of that in cash" (≈$25bn), which conflicts with the $40bn in claim 41 unless that figure includes securities. | [Zitron][zitron]; [PYMNTS][pymnts] | Yes | C (RU); the reported FT verification does not make our access primary |
| 7 | Feb-2026 burn forecast: 2026 $25bn, 2027 $57bn, 2028 $85bn, 2029 $51bn, 2030 +$39bn | Same. The same table gives the Q1-2025 and Q3-2025 forecast vintages, which the note leaves out (see Arithmetic). Training compute: 2026 $32bn, 2027 ~$65bn, ~$440bn through 2030. Revenue forecasts: 2026 $30bn, 2027 ~$62bn. | [The Decoder][decoder] | Yes | C (RU) |
| 8 | 2026–30 FCF −$278bn; compute $856bn; revenue $840bn; $36bn→$350bn | Same. Reuters/FT also say OpenAI "is on track to exhaust that cash [the $122bn round] by 2028". **The note leaves this out.** | [Reuters/FT, Sep 18][r-sep18]; [dispute][dispute] | Yes, but material context is missing | D for the plan as contested. The 2028 exhaustion date also follows from the C-grade Feb vintage (see Arithmetic), so the direction does not depend on the disputed deck alone. |
| 9 | Adjusted gross margin 33% (2025) vs 40% (2024), 46% target; future 52–67% | Same. The source adds that the 52–67% range "miss[es] the previous goal of 70% by 2029" and that inference cost "quadrupled in 2025". | [The Decoder][decoder] | Yes | C (RU) |
| 13 | $122bn committed, $852bn post-money; ~$4.7bn undrawn revolver | The OpenAI page returned 403. Secondary coverage confirms $122bn "committed capital" at $852bn post-money, closed Mar 31. That coverage notes the round was $110bn at $730bn in February, so it grew. I could not independently reconfirm the revolver; Codex verified it from the release. | [Yahoo, Apr 28][yahoo-apr28]; [Codex xcheck](/reviews/openai-codex-xcheck) | Yes (revolver via Codex) | A |
| 18 | Dec RPO $625bn, ~45% OpenAI ≈ $281bn; June 41.5% if unchanged | 45% of $625bn is confirmed by multiple reports of the Q2 FY26 call. The rest of RPO (~$350bn) grew 28%. Q3 (Mar) RPO was $627bn. | [Constellation][constellation]; [The Register][register] | Yes | A for the 45% statement; B for the dollar estimate; conditional calculation for June |
| 19 | FY26 Microsoft revenue from OpenAI $24.1bn; receivable $6bn; $13bn committed / $11.9bn funded; ~25% stake | Same, quoted directly. Microsoft uses HLBV equity-method accounting. The dilution gains are cross-referenced to note 3 (the $6.5bn is not in R11). | [Microsoft 10-K R11][ms-r11] | Yes | A |
| 22 | Nvidia $105bn cap, 4.25GW, 20-year leases; tenant-default triggers | Consistent across reporting of the filing. These are **residual value guaranties** with SB Energy (a SoftBank affiliate). They pay the shortfall between guaranteed lease value and recoveries. They **fall away if OpenAI achieves a satisfactory credit rating**, and OpenAI must reimburse Nvidia. The WSJ had earlier reported talks of ~$250bn. | [Unite.AI / TNW summaries of filing][nv-sum]; [Codex: 10-Q note 10](/reviews/openai-codex-xcheck) | Yes. The note leaves out the credit-rating fall-away and SoftBank's landlord role. | A |
| 42 (with 28, 36) | ≥$80bn funded by Oct 1: Amazon $50bn ($28.7bn by June + $21.3bn after) + SoftBank $30bn | SoftBank: the $10bn third tranche completed Oct 1. The 2026 follow-on totals $30bn, cumulative $64.6bn, ~13% stake, funded by foreign-currency senior notes announced Sep 24. The $40bn bridge was repaid and its undrawn $10bn cancelled Sep 30. Amazon: the 10-Q split (15 + 13.7 + 21.3) is confirmed by secondary relay. | [SoftBank, Oct 1][softbank]; [Odaily relay of Amazon 10-Q][amzn-relay] | Yes. 50 + 30 = 80. | A components; B sum |
| 41 | Cash and securities $73bn at Mar 31 vs $40bn at Dec 31 | Same (PYMNTS citing The Information). Decoder gives "roughly $40bn in cash and cash equivalents" at end-2025. Zitron's "almost half" of ~$50bn assets (~$25bn) is a basis conflict the note should record. | [PYMNTS][pymnts]; [Decoder][decoder]; [Zitron][zitron] | Yes | C (RU) |

## Arithmetic checks

I recomputed every derived figure in the Analysis and in claims 2, 14, 18, 27–29, 39, 40, 42, 44 and 51. **All are numerically correct.** Specifically:

- **Claim 2:** 2 × 12 = 24.
- **Claim 14:** 26 + 27 + 47 = 100. $130bn / 26% = a $500bn implied valuation, consistent with the October 2025 secondary sale.
- **Claim 18:** 625 × 0.45 = 281.25, and 281.25 / 678 = 41.48%.
- **Claims 27, 28, 42:** 38 + 100 = 138; 28.7 + 21.3 = 50; 50 + 30 = 80.
- **Claim 29:** 1,004.571 − 86.327 = 918.244.
- **Claim 39:** 300 / 5 = 60, and 60 / 50 = 120%. Gross profit 50 × 0.33 = 16.5 and 70 × 0.33 = 23.1. Training hurdle 32 / 0.33 = 96.97.
- **Claim 40:** 70 × 1.25⁴ = 170.9; 70 × 1.5⁴ = 354.4; 5^¼ − 1 = 49.5%; (350/36)^¼ − 1 = 76.6%; 852 / 50 = 17.04.
- **Claim 44:** 1.05 / 3.7 = 28.38%, and 5.57 / 13.07 = 42.62%.
- **Claim 51:** 32 / 0.52 = 61.54, and 32 / 0.67 = 47.76.

My concerns are about framing, not computation.

**1. The funding-gap illustration (claim 39) is indirect, and the direct version is missing.** Claim 39 compares an average Oracle bill with the run-rate and computes a training "hurdle". Neither tells the reader whether the cash runs out. With the note's own inputs:

| Step | Calculation | Result | Grade |
|---|---|---|---|
| Resources (upper bound) | End-2025 cash ~$40bn (claim 41) + $122bn round if fully funded (claim 13); the round closed after Dec 31, so no double count | **$162bn** | C + A |
| Feb-vintage burn 2026–28 | 25 + 57 + 85 | **$167bn**, exceeding resources during 2028. This matches Reuters/FT's "exhaust that cash by 2028". | C |
| Feb-vintage peak need 2026–29 | 25 + 57 + 85 + 51 | $218bn, so ~$56bn must be raised before the forecast turns positive in 2030 | C |
| Sep plan 2026–30 | 278 − 162 | **~$116bn** external funding needed after the $122bn round; ~$86bn if the ≥$30bn round in talks closes | D |

This is the funding gap in its plainest form. It does not depend on margin definitions, and the note should state it.

**2. The burn forecast has worsened in every vintage. The note shows only one vintage.** Here is cumulative 2026–30 net cash flow by forecast vintage:

| Vintage | Inputs | Net 2026–30 | Source |
|---|---|---|---|
| Q1 2025 | −8 − 20 − 11 + 12 + 41 | **+$14bn** | [Decoder][decoder], C |
| Q3 2025 | −17 − 35 − 47 − 8 + 38 | **−$69bn** | [Decoder][decoder], C |
| Feb 2026 | −25 − 57 − 85 − 51 + 39 | **−$179bn** | [Decoder][decoder], C |
| Sep 2026 plan | — | **−$278bn** (disputed) | [Reuters/FT][r-sep18], D |

Cross-check: the 2024–30 totals differ by 189 − 80 = $109bn between the Q3-2025 and Feb-2026 vintages. That matches the Decoder's "$111bn" increase, within the table's rounding. The pattern (each vintage adds roughly $80–110bn of burn) is the strongest overextension evidence about OpenAI in the record, and the note leaves it out.

**3. Claim 40's "$70bn CY2026 annual sales" base contradicts the note's own data.** H1 2026 revenue was $5.7bn + $6.7bn = $12.4bn (claims 2, 6). Full-year sales of $70bn would need $57.6bn in H2, 4.6× H1. On the other side, the plan's $36bn needs $23.6bn in H2 (~$11.8bn a quarter). That fits a ~$50bn exit run-rate ($12.5bn a quarter), which also cross-validates the $50bn basis. So the 25%/50% paths and the "49.5% CAGR" start from a year-zero that cannot happen. They flatter the required growth. If $70bn is treated as a **2027** base, reaching $350bn in 2030 needs 5^⅓ − 1 = **71.0%** a year, close to the plan's 76.6%. Replace the scenario.

**4. Microsoft's billings to OpenAI are about equal to OpenAI's revenue over overlapping periods.** The note dismisses the comparison because the periods differ. But overlapping periods can be built from the note's own rows. OpenAI revenue for Jul 2025–Jun 2026 = (13.07 − 4.3) + 5.7 + 6.7 = **$21.2bn** (C). Microsoft's FY26 revenue from OpenAI, at $24.1bn (A), is **114%** of that. Removing a revenue share of up to ~20% of OpenAI revenue (historically reported, unverified, ~$4.2bn) still leaves ~$19.9bn, **~94%** of OpenAI's revenue going to one supplier. This is B/C derived arithmetic. It is a stronger statement of supplier dependence than anything currently in the note.

**5. Other derived figures worth adding.**
- **Receivable days:** 6.0 / 24.1 × 365 ≈ **91 days** of Microsoft billings outstanding at Jun 30 (B; revenue-share timing affects this).
- **Valuation per dollar of revenue is rising:** $1.4tn pre-money in talks / $50bn ≈ **28×** (20× on the $70bn year-end target), against the note's 17× at the March price.
- **Named cloud contracts:** the four contracts with *distinct* providers sum to 300 + 250 + 138 + 22.4 = **~$710bn** nominal. They do not double-count each other; the overlap the note warns about is with the chip and Stargate headlines. That is ~14× the September run-rate and ~83% of the plan's $856bn 2026–30 compute line, although contract terms run past 2030. Grades: Oracle C; the others A.
- **Training hurdle in the right year:** the 2027 training forecast is ~$65bn, so the hurdle is $197bn at 33% and $125bn–$97bn at 52–67%, against a forecast 2027 revenue of ~$62bn (Feb vintage).
- **Oracle in the right year:** $60bn a year against 2027 forecast revenue of ~$62bn is ~97%, a same-period comparison. The current comparison is with a 2026 run-rate.

## Omissions

From the last 30 days (Sep 18 – Oct 18):
1. **Cash exhaustion by 2028** (Reuters/FT, Sep 18), as above. Material: it gives a date to the funding gap. C/D.
2. **The funding talks are a bridge in place of an IPO.** Reuters (Sep 29): the ≥$30bn round "would serve as a bridge… in place of an IPO", and Altman said OpenAI "would not go public in 2026, citing safety concerns". So OpenAI is raising at a higher price (~$1.2tn on Sep 18, ~$1.4tn by Sep 29) after the run-rate basis correction. [r-sep29], [r-sep18]. C.
3. **Anthropic overtook OpenAI in quarterly revenue.** Q2 was $11.5–11.6bn against OpenAI's $6.7bn (Reuters, Oct 8). Anthropic reported Q3 at $16.8bn with an adjusted profit (Reuters/FT, Oct 14–16; repo [signals 2026-10-17](/signals/2026-10-17), item 14). The bases differ: Anthropic counts gross partner sales, roughly half its revenue, with ~16% paid to partners. But the direction is not in doubt, and the note's only competitive datum is a 2025 Menlo estimate. C (RU).
4. **A counterweight on the other side.** OpenRouter reported OpenAI regaining the lead in weekly model spend (week of Sep 7–13) for the first time in 2.5 years, after the Astra launch. This covers OpenRouter traffic only. Primary for that platform; not representative of total API share. [OpenRouter coverage][openrouter].
5. **Counterparties are under credit stress.** The note says it records no OpenAI-wide default, which is correct. But by mid-October: CoreWeave 5-year CDS hit an intraday 1,194.5bp (Oct 15); Oracle CDS was ~288–300bp; Stargate-linked project loans were quoted ~88–94¢ (FT, Oct 15) and Jupiter loans 89–91¢ (Sep 18). CoreWeave has also just disclosed ineffective disclosure controls (repo research commit). Lenders spent more than six months syndicating the $38bn Vantage/Oracle Stargate construction loan (Bloomberg, C). These are the "credit reserves / failed funding" warning channels the note itself names. Sources: [signals 2026-10-18](/signals/2026-10-18-market-views), items C7, P8–P10; [Vantage loan][vantage].

Older but material:

6. **The CFO's own reported warning** (WSJ via Reuters, Apr 27, 2026). Friar reportedly told leaders OpenAI "might not be able to pay for future computing contracts if revenue doesn't grow fast enough". OpenAI missed several monthly revenue targets "after losing ground to Anthropic in coding and enterprise markets" and missed its 1bn weekly-user goal for end-2025. Altman/Friar: "This is ridiculous. We are totally aligned on buying as much compute as we can." The note quotes Friar on guarantees (2025) but not this. C (RU); the denial must be recorded alongside it. [Reuters/WSJ][r-apr27].
7. **SoftBank's leverage on OpenAI shares.** SoftBank sought a $10bn two-year margin loan secured on its OpenAI stake. It was cut to ~$6bn in May when lenders balked at valuing an unlisted stake, then revived in July with a SoftBank corporate guarantee; closing is unverified. Add this to the $40bn bridge and the Sep 24 senior notes. SB Energy, a SoftBank affiliate, is also the landlord under Nvidia's guarantee. SoftBank's exposure is therefore equity + secured borrowing + landlord, and its collateral value depends on OpenAI's private mark (13% × $852bn ≈ $111bn against $64.6bn cost). That is a reflexive channel; "SoftBank must service its own debt" understates it. [Bloomberg][sb-margin], [SoftBank][softbank]. C for the loan; A for the bridge and notes.
8. **The $60.35bn 2025 consolidated net loss, and 2025 R&D of $19.18bn > revenue.** The note says attributable loss "differs from consolidated net loss" but never gives the number. C (RU).
9. **The Nvidia guarantee falls away on a satisfactory OpenAI credit rating** (residual value guaranty). This is mildly favourable, because exposure shrinks if OpenAI's credit improves, and it is missing from claims 22/50.

## Summary-bullet assessment

| Bullet | Supported by the note's evidence? | Concrete enough? |
|---|---|---|
| 1. 1.2bn weekly users; profitability not established | Yes | Half. Users are dated and quantified, but the loss side has no figure. Add the 2025 operating loss of $20.9bn on $13.1bn revenue (RU). |
| 2. ~$50bn vs $68–70bn; 77% Q3 growth | Yes (C) | Yes. It could say the $70bn was an Anthropic-comparable pro-forma basis, and that Anthropic's Q2 revenue exceeded OpenAI's. |
| 3. $25bn 2026 burn; plan disputed; gap "depends on margins and cost definitions" | Partly. The last clause is not what the note's own data show. The gap exists under every vintage since Q3 2025, whatever the margin definition. | **No.** It is the vaguest bullet and the most important one. It needs the vintage drift, the $162bn vs $167bn/$278bn arithmetic, and the 2028 exhaustion date. |
| 4. $122bn/$852bn; ≥$80bn funded by Oct 1 | Yes (A/B) | Yes |
| 5. Overlaps; Nvidia $105bn guarantee vs LOI | Yes | Useful, but it only says what is *not* a liability. Add the ~$710bn of distinct-provider cloud contracts as a nominal scale anchor. |
| 6. Foundation control; $6bn receivable | Yes (A) | Moderately. The $6bn receivable is a weak illustration; Microsoft billings ≈ ~94–114% of OpenAI's overlapping-period revenue shows the dependence better. |
| 7. Unresolved payment-timing question | Yes, as a gap | It is a question rather than a finding. Acceptable as the last bullet, but it should not sit in place of the bullet-3 arithmetic. |

## Your assessment

OpenAI has demonstrable and growing demand. Direct run-rate went from ~$28bn to ~$50bn in Q3, weekly users reached 1.2bn, and it has regained share on OpenRouter. It has also raised more equity than any private company in history, and at least $80bn of that is confirmed received. On those facts the note is right that imminent insolvency is unsupported. Where I differ is on the financing judgement. Every forecast vintage since early 2025 has moved cumulative 2026–30 cash flow down by roughly $80–110bn. On OpenAI's own February numbers, which are not the disputed deck, the end-2025 cash plus the entire $122bn round is gone during 2028. Within one quarter OpenAI went back to market at a 28× run-rate multiple as a bridge in place of an IPO. Its CFO reportedly warned about compute payments. One supplier bills it roughly what it earns. Its main counterparties' credit is now pricing stress. That is a company whose solvency depends on continuous capital-market access at rising valuations: in the methodology's terms, a high-fragility, financing-dependent node, not merely an "opaque growth company". The note avoids saying this. The original Codex note and the Codex cross-check each stated a true caveat: margins are definition-dependent, receipts are real, caps are not expected losses. Together those caveats push the Summary towards what the gap is *not*, without ever saying what it *is*. A same-vendor reviewer was likely to accept that tone. In the other direction, the note is slightly harder than warranted in treating the $50bn print as a "correction": Reuters says the $70bn was a pro-forma Anthropic-comparable figure, not a restatement of OpenAI's own basis. I would rate the probability of a disorderly funding event lower than the gap arithmetic alone suggests, because the investor base is deep and strategic. But the note should state the gap in dollars and years and let the caveats qualify it.

## Recommended edits

1. **Claim 4:** change "Oct 8, 2026" to "Funding talks reported Sep 29, 2026 (Reuters citing Bloomberg; ~$1.2tn reported Sep 18); year-end ≥$70bn target reported Oct 9, 2026, basis (direct vs Anthropic-comparable) not stated". Add the Sep 29 Reuters source: https://www.investing.com/news/stock-market-news/openai-targets-30-billion-funding-at-14-trillion-valuation-bloomberg-news-reports-4923324

2. **Claim 3:** append "Reuters says the August 'approaching $70bn' figure was produced for comparison with Anthropic, which counts cloud-partner sales; OpenAI's own basis excludes them. FT reports direct revenue grew >70% in Q3; Q2 $6.7bn (≈$26.8bn annualised) × 1.77 ≈ $50bn, consistent with growth on the direct basis."

3. **Claim 8:** append "Reuters/FT also report OpenAI is on track to exhaust the $122bn round's cash by 2028; talks at ~$1.2tn."

4. **Add claim 52 (forecast-vintage drift):** "Cumulative 2026–30 net cash flow by forecast vintage: Q1-2025 +$14bn; Q3-2025 −$69bn; Feb-2026 −$179bn; Sep-2026 plan −$278bn (disputed). Author arithmetic from [Decoder] table and [Reuters/FT]. Grade C (D for Sep plan)."

5. **Add claim 53 (direct funding gap):** "Resources upper bound $162bn (≈$40bn end-2025 cash RU + $122bn committed round). Feb-vintage burn 2026–28 $167bn exceeds this during 2028; 2026–29 peak need $218bn. Sep plan $278bn implies ~$116bn further external funding needed (≈$86bn if a $30bn round closes). Not a cash-flow statement; assumes the full round funds." Grade "C inputs; D for plan variant". Replace the first sentence of the Analysis paragraph that begins "Oracle's illustrative $60bn…" with this.

6. **Replace claim 40's scenario:** drop the "$70bn CY2026 annual sales" base and the 25%/50%/49.5% figures. Replace with: "H1 2026 revenue was $12.4bn (claims 2, 6), so full-year 2026 cannot approach $70bn; the plan's $36bn is consistent with a ~$50bn exit run-rate. Treating $70bn as a 2027 base, $350bn in 2030 requires 71.0% annual growth; from the plan's $36bn 2026 base, 76.6%." Keep the 17.0× figure and add: "the ≥$30bn round discussed at $1.4tn pre-money would be ~28× the September run-rate."

7. **Add claim 54 (supplier dependence):** "OpenAI revenue Jul 2025–Jun 2026 ≈ (13.07 − 4.3) + 5.7 + 6.7 = $21.2bn (RU); Microsoft FY26 revenue from OpenAI $24.1bn (A) = 114%; ≈94% after removing a revenue share of up to ~20% (historically reported, unverified). Receivable $6bn ≈ 91 days of billings." Grade B/C derived. In the Analysis sentence "they are not a pure inference bill", add "but over overlapping periods they are roughly equal to OpenAI's total revenue".

8. **Add claim 55 (CFO warning):** "WSJ (Apr 27, 2026, via Reuters): Friar told leaders OpenAI 'might not be able to pay for future computing contracts if revenue doesn't grow fast enough'; OpenAI missed several monthly revenue targets after losing ground to Anthropic in coding/enterprise, and missed its 1bn weekly-user goal for end-2025. Altman/Friar: 'This is ridiculous. We are totally aligned on buying as much compute as we can.'" Grade C (RU). Source: https://www.marketscreener.com/news/openai-falls-short-of-revenue-and-user-targets-as-it-races-toward-ipo-wsj-reports-ce7f59dddc8ff624

9. **Add claim 56 (competition, both directions):** "Anthropic's reported Q2 revenue $11.5–11.6bn exceeded OpenAI's $6.7bn for the first time (Reuters, Oct 8); Anthropic Q3 $16.8bn reported (Oct 14–16). Bases differ: Anthropic counts gross partner sales (~half its revenue, ~16% paid to partners). Separately, OpenRouter reported OpenAI regained the weekly-spend lead in the week of Sep 7–13, 2026, for the first time in 2.5 years (platform traffic only)." Grade C. In Analysis, replace "Consumer leadership can coexist with enterprise competition" with "Consumer leadership coexists with an enterprise revenue lead for Anthropic, which reportedly overtook OpenAI's quarterly revenue in Q2 2026 on a different gross basis; platform data show OpenAI regaining API spend share after the Astra launch."

10. **Extend claims 5 and 41:** add to claim 5 "2025 consolidated net loss $60.35bn incl. $41.55bn fair-value change on convertible interests/warrants; 2025 R&D $19.18bn; 2024 operating loss $8.78bn". Add to claim 41 "Conflict: the same leak reports end-2025 assets 'just over $50bn, almost half in cash' (~$25bn), versus ~$40bn cash and securities reported by The Information; likely a cash vs cash-plus-securities basis difference, unreconciled."

11. **Extend claims 22/50:** "Residual value guaranties with SB Energy (SoftBank affiliate); obligations fall away if OpenAI achieves a satisfactory credit rating, terminates a lease, or at year 20."

12. **Extend claim 36 and the loss-bearing paragraph:** replace "SoftBank must service its own debt" with "SoftBank financed its 2026 follow-on with a $40bn bridge (repaid/cancelled by Sep 30) and Sep 24 senior notes, and sought a $10bn margin loan secured on its OpenAI shares (cut to ~$6bn in May, revived in July with a SoftBank guarantee; closing unverified). Through SB Energy it is also landlord under Nvidia's guarantee. Its exposure is equity, secured borrowing and lease credit, with collateral valued at OpenAI's private mark (13% × $852bn ≈ $111bn vs $64.6bn cost)."

13. **Add to Signals:** "Counterparty credit | CoreWeave 5y CDS intraday 1,194.5bp (Oct 15); Oracle ~288–300bp; Stargate-linked project loans ~88–94¢ | Oct 2026 | [signals 2026-10-18](/signals/2026-10-18-market-views) C7, P8–P10 | The 'credit reserves / failed funding' channel the note names as its first warning."

14. **Replace Summary bullet 1:** "On September 29, 2026, OpenAI reported 1.2bn weekly users, yet leaked 2025 accounts show a $20.9bn operating loss on $13.1bn revenue (RU); public evidence does not establish profitability after research and corporate costs (claims 5–9, 45)."

15. **Replace Summary bullet 3:** "Each burn forecast has been worse than the last: cumulative 2026–30 cash flow went from +$14bn (Q1 2025 vintage) to −$179bn (Feb 2026) and a disputed −$278bn (Sep 2026). On the February numbers, end-2025 cash (~$40bn) plus the full $122bn round runs out during 2028, as Reuters/FT report; a ≥$30bn bridge round at $1.4tn pre-money is in talks (RU). In April the CFO reportedly warned compute contracts might become unaffordable without faster growth, which she and Altman denied (claims 7–8, 52–53, 55)."

16. **Replace Summary bullet 5:** "Cloud contracts with four distinct providers total ~$710bn nominal (Oracle $300bn RU, Azure $250bn, AWS $138bn, CoreWeave $22.4bn), ~14× the September run-rate; chip plans and Stargate overlap these and are not additive. Nvidia's August 2026 $105bn residual-value guarantee is contingent credit support, not cash (claims 16, 20–31, 50)."

17. **Replace Summary bullet 6:** "The Foundation controls OpenAI Group PBC. Supplier dependence is high: Microsoft's FY26 revenue from OpenAI ($24.1bn) roughly equals OpenAI's own revenue for the overlapping twelve months (~$21bn, RU), with a $6bn receivable at June 30, 2026 (claims 14, 19, 54)."

18. **Update the Conflicts "Burn versus liquidity" bullet** so the gap arithmetic of claim 53 is stated first and the receipts/liquidity counterweight second. Keep "imminent insolvency is unsupported", and add "but solvency through 2028 depends on raising further capital under every reported forecast vintage since Q3 2025."

[r-oct8]: https://uk.marketscreener.com/news/openai-s-september-annualized-revenue-nears-50-billion-less-than-previously-indicated-source-says-ce785ddfdf8bff23
[cnbc-relay]: https://primexbt.com/news/nvidia-oracle-and-coreweave-fall-as-openais-real-revenue-trails-earlier-reports/
[r-sep29]: https://www.investing.com/news/stock-market-news/openai-targets-30-billion-funding-at-14-trillion-valuation-bloomberg-news-reports-4923324
[b-oct9]: https://www.investing.com/news/stock-market-news/openai-expects-to-reach-70-bln-revenue-by-end2026-bloomberg-reports-4940179
[zitron]: https://www.wheresyoured.at/exclusive-openai-financials/
[pymnts]: https://www.pymnts.com/news/artificial-intelligence/2026/openai-ran-through-4-billion-dollars-q1/
[decoder]: https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/
[r-sep18]: https://www.marketscreener.com/news/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports-ce785adade89f226
[dispute]: https://www.theinformation.com/briefings/openai-said-forecast-nearly-280-billion-cash-burn-end-2030
[yahoo-apr28]: https://finance.yahoo.com/markets/article/oracle-coreweave-back-openai-after-report-says-chatgpt-developer-missed-sales-user-targets-130600514.html
[constellation]: https://www.constellationr.com/index%2Ephp/insights/news/microsoft-q2-strong-azure-growth-39-openai-45-rpo
[register]: https://www.theregister.com/2026/01/29/microsoft_earnings_q2_2026/
[ms-r11]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R11.htm
[nv-sum]: https://www.unite.ai/nvidia-guarantees-up-to-105b-for-8-gw-ohio-ai-campus-leased-by-openai/
[softbank]: https://group.softbank/en/news/press/20261001
[amzn-relay]: https://www.odaily.news/en/newsflash/505747
[openrouter]: https://aiweekly.co/alerts/openai-retakes-openrouter-weekly-spend-lead-after-25-years
[vantage]: https://aiweekly.co/alerts/banks-still-working-off-oracles-38b-ai-data-center-loan
[r-apr27]: https://www.marketscreener.com/news/openai-falls-short-of-revenue-and-user-targets-as-it-races-toward-ipo-wsj-reports-ce7f59dddc8ff624
[sb-margin]: https://www.bloomberg.com/news/articles/2026-04-23/softbank-seeks-10-billion-margin-loan-backed-by-openai-shares
