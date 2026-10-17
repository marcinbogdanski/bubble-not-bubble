# GPU pricing, utilization and residual value

*Last updated: 2026-10-17 · Author: Codex / OpenAI · Status: reviewed · Reviewer: Codex (gpt-6-astra) cross-check, applied 2026-10-17*

## Summary

- On September 17, 2026, CoreWeave disclosed 3–6-month cluster contracts at about $40m/MW-year; its North America H100 spot list was $2.464/GPU-hour on October 17. These different products support segmented pricing, not a measured market-wide shortage or glut. ([row 20][s21], [row 9][s9])
- Silicon Data's October 17, 2026 H100 display was $2.82/GPU-hour; OCPI's October 16 print was $2.74; FastGPU's October 16 advertised floor was $1.785. Silicon standardizes configurations and weights providers, OCPI weights active on-demand rentals, and FastGPU tracks advertised floors. These observations cannot form a single price history. ([row 1][s1], [row 3][s5], [row 6][s6], [Silicon method][s42], [OCPI method][s43], [FastGPU method][s7])
- OCPI's October 1–16, 2026 means versus September were H100 $2.831 versus $2.829, H200 $5.748 versus $4.880, B200 $7.693 versus $7.245, and A100 $0.927 versus $1.000/GPU-hour. These average daily prints, not all monthly transactions; H100's October 16 daily fall of 12.5% does not describe all accelerators. ([rows 4–5][s5], [method][s43])
- CoreWeave reported a 59% adjusted EBITDA margin but a $626m net loss in Q2 2026. Neither establishes returns after hardware replacement and financing. Take-or-pay and supplier capacity commitments reduce some revenue risk while leaving delivery, counterparty and renewal exposure; paid capacity alone does not establish independent end-user demand. ([row 18][s18], [row 44][s49], [row 45][s50])
- SemiAnalysis's one-year H100 midpoint rose from $1.70 in October 2025 to $2.35 in March 2026. This survey supports continued earning potential for older GPUs, with C confidence in market levels/recovery; it does not validate company-wide useful lives or Silicon Data's modeled resale values as completed sales. ([row 16][s16], [dashboard][s17], [row 30][s32])
- Paid GPU-hours and comparable renewal prices remain the main missing denominators in this evidence: CoreWeave's 98% committed-revenue share in Q2 2026 and SF Compute's September 9, 2026 average 25% resale rebate measure neither productive utilization nor fleet occupancy. ([row 18][s19], [row 15][s15])

## Key claims

Rental units: **USD/GPU-hour**. “Observed” is the access date, not settlement. A grades the published statement/print, not market representativeness. Proposed thresholds are D judgments. All sources accessed **2026-10-17**.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Silicon Data public neocloud panel | H100 $2.82; H200 $3.51; B200 $6.12; B300 $7.01; A100 $1.53; displayed weekly changes +6.4%, +6.0%, +7.0%, +0.9%, −3.2% respectively | observed 2026-10-17; no settlement stamp | [panel][s1] | primary | A print; C freshness |
| 2 | Brief/register baseline not independently reproduced | H100 $2.83 on 2026-10-16; February 2025 low ~$1.86; claimed ~53% rise; arithmetic on those rounded inputs = 52.2% | alleged periods | [register](/forecasts/register); portal sign-in ([2][s2]) | tertiary / unverified input | D |
| 3 | OCPI settled panel | H100 $2.74; H200 $6.34; B200 $8.12; A100 SXM4 $0.94 | 2026-10-16 | [Ornn][s3] | primary | A print; C market coverage |
| 4 | OCPI H100 short-term reversal | $3.21 Oct 14 → $3.13 Oct 15 → $2.74 Oct 16; last day −12.5%; week −1.8%; month +4.6% | 2026-10-16 | [dated market page][s4] | primary, derived changes | A prices; B calculated changes |
| 5 | OCPI equal-weight means of daily 4 p.m. ET observations, not monthly transaction averages | Aug / Sep / Oct-to-16: H100 $2.7710 / $2.8293 / $2.8306; H200 $4.7048 / $4.8803 / $5.7475; B200 $6.1419 / $7.2450 / $7.6925; A100 $1.0571 / $0.9997 / $0.9269 | partial Oct 2026 | [history API][s5], model-specific endpoints in CSV | primary, derived | B |
| 6 | FastGPU frozen provider medians | H100 SXM $3.949; H200 $4.54; B200 $6.69; B300 $9.765; A100 80GB $1.99; corresponding floors $1.785 / $2.69 / $3.69 / $4.89 / $0.873 | 2026-10-16 fixing | [fixing CSV][s6] | tertiary, reported unverified | C |
| 7 | FastGPU floor composite | 100.3, +0.3% since Oct 12; only 5 days through Oct 16 | observed 2026-10-17 | [index][s7] | tertiary | C |
| 8 | Lambda instances; node-size effect | H100 SXM $3.99 on 8-GPU node, $4.29 single; B200 $6.69 / $6.99; A100 SXM 80GB $2.79 on node | observed 2026-10-17 | [pricing][s8] | primary | A |
| 9 | CoreWeave North America, normalized node rates | H100 on-demand $6.155, spot $2.46375; H200 $6.305 / $2.61625; B200 $8.60 / $4.26375; B300 spot $4.48; A100 $2.70 / $1.20625; nodes have 8 GPUs | observed 2026-10-17 | [pricing][s9] | primary, derived | B division; A node quotes |
| 10 | Oracle USD list, browser-rendered | H100/H200 $10; B200 $14; B300 $15; A100 80GB $4; each relevant shape has 8 GPUs | observed 2026-10-17 | [price list][s10] | primary | A |
| 11 | RunPod advertised Pod rates | H100 SXM $3.99; PCIe $2.89; NVL $3.19; B200 $7.99; A100 SXM/PCIe 80GB $1.79 | observed 2026-10-17 | [pricing][s11] | primary | A |
| 12 | Hyperstack on-demand / starting reservation | H100 SXM $3.20 / $2.72; H200 $3.99 / $2.79; B200 $6; B300 $7.40; A100 SXM 80GB $1.60 | observed 2026-10-17 | [pricing][s12] | primary | A |
| 13 | Vast earlier marketplace snapshot; differing values not independently reproduced | Earlier note recorded H100 SXM $1.73 / $2.40 and A100 SXM4 $0.40 / $0.65 floor/median; H200/B200/B300 floors $3.95 / $6.25 / $9.94. Later verified display in row 50; hourly offers can change | 2026-10-17; earlier time unrecorded | [rendered pricing][s13] | primary page; earlier differing values unverified | Earlier H100 floor/A100 median not independently reproduced; A reproduced displays; D comparability |
| 14 | SF Compute Autoresearch | H100 interactive weekend $4.032; batch $0.063/minute = $3.78/hour | observed 2026-10-17 | [pricing][s14] | primary, derived | A/B |
| 15 | SF Compute customer idle-capacity resale | Average 25% realized discount through resale; not a fleet utilization percentage | 2026-09-09 | [company explanation][s15] | primary, unaudited | A statement |
| 16 | SemiAnalysis reports H100 contract recovery | One-year midpoint $1.70 Oct 2025 → $2.35 Mar 2026: +38.2%; interquartile ranges $1.45–1.95 → $2.00–2.70; typically 25% prepayment assumed; April extension in row 49 | 2026-04-02 article; dashboard through Apr 2026 | [SemiAnalysis][s16], [dashboard][s17] | secondary survey / estimate | C market levels/recovery; A publisher attribution; B conditional arithmetic |
| 17 | CoreWeave blended revenue/power proxy | Q2 revenue $2.575bn, ending active power 1.5 GW; annualized quotient ~$6.87m/MW-year, rounded ~$6.9m in companion note | 2026-Q2 | [release][s18]; [note](/research/stack/coreweave) | primary, derived | B arithmetic; D contract-price interpretation |
| 18 | Adjusted EBITDA versus GAAP bottom line | CoreWeave adjusted EBITDA margin 59%, net loss $626m; committed contracts 98% of revenue | 2026-Q2 | [release][s18], [10-Q][s19] | primary | A |
| 19 | Nebius contracted yields and financing | Four landmark Q2 deals $20–25m/MW-year; overall Q2 average above $20m; most associated capacity arrives late 2026 and contributes mainly in 2027; core terms 1–3 years; 70% of deals included prepayments covering 50–60% of associated capex; projected payback 1 year 10 months | 2026-08-12 | [shareholder letter][s20]; [companion note](/research/stack/neoclouds-other) | primary, company estimates | A statement; C realized return |
| 20 | CoreWeave new short-term cluster contracts | ~$40m/MW-year annualized, terms 3–6 months | 2026-09-17 | [IR disclosure][s21] | primary | A |
| 21 | Illustrative conversion inputs and outputs | DGX H100/H200: 8 GPUs, maximum 10.2 kW; B200: 8, 14.3 kW; 1 MW = 1,000 kW; annual convention 8,760 hours; proxy $6.87m → ~$1.00/H100-hour; $20–25m → ~$4.08–5.10/B200-hour | specs accessed 2026-10-17 | [H100 guide][s22], [B200 guide][s23]; rows 17,19 | primary, conditional derivation | B arithmetic; D actual contract rate |
| 22 | Disclosed contract without GPU count | IREN–Microsoft ~$9.7bn, 5-year term, 200 MW critical IT load, 20% prepayment; implies ~$9.7m/MW-year; exact GPU-hour rate not identifiable | 2025-11-03 | [IREN release][s24] | primary, derived | A/B |
| 23 | Future power delivery pipeline, not proof of overdue supply | CoreWeave 393 MW undelivered at one site, phases scheduled in 2026 and 2028; 355 MW elsewhere scheduled during 2026–2028. These figures alone establish neither missed schedules nor stranded GPUs | 2026-06-30 | [10-Q, lease commitments][s19] | primary | A amounts/timing; D missed-schedule inference |
| 24 | Direct counterexample to universal profitability | Soluna ended HPE GPU-service arrangement in March 2025 after weak pricing and inadequate cluster scale | 2025-03 presentation | [company deck, p.15][s25] | primary | A statement |
| 25 | Accounting lives, linked to existing register | CoreWeave technology equipment 6 years; Amazon servers/networking 5–6, subset shortened 6→5 effective 2025 for faster technological development; Nebius server/network equipment 4→5 in 2026; policies do not validate individual GPU economic lives | latest retrieved filings | [CoreWeave 10-K][s26], [Amazon 10-K][s27], [Nebius letter][s20]; [CSV](/data/ai-unit-economics-useful-life.csv) | primary | A accounting policies; no economic-recoverability grade transfer |
| 26 | Existing A100 median not reproduced | Existing note $1.84; fetched GetDeploying page $1.79, explicitly dated Oct 2, 2026; 48 listed providers; cannot establish like-for-like change | retrieved 2026-10-17 | [existing note](/research/theory/ai-unit-economics), [page][s28] | tertiary | C; D comparison |
| 27 | Used asking prices, not sales | H100 SXM5 median $19,550 (3 US listings); A100 SXM4 80GB $9,925 (4); PCIe medians $32,000 / $18,500 | 2026-09-09 | [Caladan survey][s29] | tertiary, reported unverified | D |
| 28 | Claimed completed-sale index shows weakness | American Compute index 107 Apr → 86 Jul → 75 Aug; base H1 2025=100; older chips led fall, HGX H100 held | Oct 2026 edition, Aug observation | [resale index][s30] | tertiary, reported unverified | D |
| 29 | Opposing used-server report | Eight-GPU A100 server $180,000 Sep 2024 → $70,000 Sep 2025 → $84,000 Sep 2026; latest rebound +20% | 2026-10-07 | [report tracing Epoka chart][s31] | secondary, reported unverified | C |
| 30 | Residual-value model is not a sale tape | Silicon Data discounts projected rental cash flows; forward inputs through 36 months, modeled tail/utilization and fixed blended operating-cost ratio; configurable maximum physical life around 8 years | observed 2026-10-17 | [product/method][s32] | primary | A description; D independent resale evidence |
| 31 | Dated bearish marketing versus actual historical cut | Thunder Compute updated Oct 1, 2026 describes “pricing pressure”; cited AWS cut was announced June 5, 2025, up to 45% | respective publication dates | [vendor article][s33], [AWS announcement][s34] | primary | A dates/statements; D current decline inference |
| 32 | Mid-October record claim unverified | Oct 15 report relays B300 “17 consecutive days” to record; original Compute Desk transaction series not retrieved | 2026-10-15 | [Yash Thakker's report][s35] | tertiary, reported unverified | D |
| 33 | Epoch Nvidia estimated shipments, completed periods | 2024 ~3.838m; 2025 ~4.458m; H1 2026 ~2.917m dataset units, including ~2.327m B300 | dataset updated 2026-10-14 | [downloadable timelines][s36], [documentation][s37] | secondary estimate, derived | C |
| 34 | Cumulative shipments are not installed usable capacity | Since 2022 through Q2 2026: Nvidia ~13.342m units; all covered designers ~31.595m H100-equivalent peak compute; excludes flagged incomplete quarters; sums component estimates/medians, not an aggregate median or operating fleet | dataset updated 2026-10-14 | [Epoch timelines][s36] | secondary estimate, derived | C |
| 35 | Supply pipeline forecasts, different denominators | TrendForce Apr: high-end Nvidia GPUs +~26%, Blackwell mix 71%; Oct: all AI servers +32.2% in 2026, nearly +36% in 2027 | 2026-04-08 / 2026-10-14 | [April][s38], [October][s39] | secondary forecast | C |
| 36 | Analyst-summary unit trap | Global X says 5.2m Blackwell in 2025, 5.7m in 2026; its footnote instead labels 2026 1.8m Blackwell plus 5.7m Rubin; excluded from supply estimate | 2026 report | [PDF, pp.2,5][s40] | secondary, internally conflicting | D |
| 37 | Dataset scope | 4,491 observations: 364 OCPI, 3,883 FastGPU provider-day means, 192 FastGPU fixings, 50 direct snapshots, 2 survey midpoints; FastGPU history Aug 19–Oct 16 | retrieved 2026-10-17 | [rental CSV](/data/gpu-rental-prices.csv), [FastGPU dataset][s41] | mixed, labeled per row | A provenance; C/D inference |
| 38 | P1 resolution rule | Monthly mean SDH100RT < $1.50 for 3 consecutive complete months; require ≥80% scheduled publication coverage; no interpolation | proposal 2026-10-17 | [P1](/forecasts/register), [Silicon methodology][s42] | primary rule / author judgment | D threshold |
| 39 | Additional glut warnings, not estimated break-even | H100 <$2.00 for 30 days; H200/B200 comparable prices down >40% YoY for 3 months; paid occupancy <60% for 2 quarters; comparable used-sale prices down >40% YoY | proposal 2026-10-17 | author monitoring design using rows 3–30 | primary rule / author judgment | D |
| 40 | Successor-series rule | If SDH100RT unavailable for a complete month, OCPI-H100 successor threshold $1.50 × median(OCPI/SDH100RT) over preceding 90 overlapping daily dates; require ≥60 fresh pairs; exclude carried-forward/disrupted prints from overlap and fresh-publication coverage, record quality flags; otherwise unresolved | proposal 2026-10-17 | [OCPI methodology][s43], author design | primary rule / author judgment | D |
| 41 | Nebius October posted prices and cached prior comparison | H100 $3.85→$4.50 (+16.9%); H200 $4.50→$5.40 (+20.0%); B200 $7.15→$8.50 (+18.9%); B300 $7.85→$9.50 (+21.0%). Separate dynamic preemptible floors: H100/H200 $0.79, B200/B300 $0.99 | increases effective 2026-10-01 per search-cached primary page; current levels fetched 2026-10-17 | [Nebius prices, live and search-cached versions][s46] | primary; historical page recovered through search cache; changes derived | A current posted levels/floors; B historical dates/comparisons |
| 42 | Rubin production availability and workload-specific performance | CoreWeave reports limited availability, hundreds of GPUs across multiple regions, production use by Cognition; up to 4.8× GB200 inference token throughput per GPU at matched interactivity for Cognition's SWE-2 workload | 2026-09-30 | [CoreWeave deployment account][s47] | primary, vendor/customer result | A announcement; C generalized performance/economic implications |
| 43 | CoreWeave convertible financing priced, not closing verified | $3.7bn senior unsecured convertible notes, 2.875% coupon, due 2033; $0.5bn option; estimated net proceeds before other offering expenses $3.6445bn, planned capped calls $0.4988bn, leaving ~$3.1457bn before those expenses | 2026-09-18 pricing announcement | [CoreWeave financing release][s48] | primary terms; derived subtraction | A terms; B subtraction |
| 44 | NVIDIA backstop for covered CoreWeave capacity | September 9, 2025 agreement: initial value $6.3bn; NVIDIA obligated to buy residual unsold capacity covered by the agreement through April 13, 2032, subject to delivery, service availability and termination provisions; not a whole-fleet/debt guarantee | agreement 2025-09-09; filed 2025-09-15 | [CoreWeave 8-K][s49] | primary | A disclosure; risk-transfer interpretation is inference |
| 45 | NVIDIA AI-cloud commitments | $36bn, typically six years; commitments decrease as third parties or NVIDIA use capacity. Overlap with row 44 unresolved: do not add them | 2026-07-26 | [NVIDIA 10-Q][s50] | primary | A disclosure |
| 46 | Geographically restricted H200 inventory impairment | $0.4bn excess-inventory/purchase-obligation charge amid China sales restrictions; does not imply these units are freely transferable to the sampled rental market | H1 FY2027, ended 2026-07-26 | [NVIDIA 10-Q][s50] | primary | A charge and disclosed context |
| 47 | OCPI observation window and stale-print treatment | Rolling one-hour calculation window; market page daily observations at 4 p.m. ET; disruption rules permit carry-forward or suspension. Row 5 averages daily prints equally; fresh-publication coverage must exclude stale carried-forward prints | methodology/market page fetched 2026-10-17 | [OCPI method, §§3.1, 3.7, 4.3][s43], [market page][s4] | primary description; author monitoring rule | A description; D monitoring rule |
| 48 | FastGPU composite smoothing versus frozen fixings | Three-day endpoint averaging; plotted line is a seven-day trailing average; current incomplete UTC day excluded; daily fixings frozen separately | methodology fetched 2026-10-17 | [FastGPU index methodology][s7] | primary description of tertiary series | A methodology description; no upgrade to underlying price evidence |
| 49 | SemiAnalysis April extension and financing assumption | One-year H100 range $2.10–2.70, midpoint $2.40; dashboard assumes typically 25% prepayment for terms of at least three months; not an audited renewal tape | Apr 2026 survey; fetched 2026-10-17 | [SemiAnalysis dashboard][s17] | secondary survey / estimate; derived midpoint | C market levels/recovery; A publisher attribution; B conditional midpoint |
| 50 | Vast later live snapshot verified in cross-check and application | H100 SXM floor/median $1.33 / $2.40; A100 SXM4 $0.40 / $0.80; H200/B200/B300 floors $3.95 / $6.25 / $9.94; available-offer prices update hourly | cross-check 2026-10-17 around 20:55 UTC; reproduced on application 2026-10-17 | [Vast rendered pricing][s13] | primary; pricing-mode mix unclear | A displayed values; D like-for-like market inference |

## Analysis

### Reading the market without mixing products

**Connected, deliverable clusters can be scarce while standalone GPU-hours remain cheap.** Silicon Data standardizes records for term, geography, platform and variant, then weights providers. Its weekly-recalibrated proprietary basis model is not externally reproducible. The portal required sign-in; the public panel lacks a settlement timestamp. ([1][s1], [2][s2], [42][s42])

Ornn says OCPI uses active on-demand transactions, volume weighting and winsorization, excluding reserved contracts. Contributor identities and the winsorization parameter remain private. Its methodology makes the administrator's published benchmark primary evidence, with unverified market representativeness. Public history was retrieved despite documentation emphasizing API keys. Row 5 equally averages daily 4 p.m. ET observations of a rolling one-hour benchmark, not all monthly transactions; disruption rules permit stale carry-forward prints. Publication and quality flags are needed for fresh-observation coverage (row 47). ([3][s3], [4][s4], [5][s5], [43][s43])

FastGPU records offers, not transactions or volumes. Its floor composite averages proportional changes geometrically; frozen fixings separately publish provider medians. The composite has much shorter history than its downloadable provider series. It averages endpoints over three days and plots a seven-day trailing average; the frozen daily fixings are a separate output (row 48). Historical observations in the CSV remain tertiary, reported unverified; direct current pages provide spot checks. ([6][s6], [7][s7], [41][s41], [44][s44])

CoreWeave's spot discount buys interruptibility; Lambda's instance and cluster products carry different connectivity and availability promises. Shadeform's [pricing page](https://shadeform.com/prices) loaded without numeric catalogue data. SF Compute's wholesale price URL redirected to its homepage; Autoresearch retail rates are not wholesale clears. Vast's rendered cards do not establish a mode-specific transaction series. Inventory was not tested by ordering. Nebius's October 1 list increases of 16.9–21.0% across H100/H200/B200/B300, alongside separate cheap preemptible floors, strengthen the case for segmented asking-price power, without measuring transactions or occupancy (row 41). ([Nebius pricing][s46])

### Contract economics, utilization and losses

The [CoreWeave note](/research/stack/coreweave)'s revenue/MW quotient combines quarterly revenue with ending active power. Ramping and hardware mix distort it. The [Nebius note](/research/stack/neoclouds-other)'s $20–25m yield describes four landmark deals, with an overall Q2 average above $20m/MW-year; most associated capacity arrives late 2026 and contributes mainly in 2027. These numbers are not comparable tariffs. CoreWeave's subsequent short-term disclosure independently supports a premium for near-term clusters. ([18][s18], [19][s19], [20][s20], [21][s21])

**Rate = annual revenue per MW × kW per GPU / (1,000 × 8,760)** at full-year paid availability. Retrieved DGX maximum powers produce row 21's conditional examples. Networking, storage, headroom, PUE, actual draw and billing occupancy alter them. These are dimensional checks, not discovered customer tariffs; there is no evidence these exact DGX configurations underpin Nebius's deals. IREN's $9.7m/MW-year is a contract-term average with phased delivery, not a 2026 run-rate; its release lacks a GPU count, preventing an exact GPU-hour calculation. ([specifications][s22], [B200 guide][s23], [IREN release][s24]) Ornn's [reserve listings](https://ornn.com/) are indicative offers, not executed contracts.

Contracted occupancy, billed occupancy, uptime and productive utilization differ. Take-or-pay lets idle chips earn revenue. SF Compute's resale demonstrates spare customer hours without measuring fleet occupancy. The undelivered MW in row 23 are scheduled future supply; those disclosures alone do not show overdue power or stranded purchased GPUs. ([15][s15], [19][s19], [26][s26])

Adjusted EBITDA can be positive while GAAP earnings are negative; assessing capital returns additionally requires cohort-level replacement spending, financing cash flows and lifetime revenue. Prepayments finance construction but create delivery obligations. Equity absorbs disappointing renewals first; secured lenders depend on contracted cash flows and recoverable hardware, with unsecured and vendor lenders exposed according to claim priority. Customers risk interrupted service and lost prepayments. Soluna is a primary counterexample to universal GPU-rental profitability. ([18][s18], [19][s19], [20][s20], [25][s25])

CoreWeave's September 18, 2026 convertible pricing adds unsecured financing exposure; planned capped calls and conversion rights mean its 2.875% coupon is not an all-in capital cost. The announcement alone does not verify closing (row 43). ([Financing release][s48])

NVIDIA's September 2025 agreement backstops residual unsold capacity covered by its CoreWeave contract through April 2032, subject to conditions (row 44). My inference is that this shifts some revenue risk to the supplier and weakens the link between paid capacity and independent final demand; it guarantees neither the entire fleet nor debt. NVIDIA separately discloses $36bn of AI-cloud commitments at July 26, 2026 (row 45); overlap is unresolved, so these amounts must not be added. ([CoreWeave 8-K][s49], [NVIDIA 10-Q][s50])

### Depreciation and used equipment

The [useful-life register](/data/ai-unit-economics-useful-life.csv) and [unit-economics note](/research/theory/ai-unit-economics) remain the central comparison. SemiAnalysis reports a 38.2% rise in its one-year H100 midpoint from October 2025 to March 2026, with typically 25% prepayment; April's range is $2.10–2.70, midpoint $2.40 (rows 16, 49). This is C-grade survey evidence of continued earning potential, not an independently audited renewal tape. ([Dashboard][s17]) The prior A100 median was not reproduced; the fetched page differs in date and coverage. Neither proves individual assets will earn their carrying values. Nebius's letter now directly confirms the register's previously unverified life extension. These policies cover broader equipment categories, not individually validated GPU economic lives; Amazon attributes its shortening to faster technological development. ([16][s16], [20][s20], [26][s26], [27][s27], [28][s28])

SXM modules require compatible hosts; servers include more than GPUs. Asking prices, completed sales and modeled valuations measure different things. Opposing American Compute and Epoka-linked readings need matched configurations, regions and sale records; neither ledger was retrieved. Silicon Data's residual product capitalizes projected rents: it cannot independently corroborate rental-driven hardware appreciation. ([29][s29], [30][s30], [31][s31], [32][s32])

Rubin is already a production competitor: on September 30, 2026, CoreWeave reported limited deployment and up to 4.8× GB200 inference token throughput per GPU at matched interactivity for Cognition's workload (row 42). This vendor/customer result raises renewal and residual-value risk despite firmer older-card rents; it is not a universal price-performance ratio. ([Deployment account][s47])

### Supply and a fiber-style glut

Epoch's shipment estimates include uncertainty fields. Cumulative shipments precede deductions for warehouses, retirements and unavailable power; they are not energized installed capacity. H100-equivalent peak operations differ from workload throughput; the aggregates sum component estimates/medians rather than estimate an aggregate median. September's Rubin deployment makes successor throughput a current effective-supply consideration (row 42). SemiAnalysis's customer-level shipment/install-base tables were not publicly retrievable. TrendForce's server forecast counts a different denominator from its GPU mix forecast. ([36][s36], [37][s37], [38][s38], [39][s39], [40][s40])

NVIDIA's $0.4bn H200 inventory/purchase-obligation charge in H1 FY2027 amid China restrictions shows why rising OCPI H200 rents do not establish healthy inventory economics everywhere (row 46). Restricted inventory is not necessarily available to these rental markets. ([NVIDIA 10-Q][s50])

A fiber-style glut would combine persistent price declines with immediately available connected clusters, failed renewals, distressed sales and unpaid debt despite growing compute consumption. Cheap isolated hours or efficiency-driven token-price declines alone are insufficient. Row 39's thresholds are monitoring judgments, not universal cost floors.

## Conflicts and open questions

**Original note versus Codex cross-check judgment (2026-10-17):** the original Summary assigned B confidence to local cluster scarcity/no market-wide glut. The reviewer agrees the evidence does not demonstrate a glut, but judges it insufficient to measure aggregate availability or shortage: no inventory was ordered, and row 23 is scheduled future delivery. The applied view is segmented pricing with demonstrated premiums in selected contracts and unproven lifetime capital returns; supplier commitments and Rubin-driven throughput make the reviewer less comfortable inferring economic durability from rents alone. Both readings remain bounded interpretations, not measured market-wide supply balances.

The original row 16 graded the direction of H100 recovery B and said SemiAnalysis “directly verifies” it. The reviewer grades market levels and inferred recovery C because the observations behind this single survey are unavailable; A applies only to attribution, B to arithmetic. The observed survey rise is retained with C market confidence, plus its prepayment assumption and April range (rows 16, 49). Independent comparable primary contract data would resolve the grading disagreement. ([Survey][s16], [dashboard][s17])

The original row 23 treated undelivered power as an active-supply constraint; the reviewer reads the disclosed dates as a future pipeline without proof of delay. The original cash-margin/capital-destruction language also went further than the reviewer accepts: adjusted EBITDA and a GAAP loss alone do not establish operating cash generation or lifetime capital impairment. The narrower readings are applied; missed delivery dates and cohort-level cash returns remain open questions. ([10-Q][s19], [results][s18])

Vast's earlier H100 floor $1.73 and A100 median $0.65 (row 13) differ from the review's later October 17 display around 20:55 UTC: $1.33 and $0.80 (row 50), reproduced when applying this review. The earlier values lack a preserved timestamped snapshot; intraday movement versus transcription error remains unresolved. The CSV retains those original snapshot records as unverified historical provenance, not the later verified display. Hourly offer updates are not a transaction-price trend. ([Vast pricing][s13])

The mid-October “all-time highs” versus “price pressure” conflict partly dissolves on dates and products. The October 15 report repeats a purported B300 record streak; the original Compute Desk method/tape was not retrieved, so the record remains D. Thunder Compute's October-updated article says “This pricing pressure creates opportunities”; its cited AWS reduction is an older event. AWS's own announcement dates that cut. FastGPU's September publication instead says “prices did not fall.” None proves an October-wide collapse. ([33][s33], [34][s34], [35][s35], [45][s45])

There is also a genuine contrary price move: OCPI H100 fell sharply after its mid-month peak, while its monthly mean stayed near September. OCPI A100 weakened as newer cards strengthened. Thin contributor pools, changing mix and different interconnect promises can explain some cross-index differences, but constituent data are needed to quantify how much. Broad record-high claims fail both historical-comparability and cross-GPU tests. ([3][s3], [4][s4], [5][s5], [6][s6], [7][s7])

Not retrieved or independently verified: Silicon portal history and the brief's historical low/rebound; original Compute Desk transactions; Shadeform dynamic catalogue; SF Compute wholesale order-book history; market-wide paid utilization; complete used-sale ledgers; SemiAnalysis shipment/install-base tables; exact GPU counts and net effective prices for the highlighted bilateral contracts. 

**Proposed P1 definition:** retain SDH100RT's neocloud reading and the register's threshold. Average each complete calendar month's official daily publications equally; require the coverage in row 38 and test consecutive months wholly inside the forecast horizon. Use published corrections available at resolution, record methodology versions and publication/quality flags, and never forward-fill missing prices. Exclude publisher-carried-forward or disruption-affected prints from fresh-observation coverage; do not assume that a dated print represents fresh trading. No qualifying complete-month sequence is demonstrated here. Capture the daily series prospectively; the public snapshot cannot resolve P1 retrospectively.

If that series becomes unavailable, apply row 40's predeclared overlap-based conversion to OCPI. Use only fresh, quality-flagged observations for the overlap pairs and successor coverage; if freshness or sufficient overlap cannot be established, mark P1 unresolved rather than silently substitute an incomparable series. FastGPU floors are corroborating signals, not the successor: a handful of cheap hosts can move a minimum without repricing the contract book. This is a proposal only; the register was not edited.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| P1 benchmark | Public H100 $2.82; settlement date absent | observed 2026-10-17 | row 1 | Obtain dated history before scoring row 38 |
| H100 daily-print monthly mean | OCPI $2.8306 October-to-date vs $2.8293 September | through 2026-10-16 | row 5 | Sustained repricing beats a volatile daily print |
| Newer capacity | OCPI H200 $6.34; B200 $8.12 | 2026-10-16 | row 3 | Look for simultaneous weakness under row 39 |
| Older capacity | OCPI A100 $0.94 | 2026-10-16 | row 3 | Obsolescence stress can precede broad excess |
| Contract renewals | Survey midpoint $2.40, range $2.10–2.70; typically 25% prepayment; later comparable renewal tape unavailable | Apr 2026 | rows 16, 49 | Financing terms and actual renewal evidence matter |
| Spot discount | CoreWeave B200 $4.26375 vs $8.60 on-demand | observed 2026-10-17 | row 9 | Track discount and available depth together |
| Paid utilization | Not disclosed market-wide; SF resale rebate 25% | 2026-09-09 | row 15 | Rebate is not occupancy; request billed-hour denominator |
| Power becoming active | CoreWeave undelivered 393 MW plus 355 MW, scheduled during 2026–2028 | 2026-06-30 | row 23 | Future energization expands supply; no delay established here |
| Used hardware | Reported resale index 75; A100 server $84,000 | Aug / Sep 2026 | rows 28–29 | Opposing samples demand matched sale evidence |
| Supply pipeline | AI server shipment growth forecast +32.2%, then nearly +36% | 2026-10-14 | row 35 | Delivery exceeding funded demand is the glut mechanism |
| Provider list-price comparison | Nebius H100/H200/B200/B300 $4.50/$5.40/$8.50/$9.50; separate preemptible floors | observed 2026-10-17 | row 41 | Test whether asking-price increases survive renewals |
| Supplier-supported receipts | Covered CoreWeave capacity backstop; NVIDIA $36bn AI-cloud commitments, overlap unresolved | 2025-09-09 / 2026-07-26 | rows 44–45 | Distinguish supplier risk absorption from final demand |
| Successor workload throughput | Rubin up to 4.8× GB200 for Cognition inference at matched interactivity | 2026-09-30 | row 42 | Track workload economics at the next hardware renewal |
| Geographic inventory stress | NVIDIA H200 charge $0.4bn | H1 FY2027 | row 46 | Strong rents can coexist with restricted-market impairment |

## Sources

All accessed **2026-10-17**; dates below identify publication or observation.

1. [Silicon Data, live GPU indices][s1], undated: https://www.silicondata.com/products/silicon-index
2. [Silicon Data portal][s2], sign-in required: https://portal.silicondata.com/
3. [Ornn Data, settled index panel][s3], settlement 2026-10-16: https://data.ornn.com/
4. [Ornn, H100 market/history][s4], settlement 2026-10-16: https://data.ornn.com/markets/h100-sxm
5. [Ornn public H100 JSON][s5], through 2026-10-16; other GPU endpoint URLs in CSV: https://data.ornn.com/api/public-index/gpu/H100%20SXM/index-history
6. [FastGPU fixings CSV][s6], daily: https://fastgpu.co/api/v1/dataset/gpu-price-fixings.csv
7. [FastGPU floor index][s7], through 2026-10-16: https://fastgpu.co/price-index
8. [Lambda pricing][s8], live: https://lambda.ai/pricing
9. [CoreWeave pricing][s9], live: https://www.coreweave.com/pricing
10. [Oracle USD price list][s10], live, numbers read in Chrome: https://www.oracle.com/cloud/price-list/
11. [RunPod pricing][s11], live: https://www.runpod.io/pricing
12. [Hyperstack pricing][s12], live: https://www.hyperstack.cloud/gpu-pricing
13. [Vast.ai live pricing][s13], numbers read in Chrome: https://vast.ai/pricing
14. [SF Compute Autoresearch pricing][s14], live: https://autoresearch.sfcompute.com/
15. [SF Compute, realized resale discount][s15], 2026-09-09: https://sfcompute.com/news/realized-discount
16. [SemiAnalysis, The Great GPU Shortage][s16], 2026-04-02: https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
17. [SemiAnalysis pricing dashboard][s17], history through Apr 2026: https://gpu-index.semianalysis.com/
18. [CoreWeave Q2 results, SEC exhibit][s18], 2026-08-11: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
19. [CoreWeave Q2 10-Q][s19], period 2026-06-30: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
20. [Nebius Q2 shareholder letter, SEC exhibit][s20], 2026-08-12: https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm
21. [CoreWeave higher-price contracts][s21], 2026-09-17: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx
22. [Nvidia DGX H100/H200 guide][s22], undated: https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html
23. [Nvidia DGX B200 guide][s23], undated: https://docs.nvidia.com/dgx/dgxb200-user-guide/introduction-to-dgxb200.html
24. [IREN–Microsoft announcement][s24], 2025-11-03: https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
25. [Soluna annual-results presentation][s25], March 2025, slide 15: https://www.solunacomputing.com/wp-content/uploads/2025/03/SLNH-10K-2025-PRESENTATION.pdf
26. [CoreWeave FY2025 10-K][s26], period 2025-12-31: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
27. [Amazon FY2025 10-K][s27], period 2025-12-31: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
28. [GetDeploying A100 comparison][s28], page dated 2026-10-02: https://getdeploying.com/gpus/nvidia-a100
29. [Caladan used-GPU asking-price survey][s29], observation 2026-09-09: https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026
30. [American Compute resale index][s30], October 2026 edition: https://www.amcompute.com/gpu-resale-index
31. [Winston Su, Australia Data Centre Index, used-GPU report][s31], 2026-10-07: https://certifiedstrategic.com/insights/used-gpu-resale-prices-australia-2026
32. [Silicon Data residual-value methodology][s32], undated: https://www.silicondata.com/products/gpu-residual-value
33. [Carl Peterson, Thunder Compute market trends][s33], updated 2026-10-01: https://www.thundercompute.com/blog/ai-gpu-rental-market-trends
34. [AWS GPU price-reduction announcement][s34], 2025-06-05: https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/
35. [Yash Thakker, explainx.ai, B300 record claim][s35], 2026-10-15: https://explainx.ai/blog/nvidia-b300-gpu-rental-prices-record-high-17-day-streak-compute-desk-claimed-vs-verified-2026
36. [Epoch AI shipment timelines CSV][s36], updated 2026-10-14: https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv
37. [Epoch AI methodology][s37], current: https://epoch.ai/data/ai-chip-sales-documentation
38. [TrendForce, Nvidia shipment mix][s38], 2026-04-08: https://www.trendforce.com/presscenter/news/20260408-13003.html
39. [TrendForce, AI server pipeline][s39], 2026-10-14: https://www.trendforce.com/presscenter/news/20261014-13269.html
40. [Global X, Memory Is the New Bottleneck][s40], 2026 report: https://assets-cms.globalxetfs.com/Memory%20Is%20the%20New%20Bottleneck%20in%20AI%20Semiconductors%20%5BFinal%5D.pdf
41. [FastGPU open dataset][s41], live; attribution: FastGPU GPU cloud pricing dataset, CC BY 4.0: https://fastgpu.co/dataset
42. [Silicon Data index methodology][s42], 2026-08-27: https://www.silicondata.com/documents/silicon-data-index-methodology.pdf
43. [Ornn OCPI methodology][s43], initially published 2026-07-24: https://data.ornn.com/methodology
44. [FastGPU data provenance][s44], live: https://fastgpu.co/data-provenance
45. [FastGPU, Are Prices Falling?][s45], 2026-09-15: https://fastgpu.co/blog/gpu-cloud-pricing-trends-2026
46. [Nebius GPU pricing][s46], live page and search-cached version showing changes effective 2026-10-01: https://nebius.com/prices
47. [CoreWeave, Cognition becomes first Vera Rubin NVL72 customer][s47], 2026-09-30: https://www.coreweave.com/blog/cognition-becomes-first-customer-for-nvidia-vera-rubin-nvl72-on-coreweave-cloud
48. [CoreWeave, convertible senior notes pricing][s48], 2026-09-18: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx
49. [CoreWeave 8-K, NVIDIA capacity agreement][s49], filed 2025-09-15, agreement 2025-09-09: https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm
50. [NVIDIA Q2 FY2027 10-Q][s50], period 2026-07-26: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

[s1]: https://www.silicondata.com/products/silicon-index
[s2]: https://portal.silicondata.com/
[s3]: https://data.ornn.com/
[s4]: https://data.ornn.com/markets/h100-sxm
[s5]: https://data.ornn.com/api/public-index/gpu/H100%20SXM/index-history
[s6]: https://fastgpu.co/api/v1/dataset/gpu-price-fixings.csv
[s7]: https://fastgpu.co/price-index
[s8]: https://lambda.ai/pricing
[s9]: https://www.coreweave.com/pricing
[s10]: https://www.oracle.com/cloud/price-list/
[s11]: https://www.runpod.io/pricing
[s12]: https://www.hyperstack.cloud/gpu-pricing
[s13]: https://vast.ai/pricing
[s14]: https://autoresearch.sfcompute.com/
[s15]: https://sfcompute.com/news/realized-discount
[s16]: https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
[s17]: https://gpu-index.semianalysis.com/
[s18]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
[s19]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
[s20]: https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm
[s21]: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx
[s22]: https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html
[s23]: https://docs.nvidia.com/dgx/dgxb200-user-guide/introduction-to-dgxb200.html
[s24]: https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
[s25]: https://www.solunacomputing.com/wp-content/uploads/2025/03/SLNH-10K-2025-PRESENTATION.pdf
[s26]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
[s27]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
[s28]: https://getdeploying.com/gpus/nvidia-a100
[s29]: https://caladansemi.com/blog/used-nvidia-h100-a100-gpu-buying-guide-2026
[s30]: https://www.amcompute.com/gpu-resale-index
[s31]: https://certifiedstrategic.com/insights/used-gpu-resale-prices-australia-2026
[s32]: https://www.silicondata.com/products/gpu-residual-value
[s33]: https://www.thundercompute.com/blog/ai-gpu-rental-market-trends
[s34]: https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/
[s35]: https://explainx.ai/blog/nvidia-b300-gpu-rental-prices-record-high-17-day-streak-compute-desk-claimed-vs-verified-2026
[s36]: https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv
[s37]: https://epoch.ai/data/ai-chip-sales-documentation
[s38]: https://www.trendforce.com/presscenter/news/20260408-13003.html
[s39]: https://www.trendforce.com/presscenter/news/20261014-13269.html
[s40]: https://assets-cms.globalxetfs.com/Memory%20Is%20the%20New%20Bottleneck%20in%20AI%20Semiconductors%20%5BFinal%5D.pdf
[s41]: https://fastgpu.co/dataset
[s42]: https://www.silicondata.com/documents/silicon-data-index-methodology.pdf
[s43]: https://data.ornn.com/methodology
[s44]: https://fastgpu.co/data-provenance
[s45]: https://fastgpu.co/blog/gpu-cloud-pricing-trends-2026
[s46]: https://nebius.com/prices
[s47]: https://www.coreweave.com/blog/cognition-becomes-first-customer-for-nvidia-vera-rubin-nvl72-on-coreweave-cloud
[s48]: https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx
[s49]: https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm
[s50]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
