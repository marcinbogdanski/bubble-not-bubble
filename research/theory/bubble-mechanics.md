# Bubble mechanics, operationalised for the AI boom

*Last updated: 2026-10-17 · Status: draft · Author: Claude (Fable 5.1 subagent) · Reviewer: none*

## Summary

- Four frameworks describe the same machine from different angles. Minsky
  explains why calm breeds fragility (hedge units drift to speculative and
  Ponzi finance). Kindleberger names the stages (displacement, boom, euphoria,
  profit-taking, panic) and insists credit is the fuel. Perez explains why the
  frenzy builds real infrastructure that outlives the crash. Dalio turns the
  whole thing into a six-item checklist. Shiller supplies the valuation
  anchor (CAPE) and the contagion theory (narratives).
- Applied to October 2026 data, the checklist is unusually full. Shiller's own
  file puts CAPE at 40.6 (September, last full month), against a series peak
  of 44.2 in December 1999 and a mean of 17.8. FINRA margin debt hit a record
  $1.50 tn in June 2026 and is $1.48 tn in September, up 25% in eleven months.
  The ten largest S&P 500 names are roughly 38–40% of the index, which Apollo
  calls a record. Forward purchases are extreme: Oracle's backlog is $664 bn,
  CoreWeave's $104 bn, and the four hyperscalers spent 94% of operating cash
  flow on capex in Q1 2026.
- The one indicator that argues the other way is the forward P/E: FactSet
  has the S&P 500 at 19.0x, below its ten-year average, because consensus has
  calendar-2026 EPS growing 32.8%. CAPE and forward P/E disagree because the
  market is priced for that earnings surge to be permanent. That is Dalio's
  "prices discounting unsustainable conditions", not evidence against a bubble.
- The two things Dalio says prick bubbles, rising rates and a flood of new
  issuance, are both now present. The Fed raised rates on 16 September 2026
  to 3.75–4.00%, its first hike since July 2023, with inflation "elevated";
  the 10-year Treasury touched 5.31% on 5 October 2026, its highest since May
  2002. Q2 2026 was a record IPO quarter ($104.8 bn), Oracle sold $20 bn of
  stock through an ATM, and Anthropic is expected to list in Q4 2026.
- Credit is where the damage is decided. Hyperscalers are still Minsky hedge
  units (capex roughly equals operating cash flow, funded by cash plus bonds);
  Oracle has become a speculative unit (free cash flow −$5 bn in a quarter,
  equity raised to fund capex); CoreWeave is speculative-to-Ponzi ($35.1 bn
  of debt, interest equal to 25% of revenue, net loss). Spreads have not yet
  priced this: high-yield OAS is 3.23%, IG 0.84%.
- Draft score: 19 of 26 on the rubric at the end of this note. Sentiment
  surveys are the only soft reading (AAII bears outnumber bulls), which in
  Kindleberger's sequence is consistent with the late-euphoria / early
  profit-taking boundary rather than with a market that has not yet bubbled.
- Biggest uncertainty: Dalio has not published a numeric gauge reading for
  2025–2026, and no fetched source gives per-measure percentiles. The scores
  here are the author's operationalisation of his questions, not his numbers.

## Key claims

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Shiller CAPE, last full month | 40.58 | 2026-09 | [Shiller ie_data.xls](https://shillerdata.com/) | primary | A |
| 2 | Shiller CAPE, partial month | 40.71 | 2026-10 | [Shiller ie_data.xls](https://shillerdata.com/) | primary | A |
| 3 | CAPE all-time peak | 44.20 (Dec 1999); 1929 peak 32.56; 2007 peak 27.55; 2021 peak 38.58 | series 1881–2026 | [Shiller ie_data.xls](https://shillerdata.com/) | primary | A |
| 4 | CAPE long-run mean / median | 17.8 / 16.6 | series 1881–2026 | [Shiller ie_data.xls](https://shillerdata.com/) (computed) | primary | B |
| 5 | CAPE daily estimate | 40.54 | 2026-10-16 | [multpl](https://www.multpl.com/shiller-pe) | tertiary | C |
| 6 | 10-year TIPS real yield | 2.78% | 2026-10-15 | [FRED DFII10](https://fred.stlouisfed.org/series/DFII10) | primary | A |
| 7 | CAPE earnings yield minus 10y real yield (excess-CAPE-yield proxy) | 2.46% − 2.78% = −0.32 pp | 2026-09/10 | computed from #1, #6 | primary | B |
| 8 | S&P 500 forward 12-month P/E | 19.0 (5-yr avg 19.8, 10-yr avg 19.1) | 2026-10-16 | [FactSet Earnings Insight](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | secondary | B |
| 9 | S&P 500 Q3 2026 blended earnings / revenue growth | 29.0% / 12.6% | 2026-10-16 | [FactSet](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | secondary | B |
| 10 | S&P 500 CY2026 EPS growth, consensus | 32.8% | 2026-10-16 | [FactSet](https://insight.factset.com/sp-500-earnings-season-update-october-16-2026) | secondary | B |
| 11 | Fed: equity premium "well below its historical average"; P/E "in the upper range of its historical distribution" | qualitative | data to 2026-04-23 | [Fed FSR May 2026](https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm) | primary | A |
| 12 | Fed: hedge fund leverage "near all-time highs", concentrated in a few large funds | qualitative | data to 2026-04-23 | [Fed FSR May 2026](https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm) | primary | A |
| 13 | Top 10 S&P 500 weights (sum) | 38.4% (page's own figure 39.9%); NVDA 7.86% | 2026-10-17 | [stockanalysis.com](https://stockanalysis.com/list/sp-500-stocks/) | tertiary | C |
| 14 | S&P 500 top-10 market-cap and earnings concentration "at record-high levels"; TMT share "as high as during the 1990s tech bubble" | qualitative | 2026-01 | [Apollo, Slok et al.](https://www.apolloacademy.com/wp-content/uploads/2026/01/011326-MarketConcentration.pdf) | secondary | B |
| 15 | FINRA margin debt, record | $1,502,072 m | 2026-06 | [FINRA margin statistics](https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics) | primary | A |
| 16 | FINRA margin debt, latest | $1,480,054 m (Oct-25: $1,183,654 m, +25.0%) | 2026-09 | [FINRA](https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics) | primary | A |
| 17 | Margin debt as share of nominal GDP | 4.5% ($1.480 tn / $32.563 tn SAAR) | 2026-Q2 GDP, Sep-26 debt | [FRED GDP](https://fred.stlouisfed.org/series/GDP), FINRA (computed) | primary | B |
| 18 | Fed funds target range raised 25 bp to 3.75–4.00%, vote 12–0, "inflation remains elevated" | +25 bp | 2026-09-16 | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) | primary | A |
| 19 | Previous meeting held at 3.50–3.75%, 9–3 with three dissents for a hike (Hammack, Kashkari, Logan) | hold | 2026-07-29 | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm) | primary | A |
| 20 | Last prior increase before Sept 2026 | 2023-07-27 (+25 bp to 5.25–5.50%); cuts Sep 2024–Dec 2025 to 3.50–3.75% | 2026-09-16 | [Fed policy-rate history](https://www.federalreserve.gov/monetarypolicy/openmarket.htm) | primary | A |
| 21 | 10-year Treasury yield, 2026 high | 5.31% (last higher close: 5.32% on 2002-05-14; 2007 peak 5.26%) | 2026-10-05 | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) (computed from CSV) | primary | B |
| 22 | 10-year Treasury yield, latest | 5.10% | 2026-10-15 | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) | primary | A |
| 23 | ICE BofA US High Yield OAS | 3.23% | 2026-10-15 | [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | primary | A |
| 24 | ICE BofA US Corporate (IG) OAS | 0.84% | 2026-10-15 | [FRED BAMLC0A0CM](https://fred.stlouisfed.org/series/BAMLC0A0CM) | primary | A |
| 25 | AAII sentiment: bullish / neutral / bearish | 38.7% / 19.7% / 41.6% (averages 37.5 / 31.0 / 31.5) | week to 2026-10-14 | [AAII](https://www.aaii.com/sentimentsurvey) | primary | A |
| 26 | BofA Global FMS: average cash 3.9%; 31% name "disorderly rise in bond yields" top tail risk; 37% would rotate to bonds at a 6% 10-year | Oct 2026 edition | 2026-10-13 | [interactive investor](https://www.ii.co.uk/analysis-commentary/fund-manager-optimism-faltering-ii540567) | secondary | B |
| 27 | US IPOs, 3Q26 | 30 deals, $32.8 bn ($6.2 bn ex SK hynix); Renaissance IPO Index −11% in the quarter | 2026-10-01 | [Renaissance Capital 3Q26 review](https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf) | secondary | B |
| 28 | US IPOs, 2Q26 (record proceeds) | 48 deals, $104.8 bn | 2026-Q2 | [Renaissance Capital 3Q26 review](https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf) (chart) | secondary | B |
| 29 | Slowdown attributed to "concerns about AI spending, a 19-year high in bond yields, and resumed rate hikes"; Anthropic expected to list 4Q26, OpenAI waiting until 2027 | qualitative | 2026-10-01 | [Renaissance Capital](https://www.renaissancecapital.com/review/3Q26USReview_Public.pdf) | secondary | B |
| 30 | Four hyperscalers (MSFT, GOOGL, AMZN, META): capex $148.4 bn vs operating cash flow $157.9 bn, i.e. 94% | CY2026 Q1 | 2026-06-16 | [Epoch AI](https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow) | secondary | B |
| 31 | Same ratio in earlier years | 35–37% (2023 trough), 72% (2025 Q2–Q4) | 2023–2025 | [Epoch AI](https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow) | secondary | B |
| 32 | Hyperscaler 2025 revenue growth vs capex growth; 2026 plan | 16.5% vs ~60% (2025); ~15.5% vs ~80% (2026 plan) | 2026-04-06 | [Futuriom](https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04) | secondary | C |
| 33 | Oracle RPO | $664 bn, +$209 bn YoY; OCI revenue +121% to $7.4 bn; quarterly FCF −$5 bn; $20 bn ATM equity sale completed | FY27 Q1 (to 2026-08-31) | [Oracle release via StorageNewsletter](https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results) | secondary (mirror of primary) | B |
| 34 | CoreWeave total debt | $35,068 m (recourse $31,405 m); cash $5,524 m | 2026-06-30 | [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm) | primary | A |
| 35 | CoreWeave Q2 2026 interest expense / revenue / net loss | $640 m / $2,575 m / −$626 m (interest = 24.9% of revenue) | 2026-Q2 | [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm) | primary | A |
| 36 | CoreWeave RPO | $103.7 bn; 41% recognised within 24 months | 2026-06-30 | [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm) | primary | A |
| 37 | Morgan Stanley: AI-related global debt issuance forecast 2026 | ~$570 bn (more than double 2025); $236 bn YTD to 2026-05-31; hyperscaler capex ~$700 bn in 2026 | 2026-06-10 | [Allwork.space](https://allwork.space/2026/06/morgan-stanley-forecasts-570-billion-ai-debt-wave-as-hyperscalers-race-to-fund-growth/) | secondary | C |
| 38 | Household equity share of financial assets (Fed Z.1) | 46.0% four-quarter average, record; 2000 peak 38.7% | 2026-Q1 | [thetrading.tools](https://www.thetrading.tools/chart-of-the-day/2026-08-14-household-equity-allocation-record) | tertiary | C |
| 39 | Dalio aggregate bubble gauge, published readings | 77th percentile (Feb 2021); 52nd percentile, "mid-range" (Mar 2024); 1929 and 2000 = 100th | 2021, 2024 | [Dalio, LinkedIn 2021](https://www.linkedin.com/pulse/we-stock-market-bubble-ray-dalio); [2024 mirror](https://hedgefundalpha.com/?p=2162956) | primary / secondary | A / B |
| 40 | Dalio 2025–26 verbal readings | AI "about 80%" of 1929/2000 euphoria (Nov 2025); "early stages of a bubble" (Jan 2026); "classic signs that we're in [one]" (Aug 2026); pins are rising rates and surging stock issuance | 2025-11 to 2026-08 | [Fortune Jan 2026](https://fortune.com/2026/01/06/ray-dalio-says-ai-is-in-the-early-stages-of-a-bubble-so-watch-out-for-2026/); [Fortune Aug 2026](https://fortune.com/2026/08/04/ray-dalio-ai-bubble-1929-2000-ipos-wealth-is-not-money/) | secondary | B |

Type: primary / secondary / tertiary. Grade: A–D (see report/methodology.md).
Computed rows (4, 7, 17, 21) are simple arithmetic on primary data; the
inputs are in `data/theory-shiller-cape.csv` and
`data/theory-finra-margin-debt.csv`.

## Analysis

### 1. Minsky: stability breeds fragility

Minsky's 1992 Levy Institute paper defines three financing postures. Hedge
units "can fulfill all of their contractual payment obligations by their cash
flows". Speculative units can pay interest but "cannot repay the principle out
of income cash flows" and must roll over. For Ponzi units "the cash flows from
operations are not sufficient to fulfill either the repayment of principle or
the interest due", so they sell assets or borrow to pay interest. His second
theorem: "over periods of prolonged prosperity, the economy transits from
financial relations that make for a stable system to financial relations that
make for an unstable system." The trigger he names is explicit: if "the
authorities attempt to exorcise inflation by monetary constraint, then
speculative units will become Ponzi units and the net worth of previously
Ponzi units will quickly evaporate" (source 25).

Operationalised for the AI stack, the indicator is the *distribution of
financing postures by layer*, read from filings:

- **Hyperscalers** are still hedge units. Epoch's compilation of their
  filings shows capex at 94% of operating cash flow in Q1 2026, up from
  35–37% in 2023 (claims 30–31). Operating cash flow still covers capex and
  interest; what has vanished is free cash flow. Epoch extrapolates the
  crossover (capex above operating cash flow) to late 2026 in aggregate, with
  Oracle already past it and Amazon at it.
- **Oracle** has crossed into speculative finance: quarterly free cash flow of
  −$5 bn, a $20 bn at-the-market equity sale in the quarter, and a $664 bn
  backlog whose delivery requires capex it cannot fund from operations
  (claim 33). Equity issuance to fund capex is not Ponzi (no borrowing to pay
  interest), but it is the posture Minsky describes as needing continuous
  market access.
- **CoreWeave** is the clearest speculative-to-Ponzi unit in the public
  stack: $35.1 bn of debt against $5.5 bn of cash, interest expense equal to a
  quarter of revenue, and a net loss (claims 34–35). It services debt by
  rolling it and by new borrowing against contracted backlog. Whether that is
  "speculative" or "Ponzi" turns on whether operating cash flow covers
  interest, which this note did not extract; the company note should.

The Minsky trigger has now fired. The Fed's September statement reads
"inflation remains elevated" and raises rates "in support of a timelier return
to the Committee's 2 percent goal" (claim 18). That is monetary constraint
applied to an economy with a growing weight of speculative units, which is
Minsky's recipe for the transition.

### 2. Kindleberger: stages, and credit as fuel

Kindleberger's sequence (displacement, boom, euphoria, profit-taking, panic),
updated by Aliber and McCauley in the 2023 eighth edition (source 26), is a
narrative template, so the useful move is to attach a dated, falsifiable
marker to each stage.

| Stage | Marker in the AI case | Reading, Oct 2026 |
|---|---|---|
| Displacement | A new profit opportunity that is real | Satisfied: S&P 500 Q3 2026 earnings growth 29% with Information Technology leading (claim 9); Oracle OCI revenue +121% (claim 33). |
| Boom | Credit expands to finance the opportunity | Satisfied: AI-related debt issuance on track to double in 2026 (claim 37); margin debt +25% in eleven months (claim 16). |
| Euphoria | Purchases for resale rather than use; new entrants; prices decouple from traditional measures | Largely satisfied: CAPE 40.6 (claim 1), record IPO proceeds in Q2 2026 (claim 28), record household equity allocation (claim 38, grade C). |
| Profit-taking / distress | Insiders sell, issuance surges, the marginal buyer tires | Early signs: Oracle's $20 bn ATM, Anthropic IPO queued, Renaissance IPO Index −11% in Q3 and "postponements near quarter end" (claims 27, 29), record $85 bn one-month drop in margin debt in July then a rebound (claim 15–16 and CSV). |
| Panic | Forced selling, credit withdrawal, spreads blow out | Not present: HY OAS 3.23%, IG 0.84% (claims 23–24). |

Kindleberger's central mechanism is credit. The indicator is the *rate of
credit growth into the asset class relative to the income it generates*. Two
data points: Morgan Stanley's forecast of ~$570 bn of AI-related debt
issuance in 2026 against hyperscaler capex of ~$700 bn (claim 37, grade C),
and the Futuriom tally of capex growing roughly 60% in 2025 and a planned 80%
in 2026 against revenue growth of about 16% (claim 32, grade C). Both need
primary confirmation in the financing note, but the direction is not in
doubt: capex is outrunning revenue by a factor of four to five, and the gap is
being closed with debt and equity issuance.

### 3. Dalio's checklist, item by item

Dalio defines a bubble as "an unsustainably high price" and asks six
questions (source 20). His published aggregate readings are 77th percentile in
February 2021 and 52nd percentile ("mid-range", "doesn't look bubbly") in March
2024; both 1929 and 2000 scored 100th (claim 39). No fetched source carries a
numeric reading for 2025 or 2026. His verbal readings have moved steadily
up: "about 80%" of the way to 1929/2000 euphoria (November 2025), "early
stages of a bubble" (January 2026), and "Classic signs that we're in [one]"
(August 2026), with two named pins, rising interest rates and surging stock
issuance ("There's almost nothing that's easier to produce than stock")
(claim 40). The task brief lists a seventh item, tightening monetary policy;
Dalio treats it as the pin rather than as a gauge component, and this note
keeps that distinction.

1. **Prices high vs traditional measures.** Indicator: Shiller CAPE from
   Shiller's own file, and the Fed's FSR language on the equity premium.
   Reading: CAPE 40.6, the 92nd-plus percentile of the post-1881 series and
   above every month outside 1997–2001 (claims 1–3). Fed: equity premium
   "well below its historical average" (claim 11). Threshold for a full
   score: CAPE above 35 or above the 2021 peak. **Score 2.**
2. **Prices discounting unsustainable conditions.** Indicator: the gap
   between CAPE and forward P/E, which measures how much of the valuation
   rests on the persistence of current earnings growth. Reading: forward P/E
   19.0, at its ten-year average, only because consensus has CY2026 EPS up
   32.8% (claims 8, 10). If earnings growth reverts to the 2025 revenue
   growth rate of about 16%, the same prices would be a forward multiple in
   the mid-20s. Apollo's January deck shows earnings growth "concentrated in
   the Magnificent 7, and slowing down" (claim 14). Threshold: full score
   when the gap between CAPE percentile and forward-P/E percentile exceeds
   40 points. **Score 2** on that definition; see Conflicts for the opposing
   reading.
3. **New buyers entering.** Indicator: IPO proceeds per quarter (Renaissance),
   household equity share of financial assets (Fed Z.1). Reading: Q2 2026 a
   record $104.8 bn, Q3 $32.8 bn with postponements; household equity share
   at a record 46% four-quarter average against 38.7% at the 2000 top (claims
   27–28, 38). Threshold: full score when both the IPO window and the
   household allocation are at records; half when one is. **Score 1**
   (the IPO window has wobbled; Anthropic's expected mega-IPO would re-open
   it).
4. **Broad bullish sentiment.** Indicator: AAII bull-bear spread, BofA FMS
   cash. Reading: AAII bears 41.6% vs bulls 38.7%, a negative spread; FMS
   cash 3.9%, low but flat (claims 25–26). Threshold: full score when AAII
   bulls exceed 50% or FMS cash is below 3.5%. **Score 1.** Note that
   Kindleberger's profit-taking stage is exactly when retail sentiment turns
   while leverage stays high, so a low score here does not argue for an
   early stage.
5. **Leverage-financed purchases.** Indicator: FINRA margin debt level and
   twelve-month growth, Fed FSR on hedge fund leverage. Reading: record
   $1.50 tn in June, $1.48 tn in September, +25% since October 2025, 4.5% of
   GDP; hedge fund leverage "near all-time highs" (claims 15–17, 12).
   Threshold: full score when margin debt is at a record and up more than
   20% year on year. **Score 2.**
6. **Extended forward purchases.** Indicator: contracted backlog relative to
   revenue (RPO), and capex as a share of operating cash flow. Reading:
   Oracle RPO $664 bn against quarterly revenue of $19.3 bn (about 34
   quarters of revenue); CoreWeave RPO $103.7 bn against $2.6 bn quarterly
   revenue; hyperscaler capex at 94% of cash flow (claims 30, 33, 36). These
   are multi-year purchase commitments made in anticipation of scarcity,
   which is Dalio's definition. Threshold: full score when RPO exceeds ten
   times annual revenue at any top-five infrastructure seller, or capex
   exceeds 80% of operating cash flow at the hyperscalers. **Score 2.**
7. **Tightening monetary policy (the pin).** Indicator: direction of the
   fed funds target and the 10-year yield versus its post-2007 range.
   Reading: first hike since 2023 on 16 September 2026; 10-year at 5.31% on
   5 October, the highest since May 2002 (claims 18–22). Threshold: full
   score when the Fed is hiking and the 10-year is at a cycle high. **Score
   2.**

### 4. Perez: installation, frenzy, and what survives

Perez's installation-versus-deployment cycle holds that each technological
revolution begins with an installation period financed by speculative
capital, peaks in a frenzy, breaks in a crash, and only then enters a
deployment "golden age" once finance is re-coupled to production. Her
specific position on AI, in a March 2024 Project Syndicate piece quoted by
Wladawsky-Berger, is that AI is "a key development within the still-evolving
information-communications-technology (ICT) revolution", that the ICT
revolution "is still in the middle of its diffusion process", and that AI is
unlikely to deliver sustainable outcomes "if financial markets remain
unregulated and decoupled from the real economy" (source 27). She does not,
in any fetched source, call the current AI build a frenzy or forecast a
crash; the inference that her framework predicts one is the commentators'
(Kedrosky, source 28, argues the opposite: that AI capex is a late
installation surge whose infrastructure will be kept even if investors lose).

The operational indicator for "frenzy" is the ratio of capital deployed to
the revenue the technology generates, and the share of that capital raised
from financial rather than productive sources. Reading: capex growing four to
five times faster than revenue at the hyperscalers (claim 32), capex at 94% of
operating cash flow (claim 30), and an AI debt wave forecast to double in a
year (claim 37). Threshold: full score when capex growth exceeds twice revenue
growth for two consecutive years and the marginal dollar of capex is
debt-financed. **Score 2.** The Perez lens also supplies the most important
caveat in this note: installation-period overbuild is normal, and the
infrastructure outlives the financial losses. The question the report must
keep separate is who holds those losses.

### 5. Shiller: CAPE and narrative

CAPE is the valuation anchor across every framework above, so the current
reading matters: Shiller's own file gives 40.58 for September 2026 and 40.71
for the partial October month, the mean is 17.8, and only the 1997–2001
episode has exceeded it (claims 1–4). A second Shiller construct, the excess
CAPE yield, compares the CAPE earnings yield to the real bond yield. Using
the 10-year TIPS yield as the real-rate proxy, the CAPE yield of 2.46% is
*below* the 2.78% real yield, so the proxy excess yield is negative (claim 7).
At the 2000 peak the 10-year nominal yield was around 6% with CAPE at 44; in
2021 CAPE was 38.6 with real yields negative. Today's combination of a
40-plus CAPE and a positive real yield near 2.8% has no precedent in the
series. Indicator: excess CAPE yield (CAPE yield minus 10-year real yield).
Threshold: full score when negative. **Score 2.**

Shiller's narrative-economics thesis says contagious stories, not just
numbers, drive both the boom and the bust. This note found no fetched source
with a quantitative narrative index for AI, so the indicator is left as an
open item: a candidate is the share of S&P 500 earnings calls mentioning
"AI", which FactSet publishes periodically.

### 6. Technology bubble vs asset-price bubble, and the role of debt

The methodology insists on separating "the technology is real" from "the
capital earns a return". The frameworks sort as follows. A pure asset-price
bubble (1929, 2021 meme stocks) inflates claims on existing assets; the loss
on bursting is a wealth transfer, damaging mainly through margin calls and
leverage. A technology bubble (1840s railways, 1999 fiber) builds real
capacity ahead of demand; the loss is real (stranded or underpriced assets)
but the capacity survives and is often re-used at a lower cost basis. What
determines how damaging the burst is, in both Minsky and Kindleberger, is
*where the debt sits and whose balance sheet absorbs the write-down*.

The AI case has features of both. The asset-price layer is the equity market:
CAPE 40.6, a 38–40% top-ten concentration, record margin debt and record
household equity exposure (claims 1, 13, 15, 38). The technology layer is the
build: four hyperscalers putting 94% of cash flow into capex, Oracle and
CoreWeave contracting $770 bn of future delivery between them. The debt map,
as far as this note establishes it from fetched sources, is: investment-grade
bonds at the hyperscalers (hedge units, losses would fall on equity holders
first); a $20 bn equity raise plus bonds at Oracle (speculative, losses to
new shareholders and bondholders); $35 bn of mostly recourse debt at
CoreWeave (speculative/Ponzi, losses to lenders and the OEM financiers in its
debt table); and a growing off-balance-sheet layer in SPVs and private credit
that this note could not size from a primary source. The Fed's FSR adds that
debt-servicing capacity is already weaker at riskier private firms with
floating-rate debt, that redemption requests have risen at some non-traded
BDCs, and that hedge fund leverage is near record highs (claims 11–12). The
operational indicator is *the share of AI capex financed by debt that is
recourse to entities without positive free cash flow*. The reading is
partial: CoreWeave's $31.4 bn of recourse debt is the only hard number;
the financing note should build the full ledger.

### 7. Draft scoring rubric

Scores: 0 = indicator not present; 1 = present but not at historical
extremes; 2 = at or beyond the extremes of 1929, 2000 or 2007. The lead agent
should treat the thresholds as proposals.

| # | Indicator (framework) | Data / source | Threshold for 2 | Current reading | Score |
|---|---|---|---|---|---|
| 1 | CAPE (Shiller, Dalio #1) | Shiller ie_data.xls | > 35 | 40.6 (Sep 2026); 40.7 partial Oct | 2 |
| 2 | Excess CAPE yield proxy (Shiller) | Shiller + FRED DFII10 | < 0 | −0.32 pp | 2 |
| 3 | Forward P/E vs 10-yr average (FactSet) | FactSet Earnings Insight | > 25% above average | 19.0 vs 19.1 | 0 |
| 4 | Valuation resting on unsustainable growth (Dalio #2) | CAPE percentile minus forward-P/E percentile; consensus EPS growth | gap > 40 pts, or consensus EPS growth > 25% | CY2026 EPS +32.8%; CAPE top-decile, forward P/E median | 2 |
| 5 | Index concentration (Dalio #1, Kindleberger euphoria) | S&P top-10 weight; Apollo | top-10 > 35% | 38.4–39.9%; "record-high" | 2 |
| 6 | Margin debt (Dalio #5, Kindleberger credit) | FINRA | record level and > 20% y/y | $1.48 tn, record $1.50 tn Jun; +25% in 11 months | 2 |
| 7 | Systemic leverage (Minsky, Fed) | Fed FSR | FSR says "near all-time highs" | hedge fund leverage near record | 2 |
| 8 | New buyers / issuance (Dalio #3, Dalio pin #2) | Renaissance IPO proceeds; Fed Z.1 household equity share | record quarter in last 12 months and household share at record | Q2 2026 record $104.8 bn, Q3 $32.8 bn; household 46% (grade C) | 1 |
| 9 | Broad bullish sentiment (Dalio #4) | AAII; BofA FMS cash | AAII bulls > 50% or FMS cash < 3.5% | bulls 38.7% < bears 41.6%; cash 3.9% | 1 |
| 10 | Forward purchases (Dalio #6) | RPO / revenue at Oracle, CoreWeave; capex / OCF at hyperscalers | RPO > 10x annual revenue or capex > 80% OCF | Oracle ~8.6x annual revenue run-rate, CoreWeave ~10x, capex 94% OCF | 2 |
| 11 | Monetary tightening (Dalio pin #1, Minsky trigger) | FOMC statements; FRED DGS10 | hiking cycle under way and 10-yr at cycle high | +25 bp 16 Sep 2026; 10-yr 5.31% (highest since 2002) | 2 |
| 12 | Capex vs revenue growth (Perez frenzy) | Company filings via Epoch, Futuriom | capex growth > 2x revenue growth for two years | ~60% vs 16.5% (2025); ~80% vs 15.5% (2026 plan) | 2 |
| 13 | Credit stress (Kindleberger panic stage) | FRED HY and IG OAS | HY OAS > 6% | HY 3.23%, IG 0.84% | 0 |
| | **Total** | | | | **19 / 26** |

A score of 19/26 with zeros only on the forward P/E and credit spreads is
the signature of a late boom with the pin already in: valuation, leverage,
forward buying and policy are at extremes, while the two indicators that
move last (spreads and the forward multiple, which collapses only when
earnings estimates are cut) have not moved. The 1999–2000 analogue is the
twelve months after the Fed's first hike in June 1999, when CAPE peaked
(December 1999) while spreads stayed tight until mid-2000.

## Conflicts and open questions

- **CAPE says 2000, forward P/E says normal.** This is the central dispute.
  The bull reading (Goldman's Oppenheimer in October 2025, as summarised in
  secondary coverage this note did not fetch) is that the rally is
  earnings-driven and valuations are below prior bubbles on forward
  measures. The bear reading is that forward earnings embed AI capex itself
  (one company's capex is another's revenue), so forward P/E is circular.
  Resolution needs the "what would EPS be ex-AI-capex" decomposition; the
  stack notes should supply it.
- **Dalio's gauge is unpublished for 2025–26.** His last numeric reading
  (52nd percentile, March 2024) said "not bubbly"; his 2025–26 remarks say
  the opposite but give no number. Scores 1–11 above are the author's
  operationalisation of his questions, not Bridgewater's. If Bridgewater
  publishes a reading, it supersedes this rubric's Dalio rows.
- **Lamont's four conditions.** Fortune (August 2026) attributes a
  four-condition framework (overvaluation, "bubble beliefs", new entrants,
  issuance) to Acadian's Owen Lamont and reports that, as of February 2026,
  three were met with IPO issuance the missing one. The Q2 2026 record IPO
  quarter would complete it. The underlying Acadian post was not reachable;
  this is grade C until it is.
- **Perez does not say "frenzy".** Her fetched position is that AI is inside
  the ICT surge, mid-diffusion. Commentators split on whether that means a
  crash is still due (Wladawsky-Berger's reading of her earlier remarks) or
  that the build is a late installation surge whose assets survive
  (Kedrosky). Her own 2025–26 view was not found.
- **Sentiment is soft while leverage is hard.** AAII bears outnumber bulls
  and FMS cash is flat, yet margin debt is at a record. Either the retail
  survey is lagging price, or leveraged positions are concentrated in a
  smaller set of hands (consistent with the Fed's "concentrated in a small
  number of large funds"). The leveraged single-stock ETF flow data
  (Morningstar) would resolve this and was not fetched.
- **Household equity allocation** rests on a tertiary chart site reading the
  Fed's Z.1; the Z.1 table itself was not parsed. Grade C.
- **The off-balance-sheet layer is unsized.** SPV and private-credit
  financing of data centres is reported widely but no primary figure was
  fetched. This is the largest gap for the "who bears the loss" question.
- **Margin debt's July drop.** The series shows a record one-month fall of
  about $85 bn in July 2026 followed by two months of rebuilding. Whether
  that was a forced deleveraging event or a reclassification is not known.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| Shiller CAPE (monthly) | 40.58 | 2026-09 | shillerdata.com | Crossing 44.2 would be an all-time high; falling below 35 would signal the valuation leg has broken |
| FINRA margin debt | $1,480 bn; record $1,502 bn | 2026-09 | FINRA | Two consecutive monthly declines of >5% have preceded every major drawdown in the series |
| Fed funds target range | 3.75–4.00%, hiking | 2026-09-16 | FOMC | Minsky's trigger; a second hike would confirm a cycle |
| 10-year Treasury yield | 5.10% (high 5.31%) | 2026-10-15 | FRED DGS10 | 37% of fund managers say 6% would move them to bonds |
| HY OAS | 3.23% | 2026-10-15 | FRED | The last indicator to move; >5% would mark the panic stage |
| S&P 500 forward P/E and CY2026/27 EPS revisions | 19.0; CY2026 EPS +32.8% | 2026-10-16 | FactSet | Downward EPS revisions would reconcile forward P/E with CAPE from the wrong side |
| Hyperscaler capex / operating cash flow | 94% | CY2026-Q1 | Epoch AI (filings) | Crossing 100% in aggregate turns the hedge units into speculative units |
| Oracle RPO and FCF | $664 bn; FCF −$5 bn/qtr | FY27-Q1 | Oracle | Backlog growth without funding is the forward-purchase indicator |
| CoreWeave interest expense / revenue | 24.9% | 2026-Q2 | 10-Q | Above 30% with negative OCF would be a Ponzi reading |
| US IPO proceeds per quarter; Anthropic listing | $32.8 bn (Q3), $104.8 bn (Q2) | 2026-10-01 | Renaissance | Dalio's issuance pin; a successful mega-IPO extends the window, a pulled one closes it |
| AAII bull-bear spread | −2.9 pts | 2026-10-14 | AAII | Sentiment reverting to >+15 would complete the euphoria checklist |
| Top-10 S&P 500 weight | 38.4–39.9% | 2026-10-17 | stockanalysis (tertiary) | Replace with S&P DJI primary; above 40% is beyond any prior peak |

## Sources

1. Federal Reserve, "Federal Reserve issues FOMC statement", 16 Sep 2026. https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm (accessed 2026-10-17)
2. Federal Reserve, "Federal Reserve issues FOMC statement", 29 Jul 2026. https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm (accessed 2026-10-17)
3. Federal Reserve, "Open Market Operations" (policy-rate history). https://www.federalreserve.gov/monetarypolicy/openmarket.htm (accessed 2026-10-17)
4. Federal Reserve, "Financial Stability Report, May 2026: Overview" (data as of 23 Apr 2026). https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm (accessed 2026-10-17)
5. FINRA, "Margin Statistics". https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics (accessed 2026-10-17)
6. Robert J. Shiller, "Online Data", ie_data.xls (file version 1791297298731). https://shillerdata.com/ (accessed 2026-10-17)
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
29. StorageNewsletter, "Oracle Fiscal 1Q27 Financial Results" (reproducing Oracle's 10 Sep 2026 release; oracle.com URL returned 403), 23 Sep 2026. https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results (accessed 2026-10-17)
30. CoreWeave, Inc., Form 10-Q for the quarter ended 30 Jun 2026, SEC EDGAR. https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000366/crwv-20260630.htm (accessed 2026-10-17)
31. Allwork.space, "Morgan Stanley forecasts $570 billion AI debt wave as hyperscalers race to fund growth", 10 Jun 2026. https://allwork.space/2026/06/morgan-stanley-forecasts-570-billion-ai-debt-wave-as-hyperscalers-race-to-fund-growth/ (accessed 2026-10-17)
32. Futuriom, Mary Jander, "Hyperscaler AI Spending Doubts Rising", 6 Apr 2026. https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04 (accessed 2026-10-17)
33. thetrading.tools, "Household equity allocation record" (Fed Z.1 derived), 14 Aug 2026. https://www.thetrading.tools/chart-of-the-day/2026-08-14-household-equity-allocation-record (accessed 2026-10-17)
34. Apollo, Torsten Slok, "Consensus just revised up capex for hyperscalers", 28 Jul 2026. https://www.apollo.com/insights-news/insights/daily-spark/consensus-just-revised-up-capex-for-hyperscalers (accessed 2026-10-17)
