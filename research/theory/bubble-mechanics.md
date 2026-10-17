# Bubble mechanics, operationalised for the AI boom

*Last updated: 2026-10-17 · Author: Claude (Fable 5.1 subagent) · Status: reviewed · Reviewer: Codex (gpt-6-astra) cross-check, applied 2026-10-17*

## Summary

- Five complementary frameworks organise the questions: Minsky on debt-service
  capacity, Kindleberger on credit and market stages, Perez on technology
  installation and deployment, Dalio on six bubble indicators, and Shiller on
  valuation and narratives. Their overlap is not independent confirmation of
  a bubble; Perez's fetched AI commentary does not predict a current crash.
- The dated evidence shows expensive US equities and a large infrastructure
  build. September CAPE was 40.58 versus a 17.8 long-run mean; September
  margin debt was $1.480 tn, up 31.4% year on year but below June's record.
  Oracle and CoreWeave reported backlogs of $664 bn and $103.7 bn at different
  quarter ends. Commitments alone do not establish inadequate returns
  (claims 1, 4, 15–16, 33, 36).
- Internal investment funding headroom is shrinking: Microsoft, Amazon,
  Alphabet and Meta spent 86.1% of operating cash flow on cash capex in
  Q1 2026 and 96.1% in Q2. The original 94% Q1 figure included Oracle as a
  fifth company. Individual firms differ, and capex/OCF alone cannot assign
  Minsky debt-service postures (claims 30–31, 41).
- Forward P/E of 19.0x is slightly below its ten-year mean and provides a
  counterweight to high CAPE. Shiller's published excess CAPE yield is
  positive, while the note's differently constructed TIPS proxy is negative.
  Neither contrast proves that earnings growth must persist indefinitely
  (claims 7–10, 44).
- Higher rates and issuance are potential pressure channels: the September
  hike, October Treasury high and record Q2 IPO proceeds are documented.
  Issuance was concentrated and Q3 weakened; financing can also improve
  liquidity. These observations do not establish an unavoidable bust or its
  date (claims 18–22, 27–29, 51).
- Financing risk varies by issuer. CoreWeave's cash flows show refinancing
  dependence, not demonstrated Ponzi finance; September disclosures show
  continued market access and demand. Broad credit spreads and sentiment
  give mixed evidence, while Fed minutes report hyperscaler credit repricing.
  The original rubric sums to 20/26, but its composite assessment is withdrawn
  pending consistent rules and calibration (claims 23–26, 42–43, 46–50).
- No current numerical Dalio aggregate reading was located in this research.
  The central unresolved tests are sustainable customer cash generation,
  contract quality, debt maturities and recoverable asset values. The May Fed
  report also records systemic resilience alongside leverage vulnerabilities
  (claims 39–40, 52).

## Key claims

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Shiller CAPE, last full month (estimated CPI input) | 40.58 | 2026-09 | [Shiller workbook](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) | primary | A |
| 2 | Shiller CAPE, partial month; price and GS10 from October 2, CPI estimated | 40.71 | 2026-10 (partial) | [Shiller workbook](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) | primary | A |
| 3 | CAPE all-time peak | 44.20 (Dec 1999); 1929 peak 32.56; 2007 peak 27.55; 2021 peak 38.58 | series 1881–2026 | [Shiller ie_data.xls](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) | primary | A |
| 4 | CAPE long-run mean / median | 17.8 / 16.6 | Jan 1881–Oct 2026, including partial October | [Shiller ie_data.xls](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) (computed) | primary | B |
| 5 | CAPE daily estimate, pending primary confirmation | 40.54 | 2026-10-16 | [multpl](https://www.multpl.com/shiller-pe) | tertiary | D |
| 6 | 10-year TIPS real yield | 2.78% | 2026-10-15 | [FRED DFII10](https://fred.stlouisfed.org/series/DFII10) | primary | A |
| 7 | CAPE earnings yield minus 10y real yield (excess-CAPE-yield proxy) | 2.46% − 2.78% = −0.32 pp | 2026-09/10 | computed from #1, #6 | primary | B |
| 8 | S&P 500 forward 12-month P/E | 19.0 (5-yr avg 19.8, 10-yr avg 19.1) | 2026-10-16 | [FactSet Earnings Insight](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | primary (FactSet's own measure/estimate) | A |
| 9 | S&P 500 Q3 2026 blended earnings / revenue growth | 29.0% / 12.6% | 2026-10-16 | [FactSet](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | primary (FactSet's own measure/estimate) | A |
| 10 | S&P 500 CY2026 EPS growth, consensus | 32.8% | 2026-10-16 | [FactSet](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | primary (FactSet's own measure/estimate) | A |
| 11 | Fed: equity premium "well below its historical average"; P/E "in the upper range of its historical distribution" | qualitative | data to 2026-04-23 | [Fed FSR May 2026](https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm) | primary | A |
| 12 | Fed: hedge fund leverage "near all-time highs", concentrated in a few large funds | qualitative | data to 2026-04-23 | [Fed FSR May 2026](https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm) | primary | A |
| 13 | S&P 500 proxy weights: ten security lines versus ten companies (Alphabet combined) | 38.39% / 39.89%; NVDA 7.86%; not S&P-certified weights | 2026-10-17 | [stockanalysis.com](https://stockanalysis.com/list/sp-500-stocks/) | tertiary | D |
| 14 | S&P 500 top-10 market-cap and earnings concentration "at record-high levels"; TMT share "as high as during the 1990s tech bubble" | qualitative | 2026-01 | [Apollo, Slok et al.](https://www.apolloacademy.com/wp-content/uploads/2026/01/011326-MarketConcentration.pdf) | secondary | B |
| 15 | FINRA margin debt, record | $1,502,072 m | 2026-06 | [FINRA margin statistics](https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics) | primary | A |
| 16 | FINRA margin debt, latest and growth | $1,480,054 m; Sep-25 $1,126,494 m: +31.4% y/y; Oct-25 $1,183,654 m: +25.0% over eleven months; below June record | 2026-09 | [FINRA history](https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx) | primary | A balances / B growth |
| 17 | Margin debt as share of nominal GDP | 4.5% ($1.480 tn / $32.563 tn SAAR) | 2026-Q2 GDP, Sep-26 debt | [FRED GDP](https://fred.stlouisfed.org/series/GDP), FINRA (computed) | primary | B |
| 18 | Fed funds target range raised 25 bp to 3.75–4.00%, vote 12–0, "inflation remains elevated" | +25 bp | 2026-09-16 | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) | primary | A |
| 19 | Previous meeting held at 3.50–3.75%, 9–3 with three dissents for a hike (Hammack, Kashkari, Logan) | hold | 2026-07-29 | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm) | primary | A |
| 20 | Last prior increase before Sept 2026 | 2023-07-27 (+25 bp to 5.25–5.50%); cuts Sep 2024–Dec 2025 to 3.50–3.75% | 2026-09-16 | [Fed policy-rate history](https://www.federalreserve.gov/monetarypolicy/openmarket.htm) | primary | A |
| 21 | 10-year Treasury yield, 2026 high | 5.31% (last higher close: 5.32% on 2002-05-14; 2007 peak 5.26%) | 2026-10-05 | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) (computed from CSV) | primary | A daily observations / B historical comparisons |
| 22 | 10-year Treasury yield, latest | 5.10% | 2026-10-15 | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) | primary | A |
| 23 | ICE BofA US High Yield OAS | 3.23% | 2026-10-15 | [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | primary | A |
| 24 | ICE BofA US Corporate (IG) OAS | 0.84% | 2026-10-15 | [FRED BAMLC0A0CM](https://fred.stlouisfed.org/series/BAMLC0A0CM) | primary | A |
| 25 | AAII sentiment: bullish / neutral / bearish | 38.7% / 19.7% / 41.6% (averages 37.5 / 31.0 / 31.5) | week to 2026-10-14 | [AAII](https://www.aaii.com/sentimentsurvey) | primary | A |
| 26 | BofA Global FMS: average cash 3.9%; 31% name "disorderly rise in bond yields" top tail risk; 37% would rotate to bonds at a 6% 10-year | Oct 2026 edition | 2026-10-13 | [interactive investor](https://www.ii.co.uk/analysis-commentary/fund-manager-optimism-faltering-ii540567) | secondary | B |
| 27 | US IPOs, 3Q26 | 30 deals, $32.8 bn ($6.2 bn ex SK hynix); Renaissance IPO Index −11% in the quarter | 2026-10-01 | [Renaissance Capital 3Q26 review](https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf) | primary (own tally/index) | A |
| 28 | US IPOs, Q2 2026, publisher's record tally | 48 deals, $104.8 bn | 2026-Q2 | [Renaissance Q2 review](https://www.renaissancecapital.com/review/2Q26USReview_Public.pdf) | primary (own tally) | A |
| 29 | Renaissance attributes slowdown to AI-spending concerns, bond yields and resumed hikes; private-lab listing forecasts, reported, unverified | Anthropic expected Q4 2026; OpenAI 2027; forecasts, not completed listings | 2026-10-01 | [Renaissance Q3 review](https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf) | primary for publisher's assessment / secondary for private-company plans | A assessment / C private plans |
| 30 | Four hyperscalers (MSFT, AMZN, GOOGL, META): cash capex / operating cash flow | $129.750 bn / $150.727 bn = 86.08%; OCF less cash capex $20.977 bn | CY2026-Q1 | [Microsoft](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/cash-flows), [Amazon](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm), [Alphabet](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm), [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx); reconstructed | primary | B |
| 31 | Epoch five-company scope (includes Oracle): historical cash capex/OCF and Q1 2026 | 2023 Q2/Q3 trough 36.5%/34.9%; 2025 Q2/Q3/Q4 72.3%/63.3%/72.3%; Q1 2026 $148.4 bn/$157.9 bn ≈94% | 2023–2026-Q1 | [Epoch scope and filings compilation](https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow) | secondary compilation of primary inputs | B arithmetic |
| 32 | Hyperscaler 2025 revenue growth vs capex growth; 2026 plan | 16.5% vs ~60% (2025); ~15.5% vs ~80% (2026 plan) | 2026-04-06 | [Futuriom](https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04) | secondary | C |
| 33 | Oracle FY27 Q1: backlog, revenue, investment funding and completed equity issuance | RPO $664 bn, +$209 bn y/y; OCI $7.4 bn, +121%; revenue $19.345 bn; OCF $23.103 bn less cash capex $28.499 bn = FCF −$5.396 bn; $20 bn ATM completed | quarter to 2026-08-31 | [Oracle release](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx); [10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm) | primary | A stated inputs / B FCF subtraction |
| 34 | CoreWeave carrying debt, net of discounts/issuance costs; principal and cash | $31,405 m recourse + $3,663 m non-recourse = $35,068 m carrying debt; scheduled principal $35,551 m; cash $5,524 m | 2026-06-30 | [10-Q, Note 10 and balance sheet](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm) | primary | A components, principal, cash / B sum |
| 35 | CoreWeave Q2 net interest expense / revenue / net loss | $640 m / $2,575 m / −$626 m; net interest expense/revenue 24.9%, not cash-interest coverage | 2026-Q2 | [CoreWeave Q2 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/); [10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm) | primary | A statements / B ratio |
| 36 | CoreWeave RPO and expected recognition schedule | $103.7 bn; 41% in initial 24 months, 39% in months 25–48, balance in months 49–78 | 2026-06-30 | [10-Q, revenue recognition](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm) | primary | A management estimates |
| 37 | Morgan Stanley: AI-related global debt issuance forecast 2026 | ~$570 bn (more than double 2025); $236 bn YTD to 2026-05-31; hyperscaler capex ~$700 bn in 2026 | 2026-06-10 | [Allwork.space](https://allwork.space/2026/06/morgan-stanley-forecasts-570-billion-ai-debt-wave-as-hyperscalers-race-to-fund-growth/) | secondary | C |
| 38 | Household equity share of financial assets, reported Z.1 derivation, unverified against originating table | 46.0% four-quarter average, claimed record; claimed 2000 peak 38.7% | 2026-Q1 | [thetrading.tools](https://www.thetrading.tools/chart-of-the-day/2026-08-14-household-equity-allocation-record) | tertiary | D |
| 39 | Dalio aggregate bubble gauge, published readings | 77th percentile (Feb 2021); 52nd percentile, "mid-range" (Mar 2024); 1929 and 2000 = 100th | 2021, 2024 | [Dalio, LinkedIn 2021](https://www.linkedin.com/pulse/we-stock-market-bubble-ray-dalio); [2024 mirror](https://hedgefundalpha.com/?p=2162956) | primary / secondary | A / B |
| 40 | Dalio 2025–26 verbal readings | AI "about 80%" of 1929/2000 euphoria (Nov 2025); "early stages of a bubble" (Jan 2026); "classic signs that we're in [one]" (Aug 2026); pins are rising rates and surging stock issuance | 2025-11 to 2026-08 | [Fortune Jan 2026](https://fortune.com/2026/01/06/ray-dalio-says-ai-is-in-the-early-stages-of-a-bubble-so-watch-out-for-2026/); [Fortune Aug 2026](https://fortune.com/2026/08/04/ray-dalio-ai-bubble-1929-2000-ipos-wealth-is-not-money/) | secondary | B |
| 41 | Named four: Q2 cash capex / OCF, with company inputs (capex/OCF, USD bn) | MSFT 35.802/55.441; AMZN 54.208/45.387; GOOGL 44.924/39.069; META 30.116/31.862; total $165.050 bn/$171.759 bn = 96.09% | CY2026-Q2 | [Microsoft](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast), [Amazon](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm), [Alphabet Q1](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm) and [H1](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm), [Meta Q1](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx) and [H1](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm); quarter reconstruction | primary | A reported inputs / B quarter differences, sums and ratio |
| 42 | CoreWeave H1 cash-flow and debt-service inputs | OCF +$3.663 bn after $0.806 bn operating cash interest; total cash interest $0.982 bn including capitalised amounts; principal repayments $5.219 bn; deferred-revenue contribution $1.365 bn | H1 to 2026-06-30 | [10-Q, cash flows and debt-service risk disclosure](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm) | primary | A |
| 43 | CoreWeave H1 cash before operating interest versus principal plus total cash interest | $3.663 bn + $0.806 bn = $4.469 bn versus $5.219 bn + $0.982 bn = $6.201 bn | H1 to 2026-06-30 | computed from #42, [10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm) | primary | B |
| 44 | Shiller's published excess CAPE yield, distinct from TIPS proxy | +0.81980% September; +0.55724% partial October; October price and GS10 use October 2 observations, September/October CPI estimated | 2026-09/10 | [Shiller workbook, column Q and footnotes](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) | primary | A |
| 45 | September CAPE percentile and current-year counterexample to historical exclusivity | 98.86th percentile (share ≤ September value) of 1,750 months, Jan 1881–Oct 2026 including partial October; August 2026 CAPE 40.9874 | 2026-10 workbook | [Shiller workbook](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731) | primary | A August value / B sample and percentile |
| 46 | September FOMC minutes: differentiated credit risk, earnings and policy assessments | Hyperscaler spreads elevated after earlier widening, with slight recent narrowing; equity gains attributed to actual/expected earnings as multiples declined; yields had multiple drivers; several participants saw policy as mildly restrictive or not restrictive | meeting 2026-09-15/16; released 2026-10-07 | [FOMC minutes](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm?trk=article-ssr-frontend-pulse_little-text-block) | primary | A for recorded assessments |
| 47 | CoreWeave convertible-note pricing announcement (not settlement confirmation) | $3.7 bn at 2.875%, due 2033; $500 m purchaser option; expected net proceeds $3.6445 bn before offering expenses; $498.8 m for capped calls | 2026-09-18 | [Company pricing announcement](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx) | primary | A announced terms/estimates |
| 48 | CoreWeave convertible proceeds remaining after capped calls, before offering expenses, excluding option | $3.6445 bn − $0.4988 bn = $3.1457 bn intended for general corporate purposes | 2026-09-18 | computed from #47, [announcement](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx) | primary | B |
| 49 | CoreWeave authorised ATM capacity, not completed equity sales | Up to 35 m shares; no obligation to sell | 2026-09-17 | [Company ATM announcement](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-At-the-Market-Offering-Program/default.aspx) | primary | A |
| 50 | CoreWeave management demand/pricing update, not recognised revenue | Higher-priced short contracts; >$25 bn early-Q3 net new commitments excluded from June backlog | 2026-09-17 (commitments previously disclosed Aug 11) | [Company update](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx) | primary | A for management disclosures |
| 51 | Q2 IPO concentration in SpaceX | $75 bn of $104.8 bn = 71.6%; $29.8 bn excluding SpaceX, still strong per publisher | 2026-Q2; review 2026-07-01 | [Renaissance Q2 review](https://www.renaissancecapital.com/review/2Q26USReview_Public.pdf) | primary | A inputs/assessment / B share and subtraction |
| 52 | May FSR's systemic counterevidence and leverage scope | Moderate business/household debt vulnerabilities and funding risks; declining aggregate debt/GDP; strong bank capital; hedge-fund leverage spans Treasury, rates and equity strategies | data to 2026-04-23; published 2026-05-28 | [Fed overview](https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm) | primary | A for Fed assessments |
| 53 | Illustrative earnings sensitivity at fixed prices and a common earnings base | 19 × 1.328 / 1.16 = 21.75x (21.8x rounded); CY2026 and NTM periods do not match | inputs 2026-10-16; calculation 2026-10-17 | computed from #8, #10; 16% is an illustrative assumption | primary inputs / author scenario | B conditional arithmetic |
| 54 | FINRA July margin-debt decline, absolute versus percentage comparison | $1,417,225 m − $1,502,072 m = −$84,847 m (−5.65%); largest absolute-dollar monthly decline in Jan 1997–Sep 2026 history, not largest percentage fall | 2026-07; history through 2026-09 | [FINRA history](https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx) | primary | B |
| 55 | Backlog versus static annualised revenue and combined stock | Oracle $664 bn/(4 × $19.345 bn) = 8.581x; 664/19.3 ≈34.40 quarters using rounded quarterly revenue; CoreWeave $103.7 bn/(4 × $2.575 bn) = 10.068x; combined RPO $767.7 bn at different dates | Oracle Aug 31 / CoreWeave Jun 30, 2026 | computed from #33, #35–36 | primary | B |
| 56 | Conditional capex-growth / revenue-growth ratios; not financing-dollar gaps | 60/16.5 = 3.64x for 2025; 80/15.5 = 5.16x for the 2026 plan | inputs 2026-04-06; calculation 2026-10-17 | computed from #32, [Futuriom](https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04) | secondary inputs / author calculation | B arithmetic / C underlying estimates |
| 57 | Dalio's sustainability measure and timing limitation | Required earnings growth for equity returns above bonds; gauge does not precisely time tops or bottoms | 2021-02-02 | [Bridgewater original](https://www.bridgewater.com/research-and-insights/ray-dalio-stock-market-bubble) | primary | A for stated method/caveat |
| 58 | Perez's accessible current-revolution framing | AI is a development within the existing ICT revolution; full article not independently verified | 2024-03-11 | [Project Syndicate introduction](https://www.project-syndicate.org/magazine/ai-is-part-of-larger-technological-revolution-by-carlota-perez-1-2024-03) | primary | A for accessible introduction |

Type: primary / secondary / tertiary. Grade: A–D (see report/methodology.md).
A grades for company guidance, consensus estimates and institutional assessments
verify what was published, not whether the forecast or interpretation is true.
Arithmetic is B; unverified underlying forecasts retain their lower confidence.
The existing CSVs contain recent Shiller and FINRA observations, not the full
histories used for sample statistics. Full-history calculations cite the fetched
workbooks. New quarterly figures use cash capex, excluding newly signed leases;
year-to-date cash flows are differenced to obtain individual quarters.

## Analysis

### 1. Minsky: stability breeds fragility

Minsky's original paper distinguishes hedge finance, where operating cash can
meet contractual interest and principal, from speculative finance, which can
pay interest but needs refinancing for principal, and Ponzi finance, which
requires borrowing or asset sales even to meet interest. Prolonged stability
can encourage a shift toward fragile financing; monetary constraint can
expose that fragility (source 25). These are debt-service tests, not tests of
net profit or discretionary growth capex.

- **Hyperscalers:** the named four generated $150.727 bn OCF against
  $129.750 bn cash capex in Q1, leaving $20.977 bn, rather than no free cash
  flow (claim 30). Q2 cash capex/OCF rose to 96.1% (claim 41). Amazon and
  Alphabet spent more than operating inflows in Q2, while Microsoft and Meta
  retained surpluses. This compresses investment funding headroom, but the
  aggregate cannot classify each firm's contractual debt-service posture.
  Epoch's historical series includes Oracle; its trough and subsequent
  quarterly readings are shown separately in claim 31. Its extrapolated
  crossover is a scenario, not an observed transition to speculative finance.
- **Oracle:** negative investment FCF and completed equity issuance (claim
  33) show external funding of expansion. They do not establish inability to
  repay maturing debt from operating cash, nor a need to borrow for interest.
- **CoreWeave:** the missing cash test is available. H1 OCF was +$3.663 bn
  after $806 m of operating cash interest. Cash generation before that
  interest was $4.469 bn, below $6.201 bn of principal and total cash interest
  paid (claims 42–43). Deferred revenue contributed $1.365 bn to OCF.
  This supports speculative financing exposure and a test of customer
  prepayment sustainability; it does not establish present Ponzi finance.
  Net interest expense/revenue in claim 35 is not cash-interest coverage.

The September rate increase is a potential Minsky pressure channel, not
proof that a transition has occurred. The newer Fed record also includes
views that policy remained only mildly restrictive or not restrictive
(claim 46); contractual maturities and borrower-specific cash flows must
show the transmission.

CoreWeave's September financing and demand disclosures qualify the distress
reading. The September 18 pricing announcement covers $3.7 bn of convertible
notes at 2.875%, due 2033, with a $500 m option. Expected proceeds after capped
calls were $3.1457 bn before offering expenses (claims 47–48). This shows
market access and potential dilution, not cheap comparable straight debt or
confirmation of settlement. Its September 17 ATM authorises up to 35 m
shares without establishing any completed sales (claim 49). The same day's
pricing update reports higher-priced short contracts and >$25 bn of early-Q3
net commitments outside June backlog (claim 50). Management's disclosures
counter a simple demand-collapse story without proving customer solvency or
turning commitments into recognised revenue.

### 2. Kindleberger: stages, and credit as fuel

The displacement, boom, euphoria, profit-taking and panic sequence (source
26) provides hypotheses to test, not a unique stage inferred from proxies.

| Stage | Marker in the AI case | Reading, Oct 2026 |
|---|---|---|
| Displacement | New profit opportunity | Earnings and cloud-revenue growth support a real opportunity (claims 9, 33); profitability of all new capital is a separate question. |
| Boom | Credit expands to finance the opportunity | Margin debt rose 31.4% y/y; the AI-debt issuance forecast is still grade C (claims 16, 37). Neither measures all AI credit growth relative to income. |
| Euphoria | Resale speculation, new entrants, high valuations | High CAPE and issuance are consistent with froth, but direct new-buyer/resale data are missing; household allocation is grade D (claims 1, 28, 38). |
| Profit-taking / distress | Insider selling, weaker marginal demand | Q3 IPO returns and postponements suggest a weaker window (claims 27, 29). Corporate equity issuance is not insider profit-taking; July's absolute-dollar margin decline was followed by rebuilding (claim 54). |
| Panic | Forced selling, broad credit withdrawal | Broad OAS does not show panic (claims 23–24); sector credit repricing is already reported (claim 46). |

Renaissance's record Q2 proceeds were concentrated: SpaceX supplied 71.6%,
leaving $29.8 bn, still strong by its assessment (claim 51). Q3 proceeds
excluding SK hynix were only $6.2 bn, with postponements (claim 27). Rounded
headline and mega-deal totals need not subtract to that separately reported
exclusion figure. IPO dollars do not count new investors; existing investors
can buy new issuance. Equity portfolio weights can rise with prices alone.

Credit remains the mechanism to investigate. The debt-issuance forecast and
Futuriom growth inputs (claims 32, 37) need primary confirmation. Conditional
on claim 32 (arithmetic in claim 56), capex growth was about 3.6 times revenue growth in 2025 and the
2026 plan implied 5.2 times. Ratios of growth rates do not measure funding
dollars, and a plan is not a second realised year. Those conditional inputs
cannot establish the direction or scale of the financing gap by themselves.

### 3. Dalio's checklist, item by item

Dalio asks six questions about unsustainable prices (sources 20, 35). His
published past readings and later verbal comments are in claims 39–40.
No current numerical aggregate reading was located in this research. Rate
increases and issuance are potential pins, separate from the six measures.
This note's proposed proxies and thresholds are not Bridgewater's gauge.

1. **Prices high versus traditional measures.** September CAPE is near
   the 98.9th percentile of the January 1881–October 2026 sample, including
   partial October, below the 1999 peak and August 2026 (claims 1–4, 45).
   The Fed's valuation warning is consistent with expensive equities
   (claim 11). The draft CAPE threshold is retained in §7 for audit.
2. **Prices discounting unsustainable conditions.** Dalio's own measure
   estimates growth needed for equity returns to exceed bond returns
   (claim 57; source 35). A CAPE/forward-P/E percentile gap is not that calculation.
   No matched forward-P/E distribution was supplied. The 19.0x multiple is
   slightly below its ten-year mean (claim 8); a mean does not establish a
   median or percentile. Illustratively, reducing growth from 32.8% to 16%
   gives 19 × 1.328 / 1.16 = 21.8x at unchanged prices and a common earnings
   base (claim 53). CY2026 growth and NTM EPS cover different periods, so
   this is not exact NTM repricing or proof of unsustainable expectations.
3. **New buyers entering.** Issuance and household equity weights are
   indirect proxies (claims 27–28, 38, 51). Concentrated mega-deals and an
   unverified allocation statistic cannot establish broad new participation.
   Private-lab listing dates remain reported, unverified forecasts (claim 29).
4. **Broad bullish sentiment.** Bears exceed bulls by 2.9 percentage
   points; FMS cash is 3.9% (claims 25–26). These readings do not satisfy
   the draft's full-score thresholds. Survey sentiment does not uniquely
   locate late euphoria or profit-taking; alternative interpretations belong
   in Conflicts.
5. **Leverage-financed purchases.** September margin debt was up 31.4%
   y/y or 25.0% since October, but remained below June's record (claims
   15–16). The 4.5% debt/GDP figure mixes a debt stock with annualised output
   and reference dates; it is not AI-specific (claim 17). The FSR's hedge-fund
   warning spans several strategies, not just AI (claims 12, 52).
6. **Extended forward purchases.** Oracle's backlog is about 34 quarters
   of current revenue, or 8.6 times annualised revenue; CoreWeave's is
   10.068 times using unrounded quarterly revenue (claim 55). These are
   static ratios, not actual delivery duration. CoreWeave expects recognition
   over the schedule in claim 36. High capex/OCF (claims 30, 41) shows exposure
   to future demand, but neither metric alone proves purchases motivated by
   scarcity or inability to earn a return. CoreWeave's top-five-seller status
   was not established for the draft threshold.
7. **Tightening policy, a potential pin.** The hike and Treasury high
   are documented (claims 18–22); one hike does not establish an unavoidable
   bust. Yield increases have several drivers in the latest Fed record
   (claim 46). Issuance can finance productive expansion and improve liquidity.

The tertiary concentration proxy distinguishes ten security lines (38.39%)
from ten companies (39.89%), with Alphabet combined. Those are not certified
index weights (claim 13, grade D); Apollo's broader concentration assessment
is separate evidence (claim 14).

### 4. Perez: installation, frenzy, and what survives

Perez's installation/deployment framework separates technological progress
from investor returns. The accessible introduction to her March 2024 article
places AI within the ongoing ICT revolution (claim 58; source 45). The earlier note
relied on Wladawsky-Berger's quotations for her broader mid-diffusion and
finance/production argument (source 27); the cross-check did not verify the
full paywalled text. No fetched Perez source calls the current build a frenzy
or predicts its crash. Kedrosky's interpretation emphasises late installation
and surviving infrastructure (source 28); these are competing interpretations,
not Perez's current-cycle forecast.

The proposed operational test compares investment growth, revenue and
financing. Conditional growth-rate ratios of 3.6x in 2025 and 5.2x in the
2026 plan (claims 32, 56), and the observed increase in cash capex/OCF (claims 30,
41), motivate scrutiny. They do not establish the draft rule's two realised
years plus debt funding of the marginal dollar. That missing financing test
prevents a full-score frenzy finding. Useful infrastructure may survive
losses, but utilisation, operating costs and compute obsolescence determine
its recoverable value; physical survival does not guarantee recovery.

### 5. Shiller: CAPE and narrative

September CAPE was 40.58, with partial October at 40.71, versus a 17.8
sample mean (claims 1–4). The earlier historical-exclusivity claim was wrong:
August 2026 was higher (claim 45). September/October CPI is estimated, and
October's price and nominal yield use October 2 observations, not an October
17 market snapshot (claims 2, 44).

The TIPS-based proxy is −0.32 percentage points using September CAPE and
October 15 real yields (claim 7). Shiller's published excess CAPE yield is
+0.82% for September and +0.56% for partial October under a different
construction (claim 44). The opposite signs materially change the draft
negative-yield scoring interpretation; the measures cannot share an unlabeled
threshold. The review did not establish an all-history real-yield novelty
claim under a consistent real-rate definition, so none is asserted here.

Shiller's narrative lens asks how stories spread. No quantitative AI
narrative index was fetched; earnings-call mentions are a possible research
measure, not an observed signal in this note.

### 6. Technology bubble vs asset-price bubble, and the role of debt

An asset-price reversal can destroy marked-to-market wealth and transmit
losses through spending, collateral and financing. It need not be a zero-sum
wealth transfer. Technology overbuild can leave useful infrastructure, but
recoverable value depends on utilisation, operating costs and obsolescence.
Trace losses through equity, contractual claims, collateral and guarantees.

The AI case combines expensive equity claims with a large physical build.
The four-company funding ratio rose to 96.1% in Q2; Oracle and CoreWeave's
combined $767.7 bn backlog joins August and June snapshots, not same-date
near-term cash requirements (claims 41, 55). Equity ordinarily absorbs losses
before creditors at Oracle and CoreWeave as well as at hyperscalers. CoreWeave's
carrying debt is distinct from scheduled principal (claim 34); creditor
recoveries require a claim-by-claim map of security, recourse and guarantees.
The SPV/private-credit layer remains unsized here.

The May FSR highlights weaker debt service at riskier floating-rate borrowers
and some BDC redemption pressures, alongside high hedge-fund leverage. It
also describes moderate debt/funding vulnerabilities, declining aggregate
debt/GDP and strong bank capital (claims 11–12, 52; source 4). This qualifies
an economy-wide fragility inference and AI attribution. Broad HY and IG OAS
cannot establish that AI risk is unpriced; the newer sector evidence in
claim 46 changes that conclusion. The key test is whether customer cash
arrives before debt and investment commitments fall due, and what assets
are recoverable if it does not.

### 7. Draft scoring rubric

The original draft used 0 = absent, 1 = present, 2 = historical extreme.
Those labels were not historically calibrated. The original assignments
below are retained for audit, with corrected readings and explicit defects;
**all composite scoring and stage inference are suspended**. This is not a
revised numerical assessment.

| # | Indicator (framework) | Data / source | Original proposed threshold for 2 | Corrected current reading | Original assignment (withdrawn) | Review of rule |
|---|---|---|---|---|---|---|
| 1 | CAPE (Shiller, Dalio #1) | claims 1–4 | >35 | 40.58 Sep; 40.71 partial Oct | 2 | Expensive, but threshold not calibrated to historical crisis odds. |
| 2 | Excess CAPE yield proxy (Shiller) | claims 7, 44 | <0 | TIPS proxy −0.32 pp; published ECY positive | 2 | Construction changes the sign; specify the measure before scoring. |
| 3 | Forward P/E vs ten-year average | claim 8 | >25% above average | 19.0 vs 19.1, slightly below | 0 | Threshold not met; genuine valuation counterevidence. |
| 4 | Unsustainable growth (Dalio #2 proxy) | claims 8, 10, 53 | percentile gap >40 pts; table added EPS growth >25% | CY2026 consensus +32.8%; forward-P/E percentile unavailable | 2 | Gap unmeasurable; one-year growth alternative is inconsistent and does not test sustainability. |
| 5 | Concentration | claims 13–14 | top ten >35% | proxy 38.39% for securities / 39.89% for companies | 2 | Count unit matters; primary index weights still missing, proxy grade D. |
| 6 | Margin debt | claims 15–16 | current record and >20% y/y | $1.480 tn, +31.4% y/y, below June peak | 2 | Current-record condition fails despite rapid y/y growth. |
| 7 | Systemic leverage | claims 12, 52 | FSR says near all-time highs | High hedge-fund leverage; systemic counterevidence also present | 2 | Not an AI-specific or economy-wide leverage measure. |
| 8 | New buyers / issuance | claims 27–28, 38, 51 | record quarter within twelve months and record allocation | record Q2 concentrated; household claim unverified | 1 | Original 1 conflicted with claimed satisfaction of both conditions; allocation and direct entry unverified. |
| 9 | Broad bullish sentiment | claims 25–26 | AAII bulls >50% or FMS cash <3.5% | bulls 38.7%, bears 41.6%; cash 3.9% | 1 | Full threshold unmet; partial-score rule undefined. |
| 10 | Forward purchases | claims 30, 36, 41, 55 | RPO >10x annual revenue at top-five seller, or cash capex >80% OCF | Oracle 8.581x; CoreWeave 10.068x; four-company Q2 96.1% | 2 | Capex branch met; seller-rank and run-rate limitations remain. |
| 11 | Monetary tightening | claims 18–22, 46 | hiking cycle under way and Treasury cycle high | one hike; 5.31% Treasury high | 2 | A first hike is not a demonstrated cycle or a dated bust trigger. |
| 12 | Capex vs revenue growth (Perez proxy) | claims 32, 37 | >2x growth for two years; §4 also required marginal debt finance | ~60%/16.5% in 2025; ~80%/15.5% in 2026 plan | 2 | Two realised years and marginal debt funding unestablished; forecasts grade C. |
| 13 | Credit stress (Kindleberger) | claims 23–24, 46 | HY OAS >6% | HY 3.23%, IG 0.84%; sector repricing reported | 0 | Broad threshold unmet; broad OAS cannot rule out issuer risk. |
| | **Arithmetic total of original assignments** | | | **Withdrawn composite** | **20 / 26** | Not a calibrated bubble probability or stage. |

The displayed assignments sum to 20/26, not 19/26. Overlapping valuation
proxies, inconsistent thresholds and unverified inputs preclude a defensible
mechanically corrected assessment. Before any revised score, specify current
versus recent records, direct versus proxy participation, a matched valuation
test, and realised growth plus marginal funding; then calibrate against
history. Neither this rubric nor Dalio's own timing caveat (source 35)
supports a crisis clock. At unchanged prices, lower expected earnings raise
forward P/E; the observed multiple can rise or fall depending on the price
response. No claim that spreads or forward multiples necessarily move last
is established here.

## Conflicts and open questions

- **Valuation and the cross-check's judgement.** The original note read
  high CAPE and normal forward P/E as proof that permanently high growth was
  priced in, and treated the discrepancy as bubble confirmation. The review
  is less confident about unsustainable pricing: the forward multiple and
  Fed's earnings-led-rally assessment provide a genuine competing reading
  (claims 8–10, 46). The bear hypothesis is that infrastructure spending
  supports suppliers' earnings without sustainable end-user cash generation;
  the bull hypothesis is that earnings growth earns the investment return.
  Matched EPS periods and customer cash economics are needed to distinguish
  them. The unfetched Goldman commentary in the draft is not evidence here.
- **Debt-service classifications.** The original author called hyperscalers
  hedge units, Oracle speculative and CoreWeave speculative-to-Ponzi. The
  review rejects those categorical labels from capex deficits/net losses:
  CoreWeave's disclosed cash test supports refinancing dependence but not
  present Ponzi finance (claims 42–43). The original concern about continued
  market access remains a risk hypothesis. Resolve it with maturity schedules,
  cash available for interest/principal, and prepayment/contract durability.
- **Credit pricing.** The original note inferred unpriced AI risk from low
  broad OAS. The review is more concerned about differentiated credit risk,
  citing already elevated hyperscaler spreads in the minutes. Broad indices
  and sector spreads measure different exposures; retain both (claims 23–24,
  46). Neither establishes the fair spread for each borrower.
- **Stage and triggers.** The original author favoured late euphoria/early
  profit-taking with the policy pin already in. The review finds the stage
  and timing inference unsupported: bearish sentiment, financing access and
  a single hike permit several readings. Falling customer cash conversion,
  failed refinancing and broad forced selling would strengthen distress;
  durable customer cash growth, funded maturities and backlog conversion
  would weaken that diagnosis. Corporate issuance alone is not insider selling.
- **Shiller yield definitions.** The original negative TIPS proxy motivated
  full bubble points; the review adds Shiller's positive published ECY
  (claims 7, 44). Both are retained with their definitions and dates; a score
  depends on which construction is justified, not a silent sign substitution.
- **Dalio attribution and limits.** The original note treated the absence
  of a current numeric gauge as the biggest uncertainty and asserted it was
  unpublished. The review only failed to locate one. Past readings and
  verbal comments remain in claims 39–40; the rubric is the author's, not
  Bridgewater's. Proprietary percentiles would not resolve customer cash,
  maturities or recoverable asset values, nor automatically validate the rubric.
- **Lamont's four conditions.** Fortune (source 23) reports overvaluation,
  bubble beliefs, new entrants and issuance, with issuance still missing in
  February 2026. The original author said Q2 completed the framework; the
  review's participation/concentration objection prevents that deduction.
  The underlying Acadian post was not reached: the attribution is grade C,
  and the conditions need direct, dated evidence.
- **Perez.** The original author used capex growth and debt forecasts to
  diagnose frenzy while acknowledging that Perez did not make that call.
  The review emphasises her placement of AI within ICT and the unverified
  marginal-debt/two-realised-year tests. Wladawsky-Berger and Kedrosky offer
  differing current-cycle interpretations (sources 27–28, 45). Infrastructure
  survival and adequate economic recovery are separate propositions.
- **Sentiment versus leverage.** The draft explained bearish AAII as a
  lagging retail survey or leverage concentrated elsewhere. The review
  treats those as hypotheses, not a stage deduction; sentiment can also have
  contrarian interpretations. Margin debt remains below June's peak. Direct
  participation, positioning and leveraged-product flows would help resolve it.
- **Concentration and evidence grades.** The draft's 38.4–39.9% range
  mixed securities with companies; the review reconciles the units and grades
  the tertiary proxy D pending S&P confirmation (claim 13). It also downgrades
  the unparsed household-allocation claim to D (claim 38). By contrast,
  FactSet and Renaissance are primary for their own tallies/estimates, not
  secondary merely because they are private publishers.
- **Unverified inputs and loss mapping.** Futuriom growth estimates, the
  Morgan Stanley debt forecast and private-lab listing dates retain their
  reported/forecast status (claims 29, 32, 37). The off-balance-sheet SPV and
  private-credit layer is unsized. This gap and the collateral/guarantee map
  matter directly to who bears losses.
- **Margin debt's July drop.** Claim 54 establishes the largest
  absolute-dollar fall in the downloaded history, not the largest percentage
  decline. Forced deleveraging versus reporting/reclassification remains open;
  FINRA cautions that reporting-method changes can affect monthly balances.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| CAPE and both excess-yield constructions | CAPE 40.58; published ECY +0.82%; TIPS proxy −0.32 pp | Sep CAPE/ECY; Oct 15 TIPS | claims 1, 7, 44 | Track valuation and definition sensitivity; October inputs are partial. |
| FINRA margin debt | $1,480 bn; June record $1,502 bn; +31.4% y/y | 2026-09 | claims 15–16 | Declines may reveal deleveraging; no universal drawdown rule is established. |
| Policy and Treasury yields | target 3.75–4.00%; 10-year 5.10%, high 5.31% | Sep 16 / Oct 15 | claims 18–22 | Test refinancing costs and policy transmission; not a bust clock. |
| Broad and issuer credit spreads | HY 3.23%, IG 0.84%; sector repricing reported | Oct 15 / September meeting | claims 23–24, 46 | Obtain borrower-specific spread, collateral and maturity data. |
| Forward P/E and earnings revisions | 19.0x; CY2026 consensus +32.8% | 2026-10-16 | claims 8–10 | Match EPS periods; at fixed price, lower EPS raises P/E. |
| Named-four cash capex/OCF | 86.1% Q1; 96.1% Q2 | CY2026-Q1/Q2 | claims 30, 41 | Track funding headroom and constituent dispersion, alongside debt service. |
| Oracle backlog and investment FCF | $664 bn; −$5.396 bn | FY27-Q1 | claim 33 | Test backlog cash conversion and funding of committed investment. |
| CoreWeave cash debt service and market access | H1 cash before operating interest $4.469 bn vs $6.201 bn debt service; September financing announcements | H1 / Sep 17–18 | claims 42–43, 47–50 | Track actual settlement, ATM sales, prepayments and maturities separately. |
| IPO breadth and completed listings | Q2 $104.8 bn, 71.6% SpaceX; Q3 $32.8 bn, $6.2 bn ex SK hynix | Q2/Q3 2026 | claims 27–29, 51 | Separate dollar concentration, new entrants and forecast listings. |
| AAII and FMS | bull-bear spread −2.9 pp; cash 3.9% | Oct 14 / Oct 13 | claims 25–26 | Compare sentiment with direct positioning; avoid unique stage inference. |
| Primary index concentration and household allocation | proxy 38.39% securities / 39.89% companies; allocation unverified | 2026-10-17 / Q1 | claims 13, 38 | Replace grade-D proxies with originating index and Z.1 data. |

## Sources

1. Federal Reserve, "Federal Reserve issues FOMC statement", 16 Sep 2026. https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm (accessed 2026-10-17)
2. Federal Reserve, "Federal Reserve issues FOMC statement", 29 Jul 2026. https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm (accessed 2026-10-17)
3. Federal Reserve, "Open Market Operations" (policy-rate history). https://www.federalreserve.gov/monetarypolicy/openmarket.htm (accessed 2026-10-17)
4. Federal Reserve, "Financial Stability Report, May 2026: Overview" (data as of 23 Apr 2026). https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm (accessed 2026-10-17)
5. FINRA, "Margin Statistics". https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics (accessed 2026-10-17)
6. Robert J. Shiller, "Online Data", ie_data.xls, Data sheet, file version 1791297298731. https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls?ver=1791297298731 (downloaded and parsed 2026-10-17; October price/GS10 from Oct 2; September/October CPI estimated)
7. multpl.com, "Shiller PE Ratio", 16 Oct 2026. https://www.multpl.com/shiller-pe (accessed 2026-10-17)
8. FRED, "10-Year Treasury Constant Maturity Rate (DGS10)". https://fred.stlouisfed.org/series/DGS10 (accessed 2026-10-17; full CSV via fredgraph.csv)
9. FRED, "10-Year Treasury Inflation-Indexed Security (DFII10)". https://fred.stlouisfed.org/series/DFII10 (accessed 2026-10-17)
10. FRED, "ICE BofA US High Yield Index Option-Adjusted Spread (BAMLH0A0HYM2)". https://fred.stlouisfed.org/series/BAMLH0A0HYM2 (accessed 2026-10-17)
11. FRED, "ICE BofA US Corporate Index Option-Adjusted Spread (BAMLC0A0CM)". https://fred.stlouisfed.org/series/BAMLC0A0CM (accessed 2026-10-17)
12. FRED, "Gross Domestic Product (GDP)". https://fred.stlouisfed.org/series/GDP (accessed 2026-10-17)
13. FactSet, John Butters, "S&P 500 Earnings Season Update: October 16, 2026". https://insight.factset.com/sp-500-earnings-season-update-october-16-2026 (accessed 2026-10-17)
14. AAII, "Investor Sentiment Survey", week ending 14 Oct 2026. https://www.aaii.com/sentimentsurvey (accessed 2026-10-17)
15. interactive investor, "Fund manager optimism faltering" (BofA Global Fund Manager Survey, October 2026), 13 Oct 2026. https://www.ii.co.uk/analysis-commentary/fund-manager-optimism-faltering-ii540567 (accessed 2026-10-17)
16. Renaissance Capital, "US IPO Market: 3Q 2026 Quarterly Review", 1 Oct 2026. https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf (accessed 2026-10-17)
17. Epoch AI, "Hyperscaler capex vs cash flow", 16 Jun 2026. https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow (accessed 2026-10-17)
18. Apollo Global Management, Torsten Slok, Rajvi Shah, Shruti Galwankar, "The extreme weight of AI in the S&P 500", Jan 2026. https://www.apolloacademy.com/wp-content/uploads/2026/01/011326-MarketConcentration.pdf (accessed 2026-10-17)
19. stockanalysis.com, "S&P 500 Stocks List". https://stockanalysis.com/list/sp-500-stocks/ (accessed 2026-10-17)
20. Ray Dalio, "Are We in a Stock Market Bubble?", LinkedIn, 22 Feb 2021. https://www.linkedin.com/pulse/we-stock-market-bubble-ray-dalio (accessed 2026-10-17)
21. Ray Dalio, "Are We in a Stock Market Bubble?" (March 2024), republished by The Acquirer's Multiple at Hedge Fund Alpha, 6 Mar 2024. https://hedgefundalpha.com/?p=2162956 (accessed 2026-10-17)
22. Fortune, "Ray Dalio says AI is in the early stages of a bubble, so watch out for 2026", 6 Jan 2026. https://fortune.com/2026/01/06/ray-dalio-says-ai-is-in-the-early-stages-of-a-bubble-so-watch-out-for-2026/ (accessed 2026-10-17)
23. Fortune, "Ray Dalio: AI bubble, 1929, 2000, IPOs, 'wealth is not money'", 4 Aug 2026. https://fortune.com/2026/08/04/ray-dalio-ai-bubble-1929-2000-ipos-wealth-is-not-money/ (accessed 2026-10-17)
24. Bloomberg Law, "Dalio Sees AI Bubble Bursting as Wealth Is Converted Into Money", 3 Jun 2026. https://news.bloomberglaw.com/financial-accounting/dalio-sees-ai-bubble-bursting-as-wealth-is-converted-into-money (accessed 2026-10-17)
25. Hyman P. Minsky, "The Financial Instability Hypothesis", Levy Economics Institute Working Paper No. 74, May 1992. https://www.levyinstitute.org/pubs/wp74.pdf (accessed 2026-10-17)
26. Charles P. Kindleberger, Robert Z. Aliber, Robert N. McCauley, *Manias, Panics, and Crashes: A History of Financial Crises*, 8th ed., Palgrave Macmillan, 2023. https://link.springer.com/book/9783031160073 (accessed 2026-10-17)
27. Irving Wladawsky-Berger, "What Is AI's Place in History?" (quoting Carlota Perez, Project Syndicate, March 2024), 24 Dec 2025. https://blog.irvingwb.com/blog/2025/12/what-is-ais-place-in-history.html (accessed 2026-10-17)
28. Paul Kedrosky, "Why AI Capex isn't a Bubble: A Perez-ian Perspective", 9 Oct 2025. https://paulkedrosky.com/why-ai-capex-isnt-a-bubble-a-perez-ian-perspective/ (accessed 2026-10-17)
29. Oracle, "Oracle Announces Q1 Results Driven by Triple Digit Growth in Cloud Infrastructure Revenues", 10 Sep 2026. https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx (fetched 2026-10-17; replaces the draft's secondary mirror)
30. CoreWeave, Inc., Form 10-Q for the quarter ended 30 Jun 2026, SEC EDGAR. https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm (accessed 2026-10-17)
31. Allwork.space, "Morgan Stanley forecasts $570 billion AI debt wave as hyperscalers race to fund growth", 10 Jun 2026. https://allwork.space/2026/06/morgan-stanley-forecasts-570-billion-ai-debt-wave-as-hyperscalers-race-to-fund-growth/ (accessed 2026-10-17)
32. Futuriom, Mary Jander, "Hyperscaler AI Spending Doubts Rising", 6 Apr 2026. https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04 (accessed 2026-10-17)
33. thetrading.tools, "Household equity allocation record" (Fed Z.1 derived), 14 Aug 2026. https://www.thetrading.tools/chart-of-the-day/2026-08-14-household-equity-allocation-record (accessed 2026-10-17)
34. Apollo, Torsten Slok, "Consensus just revised up capex for hyperscalers", 28 Jul 2026. https://www.apollo.com/insights-news/insights/daily-spark/consensus-just-revised-up-capex-for-hyperscalers (accessed 2026-10-17)

35. Bridgewater Associates, Ray Dalio, "Stock Market Bubble?", 2 Feb 2021. https://www.bridgewater.com/research-and-insights/ray-dalio-stock-market-bubble (fetched 2026-10-17; original six measures and timing caveat)
36. Federal Reserve, "Minutes of the Federal Open Market Committee, September 15–16, 2026", released 7 Oct 2026. https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm?trk=article-ssr-frontend-pulse_little-text-block (fetched 2026-10-17)
37. Renaissance Capital, "US IPO Market: 2Q 2026 Quarterly Review", 1 Jul 2026. https://www.renaissancecapital.com/review/2Q26USReview_Public.pdf (fetched 2026-10-17)
38. Microsoft, FY26 Q3 cash flows (quarter ended 31 Mar 2026), released 29 Apr 2026: https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/cash-flows; FY26 Q4 earnings release (quarter ended 30 Jun 2026), 29 Jul 2026: https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast (fetched 2026-10-17). The review's SEC company-facts endpoint, https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json, was unavailable on re-fetch; issuer cash-flow tables verify the same inputs.
39. Amazon, Form 10-Q, quarter ended 30 Jun 2026. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm (fetched 2026-10-17; Q1 = H1 less Q2). Review reconstruction endpoint: https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json (unavailable on re-fetch; filing used).
40. Alphabet, "Alphabet Announces First Quarter 2026 Results", 29 Apr 2026: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm; Form 10-Q for quarter ended 30 Jun 2026: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm (fetched 2026-10-17; Q2 = H1 less Q1). Review reconstruction endpoint: https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json (unavailable on re-fetch; filing/release used).
41. Meta, "Meta Reports First Quarter 2026 Results", 29 Apr 2026: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx; Form 10-Q for quarter ended 30 Jun 2026: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm (fetched 2026-10-17; Q2 = H1 less Q1). Review reconstruction endpoint: https://data.sec.gov/api/xbrl/companyfacts/CIK0001326801.json (unavailable on re-fetch; filing/release used).
42. CoreWeave, "CoreWeave Prices Upsized $3.7 Billion Convertible Senior Notes Offering", 18 Sep 2026. https://investors.coreweave.com/news/news-details/2026/CoreWeave-Prices-Upsized-3-7-Billion-Convertible-Senior-Notes-Offering/default.aspx (fetched 2026-10-17)
43. CoreWeave, "CoreWeave Announces At-the-Market Offering Program", 17 Sep 2026. https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-At-the-Market-Offering-Program/default.aspx (fetched 2026-10-17)
44. CoreWeave, "CoreWeave Continues to Contract New Compute Capacity at Higher Prices", 17 Sep 2026. https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx (fetched 2026-10-17)
45. Carlota Perez, "What Is AI’s Place in History?", Project Syndicate, 11 Mar 2024. https://www.project-syndicate.org/magazine/ai-is-part-of-larger-technological-revolution-by-carlota-perez-1-2024-03 (accessible introduction fetched 2026-10-17; full text not independently verified)
46. FINRA, "Customer Margin Balances", historical workbook. https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx (downloaded and parsed 2026-10-17)
47. Oracle, Form 10-Q, quarter ended 31 Aug 2026. https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm (fetched 2026-10-17; exact cash-flow inputs)
48. CoreWeave, "CoreWeave Reports Strong Second Quarter 2026 Results", 11 Aug 2026. https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/ (fetched 2026-10-17; distinguishes net interest expense from cash paid)

Review applied: [Independent Codex cross-check](../../reviews/bubble-mechanics-codex-xcheck.md), 2026-10-17. Its scope was selected claims and Analysis arithmetic, not independent verification of every original claim. New figures above were re-fetched from originating sources; original unverified inputs retain their stated limitations.
