# Independent cross-check: Amazon

*Review date: 2026-10-17. Reviewed `research/stack/amazon.md` as supplied; methodology and research brief read first. All external sources below were fetched on 2026-10-17. Only this review was written; no git commands or subagents were used.*

## Verdict

The 15 selected claims match their cited evidence, with qualifications; no material arithmetic error was found.
The central conclusion holds: profitable AWS, an externally financed consolidated expansion, and unproven returns on new AI capacity.
Revise before treating the note as current: it misses September borrowing, AWS capital-addition data, and recent evidence on Anthropic’s competing payment commitments.

## Claim re-verification

Selection prioritizes the six Summary bullets and the financing/demand argument. Dollars are billions unless indicated. **A** grades a direct disclosure or explicitly attributed management statement, not the eventual fulfillment of a forecast; **B** grades arithmetic. Mixed grades below distinguish the inputs from the calculation. “Match” means the evidence supports the dated claim, not an independent audit of company accounts.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 9 | 2024 OCF/capex/FCF: 115.877/77.658/38.219; 2025: 139.514/128.320/11.194 | Same annual figures | [FY2025 results][R425], FCF reconciliation | Yes | A, including directly published FCF |
| 10 | March 2026 TTM: 148.531/147.299/1.232; June: 161.403/169.007/−7.604 | Same OCF/net cash capex/FCF | [Q2 results][R226], supplemental metrics | Yes | A |
| 11 | FCF after lease principal / after both principal categories: Dec 9.637/9.309; Mar −0.383/−0.710; Jun −9.203/−9.511 | Same; calculations below | [10-K][K25], [Q1 10-Q][Q126], [Q2 10-Q][Q226], cash-flow statements | Yes | B, reconstructed measures |
| 12 | H1 OCF 71.419; capex 96.310; FCF −24.891; acquisition/investment/other outflow 39.767 | Same; net capex = 98.411−2.101 | [Q2 results][R226], cash-flow statement | Yes | A inputs; B net capex and H1 FCF |
| 13 | 2026 capex guidance ≈200 → ≈220; memory costs cited | February release: ≈200 capital expenditures; July spoken transcript: ≈220 cash capex, with memory costs explaining increase | [Feb 5 release][R425]; [July 30 call][CALL], Jassy’s remarks | Yes; original release itself does not say “cash” | A for attributed guidance; transcript not audio-authenticated |
| 14 | AWS Q4/Q1/Q2 revenue 35.579/37.587/42.232; growth 24%/28%/37%; margins 35.0%/37.7%/39.4%; Q2 OI 16.621 | Same published figures; Q2 calculated growth 36.7927%, versus quotation 36.7% | [Q2 results][R226], segment metrics and CEO quotation | Yes; discrepancy already acknowledged | A disclosed; B calculated growth |
| 15 | Backlog/life: Dec 244/4.1 years; Mar 364/5.5; Jun 496/6.4 | Same; qualifying commitments primarily AWS, not all contracts or collected cash | [10-K][K25], [Q1][Q126], [Q2][Q226], revenue-recognition disclosures | Yes | A |
| 17 | Rainier nearly 500,000 Trainium2; Anthropic >1m overall by April | Launch page: nearly half-million; Apr 20 Anthropic: >1m in use. Feb 5 release already describes Rainier as 500,000+ | [Rainier][RAIN], [Anthropic][ANT], [FY2025 results][R425] | Yes as dated history; newer count should be distinguished | A, company-reported deployment |
| 19 | Anthropic funded 18; remaining facility 15; exact ownership undisclosed | 8+5+5=18; facility 20−5=15, subject to delivery milestones | [Q2 10-Q][Q226], Note 2, Anthropic | Yes; 15 is remaining capacity, not necessarily immediately drawable | A components/terms; B funded total |
| 22 | Anthropic >100 over ten years; up to 5GW; nearly 1GW by end-2026 | Same April announcement | [Anthropic, Apr 20][ANT] | Yes; capacity delivery remains forward-looking | A, attributed commitment/plan |
| 24 | OpenAI original 38/seven years; additional 100/eight years; ≈2GW Trainium | Same terms | [OpenAI, Nov 3, 2025][OA0]; [Amazon, Feb 27, 2026][OA] | Yes; differing periods cannot be collapsed into one annual revenue number | A |
| 25 | OpenAI 28.7 through June +21.3 subsequently =50 funded | 15 in Q1 +13.7 in Q2 +21.3 after June, disclosed in July 31 filing | [Q2 10-Q][Q226], Note 2 and subsequent event | Yes; 50 was not the June balance | A component payments; B total |
| 28 | March $37 and €14.5; May CHF2.8; June C$14; H1 long-term debt proceeds $66.998 | Same original-currency principal and cash proceeds | [Q2 10-Q][Q226], Note 5 and cash-flow statement | Yes; proceeds differ from translated principal | A |
| 29 | July principal 25; proceeds ≈24.867; fixed coupons 4.60–6.25%; maturities 2029–2066 | Same; 0.750 of total is floating-rate | [July 9 8-K][JULY] | Yes, but funding history is incomplete without September | A stated terms/proceeds; B sum of tranche principal |
| 30 | June liquidity 123.0; debt face value 132.995; uncommenced leases 137.214 | Same; debt includes current portion, leases are future contractual payments | [Q2 10-Q][Q226], liquidity, debt and commitments tables | Yes; these are unlike measures, not a single net-debt calculation | A |

## Arithmetic checks

The Analysis mostly discusses calculations tabulated elsewhere. I checked those supporting calculations as well as its linked eight-quarter CSV, without modifying it.

**Quarterly investment bridge.** All figures in this table are USD millions. Annual-minus-nine-month and half-year-minus-Q2 derivations use the [2025 10-K][K25], [Q3 2025 10-Q][Q325] and [Q2 2026 10-Q][Q226].

| Quarter | Net cash capex calculation | Finance-lease additions calculation | Result |
|---|---|---|---|
| 2024-Q3 | 22,620−1,342=21,278 | 186 directly disclosed | Pass |
| 2024-Q4 | (82,999−55,165)−(5,341−3,559)=26,052 | 854−409=445 | Pass |
| 2025-Q1 | (57,202−32,183)−(1,579−815)=24,255 | 991−937=54 | Pass |
| 2025-Q2 | 32,183−815=31,368 | 937 directly disclosed | Pass |
| 2025-Q3 | 35,095−867=34,228 | 977 directly disclosed | Pass |
| 2025-Q4 | (131,819−92,297)−(3,499−2,446)=38,469 | 2,911−1,968=943 | Pass |
| 2026-Q1 | (98,411−54,208)−(2,101−1,132)=43,234 | 2,128−563=1,565 | Pass |
| 2026-Q2 | 54,208−1,132=53,076 | 563 directly disclosed | Pass |

**Cash-flow reconstruction.** In billions: 115.877−77.658=38.219; 139.514−128.320=11.194; 148.531−147.299=1.232; 161.403−169.007=−7.604. H1: 71.419−96.310=−24.891. All pass. The last four CSV quarters sum to June TTM OCF 161.403, capex 169.007 and FCF −7.604. [Annual results][R425]; [Q2 results][R226].

| TTM end | FCF minus finance-lease principal | Then minus financing-obligation principal | Result |
|---|---|---|---|
| Dec 2025 | 11.194−1.557=9.637 | 9.637−0.328=9.309 | Pass |
| Mar 2026 | 1.232−1.615=−0.383 | −0.383−0.327=−0.710 | Pass |
| Jun 2026 | −7.604−1.599=−9.203 | −9.203−0.308=−9.511 | Pass |

Sources: [10-K][K25], [Q1][Q126], [Q2][Q226]. The CSV also passes all 32 within-quarter identities: gross less incentives, OCF less capex, and the two successive principal deductions. The Analysis correctly distinguishes lease additions from repayments and reproduces the [historical FCF definitions][OLD]. “The first-half deficit precedes lab-investment outflows” is true in the calculation, not necessarily in calendar time; replace “precedes” with “excludes.”

**Other derived values supporting Analysis.**

- AWS margins: 12.465/35.579=35.0347%; 14.161/37.587=37.6753%; 16.621/42.232=39.3564%. Q2 growth: 42.232/30.873−1=36.7927%. Rounded values pass. Annualizing Q2 revenue gives 42.232×4=168.928, approximately 169; actual TTM AWS revenue is 148.404, not 169. The note keeps this distinction. [Results][R226].
- Anthropic cash 8+5+5=18; unused facility capacity 20−5=15; carrying values 92.5+97.9=190.4; OpenAI cash 28.7+21.3=50. All pass, with cash, conditional commitments and accounting marks kept separate. [Q2 filing][Q226].
- Valuation: 250×10.783=2,695.750 billion equity value; 2,695.750/161.403=16.70198× OCF; 4%×2,695.750=107.830 billion FCF. All pass. The [October 16 historical price row][PRICE] is $250.00, although the same page's 3:59:57 quote header is $249.92. The note correctly uses the historical row. Share count is June actual outstanding shares, not a contemporaneous fully diluted count. [Results][R226]. Grade B fits the conditional arithmetic; 4% is an assumption, not an empirically graded fact or market-implied required yield.
- No improper addition of AI and chips run rates, backlog and contract announcements, or finance-lease additions and all principal repayments occurs. No annualization of the private lab's quarterly revenue occurs. The run-rate overlap warning is appropriate. [Official AWS excerpt][AI].

## Omissions

**September borrowing — primary, A; just outside the last 30 days.** Amazon closed £4.25bn of sterling notes on September 14, with approximately £4.235bn proceeds before offering expenses, fixed coupons 5.20–6.65% and maturities 2029–2045. July is therefore an unnecessarily stale stopping point for the financing history. This strengthens both the external-funding argument and the evidence of continued market access; it does not establish the October debt balance. [September 14 8-K][SEPT].

**Anthropic's alternative CPU supplier — primary, A; within the last 30 days.** Akamai announced an $11.6bn, seven-year Anthropic commitment on September 24 for CPU workloads. That matters because the note treats Anthropic's growing business as support for AWS demand: incremental spending also goes elsewhere. Akamai estimates $5.5bn associated capex, including $1.7bn additional 2026 capex, without changing 2026 revenue guidance. This also illustrates suppliers spending before customer revenue arrives. It does not prove Anthropic moved existing AWS workloads, and should not be added to AWS backlog or mechanically added to other reported lab commitment totals. [Akamai SEC-filed release][AKAM].

**Customer payment rigidity — secondary, C, reported, unverified; within the last 30 days.** Reuters on September 29 reported, from Anthropic's confidential prospectus, $518bn of infrastructure commitments, about 80% non-cancelable or payable regardless of usage. Its reported AWS component is $110bn over May 2026–April 2036, with payments due for spending shortfalls. No public primary prospectus was located, so this must not replace the verified >$100bn announcement as an A-grade fact. It cuts both ways: firmer contractual protection for AWS, but less flexibility for its customer if demand disappoints. The note's unqualified statement that cancellation rights are “unavailable” misses this reported evidence. [Reuters, September 29][RSEP29].

**Customer financial downside — secondary, C, reported, unverified; within the last 30 days.** Reuters' September 28 prospectus report describes a near-$42bn 2025 net loss, including approximately $34bn from revaluing convertible financing, and nearly one-quarter of revenue from two customers. The loss is not cash burn, and historical results do not contradict October's reported Q3 adjusted profitability. The omission nevertheless leaves the latest customer-risk discussion tilted toward the favorable investor-day report. [Reuters, September 28][RSEP28]; [October 14 report][ROCT14].

**AWS capital deployment is partly disclosed — primary, A/B.** H1 AWS net property-and-equipment additions were $90.120bn of $118.648bn consolidated, or 76.0% (B). These include noncash additions and are not AWS cash capex or AI-only capex. They materially narrow the note's consolidated-spending caveat: the infrastructure expansion is predominantly AWS even though the AI/core split remains unknown. [Q2 filing, segment information][Q226].

**Margin quality is acknowledged but not quantified.** The note buries energy-contract gains in Conflicts. Management said Q2 AWS margin expansion was 650 basis points reported and 520 excluding the derivative gain. That implies approximately 38.1% excluding the effect, versus 39.4% reported, using rounded management figures (B). Profitability remains substantial; the adjustment does not reverse the conclusion. [July call][CALL].

**Smaller completeness issues.** The annual filing also reports $7.7bn of 2025 upward private-equity valuation adjustments, primarily Anthropic, omitted from claim 21's list of gains; its $5.6bn conversion gain is accurate but incomplete. The June filing discloses a $17.5bn delayed-draw term loan whose undrawn commitment expired September 30: its draw status needs checking at the next results and must not be counted as October available liquidity without confirmation. [10-K][K25]; [Q2 filing][Q226].

The targeted news search covered September 17–October 17, plus older developments needed to update the financing history. The material primary finding inside that window is Akamai; the confidential-prospectus reporting is expressly lower-confidence. I did not find a primary disclosure superseding Amazon's July cash-capex guide. The next results date is October 29, confirmed by Amazon's October 15 announcement. [Webcast announcement][NEXT].

## Summary-bullet assessment

| Bullet | Supported by its own evidence? | Precision and usefulness |
|---|---|---|
| 1 — profitable AWS | Yes: claim 14 supports revenue, growth and reported segment margin. The limit on new AI returns is sound. | Has figures but “latest quarterly” needs **Q2 2026**. Add the approximately 38.1% margin excluding the derivative effect; see edit 1. |
| 2 — build not covered by OCF | Yes: claims 9–12 establish the consolidated cash deficit. It does not assert AWS itself has negative FCF. | Already concrete and dated; retain. It describes spending coverage, not project profitability. |
| 3 — capex and external financing | Yes: claims 13 and 28–30 support the core statement. | “Ample financing access” and “material parts” need funding amounts and dates. Lab investments consume funds; they are not a source of financing. See edits 2 and 3. |
| 4 — Anthropic exposure | Yes: claims 19 and 22 establish the cash, facility and commercial commitment. | Specify June **2026**, delivery-contingent access to the facility, and distinguish the customer's concentration from Amazon's undisclosed recognized revenue exposure. Dates/terms in edit 7. New obligations belong in Analysis. |
| 5 — OpenAI exposure | Yes: claims 24–25 support both expansion and the subsequently completed investment. | “Latest filing” is a moving reference; name July 31, 2026 and avoid putting all $50bn at June 30. The correlated-risk conclusion is reasonable analysis, not a directly disclosed metric. See edit 7. |
| 6 — evidence against immediate overbuild | Partly: revenue, contracts and deployed chips support present demand; none establishes economic utilization or future capital recovery. | Closest to being too abstract: $496bn lacks its date and duration; “deployed Trainium capacity” lacks a count/date; “today's capacity shortage” is a management assertion. Replace with edit 6. |

No Summary bullet is wholly figure-free. The useful correction is to date bullets 1, 4, 5 and 6 and quantify the unsupported shorthand in bullets 3 and 6, rather than claim the entire Summary is abstract.

## Your assessment

I agree with the note's distinction between a real, profitable cloud business and uncertain returns on the newest AI investments. Its arithmetic is unusually careful, especially on leases, lab funding and valuation marks. I differ in emphasis: available segment investment data makes the exposure to AWS expansion more measurable than the note suggests, while recent counterparty disclosures make a generic warning about correlated financing too mild. Stronger minimum-payment terms would protect contractual revenue but would not solve the customer's ability to fund all its suppliers; conversely, the margin adjustment still leaves strong AWS profitability. September borrowing supports ongoing financing capacity rather than immediate distress. My conclusion is growing capital-return and counterparty risk, not demonstrated current overbuild, insolvency, or stock mispricing; the missing segment cash flows, AI/core capital split and public lab accounts prevent a stronger finding.

## Recommended edits

1. **Replace Summary bullet 1:** “In Q2 2026, AWS earned $16.621bn operating income on $42.232bn revenue, up 37% year over year; its reported margin was 39.4%, or approximately 38.1% excluding the energy-derivative effect described by management. Neither measure establishes returns on the newest AI infrastructure.” Grade the adjusted margin B. [Results][R226]; [call][CALL].

2. **Replace the July-only sentence in Funding and loss allocation:** “After July's $25bn bond issue, Amazon issued £4.25bn of sterling notes on September 14, 2026, with approximately £4.235bn proceeds before offering expenses, coupons of 5.20–6.65%, and maturities from 2029 to 2045. These issuances demonstrate continuing funding access; they do not supply a complete October debt balance.” Add this A/B-grade issuance to Key claims. [September 8-K][SEPT].

3. **Replace Summary bullet 3 and add the available segment data:** “On July 30, management raised 2026 cash-capex guidance from approximately $200bn to $220bn, citing memory costs. Amazon received $66.998bn of long-term-debt proceeds in H1, then issued $25bn in July and £4.25bn in September; lab investments add to its cash requirements.” In Analysis add: “AWS accounted for $90.120bn, or 76.0%, of H1 2026 consolidated net property-and-equipment additions; this measure includes noncash investment and does not isolate AI spending.” [Call][CALL]; [Q2 filing][Q226]; [July][JULY]; [September][SEPT].

4. **Add the recent primary counterparty evidence:** “On September 24, 2026, Akamai disclosed an $11.6bn, seven-year Anthropic commitment for CPU workloads. Anthropic's growth therefore supports multiple infrastructure suppliers; this announcement does not establish displacement of existing AWS workloads.” Grade A for the announcement, interpretation separately labeled. [Akamai release][AKAM].

5. **Replace the blanket cancellation-rights gap and balance the favorable lab update:** “Public contracts remain unavailable, but Reuters reported on September 29 that Anthropic's confidential prospectus contains $518bn of infrastructure commitments, about 80% non-cancelable or payable regardless of usage, including $110bn to AWS. These figures and terms are reported, unverified (C): they strengthen payment obligations while increasing counterparty funding pressure.” Add: “Reuters' September 28 report also described a near-$42bn 2025 net loss, including roughly $34bn of financing revaluation charges; this is not a cash-burn figure.” [September 29][RSEP29]; [September 28][RSEP28].

6. **Replace Summary bullet 6:** “Evidence of current demand includes 37% AWS revenue growth in Q2 2026, $496bn of predominantly AWS commitments at June 30 with a 6.4-year weighted remaining life, and Anthropic's April disclosure that it used more than 1m Trainium2 chips. These demonstrate sales, contracts and deployment, but do not establish utilization or cash returns on new capacity.” [Results][R226]; [Q2 filing][Q226]; [Anthropic][ANT].

7. **Fix the remaining timing and facility wording:** In bullet 4 use “$18bn invested through June 2026 and $15bn of remaining financing-facility capacity, with availability tied to compute-delivery milestones.” In bullet 5 use “The July 31, 2026 filing reports $28.7bn invested in OpenAI through June and another $21.3bn subsequently, completing the $50bn investment.” Replace “The first-half deficit precedes lab-investment outflows” with “The first-half 2026 FCF deficit excludes lab-investment outflows.” [Q2 filing][Q226].

8. **Complete accounting evidence and distinguish assumptions from grades:** Add to claim 21: “2025 also included $7.7bn of upward private-equity valuation adjustments, primarily Anthropic.” For claim 31 replace “B; C for scenario” with “B for arithmetic conditional on the stated inputs; 4% yield is an illustrative assumption, not an observed market requirement.” [10-K][K25].

[K25]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
[Q126]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm
[Q226]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[Q325]: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm
[R425]: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx
[R226]: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
[CALL]: https://www.fool.com/earnings/call-transcripts/2026/08/07/amazon-amzn-q2-2026-earnings-call-transcript/
[ANT]: https://www.anthropic.com/news/anthropic-amazon-compute
[RAIN]: https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
[AI]: https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-revenue-growth-q2-2026-earnings
[OA0]: https://openai.com/index/aws-and-openai-partnership/
[OA]: https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment
[JULY]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926082293/tm2619352d4_8k.htm
[SEPT]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926107526/tm2624614d5_8k.htm
[AKAM]: https://www.sec.gov/Archives/edgar/data/1086222/000119312526401048/d288154dex991.htm
[RSEP29]: https://www.investing.com/news/stock-market-news/anthropics-518-billion-ai-buildout-hinges-largely-on-deals-that-cannot-be-canceled-filing-shows-4922031
[RSEP28]: https://www.marketscreener.com/news/anthropic-s-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-ce785addd98afe2c
[ROCT14]: https://ca.marketscreener.com/news/anthropic-s-q3-revenue-surges-45-to-nearly-17-billion-ce785dd2d08cf221
[OLD]: https://ir.aboutamazon.com/news-release/news-release-details/2024/Amazon-com-Announces-Second-Quarter-Results/default.aspx
[PRICE]: https://chartexchange.com/symbol/nasdaq-amzn/historical/
[NEXT]: https://press.aboutamazon.com/2026/10/amazon-com-to-webcast-third-quarter-2026-financial-results-conference-call
