# AI demand: can end-user revenue service the buildout?

*Last updated: 2026-10-17 · Author: Codex / GPT-6 · Status: reviewed · Reviewer: Codex (gpt-6-astra) cross-check, applied 2026-10-17*

## Summary

- Paid AI demand is substantial, but capital payback remains unproven. Our illustrative AI-product spending assumptions are $55bn for 2025 and $180bn for 2026, with $130–230bn used for 2026 scenarios; these are not independently measured market totals (claims 34–39).
- Lab run-rates require accounting reconciliation: OpenAI's reported ~$50bn net at end-September 2026 differs from Anthropic's gross presentation. Anthropic's reported ~$65bn July run-rate and outside ~$74bn SemiAnalysis estimate cited on October 15 are a dated sequence, not a range. These private financials remain reported, unverified. [Axios][S1], [Euronews][S2].
- Microsoft reported an AI run-rate above $37bn for the March 2026 quarter; AWS reported above $25bn for Q2. Google Cloud recorded $24.768bn in Q2 revenue, including non-AI services and TPU hardware; these overlapping measures cannot be summed as end-user AI demand. [Microsoft][S5], [AWS][S8], [Alphabet][S7].
- Census's verified May 3, 2026 observation was 19.8% business AI use; Ramp recorded 55.9% paid adoption in September 2026. Census measures employer businesses' reported use; Ramp measures payments among its customers, so the rates are not directly comparable. The note's later Census values remain unreproduced in this cross-check (claim 11). [Census][S14], [Ramp][S15].
- A November 2024 study found 15% more issues resolved per hour among 5,172 support agents. RevenueCat's 2026 consumer-app sample reports 12-month annual-plan retention of 21.1% for AI apps versus 30.7% for non-AI apps; neither result establishes enterprise-wide cash returns. [Study][S23], [RevenueCat][S31].
- Anthropic announced $65bn of equity funding in May 2026; CoreWeave issued $4.2bn of convertible senior unsecured debt in September. Both equity and debt finance the buildout; loss allocation depends on leverage, guarantees and contracts, while audited standalone lab profitability remains unresolved (claims 44–47). [Anthropic][S43], [SEC][S44].
- The illustrative base path assumes $480bn of end-user revenue in 2028 and $192–288bn of infrastructure revenue at 40–60% capture. Comparison with a hypothetical capital-recovery model does not establish the actual buildout's payback gap (claims 33, 39–40).

## Key claims

US dollars; bn = billion, tn = trillion. **A** verifies a primary-source statement, not a forecast outcome. **C/D totals are estimates.** Accessed **2026-10-17** throughout. “Model” rows disclose assumptions informed by fetched sources.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | OpenAI annualized revenue, reported, unverified | ~$50bn net; ~$70bn gross equivalent | End-Sep 2026 | [Axios][S1] | secondary | C |
| 2 | Anthropic revenue, reported, unverified | Reported run-rate ~$65bn in late July 2026; outside SemiAnalysis estimate ~$74bn cited Oct 15; Q3 $16.8bn; Q2 $11.5bn; 2025 $4.6bn | 2026-10-15 reporting, respective financial periods | [Euronews, citing Bloomberg and SemiAnalysis][S2] | secondary | C |
| 3 | OpenAI booked revenue, reported, unverified | 2025 $13.07bn; H1 2026 $12.4bn, including Q2 $6.7bn | 2026-06 / Oct | [Zitron financial reporting][S3], [compilation][S4] | secondary | C |
| 4 | Microsoft monetization | AI run-rate >$37bn, +123% y/y; M365 Copilot >30m paid seats | Mar / Jun 2026 | [Call][S5], [8-K][S6] | primary | A |
| 5 | Google Cloud, not AI-only | Q2 revenue $24.768bn, +82%; operating income $8.814bn; includes TPU-system product sales and services; shared AI R&D partly outside segment | Q2 2026 | [8-K][S7] | primary | A (segment disclosures) |
| 6 | AWS | AI run-rate >$25bn; total AWS revenue growth 36.7% | Q2 2026 | [Release][S8] | primary | A |
| 7 | Salesforce accounting scope | Agentforce ARR >$1.5bn; with Data 360 ~$3.9bn; AI definition expanded to Slackbot/Headless 360 | Jul 2026 | [Release][S9] | primary | A |
| 8 | Menlo enterprise estimate | 2025 GenAI spend $37bn; applications $19bn; excludes inference/model serving and embedded features | Dec 2025 | [Report][S10] | primary | C |
| 9 | Menlo consumer estimate | $12bn annual market snapshot; ~3% premium conversion, not audited transactions | Jun 2025 | [Report][S11] | primary | C |
| 10 | Gartner broad spending forecast | 2025 $1,764.947bn; 2026 $2,595.667bn, including infrastructure $1,431.509bn, services $585.527bn, software $453.209bn, models $32.604bn | 2026-05-19 | [Release][S12] | primary | A (forecast stated) |
| 11 | Census BTOS, nationally weighted employer businesses | Original author's API extraction: current AI use 23.8%, SE 0.41pp; expected use 27.7% (October values not independently reproduced). Verified May current use 19.8%; wording broadened Nov 2025; Oct 8 release covers through Oct 4 | Sep 21–Oct 4 / May 3, 2026 | [API, national rows][S13], [Census explanation][S14], [release metadata][S41] | primary | A for verified May/wording/release metadata; original A grade retained for October, independent verification unresolved |
| 12 | Ramp observed paid adoption | Overall 55.9%; Anthropic 43.8%; OpenAI 40.6%; overall +0.62pp m/m; token spend approximately flat Aug–Sep | Sep 2026 | [October index][S15] | primary | A (sample only) |
| 13 | Ramp concentration and intensity | Top 1% of firms drive 80% of OpenAI/Anthropic spend; top-cohort monthly spend/employee $9,568, 3.1% below July $9,873 | Sep 2026 | [Index][S15] | primary | A (sample only) |
| 14 | McKinsey adoption versus returns | 88% regular AI use; 39% enterprise EBIT impact; approximately one-third scaling | 2025 survey | [Survey][S16] | primary | A (self-reports) |
| 15 | Bain savings survey | 951 large companies; 40% of savings-measurers saved ≤10%; 44% cite targeted savings as funding | Apr 2026 | [Bloomberg syndicated report][S17] | secondary | C (underlying report unavailable) |
| 16 | MIT NANDA headline and denominator | 95% “zero return”; >300 public initiatives, 52 interviews, 153 leaders; task-specific funnel 60% evaluated / 20% piloted / 5% implemented | Jan–Jun 2025 | [Authors' preliminary report, mirrored][S18] | primary | D (generalized failure claim) |
| 17 | Morgan Stanley CIO deployment expectations | 81% expect production AI by end-2026; sample 100 US/EU CIOs | 2026-02-11 | [Bank research, p.42][S19] | primary | A (intentions) |
| 18 | Latest Morgan Stanley budget survey, indirectly reported | 2026 IT budget growth 4.0%, versus 3.8% prior quarter | Q3 2026 | [Macrostream summary][S20] | tertiary | D (original unverified) |
| 19 | ChatGPT willingness-to-pay evidence | >50m subscribers / >900m weekly users; headline quotient ~5.6%, not measured conversion | 2026-03-31 | [OpenAI][S21] | primary | A counts / B quotient |
| 20 | ChatGPT advertising monetization | $1bn annualized revenue; global rollout underway | 2026-08-31 | [OpenAI][S22] | primary | A (unaudited run-rate) |
| 21 | Customer-service productivity | +15% issues resolved/hour; 5,172 agents | Revised Nov 2024 | [Research paper][S23] | primary | A (studied setting) |
| 22 | Coding field experiments | +26.08% completed tasks; SE 10.3%; 4,867 developers | Paper listed 2026 | [Author's research page][S24] | primary | A (studied settings) |
| 23 | Coding counterevidence | METR: 19% slower; 16 developers, 246 tasks; later experiment has selection problems | 2025 / Feb 2026 update | [Trial][S25], [update][S26] | primary | A (original setting) |
| 24 | Macro productivity | Nonfarm output/hour +1.4% annualized q/q, +2.2% y/y; no AI attribution | Q2 2026 revised | [BLS][S27] | primary | A |
| 25 | Token volumes, incompatible scopes | Google monthly 9.7tn→480tn→>3.2 quadrillion, May 2024/25/26; Microsoft >300 customers on track for >1tn/year each; OpenRouter weekly 0.5tn→128.4tn, Jan 2025→Sep 2026 | Respective dates | [Google][S28], [Microsoft][S5], [OpenRouter][S29] | primary | A (company metrics) |
| 26 | Application gross-margin benchmarks | Bessemer selected “supernovas” ~25%; “shooting stars” ~60% | 2025 | [Investor research][S30] | primary | C (selected estimates) |
| 27 | Consumer-app durability | Annual-plan retention after 12 months: AI 21.1% / non-AI 30.7%; monthly-plan 6.1% / 9.5%; median first-year revenue/payer $30.16 / $21.37; not enterprise contract renewal or margin data | 2026 report | [RevenueCat][S31] | primary | A (sample) |
| 28 | Covello bear argument | ~$1tn prospective AI investment must solve sufficiently valuable, complex problems | Jul 2024 | [Goldman][S32] | primary | A (argument stated) |
| 29 | Acemoglu model, often misquoted | Ten-year cumulative TFP +0.66%; adjusted <0.53%; optimistic sensitivity +0.89%, approximately 0.9% | 2024 paper | [MIT-hosted paper][S33] | primary | A (model stated) |
| 30 | Zitron bear argument | Claims AI startups spend 300–1,000% of revenue on tokens; extrapolates 80%/1% concentration to labs globally | 2026-10-13 | [Essay][S4] | tertiary | D (unverified generalization) |
| 31 | Published annual required-revenue estimates | Sequoia $600bn; JPM $650bn at 10% return; Goldman ~$300bn breakeven / $417bn infrastructure at 10% ROIC / ~$1tn applications; Bain $2tn by 2030 | 2024–26 publications | [Sequoia][S34], [JPM][S35], [Goldman summary][S36], [Bain][S37] | primary / secondary | A estimates stated; C Goldman |
| 32 | Gartner cumulative demand warning | Through 2030: $8.5tn required at 12% ROIC versus ≤$3.6tn forecast enterprise/consumer revenue attributable to AI data centers, not all AI benefits; less than half earned by significant infrastructure owners | 2026-10-14 | [Release][S38] | primary | A (forecast stated, not realized shortfall) |
| 33 | Hypothetical new-cohort payback model, not observed revenue | $750bn new capital requires $295–468bn annual revenue; $1.36tn requires $536–848bn; assumes 3–6-year equipment life, 15-year long-lived infrastructure, 50% owner EBITDA margin and 10% discount rate; not actual 2024–26 cohorts' remaining requirements | 2026-10-17 | [Current unit-economics worked model](/research/theory/ai-unit-economics#a-worked-model), independently recalculated in [cross-check][S47] | secondary (internal model) | D (unverified assumptions; conditional arithmetic reproducible) |
| 34 | Model: lab subscriptions/API, global recognized sales | 2025 $20bn; 2026 $90bn | CY estimate, 2026-10-17 | [Lab evidence][S1], [S2], [S3], [S4]; reconstruction below | secondary (model) | D |
| 35 | Model: cloud AI compute/services, excluding ordinary cloud | 2025 $30bn; 2026 $75bn | CY estimate, 2026-10-17 | [Microsoft][S5], [Google][S7], [AWS][S8]; allocation below | secondary (model) | D |
| 36 | Model: enterprise AI applications/add-ons | 2025 $23bn; 2026 $50bn | CY estimate, 2026-10-17 | [Menlo][S10], [Microsoft][S6], [Salesforce][S9]; extrapolation below | secondary (model) | D |
| 37 | Model: consumer applications excluding lab assistants | 2025 $5bn; 2026 $10bn | CY estimate, 2026-10-17 | [Consumer market anchor][S11]; extrapolation below | secondary (model) | D |
| 38 | Model: assumed deduplication and illustrative totals | Gross sum $78bn/$225bn; overlap −$23bn/−$45bn; illustrative end-user total $55bn/$180bn, 2025/26 respectively; allocations and eliminations lack a verified transaction bridge | 2026-10-17 | [CSV](/data/ai-revenue-estimates.csv); rows 34–37 | secondary (model) | D |
| 39 | Conditional end-user paths, annual $bn | 2026/27/28: bear 130/170/210; base 180/300/480; bull 230/440/800; cumulative 510/960/1,470 | 2026-10-17 assumptions | [CSV](/data/ai-revenue-estimates.csv); scenarios below | secondary (model) | D |
| 40 | Bridge to infrastructure, sensitivity only | Assume 40–60% capture; 2028 bear $84–126bn, base $192–288bn, bull $320–480bn | 2026-10-17 assumptions | Rows 26, 32, 39; arithmetic below | secondary (model) | D |
| 41 | Ramp spending rebound and revisions | September top-cohort spend/employee +11.7% m/m; early-October AI spend peaked 1.5% above August; small top cohort volatile and revised after adding vendors | Sep / early Oct 2026; published Oct 14 | [October index][S15] | primary | A (sample only) |
| 42 | CloudZero observed spending share | Same-store panel of 422 customer organizations: median AI share of cloud bills 2.66% in August → 3.02% in September; share, not absolute dollar growth | Aug–Sep 2026; published Oct 13, updated Oct 14 | [AI Economics Pulse][S42] | primary | A (sample only) |
| 43 | CloudZero budget intentions, separate survey | Survey of 252 finance leaders: 87% plan higher FY2027 AI budgets; only 10% call funding net-new; separate population from billing panel | October 2026 report; FY2027 intentions | [AI Economics Pulse][S42] | primary | A (sample self-reports) |
| 44 | Anthropic adjusted profitability, reported, unverified | Second consecutive adjusted-profit quarter; positive free cash flow on the reported adjusted basis; 11% operating margin on that basis; no public GAAP reconciliation inspected | Q3 2026; reported 2026-10-15 | [Euronews/Bloomberg][S2] | secondary | C |
| 45 | CoreWeave debt financing | Completed $4.2bn of 2.875% convertible senior unsecured notes, due 2033; subsidiary guarantees on a senior unsecured basis | 2026-09-22 | [SEC 8-K][S44] | primary | A (debt terms) |
| 46 | OpenAI primary revenue anchor | Company stated $2bn monthly revenue; neither booked CY2026 sales nor verification of later reported run-rates | 2026-03-31 | [Company announcement][S21] | primary | A (company statement, unaudited) |
| 47 | Anthropic primary revenue and equity anchors | Run-rate crossed $47bn earlier in May; $65bn Series H announced | 2026-05-28 | [Company announcement][S43] | primary | A (company statements, unaudited) |
| 48 | OpenAI newer adoption disclosure | >1bn weekly active users and 2.5m businesses; no comparable new paid-subscriber denominator disclosed | 2026-09-08 | [Company update][S45] | primary | A (company metrics) |
| 49 | Model assumptions made explicit | Overlap/gross sales 29.49% in 2025 → 20.00% in 2026; base revenue growth 66.7% in 2027 and 60.0% in 2028; 2026–28 CAGR bear/base/bull 27.1%/63.3%/86.5% | 2026-10-17 assumptions | [CSV](/data/ai-revenue-estimates.csv), rows 38–39; [independent calculations][S47] | secondary (model) | D (assumed paths; arithmetic reproducible) |
| 50 | Final-demand boundary and omitted internal benefits | Supplier-invoice elimination does not exclude externally financed training or subsidy-funded use; internal AI savings and incremental advertising cash flow may fund owned assets outside separately sold AI products; no amount estimated | 2026-10-17 | [CSV](/data/ai-revenue-estimates.csv), [current worked-model limitations](/research/theory/ai-unit-economics#a-worked-model), [cross-check][S47] | secondary (model/boundary analysis) | D (unquantified) |

Type: primary / secondary / tertiary. Grade: A–D (see [methodology](/report/methodology)).

## Analysis

### Revenue boundaries and reconstruction

Final spending comes from operating income, household budgets or advertisers. App-to-lab-to-cloud sales overlap; even deduplicated sales can depend on subsidies.

Rows 34–38 are **illustrative spending assumptions**, not independently measured market totals or a market census. Lab sales cover assistants, enterprise subscriptions and APIs under each provider's accounting convention. Reported booked sales inform the assumptions, but do not reproduce the allocations. No audited global subscription/API split exists. Earlier primary anchors establish scale: OpenAI stated $2bn monthly revenue on March 31, and Anthropic said its run-rate crossed $47bn in May. Neither authenticates later leaks or supplies a calendar-year sales bridge (claims 46–47). [OpenAI][S21], [Anthropic][S43].

Cloud estimates allocate Microsoft's combined AI disclosure between applications and compute; total Google Cloud is an upper-bound cross-check. AWS provides a direct AI observation. Prior-year allocations are judgmental backcasts. Enterprise applications include AI-native software and incremental incumbent add-ons, anchored on Menlo and public seats/ARR. Consumer apps exclude lab assistants already counted; their allocation extrapolates Menlo's specialized-app opportunity. All allocations are grade D.

The overlap deduction is intended to remove modeled app-to-lab, lab-to-cloud and reseller pass-through sales. The segment allocations and $23bn/$45bn overlap deductions are judgmental inputs, not outputs of a verified invoice-level reconstruction. The deduction falls from 29.49% of gross layer sales in 2025 to 20.00% in 2026 without a transaction bridge (claim 49). Upgrading these D-grade totals requires company sales by period, gross/net treatment, app/compute allocation and each elimination. The [CSV](/data/ai-revenue-estimates.csv) exposes assumptions for replacement as evidence improves.

Eliminating supplier invoices is different from excluding externally financed training purchases or subsidy-funded consumption. Conversely, internal AI cost savings and incremental advertising cash flow can fund owned infrastructure without appearing as separately sold AI products. The model does not quantify either adjustment; its narrow AI-product numerator cannot settle returns on broad corporate capex (claim 50). [Boundary review][S47], [worked-model limitations](/research/theory/ai-unit-economics#a-worked-model).

Menlo's estimates differ in timing and scope; its consumer snapshot is not booked calendar-year revenue. Gartner includes hardware, devices, implementation and broad software categories. Adding it to lab sales confuses supply investment with end demand. [Menlo enterprise][S10], [consumer][S11], [Gartner][S12].

OpenAI nets certain partner sales; Anthropic expenses the partner cut. Compare booked sales and cash collections on common accounting. Anthropic's July reported run-rate and October outside estimate have different provenance, rather than forming an uncertainty range. [Accounting report][S1], [quarterly reporting][S2]. Microsoft's AI disclosure also includes applications, so it is not an Azure-only number. Google Cloud includes TPU-system hardware sales and ordinary cloud services, while shared AI research is partly outside segment expenses. AWS separately names AI and chip businesses; their run-rates cannot be added without overlap information. Salesforce explicitly broadened its Agentforce definition; its combined data-product figure cannot all be treated as incremental AI. [Microsoft][S5], [Alphabet][S7], [AWS][S8], [Salesforce][S9].

### Adoption, budgets and realized value

Census's May observation and revised business-function wording are independently verified; its October current-use, expected-use and SE values were not reproduced in the review or this application. The release page confirms coverage through October 4, but the API fetch failed, direct API/workbook requests returned HTTP 403, and browser API navigation was blocked. Access failure does not establish that the original extraction was wrong. The broader question breaks comparability with older wording. Ramp measures payments in a selected customer population; McKinsey measures respondent organizations and self-reported impact. These populations and measures differ; the evidence does not quantify how much of the Census–Ramp gap each difference explains. [API][S13], [wording][S14], [release metadata][S41], [Ramp][S15], [McKinsey][S16].

Morgan Stanley's primary deployment survey supports adoption; its latest budget figure is only a tertiary summary. AI spending may reallocate existing IT budgets. Bain's savings misses challenge self-financing assumptions. [Morgan Stanley][S19], [budget summary][S20], [Bain reporting][S17].

CloudZero's October 13 report, updated October 14, follows 422 same-store customer organizations: median AI share of cloud bills rose from 2.66% in August to 3.02% in September 2026. Its separate survey of 252 finance leaders reports 87% planning higher FY2027 AI budgets, but only 10% calling funding net-new (claims 42–43). This supports expanding demand and budget substitution simultaneously, challenging an economy-wide spending-stall inference from Ramp. A rising bill share does not establish absolute dollar growth, and neither panel represents the whole economy. [CloudZero][S42].

MIT NANDA's headline is unreliable as a universal pilot-failure rate: it combines interviews and conference responses with varying success definitions and no representative sampling frame. Its funnel distinguishes evaluation, pilots and implementation; implementation divided by pilots uses a different denominator from the headline. Time savings also need not immediately improve P&L. These critiques follow the authors' own limitations. [Report, pp.2–7][S18].

### Willingness to pay, productivity and margins

ChatGPT's subscriber count establishes substantial willingness to pay, but the subscriber/weekly-user quotient is not a cohort conversion rate: both counts are rounded lower bounds, and subscribers need not all be weekly users. Ads create another payer; their annualized milestone is neither full-year booked revenue nor proof of attractive acquisition economics. [OpenAI subscribers][S21], [ads][S22].

OpenAI's September 8 disclosure raises its reach to over 1bn weekly active users and 2.5m businesses (claim 48), strengthening the adoption evidence. Without a comparable new paid-subscriber denominator, it cannot update March's quotient or establish paid conversion. [OpenAI update][S45].

Service and coding studies measure completed work, not vendor revenue. METR found experienced maintainers slowed down, then warned that later experiments increasingly miss developers and tasks with high expected AI benefits. The original result is not a permanent verdict. [Service study][S23], [coding experiments][S24], [METR][S25], [update][S26].

BLS reports productivity without causal AI attribution. Its commentary links AI exposure to productivity and capital intensity, without identifying causation. Governor Cook emphasizes uncertainty about gains' breadth, timing and transmission to demand and prices. [BLS release][S27], [BLS commentary][S39], [Fed][S40].

Token growth is extraordinary, but Google includes internal/free surfaces, Microsoft's metric describes large customers' prospective consumption, and OpenRouter is one changing distribution channel. Cached inputs, reasoning, model mix and discounts change what a token earns. The [current unit-economics note and price series](/research/theory/ai-unit-economics) reject an automatic tokens-to-dollars inference. Ramp observed virtually flat token spending in August–September despite rising volumes. Its own counterevidence matters: September top-cohort spend/employee rebounded 11.7% m/m, and early-October AI spend reached a peak 1.5% above August (claim 41). The small top cohort is volatile and estimates were revised after vendor additions; the earlier stall cannot establish persistent market-wide weakness. [Google][S28], [OpenRouter][S29], [Ramp][S15].

Bessemer's margin dispersion challenges software-style multiples. RevenueCat's stronger monetization but weaker retention requires continued acquisition. Neither sample establishes sector profitability. Cloud profits include mature services and exclude some central AI research; incumbents can subsidize AI longer. [Bessemer][S30], [RevenueCat][S31], [Alphabet segment allocation][S7].

October 15 reporting describes Anthropic's second consecutive adjusted-profit quarter, positive free cash flow on the reported adjusted basis and an 11% operating margin (claim 44). This C-grade counterevidence weakens blanket lab cash-burn claims; definitions and public accounts remain unavailable, so it does not establish GAAP profitability or durable free cash flow. [Euronews/Bloomberg][S2].

Anthropic's May $65bn Series H and CoreWeave's September $4.2bn convertible issue show equity and debt financing operating together (claims 45, 47). Creditors already bear risk while equity financing is available; leverage, priority, subsidiary guarantees and contracts govern losses, rather than a universal sequence in which creditors become exposed only after equity funding ends. [Anthropic][S43], [SEC][S44].

### Conditional revenue paths and payback

These are illustrative stress scenarios, not probability forecasts or independently validated market estimates. Annual **assumed deduplicated end-user revenue**, $bn; inputs and arithmetic are in the CSV.

| Scenario | 2026 | 2027 | 2028 | Cumulative 2026–28 | Assumption |
|---|---:|---:|---:|---:|---|
| Bear | 130 | 170 | 210 | 510 | Discounting and churn absorb volume gains; pilots remain small; startup subsidies retreat. |
| Base | 180 | 300 | 480 | 960 | Production deployments expand; renewal spending grows; efficiency offsets lower prices without a broad budget revolution. |
| Bull | 230 | 440 | 800 | 1,470 | Agents create new recurring workflows; advertisers and operating budgets fund sustained consumption; stronger retention and margins. |

The base path requires 66.7% growth in 2027 and 60.0% in 2028. The bear/base/bull paths imply 2026–28 compound annual growth of 27.1%/63.3%/86.5% (claim 49). These rates follow from chosen endpoints; the deployment narratives do not quantitatively derive them. [CSV](/data/ai-revenue-estimates.csv), [cross-check arithmetic][S47].

Assume infrastructure owners capture 40–60% of final dollars: a sensitivity, not an observed take rate. Integration can increase capture; successive app/lab margins reduce it. Row 40 gives infrastructure revenue before costs, comparable to required **revenue**, not profit.

The base scenario is numerically below the hypothetical $1.36tn new-cohort requirement, but the asset populations, revenue boundaries and recovery schedules are not matched. Row 33 uses the current model's $295–468bn annual requirement for assumed $750bn new capital and $536–848bn for $1.36tn. Applying that fresh-cohort formula to historical spending ignores earlier recoveries, remaining lives and commissioning dates; the assumed capital is not established as AI-only. The equipment component lasts for its assumed life and the long-lived component for 15 years, rather than one combined revenue stream forever. These comparisons do not measure an actual 2028 payback gap. [Current worked model](/research/theory/ai-unit-economics#a-worked-model), [independent recalculation][S47].

The bull case yields $480bn infrastructure revenue at 60% capture, above Goldman's reported $417bn hurdle; at 40%, its $320bn falls below. This is conditional arithmetic from a secondary summary whose original bank model was not obtained. It cannot validate different capital bases or later buildout. Sequoia's heuristic includes a compute-buyer margin; JPMorgan uses an investment-return requirement, and Bain's target belongs to 2030. Matching revenue layers alone does not reconcile capital vintages or cash-flow timing. [Sequoia][S34], [JPMorgan][S35], [Goldman summary][S36], [Bain][S37].

Gartner's through-2030 cumulative figures cover a longer horizon and enterprise/consumer revenue attributable to AI data centers, rather than all AI economic benefits. Our single-year 2028 bull case cannot disprove them; infrastructure owners capture only part of final revenue. The A grade verifies Gartner's stated forecast, not a realized shortfall. [October release][S38].

## Conflicts and open questions

- **Demand and recent spending:** the original note emphasized cloud growth, paid seats and task gains as bull evidence, and Ramp's slowing intensity, Bain's unrealized savings and weak consumer-app retention as bear evidence. The cross-check agrees these observations matter, but judges the balance incomplete: Ramp's own September/early-October rebounds and CloudZero's rising September spend share challenge extrapolating a persistent market-wide stall. Neither panel establishes aggregate profitability or absolute market growth. [S5], [S6], [S8], [S15], [S17], [S23], [S31], [S42].
- **Market totals and payback:** the original note judged $55bn/$180bn a useful 2025/26 demand reconstruction and its $480bn 2028 base path evidence of a shortfall against combined historical cohorts. The cross-check accepts the conditional sums but finds no verified sales/allocation/elimination bridge and no matched historical asset population. The current unit-economics note rejects a combined historical-cohort payback interpretation; the demand scenarios therefore do not quantify an observed funding or return deficit. The active analysis retains the paths as D-grade illustrations. [CSV](/data/ai-revenue-estimates.csv), [current model](/research/theory/ai-unit-economics#a-worked-model), [cross-check][S47].
- **Largest uncertainty and financing:** the original note ranked infrastructure capture as the largest uncertainty and described equity losses preceding creditor exposure. The cross-check does not establish that ranking relative to market size, asset scope, remaining lives, costs and funding. Its view is that both equity and creditors are already exposed, with contractual protections governing losses; CoreWeave's September debt is a concrete example. These are competing risk judgments, not a measured universal loss sequence. [SEC][S44], [cross-check][S47].
- **Lab profitability:** the original Summary described standalone AI profits as opaque and emphasized external funding. The cross-check adds October reporting of Anthropic's second consecutive adjusted-profit quarter, positive free cash flow on the reported adjusted basis and an 11% operating margin. This is C-grade counterevidence to blanket cash-burn assumptions; no public reconciliation establishes GAAP profitability or durable free cash flow (claim 44). [Euronews][S2].
- **Adoption comparison and access:** the original Summary said survey coverage and wording explained much of the Census–Ramp gap. The cross-check finds different populations and measures sufficient to rule out direct comparison, but no quantified decomposition supporting “much.” The original October Census extraction and its A grade are preserved with an explicit unresolved verification gap; failed access is not evidence of falsity. May use, wording and release metadata were independently verified. [Census][S14], [release page][S41], [Ramp][S15], [cross-check][S47].
- **Covello:** expensive infrastructure needs valuable problems whose savings exceed their cost; his original investment number is historical, not today's capex forecast. **Acemoglu:** the often-cited 0.9% is an optimistic cumulative sensitivity, not annual TFP growth or his central result. Novel tasks and faster capability improvements could invalidate the exposure assumptions. [Goldman][S32], [paper][S33].
- **Zitron:** subsidy dependence and misleading run-rates are legitimate mechanisms. His global concentration claim exceeds what Ramp's sample establishes; the extreme token-spend ratios lack a representative audited denominator. Real enterprise subscription sales contradict the blanket assertion that only startups buy AI. [Essay][S4], [Ramp][S15], [Microsoft][S6].
- **Internal dependency:** the original note's conflict with an older unit-economics headline and tokens-to-dollars inference is stale. The current dependency explicitly rejects the historical-cohort and automatic token-growth revenue inferences; both notes now require a company- and cohort-specific cash-flow bridge. [Current unit-economics note](/research/theory/ai-unit-economics), [cross-check][S47].
- **Unverified:** audited lab accounts and adjusted-profit reconciliations; a common gross/net bridge; global segment totals and invoice eliminations; October Census national values and SE in this review; AI-only cloud margins; representative enterprise-app churn; the original latest CIO budget survey; infrastructure capture; treatment of externally financed training, subsidies and internal benefits; cohort commissioning dates and remaining recovery. These gaps limit the scenarios.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| Lab monetization | OpenAI ~$50bn net; Anthropic ~$65bn July gross run-rate / outside ~$74bn estimate cited Oct 15, reported, unverified | End-Sep / Jul / Oct 15, 2026 | [S1], [S2] | Bullward on recurring booked sales and cash conversion; bearward on accounting-only increases. |
| National business use | Original extraction 23.8% current / 27.7% expected, not independently reproduced; verified May use 19.8% | Oct 4 / May 3, 2026 | [S13], [S14], [S41] | Reproduce October national rows and SE before treating the later observation as independently checked. |
| Paid business adoption and spending | Ramp 55.9%; Aug–Sep token spend flat; September top-cohort intensity +11.7% m/m; early-October spend peak +1.5% versus August | Sep / early Oct 2026 | [S15] | Watch sustained expansion inside customers; small-cohort estimates are volatile and revised. |
| Independent billing panel / budgets | CloudZero median AI bill share 2.66%→3.02%; separate survey 87% plan increases, 10% net-new funding | Aug–Sep / October 2026 report, FY2027 plans | [S42] | Distinguish bill share from dollars and budget substitution from incremental demand. |
| Lab profitability and financing | Anthropic reported Q3 adjusted profit and 11% margin; May $65bn equity; CoreWeave September $4.2bn convertible | May / Sep / Oct 15, 2026 | [S2], [S43], [S44] | Seek audited profit/cash reconciliation and track leverage, guarantees and funding availability together. |
| Cloud AI growth | Microsoft AI +123%; AWS AI >$25bn run-rate; Google Cloud +82% overall | Mar / Q2 2026 | [S5], [S8], [S7] | Watch AI-only revenue net of lab purchases and credits. |
| Enterprise survey budgets | Latest reported IT growth 4.0%, original unverified; production expectation 81% | Q3 / Feb 2026 | [S20], [S19] | Incremental realized budgets move toward bull; reallocation or cuts toward bear. |
| App margins | Selected startup gross margins ~25% versus ~60% | 2025 | [S30] | Improving contribution margins support self-funded demand. |
| App durability | AI annual-plan retention 21.1% versus non-AI 30.7% | 2026 report | [S31] | Better renewal economics support base/bull; paid acquisition dependence supports bear. |
| Savings realization | Bain: 40% of measurers save ≤10% | Apr 2026 | [S17] | Renewals funded by realized savings are stronger evidence than pilot intentions. |

## Sources

All accessed **2026-10-17**. Company metrics are generally unaudited; private leaks remain reported, unverified.

1. [Axios, “OpenAI annualized revenue $20 billion less than previously reported,” 2026-10-08][S1].
2. [Euronews, Quirino Mealha, Anthropic quarterly revenue and run-rate, 2026-10-15; citing Bloomberg and SemiAnalysis][S2].
3. [Ed Zitron, “Exclusive: OpenAI Losses Increased Nearly 8X in 2025,” 2026-06-15; leaked accounts][S3].
4. [Ed Zitron, “Annualized Enron Rate,” 2026-10-13; reporting compilation and commentary][S4].
5. [Microsoft, FY2026 Q3 earnings transcript, 2026-04-29][S5].
6. [Microsoft, FY2026 Q4 earnings release, SEC exhibit, 2026-07-29][S6].
7. [Alphabet, Q2 2026 earnings release, SEC exhibit, 2026-07-22][S7].
8. [Amazon, Q2 2026 earnings release, 2026-07-30][S8].
9. [Salesforce, Q2 FY2027 earnings release, 2026-08-26][S9].
10. [Menlo Ventures, “2025: The State of Generative AI in the Enterprise,” December 2025][S10].
11. [Menlo Ventures, “2025: The State of Consumer AI,” 2025-06-26; PDF][S11].
12. [Gartner, worldwide AI spending forecast, 2026-05-19][S12].
13. [Census BTOS API, period 110, collection 2026-09-21–2026-10-04][S13]. The original author reported direct JSON extraction of national rows with geography/industry/size fields null. The cross-check and its application could not reproduce the values: web fetch failed, direct HTTP returned 403 and browser API navigation was blocked. [Release/download page][S41] confirmed the October 8 release covers through October 4, but does not verify the national estimates or SE.
14. [Census, “Large Firms With at Least 20 Employees Biggest AI Users,” 2026-05-26][S14].
15. [Ramp, Ara Kharazian, “Cracks in the AI Thesis Part 3,” 2026-10-14][S15].
16. [McKinsey, “The state of AI in 2025,” 2025-11-05][S16].
17. [Heather Landy/Bloomberg, syndicated by Insurance Journal, Bain savings survey, 2026-06-01][S17].
18. [Challapally et al., MIT NANDA, “The GenAI Divide,” July 2025, preliminary report; publisher-hosted mirror][S18].
19. [Morgan Stanley, “AI Rate of Change,” 2026-02-11, p.42][S19].
20. [Macrostream, summary of Morgan Stanley Q3 2026 CIO survey, indexed 2026-10-13; original not obtained][S20].
21. [OpenAI, “Accelerating the next phase of AI,” 2026-03-31][S21].
22. [OpenAI, “A milestone in expanding access to AI,” 2026-08-31][S22].
23. [Brynjolfsson, Li and Raymond, “Generative AI at Work,” arXiv, revised 2024-11-06][S23].
24. [Sonia Jaffe, author research page, “The Effects of Generative AI on High-Skilled Work”; listed 2026][S24].
25. [METR, experienced open-source developer productivity trial, 2025-07-10][S25].
26. [METR, “We are Changing our Developer Productivity Experiment Design,” 2026-02-24][S26].
27. [BLS, Q2 2026 productivity and costs, revised release, 2026-09-03][S27].
28. [Google, Sundar Pichai, I/O opening keynote, May 2026][S28].
29. [OpenRouter, “The Token State of Play,” 2026-09-22][S29].
30. [Bessemer Venture Partners, “The State of AI 2025,” 2025][S30].
31. [RevenueCat, “State of Subscription Apps 2026,” 2026][S31]. Annual/monthly figures agree across its sections; inconsistent weekly figures are excluded.
32. [Goldman Sachs, “A skeptical look at AI investment,” 2024-07-16][S32].
33. [Daron Acemoglu, “The simple macroeconomics of AI,” MIT-hosted published paper, 2024][S33].
34. [Sequoia, David Cahn, “AI's $600B Question,” 2024-06-20][S34].
35. [J.P. Morgan Asset Management, “Evaluating AI,” 2026-02-12; cites bank research dated 2025-11-10][S35].
36. [AdvisorAnalyst, Goldman required-revenue research summary, 2026-10-15; original bank note unavailable][S36].
37. [Bain, “How Can We Meet AI's Insatiable Demand for Compute Power?”, 2025-09-23][S37].
38. [Gartner, AI infrastructure impairment/revenue forecast, 2026-10-14][S38].
39. [BLS, “Productivity and Artificial Intelligence,” updated 2026-06-08][S39].
40. [Federal Reserve, Governor Lisa Cook, “An Update on AI and the Economy,” 2026-09-28][S40].
41. [Census BTOS, downloads and release metadata, updated 2026-10-08][S41]; accessed in Chrome 2026-10-17; National workbook coverage ends 2026-10-04, workbook contents inaccessible here.
42. [CloudZero, Keith MacKenzie, “Your AI Economics Pulse for October 2026,” published 2026-10-13, updated 2026-10-14][S42]; billing panel and separate finance survey, fetched 2026-10-17.
43. [Anthropic, “Anthropic raises $65B in Series H funding at $965B post-money valuation,” 2026-05-28][S43]; primary revenue milestone and equity financing, fetched 2026-10-17.
44. [CoreWeave, SEC Form 8-K, convertible offering completed 2026-09-22][S44]; primary debt terms, fetched 2026-10-17.
45. [OpenAI, Sarah Friar, “The Work Now Within Reach,” 2026-09-08][S45]; newer adoption metrics, fetched 2026-10-17.
46. [Project, current AI unit-economics worked model][S46], read 2026-10-17; internal assumptions, not independent validation. [Revenue reconstruction CSV](/data/ai-revenue-estimates.csv), read and recalculated 2026-10-17. Public web fetches of both internal artifacts returned HTTP 403; these model calculations were checked from local files.
47. [Codex, independent demand-side cross-check, 2026-10-17][S47]; review judgments and independent arithmetic, read 2026-10-17. New external figures were fetched from the underlying sources above when applying it; unresolved access is explicitly marked.

[S1]: https://www.axios.com/2026/10/08/openai-50-billion-arr-anthropic-revenue-accounting
[S2]: https://www.euronews.com/2026/10/15/anthropic-revenue-jumps-46-to-168bn-as-ai-firm-eyes-record-2-trillion-ipo-valuation
[S3]: https://www.wheresyoured.at/exclusive-openai-financials/
[S4]: https://www.wheresyoured.at/annualized-enron-rate/
[S5]: https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3
[S6]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm
[S7]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[S8]: https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
[S9]: https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
[S10]: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
[S11]: https://menlovc.com/wp-content/uploads/2025/11/menlo_ventures_consumer_ai_report-2025.pdf
[S12]: https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026
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
[S27]: https://www.bls.gov/news.release/archives/prod2_09032026.htm
[S28]: https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
[S29]: https://openrouter.ai/data/newsletter/the-token-state-of-play
[S30]: https://www.bvp.com/atlas/the-state-of-ai-2025
[S31]: https://www.revenuecat.com/state-of-subscription-apps
[S32]: https://www.goldmansachs.com/insights/goldman-sachs-exchanges/a-skeptical-look-at-ai-investment
[S33]: https://economics.mit.edu/sites/default/files/2024-10/The%20Simple%20Macroeconomics%20of%20AI.pdf
[S34]: https://www.sequoiacap.com/article/ais-600b-question/
[S35]: https://am.jpmorgan.com/au/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/evaluating-ai/
[S36]: https://advisoranalyst.com/2026/10/15/ai-capex-required-revenues-and-what-the-market-is-actually-pricing.html/
[S37]: https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/
[S38]: https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030
[S39]: https://www.bls.gov/productivity/articles-and-research/ai-and-productivity/home.htm
[S40]: https://www.federalreserve.gov/newsevents/speech/cook20260928a.htm
[S41]: https://www.census.gov/hfp/btos/data_downloads
[S42]: https://www.cloudzero.com/blog/ai-economics-pulse-october-2026/
[S43]: https://www.anthropic.com/news/series-h
[S44]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm
[S45]: https://openai.com/index/the-work-now-within-reach/
[S46]: /research/theory/ai-unit-economics#a-worked-model
[S47]: ../../reviews/demand-side-codex-xcheck.md
