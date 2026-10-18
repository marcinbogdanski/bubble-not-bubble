# Claude cross-check: Amazon

*Review date: 2026-10-18. Reviewer: Claude (Anthropic), fresh context, first Claude-side reviewer of `research/stack/amazon.md` (written by Codex, corrected once after the [Codex cross-check](/reviews/amazon-codex-xcheck)). Read first: `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, `tasks/CLAUDE_XCHECK_BRIEF.md`. 13 fetches (all primary except one Reuters syndication), 5 web searches, all on 2026-10-18. Only this file was written. Disclosure: the reviewer is an Anthropic model, and Anthropic is Amazon's largest disclosed AI counterparty. The findings below on Anthropic marks and concentration lean against Anthropic-flattering readings, not toward them.*

## Verdict

Every load-bearing figure I re-fetched matches the primary filings exactly. No arithmetic error, and every front-page figure taken from this note still holds as a dated figure.
The note and the Codex review both miss two things. Most of the H1 2026 backlog growth coincides with contracts from the two labs Amazon is funding. And investment marks dominate Q2 earnings: 66% of pre-tax income was non-operating.
The conclusion survives: profitable AWS, externally funded build, no solvency question. The lab-concentration and earnings-quality points should be added. So should management's explicit under-three-year server payback claim, which is the strongest pro-return evidence and is missing.

## Claim re-verification

$bn unless stated. "Mine" values are from documents fetched 2026-10-18.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 10 | June TTM OCF 161.403 / net capex 169.007 / FCF −7.604 | 161,403 / 169,007 / (7,604) $m; gross purchases 173,028 less incentives 4,021 | [Q2 10-Q][Q226] FCF reconciliation; XBRL company facts | Yes | A |
| 11 | June TTM FCF less finance-lease and financing-obligation principal −9.511 | TTM principal 1,599 and 308 $m: −7.604−1.599−0.308 = −9.511 | [Q2 10-Q][Q226] cash-flow statement | Yes | B (derived) |
| 13 | 2026 cash capex ~$200bn → ~$220bn, memory cited | Jassy: "approximately $220 billion in cash CapEx in 2026. The higher cost of memory pushing this number up from our prior estimate of about $200 billion." (The Fool's editorial summary adds "increased capacity requirements"; the spoken quote names memory only.) | [Call transcript][CALL] | Yes | A (attributed) |
| 14 | AWS Q2 revenue 42.232, +37%, OI 16.621, margin 39.4% | 42,232 vs 30,873 $m (+36.79%); OI 16,621 → 39.36%; CEO says 36.7% | [Q2 10-Q][Q226] segment table; [call][CALL] | Yes | A; B for computed growth |
| 40 | ~38.1% ex energy derivative (from 650/520 bp) | The 10-Q quantifies the effect: net unrealized energy-contract gains of $551m in Q2 2026, in "Technology and infrastructure", "primarily impacting our AWS segment". (16,621−551)/42,232 = 38.05% | [Q2 10-Q][Q226] derivatives note | Yes; now primary-sourced, not just rounded speech | B (A inputs) |
| 15 | Backlog 244/4.1y → 364/5.5y → 496/6.4y | Same three filings, same values | [10-K][K25], [Q1 10-Q][Q126], [Q2 10-Q][Q226] | Yes | A |
| 19 | Anthropic $18bn funded; $15bn remaining facility, delivery-contingent | $8.0bn notes (Q3 2023–Q4 2025) + $5.0bn Series G + $5.0bn Series H (the 10-Q says "$10.0 billion in Anthropic nonvoting preferred stock" in Q2); facility "not to exceed $20.0 billion", reduced to $15.0bn; amounts become drawable "as we reach certain delivery milestones of compute capacity"; expires 30 months after an Anthropic liquidity event | [Q2 10-Q][Q226]; [Anthropic, Apr 20][ANT] | Yes | A components; B sum |
| 21 | Q2 2026 $50.5bn preferred-stock repricing gain within $53.4bn other income | "upward adjustments of approximately $50.5 billion in Q2 2026 and $62.8 billion for the six months … to our nonvoting preferred stock"; other income $53,415m | [Q2 10-Q][Q226] | Yes. It is a Level 3 unrealized mark, not a realized gain | A |
| 25 | OpenAI $28.7bn through June + $21.3bn after = $50bn | "$28.7 billion … for the six months ended June 30, 2026, including $13.7 billion invested in Q2"; "Subsequent to June 30, 2026, we invested the remaining $21.3 billion Commitment Amount" | [Q2 10-Q][Q226] | Yes | A; B sum |
| 28 | H1 long-term-debt proceeds $66.998bn | 66,998 $m (Q1 53,441 + Q2 13,557); TTM 81,925 | [Q2 10-Q][Q226]; XBRL | Yes | A |
| 29 | July $25bn incl. $0.75bn FRN; proceeds ~$24.867bn; 4.60–6.25%; 2029–2066 | Tranches 0.75+3.5+4.25+3.0+4.5+2.75+4.0+2.25 = 25.0; offering price $24.923bn; net proceeds ~$24.867bn | [July 8-K][DEBT] | Yes | A; B sum |
| 30 | June liquidity 123.0; debt face 132.995; uncommenced leases 137.214 | $123.0bn (the same figure as at Dec 31, 2025); 132,995; 137,214 $m | [Q2 10-Q][Q226] | Yes | A |

Also re-checked and matching: claim 9 (2024/2025 OCF 115,877/139,514, gross purchases 82,999/131,819 via XBRL; net figures reconcile using incentives of 5,341/3,499). Claim 12 (H1 OCF 71,419; purchases 98,411 less 2,101; investments 39,767). Claim 20 (92.5 + 97.9). Claims 21 and 41 (2025 $5.6bn reclassification and $7.7bn upward adjustments, 10-K). Claim 22 (Anthropic page: ">$100 billion over the next ten years", "up to 5 gigawatts", "nearly 1GW … by the end of 2026", "over one million Trainium2 chips"). Claim 23 (Reuters Oct 14: Q3 $16.8bn vs Q2 $11.6bn, "profitable … on an adjusted basis", no figure given). Claim 26 (six → five years for a subset, 10-K). Claim 35 (£1.25+1+1+1 = £4.25bn; offering price £4.242bn; proceeds ~£4.235bn). Claim 42 (DDTL: single draw up to $17.5bn "on or prior to September 30, 2026"; undrawn at June 30).

## Arithmetic checks

All of these pass. The Codex review already reproduced the CSV and quarterly bridge; I re-checked only what the Analysis and front page rely on.

- **AWS margin**: 16,621/42,232 = 39.36% → 39.4%. Ex energy derivative, by the note's method: 39.4 − (6.5 − 5.2) = 38.1%. By the 10-Q dollar figure: 16,070/42,232 = 38.05%. Both agree.
- **AWS share of net PP&E additions**: 90,120/118,648 = 75.95% → 76.0%.
- **Anthropic**: 8 + 5 + 5 = 18; 20 − 5 = 15; carrying value 92.5 + 97.9 = 190.4.
- **OpenAI**: 15.0 (Q1, implied) + 13.7 = 28.7; 28.7 + 21.3 = 50.0.
- **FCF chain**: 161.403 − 169.007 = −7.604; −7.604 − 1.599 − 0.308 = −9.511. H1: 71.419 − (98.411 − 2.101) = −24.891.
- **Valuation (claim 31)**: 250 × 10.783 = 2,695.75bn; ÷ 161.403 = 16.70× OCF; 4% × 2,695.75 = 107.83.
- **Backlog increments (not computed in the note; used under Omissions)**: 364 − 244 = 120 (Q1); 496 − 364 = 132 (Q2); H1 total 252.

The note has no arithmetic errors. One wording issue: claim 14 says the computed growth is "36.8%". That is right (36.79%), but the Conflicts bullet calls 36.7% "the CEO quotation" and 36.8% "the published revenue amounts". Fine as written.

## Omissions

1. **The backlog growth comes mostly from the two labs Amazon is financing. Primary inputs (A); attribution is inference (C).** Backlog rose $120bn in Q1 2026, the quarter of the $100bn OpenAI expansion (Feb 27). It rose $132bn in Q2, the quarter of Anthropic's >$100bn commitment (Apr 20). The 10-Q names both deals inside its backlog disclosure paragraph. If both are fully counted and not yet consumed, at least $200bn of the $252bn H1 increase (≥79%) is from two customers. In the same half, Amazon paid those customers $38.7bn in equity ($28.7bn OpenAI + $10.0bn Anthropic). It then paid $21.3bn more after June and left $15bn of facility capacity tied to delivering the compute. Adding the original $38bn OpenAI deal (in the December balance), lab contracts could be roughly half of the $496bn. The filings do not confirm inclusion or the drawdown already recognized, so this is an upper-range inference, not a figure. The note does say not to add contract totals to backlog. But it never makes the inverse point: backlog is the note's main demand evidence (Summary bullet 6), and it is concentrated in investees. A same-vendor reviewer accepted "predominantly AWS commitments" as demand evidence without asking whose. [Q1 10-Q][Q126]; [Q2 10-Q][Q226]; [OpenAI][OA]; [Anthropic][ANT].

2. **Investment marks dominate reported earnings. Primary (A); shares are B.** Q2 2026 operating income was $27.461bn, against non-operating income of $53.396bn and pre-tax income of $80.857bn. So 66.0% of pre-tax income was non-operating (H1: $69.378bn of $120.691bn, 57.5%). Q2 net income was $62.647bn, more than double operating income. Anthropic's carrying value rose from $60.6bn at Dec 31, 2025 ($14.8bn preferred + $45.8bn notes) to $190.4bn at June 30. With only $10.0bn of new cash, that is about $120bn of mark-ups in six months, across earnings and OCI (B). Anthropic is now about 34.5% of Amazon's $551.6bn book equity. The 10-Q puts maximum exposure to loss at "carrying values … and any future funding commitments", about $205bn for Anthropic alone (190.4 + 15; B). The note says marks make headline earnings "a weak shortcut" but never gives the scale, and the scale is the point. This is also the place where Amazon shareholders would first see a lab-valuation reversal. [Q2 10-Q][Q226].

3. **Contractual commitments grew 48% in six months. Primary (A).** Total commitments went from $439.661bn (Dec 2025) to $650.034bn (June 2026). Within that, unconditional purchase obligations rose $84.8bn → $130.1bn, leases not yet commenced $96.4bn → $137.2bn, and long-term-debt principal and interest $108.2bn → $220.3bn. The note cites only the June uncommenced-lease figure. The change over time is the overextension signal, and the purchase obligations (energy, equipment, software) are fixed costs that persist if AI demand weakens. [10-K][K25]; [Q2 10-Q][Q226].

4. **Management's explicit payback claim is missing. Primary, attributed (A).** On July 30 Jassy said: "For servers and networking equipment, on average, it takes a little less than three years to break even … The servers currently have a useful life of at least five to six years, and most of our AI capacity these days is being contracted for at least five-year terms." He also said that for servers, "If the demand isn't there, we won't spend the capital", and that "margins and returns in AI [are] tracking what we saw with Core … a little ahead." This is the strongest pro-return evidence on the record, and it is testable. It also sits awkwardly with the 2025 change shortening a subset of servers from six to five years. The note keeps only the FCF-headwind part of the same answer. [Call][CALL]; [10-K][K25].

5. **AWS capital intensity and return on capital, both directions. Primary (A); ratios B.** AWS net PP&E additions were $48.604bn in Q2 2026, more than AWS's $42.232bn Q2 revenue. In Q2 2025 they were $16.043bn. AWS net PP&E rose from $190.1bn to $263.8bn in six months (+38.8%), after $96.5bn of 2025 additions (2024: $53.3bn). Against that, annualized H1 2026 AWS operating income of $61.6bn is about 27% pre-tax on average net PP&E, and 23% on the June balance. That is still comfortably profitable, though the PP&E includes construction in progress not yet earning. The Codex review added the 76% share; neither review gives the return ratio, which answers "comfortably profitable" more directly than the margin does. [10-K][K25]; [Q2 10-Q][Q226].

6. **The liquidity figure is dated and the bridge is missing. Primary (A); bridge B.** The $123.0bn is a June 30 balance (identical to December's). Since then: +$24.867bn July notes, +£4.235bn September notes, and −$21.3bn to OpenAI, before Q3 operating flows. So the balance is roughly unchanged, not eroded, but it has not been reported since June. Commercial paper ($30bn programme) and revolvers ($15bn plus a $5bn 364-day facility) were undrawn at June 30. [Q2 10-Q][Q226]; [July 8-K][DEBT]; [September 8-K][SEPT].

7. **Delayed-draw term loan status. Primary, weak evidence (B/C).** Amazon's EDGAR filing list for Sept 15–Oct 18, 2026 shows no 8-K other than the Sept 24 Form 8-A listing the sterling notes, plus Forms 3/4. Nothing announces a draw on the $17.5bn term loan before its Sept 30 deadline. That points toward expiry undrawn. It is not conclusive, because the June 2026 8-K on entering the facility may already have met the disclosure duty. Q3 results on Oct 29 will settle it. [EDGAR submissions][SUBS].

8. **No public Anthropic S-1, and IPO timing. Primary absence (A); timing is secondary (C).** An EDGAR full-text search on 2026-10-18 found no public S-1 or S-1/A naming "Anthropic, PBC" since June 1. The $518bn, ~80% non-cancellable and $110bn-to-AWS figures therefore stay C. Reuters (Oct 14) reports the IPO may slip past the November midterms. That matters for Amazon in three ways: the facility's 30-month clock starts at the liquidity event, notes convert at the IPO, and the Level 3 marks then meet a market price. Reuters also reports a 2025 operating loss above $8bn excluding liability writedowns. That is a better comparator for Anthropic's cash needs than the $42bn net loss the note cites. [EDGAR FTS][EFTS]; [Reuters][REUT].

9. **Minor: a non-AI capital call.** Amazon agreed on April 13, 2026 to acquire Globalstar for cash or stock: $90 per share, with cash capped at 40% of shares. On the 128.6m shares outstanding at signing, that is an equity value of about $11.6bn and at most about $4.6bn of cash (B). The S-4 went effective Aug 18. It is small, but it is another claim on the same funding. [424B3][GSAT].

10. **Implication of the $220bn guide (illustrative, C).** H1 gross purchases were $98.4bn (net $96.3bn), so H2 needs about $122–124bn, or about $61bn a quarter, against $54.2bn in Q2. Suppose H2 OCF grows at H1's rate of +44% on H2 2025's $90.0bn. Then FY2026 OCF is about $201bn and FY2026 FCF about −$19bn, before lab investments. The note would be better for stating the full-year direction rather than only the trailing figure. This is an assumption, not a forecast.

## Summary-bullet assessment

| Bullet | Supported by note's evidence? | Concrete (figure + date)? |
|---|---|---|
| 1 AWS profitable | Yes (claims 14, 40). | Yes. Could cite the 10-Q's $551m instead of rounded speech. |
| 2 Build not covered by OCF | Yes (claims 9–11). | Yes, but it is **the only bullet with no source link**. It also omits the lab-investment outflows, which are part of "the build" in a funding sense. |
| 3 Capex and borrowing | Yes (claims 13, 28, 29, 35). | Mostly. "Lab investments add to its cash requirements" has no figure: it should say $38.7bn in H1 and $21.3bn after June. |
| 4 Anthropic exposure | Yes (claims 19, 22). | Yes. It should add the $190.4bn carrying value and the 10-Q's maximum-exposure definition, because that, not the $18bn, is what moves Amazon's earnings. |
| 5 OpenAI exposure | Yes (claims 24, 25). | Yes. "Correlated financing risk" is a judgement, and it is labelled as one. |
| 6 Demand evidence | Partly. The $496bn backlog is presented as broad demand, but the note's own claims 15, 22 and 24 imply its H1 growth is mostly two investee labs. | The figures are there. The final sentence ("biggest uncertainty …") is abstract, and management's under-three-year payback claim, the testable version of that uncertainty, is absent. |

## Your assessment

AWS is comfortably profitable on the measures that can be computed: a 38–39% Q2 segment margin and roughly 23–27% annualized pre-tax operating income on segment net PP&E. Consolidated Amazon is not overextended in a solvency sense: $133bn of debt face value against $123bn of liquidity (June 30) and $161bn of trailing OCF. Where I differ from the note, and from the same-vendor review, is on what the AI expansion now depends on. Most of the H1 2026 backlog growth coincides with contracts from OpenAI and Anthropic. Amazon put $60bn of equity into them between January and the July 31 filing, and holds a $15bn facility that opens as it delivers their compute. Its Q2 earnings were two-thirds non-operating, mostly a Level 3 mark on Anthropic, which is now about a third of its book equity. That is not circular in the round-trip sense, since the labs also raise outside money and pay cash. But it means the demand evidence, the earnings and the investment risk all point at the same two counterparties. Who loses first: Amazon shareholders, through mark-downs of the ~$190bn Anthropic and ~$50bn OpenAI positions (non-cash, but large against equity) and through lower returns on AWS's fastest-ever PP&E growth. Then suppliers and landlords holding Amazon's $650bn of commitments, only if demand falls broadly. Creditors are last, and well covered. In the other direction, the note underweights management's explicit payback claim: under three years on servers that last five to six, on contracts of five years or more. If Q3 and Q4 show margin holding while PP&E grows about 40% a half, that claim is being met.

## Front-page figures

| Figure | Where | Note's value / source | Still holds? |
|---|---|---|---|
| Amazon trailing FCF −$7.6B | stack.md table (L20) and narrative (L38) | −$7.604bn, TTM to June 30, 2026 (claim 10) | Yes, as a June TTM figure. Should be dated "to June 2026". Q3 results on Oct 29 will replace it. |
| $67B long-term-debt proceeds in H1 | index.md L18; stack.md L20 | $66.998bn (claim 28) | Yes. stack.md says "drawn": these are bond proceeds, so "raised" is the accurate word. |
| +$25B in July | stack.md L20 | $25.0bn principal, $24.867bn proceeds (claim 29) | Yes, but incomplete: £4.25bn of September sterling notes (claim 35) is missing from stack.md. |
| ~$220B 2026 capex guidance | theory.md L106 | ~$220bn cash capex, July 30 (claim 13) | Yes. |
| $123B liquidity | stack.md L20 | $123.0bn at June 30, 2026 (claim 30) | Yes as of June 30. Not dated on the page, and it predates the $21.3bn OpenAI payment and the July/September bonds (roughly offsetting). |
| $50B OpenAI investment ($28.7B + $21.3B) | stack.md L23, L48; theory.md L86 | claim 25 | Yes, fully funded per the July 31 filing. |
| $18B in Anthropic + $15B facility | not found on current index/stack/theory | claim 19 | Yes in the note. If used, it needs "drawable only as compute-delivery milestones are met". |
| $496B backlog | not found on current pages | claim 15 | Yes as a figure. If used, add that its H1 growth coincides mainly with the OpenAI and Anthropic deals (Omission 1). |
| AWS +37%, 39.4% margin | not found on current pages | claim 14 | Yes. 38.05% excluding the $551m energy-derivative gain. |
| $50.5B Q2 Anthropic preferred repricing gain | not found on current pages | claim 21 | Yes. It is an unrealized Level 3 mark; non-operating income was 66% of Q2 pre-tax income. |
| "Google's and Amazon's reported ~$110B commitments each" (Anthropic) | stack.md L50 | claim 37 (C) vs claim 22 (A: >$100bn) | Holds as labelled "reported". No public S-1 as of Oct 18. |

None of the front-page figures from this note is wrong. Two are stale or incomplete in context: the undated $123B, and the "$67B … plus $25B in July" line, which omits September.

## Recommended edits

1. **Summary bullet 2: add sources and the lab-investment outflow.** Replace with: "Amazon's consolidated build is no longer comfortably covered by operating cash flow. Trailing free cash flow fell from $38.219bn at end-2024 to $11.194bn at end-2025 and −$7.604bn in the twelve months to June 2026; including lease and financing-obligation principal gives −$9.511bn. Trailing acquisition and non-marketable-investment outflows were a further $41.956bn, mostly $28.7bn to OpenAI and $10.0bn to Anthropic in H1 2026. [Results][R226]; [Q2 filing][Q226]."

2. **Summary bullet 6: name the concentration and the payback claim.** Replace the last two sentences with: "These demonstrate sales, contracts and deployment, but not utilization or cash returns. Backlog rose $252bn in H1 2026, in the two quarters when OpenAI added $100bn and Anthropic more than $100bn of AWS commitments, so most of the growth is plausibly from two labs Amazon also funds (inference, C). Management says servers break even in a little under three years and are contracted for five years or more; Q3–Q4 margins against roughly 40% half-year AWS PP&E growth will test that. [Q1 filing][Q126]; [Q2 filing][Q226]; [call][CALL]."

3. **New Key-claims rows (A/B):**
   - "Q2 2026 operating income $27.461bn; non-operating income $53.396bn; pre-tax income $80.857bn (66.0% non-operating); net income $62.647bn; H1 non-operating $69.378bn of $120.691bn pre-tax (57.5%) | 2026-Q2/H1 | [10-Q][Q226] | primary | A; B shares."
   - "Anthropic carrying value $60.6bn (Dec 2025) → $190.4bn (June 2026) with $10.0bn new cash; ~34.5% of $551.6bn equity; maximum exposure to loss defined as carrying value plus future funding commitments (~$205bn) | [10-Q][Q226] | primary | A inputs; B derived."
   - "Total contractual commitments $439.661bn → $650.034bn; unconditional purchase obligations $84.772bn → $130.065bn | Dec 2025 → June 2026 | [10-K][K25], [10-Q][Q226] | primary | A."
   - "AWS net PP&E additions Q2 2026 $48.604bn (Q2 2025 $16.043bn); AWS net PP&E $190.055bn → $263.750bn; annualized H1 AWS operating income $61.564bn ≈ 27% of average net PP&E | [10-K][K25], [10-Q][Q226] | primary | A; B ratio."
   - "Management payback claim: servers break even in 'a little less than three years', useful life 'at least five to six years', most AI capacity contracted for 'at least five-year terms' | 2026-07-30 | [Call][CALL] | primary | A (attributed)."

4. **Claim 40: source it from the filing.** Replace the value with: "10-Q: net unrealized energy-contract gains $551m in Q2 2026, primarily AWS; (16,621 − 551)/42,232 = 38.05%; consistent with management's 650 vs 520 bp." Grade "A input; B derived".

5. **Analysis, "Anthropic: customer, asset and financing counterparty": add after the first paragraph.** "Scale matters: Anthropic's carrying value rose by about $120bn in H1 2026 against $10.0bn of new cash, and non-operating items were 66% of Q2 pre-tax income. A reversal of the Level 3 marks, for example at an IPO priced below the Series H basis or after a delayed listing, would hit Amazon's net income and equity well before it touched AWS operating income or creditors."

6. **Analysis, "Funding and loss allocation": add the commitments trend and the liquidity bridge.** "Total contractual commitments rose from $439.7bn to $650.0bn between December 2025 and June 2026, including unconditional purchase obligations up from $84.8bn to $130.1bn. After June, July's $24.867bn and September's ~£4.235bn of note proceeds roughly offset the $21.3bn OpenAI payment, so June's $123.0bn of liquidity is a dated, not an eroded, figure."

7. **Delayed-draw loan (claim 42 and the Analysis paragraph):** add "Amazon's EDGAR filings from Sept 15 to Oct 18 include no 8-K announcing a draw; expiry undrawn is likely but unconfirmed until the Q3 10-Q."

8. **Conflicts, "Unverified items": add** "No public Anthropic S-1 was on EDGAR as of 2026-10-18 (full-text search); Reuters (Oct 14) reports the IPO may slip past the November midterms; Reuters also reports a 2025 operating loss above $8bn excluding liability writedowns (C)."

9. **Funding paragraph: add one line on Globalstar.** "Amazon also agreed on April 13, 2026 to acquire Globalstar for up to $90 a share, cash capped at 40% of shares (roughly $11.6bn equity value, at most ~$4.6bn cash; B), a non-AI claim on the same funding."

10. **For the lead, not this note: stack.md L20.** Change "Amazon $67B of long-term debt drawn in H1 2026 plus $25B in July" to "Amazon $67B of long-term-debt proceeds in H1 2026, $25B in July and £4.25B in September". Change "Amazon $123B" to "Amazon $123B at June 30". Add "to June" after "Amazon trailing FCF −$7.6B".

[K25]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
[Q126]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm
[Q226]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[R226]: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
[CALL]: https://www.fool.com/earnings/call-transcripts/2026/08/07/amazon-amzn-q2-2026-earnings-call-transcript/
[DEBT]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926082293/tm2619352d4_8k.htm
[SEPT]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926107526/tm2624614d5_8k.htm
[ANT]: https://www.anthropic.com/news/anthropic-amazon-compute
[OA]: https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment
[REUT]: https://ca.marketscreener.com/news/anthropic-s-q3-revenue-surges-45-to-nearly-17-billion-ce785dd2d08cf221
[SUBS]: https://data.sec.gov/submissions/CIK0001018724.json
[EFTS]: https://efts.sec.gov/LATEST/search-index?q=%22Anthropic%2C%20PBC%22&forms=S-1,S-1/A&dateRange=custom&startdt=2026-06-01&enddt=2026-10-18
[GSAT]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926098339/tm2617924-6_424b3.htm
