# GPU pricing, utilization and residual value

*Last updated: 2026-10-17 · Status: draft · Author: Codex / OpenAI · Reviewer: none*

## Summary

- Compute is locally scarce, especially connected, deliverable clusters; the evidence does not establish a market-wide glut. Contract pricing recovered, but marketplace spare capacity remains cheap. Confidence: B for this differentiated conclusion; D for universal shortage or record-high claims.
- Silicon Data, Ornn OCPI and FastGPU measure different products. Their methodologies were retrieved. A transaction-weighted index, standardized provider-weighted index and cheapest advertised offer cannot be spliced into one history.
- The retrieved OCPI history shows firmer H200/B200, broadly stable H100 monthly averages and softer A100. A brief H100 reversal is real within that series; it is not evidence that every accelerator is oversupplied.
- High rental yields can support operating cash margins without covering hardware replacement and financing. Take-or-pay contracts and prepayments protect providers temporarily; leveraged owners retain renewal, residual-value and delivery risk.
- Old accelerators retain utility, supporting the existing [unit-economics note](/research/theory/ai-unit-economics). That does not establish the appropriateness of each company's depreciation schedule or validate modeled resale values as completed sales.
- Biggest uncertainty: paid occupancy and executable contract renewals for comparable clusters. Neither public rate cards nor “sold out” statements disclose productive utilization of the installed fleet.

## Key claims

Rental units: **USD/GPU-hour**. “Observed” is the access date, not settlement. A grades the published statement/print, not market representativeness. Proposed thresholds are D judgments. All sources accessed **2026-10-17**.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Silicon Data public neocloud panel | H100 $2.82; H200 $3.51; B200 $6.12; B300 $7.01; A100 $1.53; displayed weekly changes +6.4%, +6.0%, +7.0%, +0.9%, −3.2% respectively | observed 2026-10-17; no settlement stamp | [panel][s1] | primary | A print; C freshness |
| 2 | Brief/register baseline not independently reproduced | H100 $2.83 on 2026-10-16; February 2025 low ~$1.86; claimed ~53% rise; arithmetic on those rounded inputs = 52.2% | alleged periods | [register](/forecasts/register); portal sign-in ([2][s2]) | tertiary / unverified input | D |
| 3 | OCPI settled panel | H100 $2.74; H200 $6.34; B200 $8.12; A100 SXM4 $0.94 | 2026-10-16 | [Ornn][s3] | primary | A print; C market coverage |
| 4 | OCPI H100 short-term reversal | $3.21 Oct 14 → $3.13 Oct 15 → $2.74 Oct 16; last day −12.5%; week −1.8%; month +4.6% | 2026-10-16 | [dated market page][s4] | primary | A |
| 5 | OCPI monthly means, derived from public daily observations | Aug / Sep / Oct-to-16: H100 $2.7710 / $2.8293 / $2.8306; H200 $4.7048 / $4.8803 / $5.7475; B200 $6.1419 / $7.2450 / $7.6925; A100 $1.0571 / $0.9997 / $0.9269 | partial Oct 2026 | [history API][s5], model-specific endpoints in CSV | primary, derived | B |
| 6 | FastGPU frozen provider medians | H100 SXM $3.949; H200 $4.54; B200 $6.69; B300 $9.765; A100 80GB $1.99; corresponding floors $1.785 / $2.69 / $3.69 / $4.89 / $0.873 | 2026-10-16 fixing | [fixing CSV][s6] | tertiary, reported unverified | C |
| 7 | FastGPU floor composite | 100.3, +0.3% since Oct 12; only 5 days through Oct 16 | observed 2026-10-17 | [index][s7] | tertiary | C |
| 8 | Lambda instances; node-size effect | H100 SXM $3.99 on 8-GPU node, $4.29 single; B200 $6.69 / $6.99; A100 SXM 80GB $2.79 on node | observed 2026-10-17 | [pricing][s8] | primary | A |
| 9 | CoreWeave North America, normalized node rates | H100 on-demand $6.155, spot $2.46375; H200 $6.305 / $2.61625; B200 $8.60 / $4.26375; B300 spot $4.48; A100 $2.70 / $1.20625; nodes have 8 GPUs | observed 2026-10-17 | [pricing][s9] | primary, derived | B |
| 10 | Oracle USD list, browser-rendered | H100/H200 $10; B200 $14; B300 $15; A100 80GB $4; each relevant shape has 8 GPUs | observed 2026-10-17 | [price list][s10] | primary | A |
| 11 | RunPod advertised Pod rates | H100 SXM $3.99; PCIe $2.89; NVL $3.19; B200 $7.99; A100 SXM/PCIe 80GB $1.79 | observed 2026-10-17 | [pricing][s11] | primary | A |
| 12 | Hyperstack on-demand / starting reservation | H100 SXM $3.20 / $2.72; H200 $3.99 / $2.79; B200 $6; B300 $7.40; A100 SXM 80GB $1.60 | observed 2026-10-17 | [pricing][s12] | primary | A |
| 13 | Vast live marketplace floor / median | H100 SXM $1.73 / $2.40; A100 SXM4 $0.40 / $0.65; H200 floor $3.95; B200 $6.25; B300 $9.94 | observed 2026-10-17 | [rendered pricing][s13] | primary; mode mix unclear | A print; D comparability |
| 14 | SF Compute Autoresearch | H100 interactive weekend $4.032; batch $0.063/minute = $3.78/hour | observed 2026-10-17 | [pricing][s14] | primary, derived | A/B |
| 15 | SF Compute customer idle-capacity resale | Average 25% realized discount through resale; not a fleet utilization percentage | 2026-09-09 | [company explanation][s15] | primary, unaudited | A statement |
| 16 | H100 contract recovery reconciles earlier note | One-year midpoint $1.70 Oct 2025 → $2.35 Mar 2026: +38.2%, rounded “almost 40%”; interquartile ranges $1.45–1.95 → $2.00–2.70 | 2026-04-02 publication | [SemiAnalysis][s16], [dashboard][s17] | secondary survey / estimate | B direction; C level |
| 17 | CoreWeave blended revenue/power proxy | Q2 revenue $2.575bn, ending active power 1.5 GW; annualized quotient ~$6.87m/MW-year, rounded ~$6.9m in companion note | 2026-Q2 | [release][s18]; [note](/research/stack/coreweave) | primary, derived | B arithmetic; D contract-price interpretation |
| 18 | Operating margin versus bottom line | CoreWeave adjusted EBITDA margin 59%, net loss $626m; committed contracts 98% of revenue | 2026-Q2 | [release][s18], [10-Q][s19] | primary | A |
| 19 | Nebius contracted yields and financing | Q2 wins $20–25m/MW-year; core terms 1–3 years; 70% of deals included prepayments covering 50–60% of associated capex; projected payback 1 year 10 months | 2026-08-12 | [shareholder letter][s20]; [companion note](/research/stack/neoclouds-other) | primary, company estimates | A statement; C realized return |
| 20 | CoreWeave new short-term cluster contracts | ~$40m/MW-year annualized, terms 3–6 months | 2026-09-17 | [IR disclosure][s21] | primary | A |
| 21 | Illustrative conversion inputs and outputs | DGX H100/H200: 8 GPUs, maximum 10.2 kW; B200: 8, 14.3 kW; 1 MW = 1,000 kW; annual convention 8,760 hours; proxy $6.87m → ~$1.00/H100-hour; $20–25m → ~$4.08–5.10/B200-hour | specs accessed 2026-10-17 | [H100 guide][s22], [B200 guide][s23]; rows 17,19 | primary, conditional derivation | B arithmetic; D actual contract rate |
| 22 | Disclosed contract without GPU count | IREN–Microsoft ~$9.7bn, 5-year term, 200 MW critical IT load, 20% prepayment; implies ~$9.7m/MW-year; exact GPU-hour rate not identifiable | 2025-11-03 | [IREN release][s24] | primary, derived | A/B |
| 23 | Power delivery still constrains active supply | CoreWeave 393 MW undelivered at one site, 355 MW at other sites | 2026-06-30 | [10-Q][s19] | primary | A |
| 24 | Direct counterexample to universal profitability | Soluna ended HPE GPU-service arrangement in March 2025 after weak pricing and inadequate cluster scale | 2025-03 presentation | [company deck, p.15][s25] | primary | A statement |
| 25 | Accounting lives, linked to existing register | CoreWeave 6 years; Amazon 5–6, subset shortened 6→5 effective 2025; Nebius 4→5 in 2026 | latest retrieved filings | [CoreWeave 10-K][s26], [Amazon 10-K][s27], [Nebius letter][s20]; [CSV](/data/ai-unit-economics-useful-life.csv) | primary | A |
| 26 | Existing A100 median not reproduced | Existing note $1.84; fetched GetDeploying page $1.79, explicitly dated Oct 2, 2026; 48 listed providers; cannot establish like-for-like change | retrieved 2026-10-17 | [existing note](/research/theory/ai-unit-economics), [page][s28] | tertiary | C; D comparison |
| 27 | Used asking prices, not sales | H100 SXM5 median $19,550 (3 US listings); A100 SXM4 80GB $9,925 (4); PCIe medians $32,000 / $18,500 | 2026-09-09 | [Caladan survey][s29] | tertiary, reported unverified | D |
| 28 | Claimed completed-sale index shows weakness | American Compute index 107 Apr → 86 Jul → 75 Aug; base H1 2025=100; older chips led fall, HGX H100 held | Oct 2026 edition, Aug observation | [resale index][s30] | tertiary, reported unverified | D |
| 29 | Opposing used-server report | Eight-GPU A100 server $180,000 Sep 2024 → $70,000 Sep 2025 → $84,000 Sep 2026; latest rebound +20% | 2026-10-07 | [report tracing Epoka chart][s31] | secondary, reported unverified | C |
| 30 | Residual-value model is not a sale tape | Silicon Data projects rental cash flows; forward inputs through 36 months, modeled tail and utilization; configurable maximum physical life around 8 years | observed 2026-10-17 | [product/method][s32] | primary | A description; D independent resale evidence |
| 31 | Dated bearish marketing versus actual historical cut | Thunder Compute updated Oct 1, 2026 describes “pricing pressure”; cited AWS cut was announced June 5, 2025, up to 45% | respective publication dates | [vendor article][s33], [AWS announcement][s34] | primary | A dates/statements; D current decline inference |
| 32 | Mid-October record claim unverified | Oct 15 report relays B300 “17 consecutive days” to record; original Compute Desk transaction series not retrieved | 2026-10-15 | [Yash Thakker's report][s35] | tertiary, reported unverified | D |
| 33 | Epoch Nvidia estimated shipments, completed periods | 2024 ~3.838m; 2025 ~4.458m; H1 2026 ~2.917m dataset units, including ~2.327m B300 | dataset updated 2026-10-14 | [downloadable timelines][s36], [documentation][s37] | secondary estimate, derived | C |
| 34 | Cumulative shipments are not installed usable capacity | Since 2022 through Q2 2026: Nvidia ~13.342m units; all covered designers ~31.595m H100-equivalent peak compute; excludes flagged incomplete quarters | dataset updated 2026-10-14 | [Epoch timelines][s36] | secondary estimate, derived | C |
| 35 | Supply pipeline forecasts, different denominators | TrendForce Apr: high-end Nvidia GPUs +~26%, Blackwell mix 71%; Oct: all AI servers +32.2% in 2026, nearly +36% in 2027 | 2026-04-08 / 2026-10-14 | [April][s38], [October][s39] | secondary forecast | C |
| 36 | Analyst-summary unit trap | Global X says 5.2m Blackwell in 2025, 5.7m in 2026; its footnote instead labels 2026 1.8m Blackwell plus 5.7m Rubin; excluded from supply estimate | 2026 report | [PDF, pp.2,5][s40] | secondary, internally conflicting | D |
| 37 | Dataset scope | 4,491 observations: 364 OCPI, 3,883 FastGPU provider-day means, 192 FastGPU fixings, 50 direct snapshots, 2 survey midpoints; FastGPU history Aug 19–Oct 16 | retrieved 2026-10-17 | [rental CSV](/data/gpu-rental-prices.csv), [FastGPU dataset][s41] | mixed, labeled per row | A provenance; C/D inference |
| 38 | P1 resolution rule | Monthly mean SDH100RT < $1.50 for 3 consecutive complete months; require ≥80% scheduled publication coverage; no interpolation | proposal 2026-10-17 | [P1](/forecasts/register), [Silicon methodology][s42] | primary rule / author judgment | D threshold |
| 39 | Additional glut warnings, not estimated break-even | H100 <$2.00 for 30 days; H200/B200 comparable prices down >40% YoY for 3 months; paid occupancy <60% for 2 quarters; comparable used-sale prices down >40% YoY | proposal 2026-10-17 | author monitoring design using rows 3–30 | primary rule / author judgment | D |
| 40 | Successor-series rule | If SDH100RT unavailable for a complete month, OCPI-H100 successor threshold $1.50 × median(OCPI/SDH100RT) over preceding 90 overlapping daily dates; require ≥60 pairs; otherwise unresolved | proposal 2026-10-17 | [OCPI methodology][s43], author design | primary rule / author judgment | D |

## Analysis

### Reading the market without mixing products

**Connected, deliverable clusters can be scarce while standalone GPU-hours remain cheap.** Silicon Data standardizes records for term, geography, platform and variant, then weights providers. Its weekly-recalibrated proprietary basis model is not externally reproducible. The portal required sign-in; the public panel lacks a settlement timestamp. ([1][s1], [2][s2], [42][s42])

Ornn says OCPI uses active on-demand transactions, volume weighting and winsorization, excluding reserved contracts. Contributor identities and the winsorization parameter remain private. Its methodology makes the administrator's published benchmark primary evidence, with unverified market representativeness. Public history was retrieved despite documentation emphasizing API keys. ([3][s3], [4][s4], [5][s5], [43][s43])

FastGPU records offers, not transactions or volumes. Its floor composite averages proportional changes geometrically; frozen fixings separately publish provider medians. The composite has much shorter history than its downloadable provider series. Historical observations in the CSV remain tertiary, reported unverified; direct current pages provide spot checks. ([6][s6], [7][s7], [41][s41], [44][s44])

CoreWeave's spot discount buys interruptibility; Lambda's instance and cluster products carry different connectivity and availability promises. Shadeform's [pricing page](https://shadeform.com/prices) loaded without numeric catalogue data. SF Compute's wholesale price URL redirected to its homepage; Autoresearch retail rates are not wholesale clears. Vast's rendered cards do not establish a mode-specific transaction series. Inventory was not tested by ordering.

### Contract economics, utilization and losses

The [CoreWeave note](/research/stack/coreweave)'s revenue/MW quotient combines quarterly revenue with ending active power. Ramping and hardware mix distort it. The [Nebius note](/research/stack/neoclouds-other)'s yield concerns new contracts, often undelivered. These numbers are not comparable tariffs. CoreWeave's subsequent short-term disclosure independently supports a premium for near-term clusters. ([18][s18], [19][s19], [20][s20], [21][s21])

**Rate = annual revenue per MW × kW per GPU / (1,000 × 8,760)** at full-year paid availability. Retrieved DGX maximum powers produce row 21's conditional examples. Networking, storage, headroom, PUE, actual draw and billing occupancy alter them. These are dimensional checks, not discovered customer tariffs. IREN's release lacks a GPU count, preventing an exact GPU-hour calculation. Ornn's [reserve listings](https://ornn.com/) are indicative offers, not executed contracts.

Contracted occupancy, billed occupancy, uptime and productive utilization differ. Take-or-pay lets idle chips earn revenue. SF Compute's resale demonstrates spare customer hours without measuring fleet occupancy. Undelivered power can prevent purchased GPUs becoming usable supply. ([15][s15], [19][s19], [26][s26])

Cash margins can be attractive while depreciation and interest destroy capital returns. Prepayments finance construction but create delivery obligations. Equity absorbs disappointing renewals first; secured lenders depend on contracted cash flows and recoverable hardware, with unsecured and vendor lenders exposed according to claim priority. Customers risk interrupted service and lost prepayments. Soluna is a primary counterexample to universal GPU-rental profitability. ([18][s18], [19][s19], [20][s20], [25][s25])

### Depreciation and used equipment

The [useful-life register](/data/ai-unit-economics-useful-life.csv) and [unit-economics note](/research/theory/ai-unit-economics) remain the central comparison. SemiAnalysis directly verifies H100 contract recovery, supporting continued earning power. The prior A100 median was not reproduced; the fetched page differs in date and coverage. Neither proves individual assets will earn their carrying values. Nebius's letter now directly confirms the register's previously unverified life extension. ([16][s16], [20][s20], [26][s26], [27][s27], [28][s28])

SXM modules require compatible hosts; servers include more than GPUs. Asking prices, completed sales and modeled valuations measure different things. Opposing American Compute and Epoka-linked readings need matched configurations, regions and sale records; neither ledger was retrieved. Silicon Data's residual product capitalizes projected rents: it cannot independently corroborate rental-driven hardware appreciation. ([29][s29], [30][s30], [31][s31], [32][s32])

### Supply and a fiber-style glut

Epoch's shipment estimates include uncertainty fields. Cumulative shipments precede deductions for warehouses, retirements and unavailable power; they are not energized installed capacity. H100-equivalent peak operations differ from workload throughput. SemiAnalysis's customer-level shipment/install-base tables were not publicly retrievable. TrendForce's server forecast counts a different denominator from its GPU mix forecast. ([36][s36], [37][s37], [38][s38], [39][s39], [40][s40])

A fiber-style glut would combine persistent price declines with immediately available connected clusters, failed renewals, distressed sales and unpaid debt despite growing compute consumption. Cheap isolated hours or efficiency-driven token-price declines alone are insufficient. Row 39's thresholds are monitoring judgments, not universal cost floors.

## Conflicts and open questions

The mid-October “all-time highs” versus “price pressure” conflict partly dissolves on dates and products. The October 15 report repeats a purported B300 record streak; the original Compute Desk method/tape was not retrieved, so the record remains D. Thunder Compute's October-updated article says “This pricing pressure creates opportunities”; its cited AWS reduction is an older event. AWS's own announcement dates that cut. FastGPU's September publication instead says “prices did not fall.” None proves an October-wide collapse. ([33][s33], [34][s34], [35][s35], [45][s45])

There is also a genuine contrary price move: OCPI H100 fell sharply after its mid-month peak, while its monthly mean stayed near September. OCPI A100 weakened as newer cards strengthened. Thin contributor pools, changing mix and different interconnect promises can explain some cross-index differences, but constituent data are needed to quantify how much. Broad record-high claims fail both historical-comparability and cross-GPU tests. ([3][s3], [4][s4], [5][s5], [6][s6], [7][s7])

Not retrieved or independently verified: Silicon portal history and the brief's historical low/rebound; original Compute Desk transactions; Shadeform dynamic catalogue; SF Compute wholesale order-book history; market-wide paid utilization; complete used-sale ledgers; SemiAnalysis shipment/install-base tables; exact GPU counts and net effective prices for the highlighted bilateral contracts. 

**Proposed P1 definition:** retain SDH100RT's neocloud reading and the register's threshold. Average each complete calendar month's official daily publications equally; require the coverage in row 38 and test consecutive months wholly inside the forecast horizon. Use published corrections available at resolution, record methodology versions, and never forward-fill missing prices. No qualifying complete-month sequence is demonstrated here. Capture the daily series prospectively; the public snapshot cannot resolve P1 retrospectively.

If that series becomes unavailable, apply row 40's predeclared overlap-based conversion to OCPI. If overlap is insufficient, mark P1 unresolved rather than silently substitute an incomparable series. FastGPU floors are corroborating signals, not the successor: a handful of cheap hosts can move a minimum without repricing the contract book. This is a proposal only; the register was not edited.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| P1 benchmark | Public H100 $2.82; settlement date absent | observed 2026-10-17 | row 1 | Obtain dated history before scoring row 38 |
| Realized H100 month | OCPI $2.8306 October-to-date vs $2.8293 September | through 2026-10-16 | row 5 | Sustained repricing beats a volatile daily print |
| Newer capacity | OCPI H200 $6.34; B200 $8.12 | 2026-10-16 | row 3 | Look for simultaneous weakness under row 39 |
| Older capacity | OCPI A100 $0.94 | 2026-10-16 | row 3 | Obsolescence stress can precede broad excess |
| Contract renewals | H100 midpoint $2.35; later comparable series unavailable | Mar 2026 | row 16 | Main cash-flow test for leveraged owners |
| Spot discount | CoreWeave B200 $4.26375 vs $8.60 on-demand | observed 2026-10-17 | row 9 | Track discount and available depth together |
| Paid utilization | Not disclosed market-wide; SF resale rebate 25% | 2026-09-09 | row 15 | Rebate is not occupancy; request billed-hour denominator |
| Power becoming active | CoreWeave undelivered 393 MW plus 355 MW | 2026-06-30 | row 23 | Energization can abruptly expand usable supply |
| Used hardware | Reported resale index 75; A100 server $84,000 | Aug / Sep 2026 | rows 28–29 | Opposing samples demand matched sale evidence |
| Supply pipeline | AI server shipment growth forecast +32.2%, then nearly +36% | 2026-10-14 | row 35 | Delivery exceeding funded demand is the glut mechanism |

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
