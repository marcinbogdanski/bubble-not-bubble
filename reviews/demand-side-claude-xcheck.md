# Independent cross-check: AI demand (Claude)

*Review date: 2026-10-18. A fresh-context Claude review of `research/macro/demand-side.md`, as revised after the [Codex cross-check](demand-side-codex-xcheck.md). Before starting I read `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, the note, the Codex review, `data/ai-revenue-estimates.csv` and `report/index.md` Part 2. I made 14 web fetches on 2026-10-18; three returned HTTP 403 (Axios, OpenAI, Bloomberg). Where a figure comes from a search-result relay rather than a fetched page, the text says so. I edited no other files and ran no git commands.*

## Verdict

$180B is the right order of magnitude but probably somewhat high. The deduplication cannot be reproduced and appears to under-deduct. My own payer-based rebuild gives **about $165B for 2026 (plausible range $130–205B)**, so the $230B top of the note's range is too high.
About half the total, the ~$90B of OpenAI plus Anthropic revenue, can be summed from reported quarterly figures and graded C. The rest is allocation and is D. The overall D label is right but hides this split.
The 2028 paths ignore the steep ramp within 2026. The December 2026 exit run-rate is about $250B, so the bear path ($170B in 2027) is a revenue contraction, not slow growth. The base path implies a sharp slowdown and the bull path roughly matches SemiAnalysis. The front page's Part 2 conclusion still holds.

## Claim re-verification

"Match" means the cited source states the value. It does not mean the value is audited.

| Note claim | Note's value | What I found (source, fetched 2026-10-18 unless stated) | Match? | Grade |
|---|---|---|---|---|
| 1 OpenAI run-rate | ~$50bn net; ~$70bn gross equivalent, end-Sep | Axios page returned 403. Search relays: FT/CNBC/Bloomberg give ~$50bn at end-September. Axios (Sep 29) gave "nearly $70bn", +70% since the start of Q3; later reporting says that figure included gross partner revenue. Bloomberg (Oct 9) reports OpenAI **expects ≥$70bn annualized by year-end 2026**; the note omits this. | Yes in substance. The $70bn comes from Axios Sep 29, not the Oct 8 piece | C |
| 2 Anthropic | ~$65bn late July (reported) / ~$74bn SemiAnalysis; Q3 $16.8bn; Q2 $11.5bn; 2025 $4.6bn | [Euronews][eu]: Q3 $16.8bn, Q2 $11.5bn, 2025 $4.6bn, 11% adjusted margin and $1.70 of revenue per compute dollar all match. In the fetched text, "$65bn in late July" sits in the same SemiAnalysis-attributed sentence as "$74bn". Run-rate is "expected to end 2026 below $100bn". | Values match. **Provenance does not**: the Summary's "different provenance" framing is not supported by this source | C |
| 3 OpenAI booked revenue | 2025 $13.07bn; H1 2026 $12.4bn incl. Q2 $6.7bn | Search relays: Q1 $5.7bn (The Information) and Q2 $6.7bn (WSJ), summing to $12.4bn. Not fetched. | Yes | C |
| 4 Microsoft | AI run-rate >$37bn, +123%; >30m Copilot seats | [FY26 Q3 call][ms3]: "AI business annual revenue run rate surpassed $37 billion … growing 123%"; >20m seats in March. [FY26 Q4 release][ms4]: ">30 million paid seats"; **no AI run-rate update** in July, and none found from that call. | Yes, but the AI figure dates from March and is now 6+ months old | A |
| 5 Google Cloud | $24.768bn, +82%; op. income $8.814bn | [8-K exhibit][goog]: same figures. "Product revenues primarily from the sale of TPU systems." No AI revenue figure. Gemini app has 950m MAU; no subscriber count. | Yes | A |
| 6 AWS | AI run-rate >$25bn; AWS +36.7% | [Release][amzn]: AI ">$25 billion … triple-digit"; **chips business separately >$25bn run-rate**; AWS $42.2bn, +37% (36.7% in Jassy's quote). | Yes | A |
| 7 Salesforce | Agentforce >$1.5bn; ~$3.9bn with Data 360; definition widened | [Release][crm]: same figures, +240% / +210%; definition now includes Slackbot and Headless 360. Total revenue $11.3bn per quarter, so AI is ~8% of ARR at most. | Yes | A |
| 8 Menlo enterprise | $37bn; apps $19bn; excludes inference and embedded features | [Menlo][menlo]: same. **Apps include ChatGPT Enterprise, Claude for Work and Microsoft Copilot (copilots $7.2bn)**; infrastructure includes $12.5bn of foundation-model APIs. The anchor for row 36 therefore already contains lab and Microsoft revenue. | Yes; overlap not flagged in note | C |
| 9 Menlo consumer | $12bn; ~3% conversion | [Menlo PDF][menloc], text extracted: "$12 billion market … only about 3% pay". **General assistants take 81% of the $12bn**, which leaves ~$2.3bn for specialized apps. | Yes; row 37's $5bn (2025) is ~2× its own anchor | C |
| 19 ChatGPT subscribers | >50m / >900m WAU, Mar 31 | OpenAI page returned 403; not re-fetched. Searches find no newer official count. The Sep 8 update (claim 48) gives 1bn WAU and no subscriber figure. | Not independently re-verified | A (per Codex), unchecked here |
| 46 OpenAI primary anchor | $2bn monthly revenue, Mar 31 | Page returned 403. Consistent with reported Q1 revenue of $5.7bn. | Consistent, not re-fetched | A (unchecked here) |
| 47 Anthropic primary anchor | >$47bn run-rate in May; $65bn Series H | [Anthropic][ant]: "run-rate revenue crossed $47 billion earlier this month", $65bn at $965bn post-money, May 28. **Consistent with reported Q2 $11.5bn (= $46bn annualized)**, which corroborates the leaked Q2 figure. | Yes | A |

## Deduplication check

**What the $180B includes** (CSV rows): lab subscriptions and API $90bn (global, mixed gross/net, consumer assistants included); cloud AI compute and services $75bn ("excluding ordinary cloud"; Microsoft's combined metric split between cloud and apps); enterprise AI applications and add-ons $50bn (anchored on Menlo apps plus incumbent ARR); consumer apps excluding labs $10bn; less an overlap of $45bn.

**What it excludes or leaves undefined:** advertising uplift (except ChatGPT ads, inside OpenAI), internal savings, Gartner's hardware and services, and training subsidies. Also missing are Chinese revenue (Alibaba alone booked $1.824bn of AI-related product revenue in the June quarter, [6-K][baba], A), Gemini consumer subscriptions, xAI/SpaceX, and the AI-native app layer by name. None of these appears in the note.

**Arithmetic:** 90+75+50+10 = 225; 225−45 = 180; 2025: 78−23 = 55. All correct, as are the scenario CAGRs (27.1%, 63.3%, 86.5%) and the capture products. The arithmetic is not the issue.

**The problem is that the elimination is too small for the flows now visible in primary data:**
- **Lab → cloud.** Microsoft's FY26 10-K reports **$24.1bn of revenue from OpenAI**, about 114% of OpenAI's own reconstructed revenue for the same period (cited in `research/stack/openai.md`, A; not re-fetched here). Microsoft's AI run-rate very probably contains much of it: an outside estimate puts Copilot at no more than a quarter of the $37bn (Om Malik analysis, C). AWS's >$25bn AI run-rate includes Anthropic's compute; an analyst estimate puts Anthropic at 8–9% of AWS revenue in Q1 2026, i.e. ~$13–14bn annualized (C). Google Cloud includes TPU-system sales and Anthropic capacity. Lab-to-cloud flows into these three clouds alone are therefore about **$45–55bn** in 2026.
- **App → lab and app ↔ Microsoft.** Row 36 is anchored on Menlo apps, which already include ChatGPT Enterprise, Claude for Work and Microsoft Copilot. AI-native apps also pay 40–75% of revenue to labs, using Bessemer's 25–60% gross margins (claim 26). That is another **~$15–25bn**.
- **Required elimination** if row 35 contains lab purchases: about **$60–80bn**, against $45bn used. If row 35 already excludes them, then $75bn of non-lab cloud AI is about $30bn above what the disclosed anchors support (see below). Either way the total looks **$15–30bn too high**, and the note does not say which reading applies.
- **Rows 36–37 look high on their own anchors.** Disclosed incumbent AI ARR is small: Salesforce ~$3.9bn including Data 360, ServiceNow's ~$1.5bn 2026 ACV target, Adobe AI-first >$0.5bn. Menlo's specialized consumer apps were ~$2.3bn in mid-2025, against row 37's $5bn for 2025.

**Is grade D right?** For the total, yes: it depends on allocations no source states. But the label hides a split. The **two-lab component (~$90bn, 55% of my total)** is simple arithmetic on reported quarterly figures. Anthropic: Q1 $4.7bn (single report) + Q2 $11.5bn + Q3 $16.8bn + Q4 ~$20.5bn ≈ $53.5bn. OpenAI: $5.7bn + $6.7bn + ~$9.8bn + ~$15bn ≈ $37bn, against the company's own reported plan of **$36bn for 2026** ([Reuters/FT][oaiplan], C). The H1 figures are corroborated by primary anchors (Anthropic's $47bn May run-rate matches Q2; OpenAI's $2bn a month matches Q1). That makes the lab component **C, arguably B for H1**. The hyperscaler anchors are A, but the split between lab and non-lab use is D. Apps, consumer and overlap are D.

## Independent estimate

Method: count each dollar once, at the point where a final customer (consumer, enterprise or advertiser) pays. Count lab revenue in full. Count clouds only for AI sold to non-lab customers. Count apps net of what they pay labs and clouds. Calendar year 2026, USD bn.

| Component | Central | Range | Inputs and assumptions | Grade |
|---|---:|---:|---|---|
| OpenAI, net basis | 37 | 34–39 | Q1 5.7 / Q2 6.7 (C); end-Sep ~$50bn and year-end ≥$70bn run-rate (C); Q3 ≈ average of ~$29bn and $50bn run-rate ÷ 4; Q4 ≈ $60bn ÷ 4; company plan $36bn (C, disputed). Net basis leaves Microsoft-sold Azure OpenAI to the Microsoft row | C |
| Anthropic, gross (customer-paid) basis | 53 | 50–57 | Q1 4.7 (single report), Q2 11.5, Q3 16.8 (C); Q4 ~20.5 from ~$74bn in October and <$100bn at year-end | C |
| Other labs and assistants | 12 | 8–18 | Gemini consumer subscriptions (undisclosed; Menlo puts non-ChatGPT assistants at ~$2.7bn in mid-2025); SpaceX AI segment Q2 $2.561bn, mostly advertising and infrastructure sales (A, via `labs-other.md`), so end-user Grok/API is small; Mistral ~€0.9bn ARR target; Alibaba AI products ~$7.3bn annualized (A×4), part of it compute; other Chinese labs small (Z.AI, MiniMax H1 filings) | D |
| Microsoft AI, excluding OpenAI's purchases | 20 | 12–28 | >$37bn March run-rate (A), probably ~$45–50bn by December; less OpenAI consumption (FY26 revenue from OpenAI $24.1bn, A); 30m Copilot seats (A). **The largest single swing**: if OpenAI's spend is *not* in the metric, add ~$20bn | D |
| AWS AI, excluding Anthropic compute | 10 | 6–15 | >$25bn Q2 run-rate (A) less ~$13–15bn Anthropic (C); chips run-rate treated as overlapping | D |
| Google Cloud AI to non-lab customers | 10 | 6–15 | No AI disclosure; +82% growth includes TPU-system sales and lab capacity (A) | D |
| Oracle, CoreWeave, other neoclouds to non-lab customers | 4 | 2–7 | OCI $7.39bn, +121%, in Q1 FY27 (secondary relay), mostly OpenAI, Meta and Microsoft | D |
| Incumbent software AI attach (excluding Microsoft), net of model costs | 8 | 5–12 | Salesforce, ServiceNow, Adobe as above; SAP, Workday, Intuit, Atlassian and others assumed similar or smaller | D |
| AI-native B2B apps, net of API and cloud spend | 9 | 6–14 | ~$18bn gross assumed (Cursor >$4bn ARR in June, C; Glean $0.3bn, C), ~50% passed to labs and clouds | D |
| Specialized consumer apps, net | 3 | 2–5 | Menlo ~$2.3bn mid-2025, roughly doubled, ~70% retained | D |
| Residual overlaps | −3 | −5 to −1 | Microsoft revenue share, lab-to-lab compute (SpaceX → Anthropic), Bedrock commission | D |
| **Total** | **163** | **126–209** (sum of extremes) | Plausible interval about **$135–200bn**; the two labs are 55% of the central figure | D overall; ~55% C |

On the same method, 2025 comes to about $52bn (labs $17.7bn reported + ~$34bn rest), so growth was **~3.1×** against the note's 3.3×. "Roughly tripled" on the front page holds.

**Comparison with $180B:** the note sits about 10% above my central figure, inside my interval, and about $10bn above my figure plus the Microsoft swing factor. The **$130bn floor is fine**, roughly my sum of lows. The **$230bn ceiling is too high**: it needs every component at its maximum and the Microsoft metric to exclude OpenAI. My verdict: **slightly mis-centred high, with the upper tail too wide.** A defensible restatement is **~$170bn (range $130–210bn)**. With 165–180 the front page's required-growth arithmetic barely moves: (1,600/170)^(1/4)−1 = 75% and (2,700/170)^(1/3)−1 = 151%, against 73% and 147% at $180bn.

## Scenario check

**Observed 2025–26 growth:** about +210–230% for the total; OpenAI ~+185% (13.07 → ~37); Anthropic ~+1,050% (4.6 → ~53); Microsoft AI +123% y/y (March); AWS AI triple-digit (Q2); Google Cloud +82% (Q2, total); Agentforce +240% (with the definition change); Alibaba AI products triple-digit for 12 quarters. **The slowdown is already visible**: Anthropic's quarter-on-quarter growth went 2.45× (Q2) → 1.46× (Q3) → ~1.22× (Q4 implied). Ramp shows token spend flat in August–September, with early October only 1.5% above August.

**The paths start from a calendar-year 2026 figure and ignore the run-rate exiting 2026.** The two labs alone exit at about $160bn (OpenAI ≥$70bn target, Anthropic <$100bn), and my other components add ~$95bn. That gives a **December 2026 run-rate of ~$250bn**; the Q3 2026 annualized pace was ~$180–190bn. Consequences:
- **Bear (130/170/210):** 2027 is ~30% below the exit run-rate and below the Q3 pace; 2028 is still ~16% below the exit. This is a **revenue-contraction stress** (subsidised API use retreating, run-rates proving inflated). That is a legitimate stress case, but "discounting and churn absorb volume gains" and a "27% CAGR" mislabel it.
- **Base (180/300/480):** 2027 is only ~20% above the exit run-rate, i.e. about 5–7% sequential growth a quarter after 25–45% a quarter in 2026; 2028 needs ~10% a quarter. Plausible, and not aggressive given the carry-over.
- **Bull (230/440/800):** consistent with SemiAnalysis/Patel's $600–700bn two-lab run-rate by December 2027 (claim 54), which implies two-lab 2028 revenue alone of ≥$650bn.

**Against the note's outside estimates:**
- **OpenAI's own plan** ($36bn → $350bn by 2030, cumulative $840bn) implies ~$110–120bn in 2028 for OpenAI alone. Add Anthropic on any continued growth and the base path is roughly "the labs hit their plans."
- **Gartner's** ≤$3.6tn cumulative attributable revenue through 2030 sits **between base and bull**. Under my own extension (2029 $720bn, 2030 $1,000bn), the base path sums to ~$2.7tn for 2026–30 and the bull path (1,200 / 1,600) to ~$4.3tn. Scopes differ.
- **IoT Analytics** forecasts a $236bn Microsoft+AWS AI run-rate in Q4 2028. That is **82–123% of the base path's all-owner 2028 band** ($192–288bn) from two owners alone. Either IoT is closer to the bull case, or owner capture runs above 60%.
- **Capture evidence today is above 60%.** Anthropic's compute was ~59% of revenue in Q3 ($1.70 per compute dollar, C) and ~159% in 2025 ($7.33bn on $4.6bn, C). OpenAI's payments to Microsoft alone were ~114% of its revenue (A/C). First-party products such as Copilot are 100% owner revenue. 40–60% is a reasonable *steady-state* band, but 2026–27 capture is higher and is funded by lab equity. The note should say so.

## Omissions

Most of these date from the last 30 days.
- **OpenAI's reported financial plan** (FT via Reuters, Sep 18–19): 2026 revenue $36bn → 2030 $350bn; $856bn compute; $278bn cumulative negative FCF ([Reuters relay][oaiplan], C; `openai.md` grades the plan D as disputed). It is a direct CY2026 anchor for the lab row.
- **OpenAI's year-end target** of ≥$70bn annualized (Bloomberg, Oct 9, via search relay, C), and Axios (Sep 29) on enterprise sales more than doubling since July.
- **Anthropic Q1 2026 $4.7bn** (single secondary report of prospectus figures, C/D), which completes a calendar-2026 sum. Also the reported expectation of a year-end run-rate below $100bn.
- **Microsoft FY26 revenue from OpenAI, $24.1bn** (10-K, A, already in the repo's OpenAI note). This is the most important primary datum for deduplication and the note does not use it. Also: Microsoft did not update its AI run-rate in July.
- **AWS chips run-rate >$25bn**, disclosed separately from AI in the same release (A).
- **Anthropic's $1.70 of revenue per compute dollar** (in the note's own Euronews source), which measures current owner capture.
- **China:** Alibaba AI-related product revenue of $1.824bn in the June quarter, triple-digit growth ([6-K][baba], A). The note says "global" but includes no Chinese revenue.
- **SpaceX AI segment**, Q2 $2.561bn, of which most is infrastructure and advertising (10-Q/8-K, A, in `labs-other.md`). This is a lab-to-lab compute flow (SpaceX/xAI → Anthropic) that a deduplication must remove.
- **App-layer anchors:** Cursor >$4bn ARR in June, then acquired by SpaceX in August (C); ServiceNow's $1.5bn AI ACV target; Adobe AI-first >$0.5bn. These are the actual inputs to row 36.
- **Oracle Q1 FY27** (September): OCI $7.39bn, +121%, >300k GPUs delivered (secondary relays of the 8-K). Oracle is mostly lab and hyperscaler customers and is relevant as intermediate demand.
- **Forthcoming:** Microsoft, Alphabet and Amazon Q3 results (about Oct 27–30) and a public Anthropic S-1. Each could resolve the largest swing factors and belongs in Signals.

## Summary-bullet assessment

1. **"$55bn / $180bn illustrative … $130–230bn."** Honestly labelled, but it should state the composition (about half is the two labs, C) and that an independent payer-based rebuild lands lower (~$165bn) with a narrower upper tail. *Partly supported.*
2. **Lab run-rates.** Correct caution. The "$65bn July reported / $74bn outside estimate, different provenance" framing is not supported by the cited Euronews text, which puts both in a SemiAnalysis sentence. The bullet should give the calendar-2026 sums and OpenAI's year-end target. *Supported with a provenance fix.*
3. **Microsoft / AWS / Google.** Figures are right. It should add that the $37bn is from March and has not been updated. It should also give the reason the figures cannot be summed: they contain the labs' compute purchases ($24.1bn from OpenAI to Microsoft). *Supported; missing the key reason.*
4. **Census / Ramp.** The sentence "remain unreproduced in this cross-check" is review language that has leaked into the Summary. It is also tangential to the size of demand. *Reword.*
5. **Productivity / retention.** Accurate, but it says nothing about the demand total. *Supported; low value in a demand Summary.*
6. **Financing.** Accurate. *Supported.*
7. **$480bn base / 40–60% capture.** Accurate as conditional arithmetic. It should note that current capture exceeds 60% because lab equity funds compute, and that the path starts below the 2026 exit run-rate. *Partly supported.*

## Your assessment

The note is careful, well caveated, and now honest that its totals are assumptions. Its weak point is structural. It sums layers by seller and then subtracts one judgmental overlap, instead of counting by payer. That makes the deduplication impossible to audit and, on the newly visible flows (Microsoft's $24.1bn from OpenAI, Anthropic's AWS and Google compute, Menlo's apps containing lab products), probably too small. A payer-based rebuild from the same public inputs gives ~$165bn. That is close enough that the front page's argument is unaffected: the required growth is 75–150% a year rather than 73–147%. But the stated range should be $130–210bn, not $130–230bn, and the note should say that about half of the figure rests on C-grade lab revenue rather than calling the whole thing D.

I differ from the note in three places. **First**, the scenarios should be anchored to the exit run-rate. Without that, the bear case reads as mild growth when it is actually a ~30% contraction, and the base case looks more demanding than it is. **Second**, observed owner capture is currently above the 40–60% band because lab equity funds compute purchases. This cuts both ways: owner revenue today overstates what final demand alone would support, and the band is a steady-state assumption, not today's take rate. **Third**, Microsoft's AI run-rate is the largest single unknown in the 2026 total, worth about ±$20bn. Microsoft's late-October results should be treated as the next resolving datum.

## Recommended edits

1. **Summary bullet 1:** replace with: "Paid AI demand is substantial, but capital payback remains unproven. Our illustrative estimate of deduplicated end-user AI revenue is ~$55bn for 2025 and ~$170bn for 2026 (range $130–210bn). About half of 2026 is OpenAI and Anthropic revenue summed from reported quarterly figures (C); the rest is allocation (D). An independent payer-based rebuild gives ~$165bn ([Claude cross-check](/reviews/demand-side-claude-xcheck))." Change CSV row `reconstruction,2026,deduplicated_end_user_total` to 170, base 2026 to 170 and bull 2026 to 210. Leave bear 2026 at 130.
2. **Rows 34–38: rebuild by payer.** Replace the four seller segments and the single overlap with the component table in "Independent estimate" above: OpenAI net; Anthropic gross; other labs; each hyperscaler excluding lab purchases; neoclouds excluding lab purchases; incumbent attach net; AI-native apps net; consumer apps net; residual overlap. Each row should carry its own grade. Add to Analysis: "Cloud AI metrics contain the labs' own compute purchases: Microsoft's FY26 revenue from OpenAI was $24.1bn (10-K, A), and Anthropic is reported at 8–9% of AWS revenue (C). These are intermediate flows, so cloud AI is counted only for non-lab customers."
3. **Add claim rows:** (a) "OpenAI 2026 revenue plan $36bn; 2030 $350bn; reported, unverified, disputed | Sep 18–19, 2026 | Reuters/FT | secondary | C". (b) "OpenAI expects ≥$70bn annualized by year-end 2026 | Oct 9 | Bloomberg | secondary | C". (c) "Anthropic Q1 2026 revenue $4.7bn; CY2026 ≈ $53bn (Q1–Q3 reported + Q4 assumed) | secondary + arithmetic | C". (d) "Microsoft FY26 revenue from OpenAI $24.1bn | 10-K | A". (e) "AWS chips run-rate >$25bn, separate from AI | Q2 release | A". (f) "Alibaba AI-related product revenue $1.824bn, June quarter | 6-K | A". (g) "Anthropic $1.70 revenue per compute dollar, Q3 | Euronews/Bloomberg | C".
4. **Row 2 and Summary bullet 2:** replace "Anthropic's reported ~$65bn July run-rate and outside ~$74bn SemiAnalysis estimate cited on October 15 are a dated sequence, not a range" with "Euronews (Oct 15), citing SemiAnalysis, puts Anthropic's run-rate at ~$65bn in late July and ~$74bn in October; reported quarterly revenue was $11.5bn (Q2) and $16.8bn (Q3), and the year-end run-rate is reportedly expected below $100bn."
5. **Row 36:** append: "Menlo's $19bn applications figure includes ChatGPT Enterprise, Claude for Work and Microsoft Copilot (copilots $7.2bn), already counted in the lab and Microsoft rows, and is gross of app companies' API payments. Disclosed incumbent AI ARR is small (Salesforce ~$3.9bn including Data 360; ServiceNow ~$1.5bn 2026 ACV target)."
6. **Row 37:** append: "Menlo attributes 81% of its $12bn consumer market to general assistants, leaving ~$2.3bn for specialized apps in mid-2025; the $5bn 2025 allocation is about twice that anchor." Lower it to ~$3bn (2025) and ~$5bn gross / ~$3bn net (2026).
7. **Scenario section:** add after the table: "Because revenue rose steeply through 2026, the December 2026 exit run-rate (~$250bn: OpenAI ≥$70bn target, Anthropic <$100bn, others ~$95bn; C/D) is well above the calendar-year figure. The bear path's 2027 value is ~30% below that exit rate and below the Q3 2026 annualized pace, so it is a revenue-contraction stress. The base path's 2027 value is ~20% above the exit rate, i.e. quarterly growth slowing from 25–45% in 2026 to ~5–7%." Rename the bear assumption to "Contraction: subsidised API use retreats and run-rates prove inflated; revenue falls from the 2026 exit rate before recovering."
8. **Capture paragraph:** add: "Observed capture is currently above this band: Anthropic's compute was ~59% of Q3 revenue (C), OpenAI's payments to Microsoft alone were ~114% of its revenue over July 2025–June 2026 (A/C), and first-party products such as Copilot are 100% owner revenue. Lab equity funds the gap, so 40–60% is a steady-state assumption, not today's take rate."
9. **Outside-estimates paragraph:** add: "IoT Analytics' Microsoft+AWS Q4-2028 AI run-rate forecast alone ($236bn) equals 82–123% of the base path's all-owner 2028 band ($192–288bn), so IoT sits nearer the bull path or implies capture above 60%. Extended to 2030, Gartner's ≤$3.6tn cumulative ceiling lies between our base (~$2.7tn) and bull (~$4.3tn) paths."
10. **Summary bullet 3:** append: "Microsoft has not updated the $37bn figure since April. Cloud AI metrics include the labs' compute purchases (Microsoft's FY26 revenue from OpenAI was $24.1bn), which is why they cannot be added to lab revenue."
11. **Summary bullet 4:** replace the last sentence with "October Census values were extracted from the API by the original author but have not been independently reproduced (claim 11)."
12. **Signals table:** add "Hyperscaler Q3 disclosures (Oct 27–30): updated Microsoft AI run-rate and its OpenAI content; AWS AI vs chips; any Google Cloud AI figure" and "Public Anthropic/OpenAI S-1: gross vs net, channel mix, compute paid to each cloud".
13. **Front page (`report/index.md`, Part 2),** for the lead to apply: replace "against a grade-D estimate of about $180B in 2026" with "against an estimate of about $170B in 2026 (range $130–210B; about half is the two labs' reported revenue, C, the rest allocation, D)" and "roughly 70-150% a year" with "roughly 75-150% a year". "It roughly tripled in 2026" can stay (~3.1×).

[eu]: https://www.euronews.com/2026/10/15/anthropic-revenue-jumps-46-to-168bn-as-ai-firm-eyes-record-2-trillion-ipo-valuation
[ms3]: https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3
[ms4]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm
[goog]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[amzn]: https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
[crm]: https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
[menlo]: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
[menloc]: https://menlovc.com/wp-content/uploads/2025/11/menlo_ventures_consumer_ai_report-2025.pdf
[ant]: https://www.anthropic.com/news/series-h
[oaiplan]: https://gvwire.com/2026/09/19/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports/
[baba]: https://www.sec.gov/Archives/edgar/data/0001577552/000110465926099220/tm2623667d1_ex99-1.htm

Other leads from search relays only (not fetched; trace to primary before use): Axios Sep 29 (~$70bn OpenAI), Bloomberg Oct 9 (≥$70bn year-end target), WSJ/The Information (OpenAI Q1 $5.7bn, Q2 $6.7bn), Implicator (Anthropic Q1 $4.7bn), Om Malik (Copilot share of Microsoft AI), the analyst estimate of Anthropic's share of AWS, Cursor ARR (Dealroom/Forbes), ServiceNow and Adobe AI figures, Oracle Q1 FY27 relays.
