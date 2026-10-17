# AI unit economics — independent Codex cross-check

*Review date: 2026-10-17. Note reviewed: research/theory/ai-unit-economics.md, dated 2026-10-17. All external sources below accessed 2026-10-17. No changes made to the note or its data files.*

## Verdict

**Major revision required:** many reported figures check out, but the claimed sector revenue shortfall is not established by the evidence or model.
**Arithmetic:** all 20 annuity-table cells reproduce; errors lie mainly in aggregation, denominators, margin comparisons and the inference from tokens to revenue.
**Material omissions:** current lease accounting, customer/vendor financing and September–October lab disclosures change both the profitability assessment and who bears losses.

## Claim re-verification

I selected these 15 rows because they underpin the capex denominator, revenue numerator, margin assumptions, asset-life sensitivity and inference/training conclusions. “Matches” distinguishes reproducing a published assertion from independently establishing its economic truth. A is a directly disclosed primary-source figure; B is simple derivation or appropriately corroborated reporting; C is an estimate or private-company reporting without primary confirmation. An original research publication is primary evidence of its authors' findings, but a modeled company cost is still an estimate. No private lab leak is upgraded merely because multiple outlets repeat it.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 1 | Big four capex: $230.9bn in 2024; $380.5bn in 2025 | $230.869bn and $380.543bn using the stated mixed definitions. Microsoft contributes $56.110bn and $85.062bn for years ending June, not December. These are mixed-fiscal-year sums, not calendar-year investment cohorts. | [Amazon 2025 10-K][amzn25]; [Microsoft 2025 annual report][ms25], cash flows and Note 14; [Alphabet 10-K][goog25]; [Meta 10-K][meta25] | Numerical match; period interpretation fails. | **B**, explicitly labeled mixed periods/bases. |
| 5 | Microsoft CY26 ~$190bn, including ~$25bn component inflation; two-thirds short-lived GPUs/CPUs | April guidance and Q3 asset mix match. July guidance is **~$175bn** after finance-to-operating lease reclassification; underlying investment expectations unchanged. Two-thirds describes that quarter, not an audited industry-wide mix. | [FY26 Q3 call][msq3]; [FY26 Q4 call][msq4] | Historically yes; stale as latest reported capex guidance. | **A** for dated statements; **C** for extrapolating mix to the whole sector. |
| 6 | Alphabet capex $52.5bn/$91.4bn; H1 2026 $80.6bn; guide $195–205bn | $52.535bn/$91.447bn; H1 $80.598bn. AP reports the $195–205bn guidance. I could not fetch the official Q2 call or the cited CNBC page, so the guide remains secondary verification. | [10-K][goog25]; [Q2 release][googq2]; [AP earnings report][amazon-ap] | Actuals yes; guide corroborated, not independently primary-verified. | **A** actuals; **B** reported public-company guidance. |
| 7 | Meta capex $39.2bn/$72.2bn; 2026 $130–145bn | $39.225bn/$72.215bn including finance-lease principal; July guide $130–145bn. | [10-K][meta25], FCF reconciliation; [Q2 release][metaq2] | Yes. | **A** disclosed capex/guidance; **B** if reconstructed from cash-flow components. |
| 8 | Oracle FY26 capex $55.7bn, FCF −$23.7bn; Q1 FY27 capex $28.5bn, RPO $664bn, $20bn ATM sold | FY26 $55.663bn capex, $31.977bn OCF, −$23.686bn FCF; Q1 $28.499bn capex; RPO $664bn; $20bn stock sold before commissions. | [Q1 FY27 release][orclpr], including historical cash-flow table; [Q1 10-Q][orclq] | Yes; gross capex alone omits customer financing. | **A**. |
| 17 | Amazon servers 5→6 years in 2024, +$2.5bn net income; subset 6→5 in 2025, +$1.4bn D&A/−$1bn income | Both changes and effects match. The 2024 change reduced D&A by $3.2bn. | [2024 10-K][amzn24], estimates; [2025 10-K][amzn25], estimates | Yes. | **A**. |
| 18 | Meta most servers/network assets to 5.5 years; depreciation −$2.92bn, net income +$2.59bn, EPS +$1 | All match. These are full-year effects based on assets already in service at end-2024. | [2025 10-K][meta25], accounting estimates | Yes. | **A**. |
| 24 | GB200 $0.19 versus H100 $0.42 per million tokens at 91 tok/s/user; chip-hours $1.86/$1.17 | Benchmark page reproduces $0.19/$0.42 and 2,725/772 tok/s/chip for 8k/1k FP8. Implied hourly costs are ~$1.864/$1.167. At 50 tok/s/user it reports $0.06/$0.19. The alternative page did not expose all original ownership/pricing assumptions. | [InferenceX comparison][inferencex] (original URL failed; same experiment's comparison page fetched) | Core numbers yes; full cost model only partly verified. | **A** as publication of benchmark measurements; **C** for economic cost estimates; **B** for ratios calculated from them. |
| 27 | Gemini 2.5 Pro $1.25/$10; 3 Pro $2/$12; Argon $2/$10→$4/$20 Dec 1; Flash $0.75/$3.75→$1.50/$7.50 Jan 1 | Current Argon and both Flash schedules match; 2.5 Pro matches for prompts ≤200k. Historical 3 Pro launch is confirmed, but its original price was not recovered from the current pricing page. | [Google pricing][gemprice]; [release notes][gemlog] | Current/scheduled prices yes; historical 3 Pro price unresolved. | **A** current published prices; historical subclaim not independently verified. |
| 29 | Google monthly tokens 9.7tn→480tn→>3.2 quadrillion; 22bn/min API; 950m app MAU | All company-stated figures match. Monthly totals are across Google's surfaces, not a series of paid API tokens. | [I/O keynote][io26]; [Q2 release][googq2] | Yes, with crucial scope qualification. | **A** as unaudited company metrics; no grade-A revenue inference. |
| 30 | Microsoft AI annual run-rate >$37bn/+123%; >300 trillion-token customers/+30% q/q; Azure >$100bn FY26 | Disclosed values match. April call's “accelerating 30%” wording does not clearly establish 30% growth in each customer's consumption. July call explicitly tracks the **number of customers** at a trillion-token run-rate. | [Q3 release][msq3pr]; [Q3 call][msq3]; [Q4 call][msq4] | Revenue yes; token-growth interpretation overstated. | **A** management disclosures; not an audited standalone AI segment. |
| 32 | OpenAI adjusted gross margin 33% in 2025 vs 40%, target 46%; future 52–67%; inference cost 4x | Decoder repeats all figures, attributing them to The Information. No primary financial statement or reconciliation was obtained. A positive gross margin does not mean inference is sold below the costs included in that measure. | [Decoder report][decoder] | Matches reporting; economic definition unverified. | **C**, reported, unverified. |
| 33 | OpenAI Q2 $6.7bn revenue, Q1 $3.7bn burn; Anthropic July run-rate >$65bn, from ~$9bn end-2025 | Secondary reports reproduce $6.7bn, $3.7bn and >$65bn. Anthropic itself confirms the ~$9bn end-2025 baseline and >$30bn in April. October 14 reporting updates Anthropic to **$16.8bn Q3 revenue and adjusted profitability**. | [WSJ report summary][oaiq2]; [Reuters/CNA][oaiburn]; [Axios August report][anth65]; [Anthropic statement][anthcompute]; [Reuters October 14][anthq3] | Historical figures broadly corroborated, but material newer evidence omitted. | **C** private figures; **A** company-stated April run-rate/baseline. |
| 34 | Google Cloud Q2 $24.8bn/+82%, operating income $8.8bn; $49.6bn equity raise, $40bn ATM | $24.768bn/+82%, $8.814bn; $49.6bn raised. ATM is an authorization with **no shares sold as of June 30**, primarily intended for employee-equity tax obligations. Shared AI R&D is recorded partly outside Cloud. | [Alphabet Q2 release][googq2], segment footnote and financing disclosures | Yes; ATM and segment-margin interpretations need qualification. | **A**. |
| 37 | Final runs ~10% OpenAI, MiniMax 22.6%, Z.ai 12.3%, “per IPO filings”; OpenAI research amortized over multiple years | Epoch estimates **9.6%, 22.6%, 12.3%**. Filings supply R&D spending denominators; Epoch models final-run numerators using utilization, rental-price and training-compute assumptions. OpenAI's two-year amortization is Epoch's assumption based on reporting. | [Epoch methodology][epoch-rd]; [OpenAI compute analysis][epoch-oai] | Numbers match; attribution to direct prospectus disclosure does not. | **C** ratios/accounting inference; **A** only that Epoch publishes these estimates. |

Access limits are not findings of falsity. The Microsoft FY26 10-K and Oracle FY26 10-K fetches failed; Microsoft's FY25 company annual report and Oracle's Q1 release supplied the historical numbers needed above. The two cited lab-revenue aggregator URLs failed, so I followed alternative reporting and Anthropic's own statement. I did not obtain either lab's primary financial statements or Anthropic's draft prospectus; reports about those documents remain C. I did not independently recreate Epoch's model-level training-cost estimates or certify unselected table rows.

## Arithmetic checks

Recomputed with Python using `A(r,n) = (1-(1+r)**(-n))/r`. Dollar figures below are billions unless specified. A numerical pass is conditional on the inputs; it does not validate their scope or economics.

| Analysis calculation | Recalculation and judgment |
|---|---|
| Historical big-four totals | 2024: 82.999 + 56.110 + 52.535 + 39.225 = **230.869**. 2025: 131.819 + 85.062 + 91.447 + 72.215 = **380.543**. Rounding passes; mixed fiscal/calendar years remain a problem. |
| 2026 ~$730bn, then $750bn in worked model | Stated midpoint sum is 200 + 190 + 200 + 137.5 = **727.5**. The switch to 750 is an unexplained 3.09% increase. Updated Amazon 220 (AP, B) and Microsoft 175 (primary, A) give **732.5**, range **720–745** using Alphabet/Meta guidance ranges. Keeping Microsoft's earlier investment basis instead gives **747.5**. These are different accounting bases, not competing estimates of the same cash quantity. |
| Oracle FCF and annualization | 31.977 − 55.663 = **−23.686**; 28.499 × 4 = **113.996**. Correct. Quarterly annualization is not calendar-2026 guidance. |
| Adding Oracle/CoreWeave gives $830–900bn | Old big-four 727.5 + Oracle FY26 55.7 + CoreWeave 35–39 = **818.2–822.2**, not 830–900. Substitute Oracle quarterly annualization 114 and get **876.5–880.5**. Neither construction is a synchronized calendar-year estimate. The “another $100bn+” assertion likewise needs its Oracle period specified. |
| Nvidia and Sequoia | 89 × 4 = **356** annualized Data Center revenue; ×4 = **1,424** under Sequoia's heuristic. Arithmetic passes. Nvidia's [release][nvdaq2] verifies the quarter; [Sequoia][sequoia] verifies its multiplier. This global sales flow is not a direct reconciliation to US big-four AI-only capex, nor the same model as discounted capital recovery. |
| Other published revenue/financing estimates | [Bain's model][bain] gives 2,000/500 = **4x**, with an implied 1,200 available against a 2,000 requirement and an 800 shortfall. Its scenario includes reinvested savings as well as migration of on-premises IT. JPM's 650 at a 10% return is confirmed on its own [page][jpm], but cannot be independently rebuilt from the blog. Morgan Stanley's stated 2,900−1,400 = **1,500** gap; enumerated 800+200+150 = **1,150**, leaving **350** unspecified. Goldman figures reproduce the [summary][goldman-summary], not a fetched primary model. Do not describe these differing methods as interchangeable arithmetic. |
| Cloud growth / tripled income | 24.768/13.624−1 = **81.80%**; 8.814/2.826 = **3.119x**. Correct rounding. Implied segment operating margin is **35.59%**, not a standalone AI investment return. |
| OpenAI annualization and aggregate end revenue | 6.7 × 4 = **26.8**, correctly rounded to 27. [Axios reported][oai70] OpenAI's near-$70bn run-rate on September 29; this is C, not recognized annual revenue. The **150–250** AI end-revenue range has no component bridge, period reconciliation or double-count elimination. Adding run-rates to cloud revenue cannot establish it. Even conditionally, 150–250 is **50–83%** of Goldman's 300 break-even figure, not roughly at that line throughout the range. |
| Meta extension as “10% of a quarter's worth” | Unspecified quarter. Against 2025 income 60.458, 2.59/60.458 = **4.28% of the year**, or **17.14% of an average quarter**, not 10%. Use an explicit denominator or delete the comparison. |
| Depreciation | 500/6 = **83.333**; /4 = **125**; /3 = **166.667**; difference **83.333 annually**. Correct for a fully operating, zero-residual, $500bn short-lived asset pool. It is not an observed big-four earnings misstatement. With the note's 727.5 capex base, the analogous difference is **80.833**. |
| Burry comparison | The note's one-cohort 83.3 annual difference does not reproduce a cumulative **176 over 2026–28** or company-specific **20.8%/26.9%** earnings overstatements. Different cohorts, in-service dates, taxes and earnings denominators are needed. Calling it similar scale is not a verification. |
| Rental / inference hardware ratios | (2.35/1.70−1) = **38.24%**, reasonably “about 40%.” 0.19/0.42 = **45.24%**, i.e. **54.76% cheaper**, or the H100 cost is 2.21x. InferenceX itself incorrectly says “122% cheaper”; do not propagate that wording. Rental listings alone do not measure achieved utilization or lifetime return. |
| Model list-price ratios | Given the note's inputs: 30/1.25 = **24x** input-price decline; 60/10 = **6x** output decline. Opus 15/4 = 75/20 = **3.75x** decline. Google scheduled prices double. GPT-5→5.5 rises **4x/3x** input/output, but GPT-5.5→Sol falls **2.5x/3x**. Mixing premium and mainstream tiers does not identify a market-wide reversal. This checks the arithmetic, not every historical OpenAI price in unselected claim 25. |
| Claimed commodity gross margins | At 0.06–0.19 cost and 2–10 revenue per million, mechanical margins span **90.5–99.4%**. Those are not measured margins: the cost benchmark and closed-model price refer to different models, input/output mixes and service costs. |
| Token multipliers | 480/9.7 = **49.48x**; 3,200/480 = **6.667x**; 3,200/9.7 = **329.90x**. Correct rounded growth. 22bn/min is **950.4tn/month** for a 30-day month if sustained; it is a narrower scope and later date than total surfaces. 25/12.1 = **2.066x**, so the note's OpenRouter doubling is numerically consistent with its reported inputs. |
| Price × volume / Jevons | **Fails.** Sevenfold volume with 10–40-fold lower price gives **0.70x–0.175x revenue**, a **30–82.5% decline**, if units and mix are held fixed. In reality benchmark-capability prices and aggregate raw tokens are not comparable units. Neither the sign of paid revenue nor a causal Jevons effect follows from these series alone. |
| Training and R&D | 0.5/5 = **10%**; Epoch's more precise estimate is 9.6%. DeepSeek's stated 2.788m GPU-hours × $2 = **$5.576m**; rounding to 2.8m/$5.6m passes, conditional on assumed hourly cost, excluding research. Meta 57.372/43.873−1 = **30.77%**, correctly 31%. Epoch's 2.4x trend is an estimated historical fit; its published interval is **95%**, not the note's 90%, and >$1bn by 2027 is conditional extrapolation. [DeepSeek report][deepseek]; [Epoch training research][epoch-training]. |
| Eight-month efficiency halving | 2^(12/8) = **2.828x/year**, compatible in scale with ~3x. This does not independently verify the separate studies' populations or turn Huang's compute claim into a measured **10–100x tokens per answer** distribution. [Epoch efficiency research][epoch-efficiency]; [MIT preprint][mit]. |
| Model economic life “about a year” | Does not follow from 12–18-month API retirements or price declines. Official retirement dates include Opus 3 in January 2026 for its February-2024 model version—about **22 months**. Endpoint support life is also not the useful life of research, data or a model family. [Anthropic deprecations][deprecations]. |

All **20 cells** of the worked-model table are correct to the nearest billion:

| GPU life | 8%, 50% | 10%, 50% | 12%, 50% | 10%, 30% | 10%, 60% |
|---|---:|---:|---:|---:|---:|
| 3 | 446.448 | 467.852 | 489.761 | 779.753 | 389.876 |
| 4 | 360.336 | 381.208 | 402.647 | 635.346 | 317.673 |
| 5 | 308.871 | 329.534 | 350.822 | 549.224 | 274.612 |
| 6 | 274.730 | 295.344 | 316.638 | 492.240 | 246.120 |

The remaining worked-model conclusions need these corrections:

- **Combined cohorts:** exactly $1,360bn gives **$535.56–848.37bn**, rounded **$536–848bn**, not $535–847bn. The displayed 230.9+380.5+750 actually totals **1,361.4**, giving **536.11–849.24**. Using 727.5 instead gives **1,338.9**, requiring **527.25–835.21**. More fundamentally, summing original spending and applying fresh annuities ignores past cash recovery and remaining lives. It is not a prospective 2026 fleet valuation.
- **Sensitivity:** life 3 versus 6 years gives **1.584x**, correct as 1.6x. Margin 50% versus 30% gives **1.667x**, correct as 1.7x. Cost of capital 8%→12% raises the requirement by **9.70%, 11.74%, 13.58%, 15.25%** for lives 3/4/5/6; write **10–15%**, not simply ~10%. The chosen margin range has a slightly larger multiplier than the life range; the claimed ranking is not demonstrated.
- **Goldman's 417:** in this model it can be reproduced at approximately **39.5% EBITDA margin with five-year life**, or **35.4% with six-year life**. That is numerical compatibility, not confirmation of Goldman's capital base, return definition or tax treatment. ROIC is not automatically equivalent to an annuity discount rate.
- **“Double by 2028”:** 295–468 divided by 150–250 spans **1.18–3.12x** even accepting the unsupported revenue range. Combined-cohort 535–847 divided by that range spans **2.14–5.65x**. No commissioning schedule, 2027–28 investment or revenue path establishes the asserted deadline. Five-plus-year GPU life is not mathematically necessary: the table explicitly permits three years at sufficiently high revenue.
- **Margin boundary:** a renter's gross margin includes payments to a cloud provider; those payments already fund hardware ownership. Substituting it for the owner's EBITDA margin and then recovering the owner's capex again mixes layers. Positive adjusted gross margin can coexist with R&D losses and cash burn; it is not evidence that the included inference costs exceed sales.
- **Model boundary:** treat this as a scenario, not “the sector's own assumptions.” The two-thirds mix is extrapolated from Microsoft; 15 years for the remainder is assumed; all capex is attributed to incremental AI revenue. Replacement equipment, conventional cloud, logistics, internal advertising improvements, commissioning delays, taxes, working capital, declining utilization/prices, residual values and land are not separately modeled. The annuity formula also requires the short-life revenue stream to last L years and the long-life component 15 years; it is not one fixed combined annual revenue lasting forever.

## Omissions

The recent-event search covered **2026-09-17 through 2026-10-17**. These findings change the interpretation in both directions; reporting without primary access is expressly marked.

1. **September 22: fresh financing rather than an immediate funding shutoff.** CoreWeave's filed 8-K records **$4.2bn** of 2.875% convertible notes due 2033, including the exercised option; net proceeds before offering expenses were $4.137bn, with $566.2m spent on capped calls. That leaves about **$3.571bn** before other expenses, not $4.2bn of deployable cash. Financing remains available, while leverage and potential dilution increase. **A** contractual terms; **B** subtraction. [SEC 8-K][crwvsept].

2. **September 28–October 1: concrete lab obligations and supplier credit.** Reuters reports from Anthropic's nonpublic prospectus nearly **$4.6bn 2025 revenue, >$8bn operating loss and ~$42bn net loss**, of which ~$34bn was a financing-valuation charge, not cash burn; future compute obligations were **$518bn**. Its follow-up describes up to **$42bn** of Broadcom-arranged convertible financing linked to a **$125.2bn five-year TPU lease**, with acceleration/availability risks on default. These are **C, reported, unverified**, not directly inspected SEC disclosures. They make counterparty funding and contractual maturity at least as important as physical GPU life. [Reuters prospectus report][anthprospectus]; [Reuters financing report][anthbroadcom].

3. **October 14: stronger lab monetization contradicts the blanket lab-loss characterization.** Reuters reports Anthropic Q3 revenue of **$16.8bn**, up **44.83%** from $11.6bn, and adjusted profitability. Quarterly annualization is **$67.2bn**; Q1–Q3 sums to **$33.1bn**. Neither is full-year recognized revenue or audited profit. The note should include this strongest counterevidence alongside the financing risk, with **C, reported, unverified**. A September Reuters analysis also reports approximately **40% 2025 gross margin**, so OpenAI's leak is no longer the only publicly reported lab-margin figure. [Reuters October 14][anthq3]; [Reuters Breakingviews][anthmargin].

4. **Recent price competition contradicts a universal frontier-price turn.** Anthropic's current Opus 5.5 announcement lists input/output prices of **$4/$20 versus Opus 5's $5/$25**, a **20% decrease**, and cheaper cache reads. Its performance assertions are vendor claims, not independent validation. The note mentions falling Opus prices but fails to carry that contradiction into its Summary. [Anthropic announcement][opus55].

5. **Older but indispensable: financing and accounting already visible in the cited filings.** Microsoft's July call changes building lives from **15 to 25 years**, changing lease classification and reported capex without changing investment plans. Oracle's Q1 operating cash flow includes **$11.363bn customer prepayments with a significant financing component**; its disclosed net cash outlay for capex is **$17.966bn**, versus $28.499bn gross. This shifts timing and risk, not the ultimate need to earn a return. [Microsoft Q4 call][msq4]; [Oracle 10-Q][orclq]; [Oracle release][orclpr].

6. **Losses after financing are already material at CoreWeave.** Q2 adjusted EBITDA margin is **59%**, yet adjusted net loss is **$567m/22% of revenue**; GAAP net loss is **$626m/24%**, with **$640m net interest expense**. “Roughly break-even after depreciation and interest” is contradicted by the same release the note cites. This is exactly why EBITDA, operating profit and net profit must be separated. [CoreWeave Q2 release][crwvq2].

7. **The hardware boundary is wider than Nvidia GPUs.** Anthropic identifies Trainium, TPUs and Nvidia GPUs in its compute mix. Broadcom/Apollo/Blackstone's June primary announcement describes an initial **$35bn** infrastructure financing tranche. This is an additional financing channel, but should not be added to lab lease commitments or hyperscaler capex without eliminating overlap. A Nvidia-only revenue multiplier cannot precisely measure total AI infrastructure. [Anthropic][anthcompute]; [Broadcom financing announcement][broadcomplatform].

8. **Total capex can earn returns without separately billed AI revenue.** Amazon explicitly includes fulfillment capacity in its investment description. Internal AI can improve existing ads, recommendation systems and software economics. Conversely, cloud segment profit does not isolate new AI-cohort returns; Alphabet allocates shared AI research expenses outside Cloud. These scope problems can bias the proposed revenue gap either way. [Amazon 10-Q][amznq2]; [Alphabet segment footnote][googq2].

A further credit-event lead merits follow-up: **Axios reported September 25 that Oracle invoked force majeure for Project Jupiter; I did not verify the notice itself.** [Axios][oracle-credit]. That report does not establish a debt default, and I have not used it as one. The primary Oracle project update on October 13 says scope is unchanged; that does not resolve lease-payment timing. [Oracle update][oracle-jupiter].

## Summary-bullet assessment

1. **Capex scale — broadly supported, precision overstated.** Historical numbers match mixed-period arithmetic. Current company guidance is stale in opposite directions for Amazon and Microsoft. Oracle's fiscal-year spend and one-quarter annualization cannot be silently added to calendar-year forecasts. ~$800bn is a scale comparison, not a filing reconciliation.

2. **Required-revenue estimates — conditionally supported as scenarios.** The $300–470bn rounding is sound for the chosen $750bn assumptions. The combined-cohort figures need minor numerical correction and major timing qualification. Sequoia, Bain, JPMorgan and Goldman do not measure a common population, capital vintage or return metric. Their figures do not form a chronological series of one “required revenue” statistic.

3. **Revenue and narrowing gap — first part supported, conclusion not established.** Cloud growth and Microsoft's disclosed run-rate are supported; lab figures need their private-reporting caveat. The $150–250bn denominator has no reproducible construction. A gap cannot be measured or shown to narrow without matching revenue, asset populations, margins and periods. Anthropic's latest quarterly report should be included.

4. **Depreciation fulcrum — useful sensitivity, overgeneralized evidence.** The $83bn difference follows from the scenario. Microsoft's asset mix is not industry disclosure; CPU/server schedules are not GPU-specific useful lives. A listed A100 rental rate shows availability, not six-year profitability or realized utilization. A single-model Blackwell comparison does not prove that all H100 workloads are viable only under scarcity.

5. **Inference prices and Jevons — partly supported facts, unsupported inference.** Fixed-capability price declines and Google's scheduled increases can coexist. The note's own Opus and Sol examples contradict the blanket “frontier prices stopped falling” claim. Aggregate tokens neither demonstrate price elasticity nor paid revenue; the 7x-versus-10–40x arithmetic runs against the stated inference when units are held constant.

6. **Training — replace the first phrase and qualify the accounting.** Final released-model runs appear to be a minority of **R&D compute spending**; this does not make training broadly defined a minority, because experiments and unreleased models are also training. The MiniMax/Z.ai percentages are estimates, not direct filing ratios. The >$1bn statement is an extrapolation. Rental, prepayment and lease structures make “labs expense, hyperscalers capitalize” too categorical.

7. **Single biggest uncertainty — not established.** GPU economic life is an important scenario variable. The displayed margin sensitivity is slightly greater over the selected ranges, while customer solvency, contract terms, utilization and funding have independent effects. The model cannot establish Burry's company-specific earnings claims, and changing an accounting schedule does not itself change cash payback.

## Your assessment

There is no single entity here: Nvidia is demonstrably highly profitable, diversified hyperscalers have real profitable businesses supporting the build, and the capital-intensive intermediary/lab layer is much less secure. Nvidia's Q2 **75% gross margin** and substantial operating profit are observed; their persistence is not guaranteed. [Nvidia results][nvdaq2]. CoreWeave is already loss-making after financing costs, and Oracle's expansion relies on customer advances and external capital despite profitable operations. Labs must be distinguished: OpenAI's reported losses remain severe, while Anthropic's reported recent adjusted profit is meaningful counterevidence, though neither proves durable free cash flow under future commitments. My judgment is that equity in highly committed labs and leveraged capacity providers bears the earliest economic losses if demand or refinancing disappoints, followed by exposed lenders, lessors and suppliers according to contractual protections; actual cash stress may arise at either customer or provider depending on prepayments and guarantees. I agree with the note that asset life matters and revenue is growing; I differ by declining to endorse its quantified aggregate shortfall, its proof of Jevons, its neocloud break-even description or its assertion that GPU life alone decides who loses.

## Recommended edits

1. **Correct the capex label and guidance.** Replace the opening historical claim with: “Using company-specific definitions and Microsoft's June fiscal years, the mixed-period totals are $230.9bn and $380.5bn; these are not calendar-year AI-only capex cohorts.” Update Microsoft to ~$175bn reported guidance, explaining unchanged investment plans, and Amazon to ~$220bn with a B-grade reporting citation. Show the resulting ~$732.5bn midpoint separately from the ~$747.5bn earlier-basis comparison. [Microsoft][msq4]; [AP][amazon-ap].

2. **Make the model a scenario and correct its extension.** Replace its setup with: “We illustrate capital recovery for an assumed $750bn cohort, with two-thirds short-lived equipment and one-third long-lived infrastructure; this is not an estimate of AI-only investment.” Keep the 20-cell table. Replace “$1.36tn…$535bn…$847bn” with “An exactly $1.36tn hypothetical new cohort requires $536–848bn annually under the same assumptions; this does not value the remaining obligations of previously deployed cohorts.”

3. **Withdraw the unsupported aggregate gap and deadline.** Replace the $150–250bn conclusion and final doubling assertion with: “Available disclosures do not establish a non-overlapping total of AI end-customer revenue. They therefore cannot quantify the sector-wide payback gap or establish a revenue-doubling deadline.” Require a company-by-company revenue bridge and commissioning/cash-flow schedule before reinstating either.

4. **Correct Jevons arithmetic.** Replace “Even at 10–40x…” with: “At constant units and mix, sevenfold volume and a 10–40-fold price decline imply revenue falling 30–82.5%. Our capability-price and aggregate-token series are not comparable enough to estimate this effect. Rising usage alone does not establish a causal Jevons effect.”

5. **Separate margins by layer.** Replace the margin-stack sentence with: “Nvidia is highly profitable; CoreWeave is profitable on adjusted EBITDA but materially loss-making after depreciation and financing; lab profitability varies and remains incompletely disclosed.” Delete the inference that positive OpenAI gross margin proves inference costs are uncovered. State that renter gross margin cannot substitute for owner EBITDA in the capex model. [CoreWeave][crwvq2].

6. **Qualify asset-life and earnings claims.** Replace “single biggest uncertainty” with “GPU economic life, utilization, operating margin and customer funding are major uncertainties.” Replace the Meta comparison with “The extension added $2.59bn to 2025 net income, 4.3% of reported annual earnings.” Change cost-of-capital sensitivity to “10–15%.” State that the $83bn sensitivity does not verify Burry's company-level earnings-overstatement estimates.

7. **Repair training attribution and forecasts.** Replace the training Summary opening with: “Epoch estimates final released-model runs at 9.6%, 22.6% and 12.3% of R&D compute spending at OpenAI, MiniMax and Z.ai; these are modeled ratios, not direct prospectus disclosures.” Grade the ratios C; change claim 36's interval to **95%** and “will pass” to “would exceed $1bn by 2027 if the historical trend continues.” [Epoch ratios][epoch-rd]; [training trend][epoch-training].

8. **Remove the asserted one-year model asset life.** Replace it with: “API retirement dates do not establish the economic life of model development. The reported OpenAI research-compute treatment lacks a primary accounting-policy disclosure, so we cannot infer a GAAP earnings overstatement.”

9. **Replace the universal pricing turn.** Use: “Some premium tiers and scheduled Google prices are rising, while other models are becoming cheaper. Compare equivalent capability, workload, caching and service tier before inferring pricing power.” Include the September Opus 5.5 price cut as counterevidence. [Anthropic][opus55].

10. **Add current lab evidence with symmetric caveats.** Insert: “October reporting describes Anthropic's Q3 revenue of $16.8bn and adjusted profitability; separate prospectus reporting reveals substantial historical losses and future compute obligations. Both remain reported, unverified.” Add the financing and concentration facts in Omissions 2, and remove the assertion that OpenAI is the only available reported lab-margin observation. [Reuters revenue][anthq3]; [prospectus][anthprospectus]; [margin][anthmargin].

11. **Add financing mechanics to the analysis and signals.** Insert: “Track customer prepayments, lease commitments, supplier credit and new securities alongside gross capex. These determine who funds the assets and when losses reach investors.” Include Oracle's customer advances, Microsoft's lease reclassification, CoreWeave's September convertible and the reported Broadcom facility; do not add overlapping funding and capex figures together. [Oracle][orclq]; [CoreWeave][crwvsept]; [Reuters facility][anthbroadcom].

12. **Fix scope and provenance in claim tables.** Label Google tokens “all surfaces,” distinguish customer-count growth from consumption growth at Microsoft, identify Alphabet's ATM as unused authorization, and label each required-revenue estimate by layer, horizon, capital base and return definition. Preserve C grades where the original bank model or private-company accounts were not inspected; a matching secondary summary is not primary verification.

[amzn24]: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm
[amzn25]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
[amznq2]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[ms25]: https://www.microsoft.com/investor/reports/ar25/index.html
[msq3]: https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3
[msq3pr]: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
[msq4]: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
[goog25]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[googq2]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[meta25]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[metaq2]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[amazon-ap]: https://apnews.com/article/b4ce02b4666a35b8975823c5c22072ee
[orclpr]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm
[orclq]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
[inferencex]: https://inferencex.semianalysis.com/compare/minimax-m27-gb200-vs-h100
[gemprice]: https://ai.google.dev/gemini-api/docs/pricing
[gemlog]: https://ai.google.dev/gemini-api/docs/changelog
[io26]: https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
[decoder]: https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/
[oaiq2]: https://ca.investing.com/news/stock-market-news/openais-q2-revenue-growth-lagged-anthropic-as-losses-deepened-wsj-reports-4806938
[oaiburn]: https://www.channelnewsasia.com/business/openai-burned-37-billion-in-first-quarter-2026-information-reports-6188641
[anth65]: https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai
[anthcompute]: https://www.anthropic.com/news/google-broadcom-partnership-compute
[anthq3]: https://ca.marketscreener.com/news/anthropic-s-q3-revenue-surges-45-to-nearly-17-billion-ce785dd2d08cf221
[anthprospectus]: https://www.marketscreener.com/news/anthropic-s-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-ce785addd98afe2c
[anthbroadcom]: https://www.marketscreener.com/news/broadcom-to-lend-anthropic-up-to-42-billion-to-lease-its-chips-filing-says-ce785ad3de89fe20
[anthmargin]: https://www.breakingviews.com/columns/breaking-view/anthropics-2-trln-goal-is-ais-biggest-moonshot-2026-09-29/
[epoch-rd]: https://epoch.ai/gradient-updates/r-and-d-vs-training-compute
[epoch-oai]: https://epoch.ai/data-insights/openai-compute-spend
[epoch-training]: https://epoch.ai/publications/how-much-does-it-cost-to-train-frontier-ai-models
[epoch-efficiency]: https://epoch.ai/publications/algorithmic-progress-in-language-models
[mit]: https://arxiv.org/html/2511.23455v1
[deepseek]: https://arxiv.org/html/2412.19437v1
[nvdaq2]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm
[sequoia]: https://sequoiacap.com/article/ais-600b-question
[jpm]: https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/how-is-ai-being-monetized/
[goldman-summary]: https://advisoranalyst.com/2026/10/15/ai-capex-required-revenues-and-what-the-market-is-actually-pricing.html/
[bain]: https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/
[oai70]: https://www.axios.com/2026/09/29/scoop-openais-annual-recurring-revenue-nears-70b
[deprecations]: https://platform.claude.com/docs/en/about-claude/model-deprecations
[crwvq2]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
[crwvsept]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm
[opus55]: https://www.anthropic.com/claude-opus-5-5
[broadcomplatform]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
[oracle-credit]: https://www.axios.com/2026/09/25/oracle-debt-data-centers
[oracle-jupiter]: https://www.oracle.com/news/announcement/project-jupiter-is-expected-to-generate-13-billion-in-economic-impact-2026-10-13/
