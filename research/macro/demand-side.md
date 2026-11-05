# AI demand: can end-user revenue service the buildout?

*Last updated: 2026-10-25 · Cross-checked by: Codex gpt-6-astra, Claude Opus 5.5 · Data: [ai-revenue-estimates.csv](/data/ai-revenue-estimates.csv)*

## Summary

- Paid AI demand is large and fast-growing; payback is unproven. Our deduplicated estimate of end-user AI product revenue is ~$55B for 2025 and **~$170B for 2026 (range $130–210B)**: roughly a tripling (claims 1, 3).
- About $90B of the 2026 figure is the two labs' reported-quarter reconstruction, OpenAI $37B plus Anthropic $53B (C, later quarters assumed). The rest is allocation (D). The components sum to $163B; the headline adds $7B of coarse upward rounding, not measured sales (claims 1–5).
- Revenue rose steeply through 2026, so the modeled December exit run-rate is ~$250B. The base path then needs +76.5% in 2027 and +60.0% in 2028 to reach $480B; the bear path is a contraction (claims 30–32).
- Against payback hurdles the gap is not measured. A hypothetical $750B cohort needs $295–468B of annual owner revenue. At 40–60% owner capture, base 2028 gives owners $192–288B. Asset populations and timing are not matched, so this is not an observed shortfall (claims 29, 33).
- Adoption is broad but measured on different populations: Census 19.8% of employer businesses (May 2026), Ramp 55.9% paid adoption among its customers (September). Ramp token spend was roughly flat in August–September, then rebounded (claims 16–18).
- Value evidence is mixed. Task studies show gains (+15% service, +26.08% coding); METR found a 19% slowdown; in Bain's survey 40% of savings-measurers saved ≤10%; AI consumer apps retain worse than non-AI apps (claims 22, 25, 28).
- Outside estimates disagree by an order of magnitude because they measure different things: Gartner's $8.5T required versus ≤$3.6T attributable through 2030; IoT Analytics' returns above hurdle now, negative by 2031; SemiAnalysis' $600–700B two-lab path by December 2027 (claims 35–37).
- Biggest uncertainty: no audited lab accounts, no invoice bridge across labs, clouds and apps, and no measured owner share of end-user spending.

## Key claims

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Model: 2026 deduplicated end-user AI revenue, headline | ~$170B; range $130–210B is a judgment band, not a confidence interval. Two-lab ~$90B (claims 4–5) is about half | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D overall; $90B two-lab part C |
| 2 | Model: component sum and rounding | 37 + 53 + 12 + 44 + 20 − 3 = $163B (claims 4–9); an independent payer-based rebuild quoted it as about $165B. Headline adds $7B coarse upward rounding, not an economic component. Sum of component extremes $126–209B | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D |
| 3 | Model: 2025 backcast | $55B = OpenAI $13.07B + Anthropic $4.6B (reported, unverified) + specialized consumer apps $3B + $34.33B balancing remainder for other labs, clouds and apps. Independent same-method backcast ~$52B | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv), [Zitron, OpenAI financials][S3], [Euronews, Anthropic revenue][S2] | secondary (model) | C lab inputs; D remainder |
| 4 | Model: OpenAI CY2026 sales, net basis, reported, unverified | $37B central, $34–39B. Q1 $5.7B + Q2 $6.7B (H1 $12.4B reported) + assumed Q3 $9.8B + Q4 $14.8B. Near the disputed reported plan of $36B for 2026. Azure-sold partner revenue left with Microsoft | 2026-10-18 | [Zitron, reporting compilation][S4], [Reuters via GV Wire, OpenAI plan][S49], [Axios, OpenAI run-rate][S1], [Investing.com, OpenAI target][S50] | secondary (model) | C; later quarters assumed |
| 5 | Model: Anthropic CY2026 sales, gross basis, reported, unverified | $53B central, $50–57B. Q1 $4.7B + Q2 $11.5B (Reuters: $11.6B) + Q3 $16.8B + assumed Q4 $20.0B. Partner gross sales included. Reported H1 $16.3B matches the Reuters quarters | 2026-10-18; H1 reported 2026-10-20 | [Euronews, Anthropic revenue][S2], [Reuters via Investing.com, Anthropic Q3][S51], [Investing.com/WSJ, draft S-1][S65] | secondary (model) | C; Q4 assumption D |
| 6 | Model: other labs and assistants | $12B, $8–18B. Gemini paid subscriptions, Chinese AI products, end-customer Grok/API. Alibaba's AI-related products were $1.824B in the June quarter but include cloud products. SpaceX's AI segment includes infrastructure and acquired Cursor revenue ([other labs note](/research/stack/labs-other)); lab-to-lab sales are not added again | CY2026 assumption, 2026-10-18 | [Alibaba 6-K][S53], [Menlo, consumer AI][S11] | secondary (model) | D |
| 7 | Model: cloud AI sold to non-lab customers | $44B = Microsoft $20B ($12–28B) + AWS $10B ($6–15B) + Google Cloud $10B ($6–15B) + Oracle, CoreWeave and others $4B ($2–7B). Anchors: Microsoft AI run-rate >$37B (March 2026, includes apps), Microsoft FY26 revenue from OpenAI $24.1B including revenue share (~114% of reconstructed OpenAI Jul 2025–Jun 2026 sales of ~$21.17B); AWS AI run-rate >$25B with an overlapping >$25B chips run-rate; Google Cloud Q2 $24.768B, +82%, including TPU hardware and ordinary cloud; Oracle OCI ~$7.4B, +121%, not AI-only. Anthropic estimated at 8–9% of Q1 AWS revenue (commentary). Largest sensitivity: if OpenAI purchases sit outside Microsoft's metric, the headline could rise ~$20B | CY2026 assumption, 2026-10-18 | [Microsoft FY26 Q3 call][S5], [Microsoft 10-K][S52], [Amazon Q2 release][S8], [Alphabet Q2 8-K][S7], [Oracle Q1 FY27][S61], [HK MoneyClub, AWS commentary][S59] | primary anchors / model | A anchors; C ratio; D allocation and AWS share |
| 8 | Model: applications and consumer apps, net of model and cloud costs | $20B = incumbent attach ex-Microsoft $8B ($5–12B) + AI-native B2B $9B ($6–14B; ~$18B gross, ~50% passed upstream) + specialized consumer $3B ($2–5B; ~$5B gross, 60–70% retained). Anchors: Salesforce Agentforce ARR >$1.5B (~$3.9B with Data 360, definition broadened); ServiceNow 2026 AI ACV target $1.5B; Adobe AI-first ARR >$0.5B; Glean ARR $0.3B; Cursor >$4B annualized in early June (reported, unverified). Menlo assigns 81% of its $12B consumer market to general assistants, leaving ~$2.3B specialized | CY2026 assumption, 2026-10-18 | [Salesforce Q2 FY27][S9], [ServiceNow, AI ACV][S55], [Adobe Q2 FY26][S56], [Glean, ARR][S57], [Forbes, Cursor][S58], [Menlo, consumer AI][S11] | primary anchors / model | A anchors; C Cursor and Menlo; D allocation |
| 9 | Model: residual overlaps | −$3B, range −$5B to −$1B: revenue share, distribution commissions, lab-to-lab compute; no invoice bridge | CY2026 assumption, 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D |
| 10 | Menlo enterprise GenAI spend | 2025 $37B; applications $19B, of which $7.2B copilots (ChatGPT Enterprise, Claude for Work, Microsoft Copilot) already counted in lab and Microsoft rows; gross of API costs; excludes inference and embedded features | 2025-12 | [Menlo, enterprise GenAI][S10] | primary | C |
| 11 | OpenAI annualized revenue, reported, unverified | ~$50B net at end-September (~$70B gross equivalent); target ≥$70B annualized by December | 2026-09 / 2026-10-19 | [OpenAI note](/research/stack/openai), [Axios, OpenAI run-rate][S1], [Investing.com, OpenAI target][S50] | secondary | C |
| 12 | Anthropic annualized revenue, reported, unverified | ~$65B late July → ~$74B October (both SemiAnalysis via Euronews); year-end expected <$100B; Reuters relays analysts' $110B | 2026-10-15 | [Anthropic note](/research/stack/anthropic), [Euronews, Anthropic revenue][S2], [Reuters via Investing.com][S51] | secondary | C |
| 13 | Anthropic Q3 economics, reported, unverified | Q3 revenue $16.8B; 11% adjusted operating margin, positive adjusted FCF; $1.70 revenue per compute dollar (~58.8% compute/revenue). No public adjusted-to-GAAP or cash reconciliation | 2026-Q3 | [Anthropic note](/research/stack/anthropic), [Euronews, Anthropic revenue][S2] | secondary | C |
| 14 | Meta: AI in advertising, unquantified | Q3 revenue +26%; management says AI already delivers substantial incremental ad revenue, with no dollar amount; Q3 FCF −$2.1B | 2026-Q3 | [Meta note](/research/stack/meta), [Meta Q3 release][M1] | primary | A disclosure; AI contribution unquantified |
| 15 | ChatGPT paid reach | >50M subscribers and >900M weekly users (March); >1B weekly users and 2.5M businesses (September), no new subscriber count; ads $1B annualized (August) | 2026-09-08 | [OpenAI, March update][S21], [OpenAI, September update][S45], [OpenAI, ads][S22] | primary | A (unaudited) |
| 16 | Census BTOS business AI use | Verified: 19.8% of employer businesses (May 3); wording broadened Nov 2025. October extraction (to Oct 4): 23.8% current (SE 0.41pp), 27.7% expected, not independently reproduced | 2026-05-03 / 2026-10-04 | [Census, AI use story][S14], [Census BTOS API][S13], [Census, release page][S41] | primary | A May; October A retained, unverified |
| 17 | Ramp paid adoption | 55.9% of customers; Anthropic 43.8%, OpenAI 40.6%; +0.62pp m/m | 2026-09 | [Ramp AI Index, October][S15] | primary | A (sample only) |
| 18 | Ramp AI spending | Token spend roughly flat Aug–Sep; September top-cohort spend/employee $9,568, +11.7% m/m but 3.1% below July's $9,873; early-October spend peak 1.5% above August; small cohort, revised after vendor additions | 2026-10-14 | [Ramp AI Index, October][S15] | primary | A (sample only) |
| 19 | Ramp spend concentration | Top 1% of firms drive 80% of OpenAI/Anthropic spend | 2026-09 | [Ramp AI Index, October][S15] | primary | A (sample only) |
| 20 | CloudZero bill share and budgets | Median AI share of cloud bills 2.66% (Aug) → 3.02% (Sep), 422 same-store organizations; separate survey of 252 finance leaders: 87% plan higher FY2027 AI budgets, 10% call funding net-new | 2026-10-14 | [CloudZero, AI Economics Pulse][S42] | primary | A (samples) |
| 21 | McKinsey adoption versus returns | 88% regular AI use; 39% report enterprise EBIT impact; about one-third scaling | 2025-11-05 | [McKinsey, state of AI][S16] | primary | A (self-reports) |
| 22 | Bain savings survey | 951 large companies; 40% of savings-measurers saved ≤10%; 44% cite targeted savings as funding | 2026-06-01 | [Bloomberg via Insurance Journal, Bain][S17] | secondary | C |
| 23 | MIT NANDA "95% zero return" | >300 public initiatives, 52 interviews, 153 leaders; funnel 60% evaluated / 20% piloted / 5% implemented; no representative frame | 2025-07 | [MIT NANDA, GenAI Divide][S18] | primary | D (as a general failure rate) |
| 24 | Morgan Stanley CIO surveys | 81% of 100 CIOs expect production AI by end-2026; latest IT budget growth 4.0% vs 3.8% prior quarter (summary only) | 2026-02-11 / 2026-Q3 | [Morgan Stanley, AI Rate of Change][S19], [Macrostream summary][S20] | primary / tertiary | A intentions; D budget |
| 25 | Task-level productivity studies | Customer service +15% issues/hour (5,172 agents); coding +26.08% completed tasks, SE 10.3% (4,867 developers); METR 19% slower (16 developers, 246 tasks), later design has selection problems | 2024-11 / 2026 / 2026-02 | [Brynjolfsson et al.][S23], [Jaffe, research][S24], [METR, trial][S25], [METR, update][S26] | primary | A (studied settings) |
| 26 | Token volumes, incompatible scopes | Google >3.2 quadrillion monthly (May 2026); OpenRouter 128.4 trillion weekly (Sep 2026); Microsoft >300 customers on track for >1 trillion/year each | 2026-09 | [Google I/O][S28], [OpenRouter][S29], [Microsoft FY26 Q3 call][S5] | primary | A (company metrics) |
| 27 | AI app gross margins | Bessemer selected "supernovas" ~25%, "shooting stars" ~60% | 2025 | [Bessemer, State of AI][S30] | primary | C |
| 28 | Consumer-app durability | 12-month annual-plan retention AI 21.1% vs non-AI 30.7%; monthly 6.1% vs 9.5%; first-year revenue/payer $30.16 vs $21.37 | 2026 | [RevenueCat, subscription apps][S31] | primary | A (sample) |
| 29 | Hypothetical cohort payback | $750B new cohort needs $295B (six-year equipment life) to $468B (three-year) annual owner revenue at 50% EBITDA margin, 10% discount rate; $1.36T needs $536–848B. Not existing cohorts' remaining requirement | 2026-10-17 | [Unit-economics note](/research/theory/ai-unit-economics#a-worked-model) | secondary (model) | D inputs; arithmetic reproducible |
| 30 | Model: conditional end-user paths | 2026/27/28: contraction $130/170/210B; base $170/300/480B; bull $210/440/800B; cumulative 2026–28 $510B/$950B/$1,450B | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D |
| 31 | Model: growth implied by paths | Base +76.5% (2027), +60.0% (2028); 2026–28 CAGR contraction/base/bull 27.1%/68.0%/95.2%. Endpoints chosen, not derived | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D |
| 32 | Model: December 2026 exit run-rate | ~$250B = OpenAI ≥$70B target + Anthropic assumed ~$85B + others ~$95B; assumed Q3 pace ~$180–190B. Contraction 2027 ~32% below exit, 2028 ~16% below; base 2027 ~20% above. Smooth bridge ~5–7% a quarter, against ~25–45% quarterly lab growth in 2026 | 2026-10 | [CSV](/data/ai-revenue-estimates.csv), [Investing.com, OpenAI target][S50], [Euronews, Anthropic revenue][S2] | secondary targets / model | C targets; D aggregate |
| 33 | Model: owner-capture sensitivity | 40–60% of end-user dollars to infrastructure owners (assumed). 2028 owner revenue: contraction $84–126B, base $192–288B, bull $320–480B | 2026-10-17 | [CSV](/data/ai-revenue-estimates.csv) | secondary (model) | D |
| 34 | Published required-revenue estimates | Sequoia $600B; JPMorgan $650B at 10% return; Goldman ~$300B breakeven / $417B infrastructure at 10% ROIC / ~$1T applications; Bain $2T by 2030 | 2024–2026 | [Sequoia][S34], [JPMorgan AM][S35], [AdvisorAnalyst, Goldman summary][S36], [Bain][S37] | primary / secondary | A stated; C Goldman |
| 35 | Gartner infrastructure-payback scenario | $8.5T owner revenue required through 2030 at 12% ROIC vs ≤$3.6T attributable to AI data centers; owners earn < half of AI revenue; >$3.5T exposed to impairment by 2030 | 2026-10-14 | [Gartner, impairment forecast][S38] | primary | A stated; C outcomes |
| 36 | IoT Analytics hyperscaler payback | Returns above 15% pre-tax hurdle now, below from 2028, negative by 2031; absorbable write-downs. Microsoft+AWS Q4-2028 annualized revenue needed $270B vs $236B forecast | 2026-10-06 | [IoT Analytics, AI bubble analysis][S70] | primary | A model stated; C results |
| 37 | SemiAnalysis two-lab path | $600–700B combined OpenAI+Anthropic revenue by December 2027; endpoint run-rate, not booked CY2027 sales | 2026-10-12 | [Big Technology transcript][S71] | secondary | C |
| 38 | SemiAnalysis revenue per MW | Anthropic revenue up to $50M/MW versus ~$10–15M/MW compute cost (inference economics); end-2027 $70–80M/MW company-blended | 2026-08-25 | [Dwarkesh, Patel interview][S72] | primary interview | A attribution; C economics |
| 39 | Model: outside-estimate positioning | IoT $236B / base 2028 owner $192–288B = 82–123%; base extended to 2029/30 at $720B/$1,000B gives $2.670T for 2026–30; bull $1,200B/$1,600B gives $4.250T; Gartner ≤$3.6T lies between | 2026-10-18 | [CSV](/data/ai-revenue-estimates.csv), [IoT Analytics][S70], [Gartner][S38] | derived | B arithmetic; D extensions |

Type: primary / secondary / tertiary. Grade: A–D (see [methodology](/report/methodology)).

## Analysis

**How the $170B is built.** Final spending comes from operating budgets, households and advertisers. App, lab and cloud sales overlap, so supplier invoices cannot be added. The reconstruction counts each final dollar once, by payer. Lab receipts count on each lab's own convention: OpenAI nets certain partner sales; Anthropic books them gross (claims 4–5). Clouds count only AI sold to non-lab customers, because cloud AI figures include the labs' compute purchases: Microsoft's FY26 revenue from OpenAI alone was $24.1B (claim 7). Apps count net of payments to labs and clouds already counted upstream (claim 8). Menlo's $19B of 2025 applications includes $7.2B of copilots already in the lab and Microsoft rows, and is gross of API costs (claim 10). The components sum to $163B; the ~$170B headline is deliberate coarse rounding (claim 2). Every input and range is in the CSV. It is an allocation, not an invoice census; residual overlaps remain D.

The two-lab $90B is half the headline and is C: reported private financials, with OpenAI's H2 and Anthropic's Q4 assumed. The single largest swing is Microsoft's metric: if OpenAI's purchases sit outside it, the headline could rise ~$20B (claim 7).

The boundary leaves two things out. Supplier-invoice elimination does not exclude externally financed training or subsidy-funded use. And internal savings and ad gains can fund owned infrastructure without appearing as sold AI products. Meta attributes substantial incremental ad revenue to AI but gives no dollar figure, while its Q3 FCF was −$2.1B (claim 14). The narrow product numerator cannot settle returns on broad corporate capex.

**Adoption and realized value.** Census measures employer businesses' reported use (19.8% in May); Ramp measures payments among its customers (55.9%). The populations differ and the gap is not decomposed (claims 16–17). Ramp's flat August–September token spend is offset by its own September rebound (+11.7% m/m) and an early-October peak 1.5% above August; CloudZero's AI bill share rose from 2.66% to 3.02% (claims 18, 20). Neither panel supports a market-wide stall, and neither measures absolute dollars economy-wide. CloudZero's survey shows 87% planning higher budgets but only 10% net-new funding: expansion and substitution at once.

Value evidence is uneven. Task studies show gains in service and coding, METR a slowdown in one setting (claim 25). McKinsey's 88% use versus 39% EBIT impact, and Bain's small savings, challenge self-financing (claims 21–22). MIT NANDA's 95% headline lacks a representative frame (claim 23). Token growth is extraordinary, but the three series have incompatible scopes, and tokens do not convert automatically into dollars (claim 26). AI consumer apps monetize better but retain worse (claim 28); selected app margins of ~25% challenge software-style economics (claim 27).

**Paths and payback.** The paths are stress scenarios, not forecasts (claim 30). The ~$250B exit run-rate sits above calendar-year sales, so the contraction case's $170B for 2027 is ~32% below exit (claim 32). The base path's +76.5% and +60.0% follow from chosen endpoints, not from the deployment narrative (claim 31).

Owners capture part of final spending. A 40–60% steady-state capture is assumed, not observed (claim 33). Today owner receipts can exceed that band: Anthropic's compute is ~58.8% of revenue, Microsoft's receipts from OpenAI are ~114% of OpenAI's overlapping-period sales (including revenue share), and lab equity funds supplier receipts above final revenue (claims 7, 13). Base 2028 gives owners $192–288B, below the $536–848B a hypothetical $1.36T new cohort would need (claim 29). The populations, lives and timing are not matched, so this is not a measured 2028 gap. At 60% capture the bull case's $480B clears Goldman's $417B; at 40%, its $320B does not (claims 33–34).

Outside estimates differ by scope. Gartner is cumulative through 2030 and owner-attributable; IoT models two owners' run-rates; SemiAnalysis forecasts lab revenue, not owner receipts (claims 35–38). IoT's $236B for Microsoft and AWS alone is 82–123% of our all-owner base 2028 band, so IoT sits nearer bull or implies capture above 60%. Gartner's ≤$3.6T lies between our base and bull 2026–30 extensions (claim 39). Each needs something to hold: Gartner, that the buildout persists with weak capture; IoT, that losses are absorbed without a financing cascade; SemiAnalysis, that paid revenue per unit of capacity survives expansion and competition.

## Open questions

- **Market total.** No verified allocation or elimination bridge exists; later lab quarters are assumed. The independent same-method backcast gives ~$52B for 2025 against our ~$55B (claim 3).
- **Anthropic quarters and exit.** Reuters' Q2 $11.6B versus Euronews' $11.5B; reported H1 $16.3B matches Reuters. Year-end below $100B (Euronews) versus $110B (Reuters analysts) (claims 5, 12).
- **Capture.** Whether current owner receipts above 60% persist once external funding slows (claims 7, 13, 33).
- **AWS allocation.** The Anthropic share of AWS rests on indirect commentary (claim 7).
- **Census October values.** Not independently reproduced; access failure is not evidence of error (claim 16).
- **Lab profitability.** Adjusted Q3 profit is not reconciled to GAAP or cash (claim 13).
- What would settle these: a public lab S-1 with gross/net sales and cloud payments; AI-only cloud revenue net of lab purchases; representative enterprise renewal data.

## Signals to watch

| Signal | Current value | As of | Why it matters |
|--------|---------------|-------|----------------|
| Lab booked sales | OpenAI ~$50B net run-rate; Anthropic Q3 $16.8B | 2026-10 | Common-period booked sales and cash would replace the C reconstruction |
| December exit run-rate | Modeled ~$250B; OpenAI target ≥$70B | 2026-10 | Sets whether the bear path is contraction or slow growth |
| Census national AI use | 19.8% verified; 23.8% unreproduced | 2026-10-04 | Broadest population measure of business use |
| Ramp AI spending | Flat Aug–Sep, then +11.7% m/m | 2026-10-14 | Sustained expansion inside customers versus a stall |
| CloudZero bill share and budgets | 3.02%; 10% net-new funding | 2026-10-14 | Separates incremental demand from budget substitution |
| Cloud AI net of lab purchases | Microsoft >$37B, AWS >$25B run-rates | 2026-Q2 | The largest allocation swing in the headline |
| Savings realization | Bain: 40% of measurers save ≤10% | 2026-06 | Renewals funded by realized savings support base and bull |
| App durability | AI annual retention 21.1% vs 30.7% | 2026 | Weak renewal means paid acquisition must keep demand up |

[S1]: https://www.axios.com/2026/10/08/openai-50-billion-arr-anthropic-revenue-accounting
[S2]: https://www.euronews.com/2026/10/15/anthropic-revenue-jumps-46-to-168bn-as-ai-firm-eyes-record-2-trillion-ipo-valuation
[S3]: https://www.wheresyoured.at/exclusive-openai-financials/
[S4]: https://www.wheresyoured.at/annualized-enron-rate/
[S5]: https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3
[S7]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[S8]: https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
[S9]: https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
[S10]: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
[S11]: https://menlovc.com/wp-content/uploads/2025/11/menlo_ventures_consumer_ai_report-2025.pdf
[S13]: https://www.census.gov/hfp/btos/api/periods/110/data
[S14]: https://www.census.gov/library/stories/2026/05/ai-use-businesses.html
[S15]: https://ramp.com/data/ai-index-oct-2026
[S16]: https://www.mckinsey.com/featured-insights/artificial-intelligence/the-state-of-ai-2025
[S17]: https://amp.insurancejournal.com/news/national/2026/06/01/871951.htm
[S18]: https://www.artificialintelligence-news.com/wp-content/uploads/2025/08/ai_report_2025.pdf
[S19]: https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_AI-Rate-of-Change.pdf
[S20]: https://www.macrostream.ai/articles/6ace4b45f30e248c42412429
[S21]: https://openai.com/index/accelerating-the-next-phase-ai/
[S22]: https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/
[S23]: https://arxiv.org/abs/2304.11771
[S24]: https://soniajaffe.com/research
[S25]: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[S26]: https://metr.org/blog/2026-02-24-uplift-update/
[S28]: https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
[S29]: https://openrouter.ai/data/newsletter/the-token-state-of-play
[S30]: https://www.bvp.com/atlas/the-state-of-ai-2025
[S31]: https://www.revenuecat.com/state-of-subscription-apps
[S34]: https://www.sequoiacap.com/article/ais-600b-question/
[S35]: https://am.jpmorgan.com/au/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/evaluating-ai/
[S36]: https://advisoranalyst.com/2026/10/15/ai-capex-required-revenues-and-what-the-market-is-actually-pricing.html/
[S37]: https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/
[S38]: https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030
[S41]: https://www.census.gov/hfp/btos/data_downloads
[S42]: https://www.cloudzero.com/blog/ai-economics-pulse-october-2026/
[S45]: https://openai.com/index/the-work-now-within-reach/
[S49]: https://gvwire.com/2026/09/19/openai-forecasts-cash-burn-near-280-billion-by-2030-ft-reports/
[S50]: https://www.investing.com/news/stock-market-news/openai-expects-to-reach-70-bln-revenue-by-end2026-bloomberg-reports-4940179
[S51]: https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208
[S52]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/R11.htm
[S53]: https://www.sec.gov/Archives/edgar/data/1577552/000110465926099220/tm2623667d1_ex99-1.htm
[S55]: https://www.servicenow.com/uk/workflow/news/servicenow-is-fortune-500-company-fourth-year.html
[S56]: https://www.sec.gov/Archives/edgar/data/796343/000079634326000109/adbeex991q226.htm
[S57]: https://www.glean.com/press/glean-surpasses-300m-arr-unrivaled-enterprise-context-fuels-ai-adoption
[S58]: https://www.forbes.com/sites/richardnieva/2026/06/08/cursor-4-billion-annualized-revenue/
[S59]: https://www.hkmoneyclub.com/en/2026/06/24/amazon-fell-behind-on-ai-can-it-stage-a-comeback/
[S61]: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/
[S65]: https://uk.investing.com/news/stock-market-news/anthropic-revenue-hits-163-billion-as-preliminary-s1-outlines-ipo-risks--wsj-4920764
[S70]: https://iot-analytics.com/why-there-is-no-ai-bubble-analysis/
[S71]: https://ceointerviews.ai/interview/3018643/
[S72]: https://www.dwarkesh.com/p/dylan-patel-3
[M1]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm
