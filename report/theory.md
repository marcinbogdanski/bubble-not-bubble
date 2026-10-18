# How bubbles work, and where this one is

*Version 0.8, 2026-10-18 · Synthesis of
[bubble-mechanics](/research/theory/bubble-mechanics),
[historical-precedents](/research/theory/historical-precedents) and
[ai-unit-economics](/research/theory/ai-unit-economics), corrected after the
[red-team review](/reviews/2026-10-17-codex-redteam-report).*

## The mechanism

Four frameworks describe one machine. Minsky: stability breeds fragility as
borrowers drift from hedge finance (cash flow covers debt service) to
speculative (covers interest only) to Ponzi (needs new money to pay
interest). Kindleberger: displacement, boom, euphoria, profit-taking, panic,
with credit as the fuel. Perez: technological revolutions have an
installation phase that can end in a frenzy and crash, after which the
infrastructure is cheap enough for a deployment phase; the fetched Perez
material places AI inside the ICT cycle rather than diagnosing a current
frenzy. Dalio: a bubble is a price level that discounts unsustainable
conditions, and it is pricked by rising rates and a flood of new issuance.

The distinction that matters: a technology can be real and the capital that
builds it can still be lost. In the precedents where the thesis can be
judged, it was right, and build-phase investors still took large losses
(about a third of capital in the railway case, most of it in telecom).
Overbuilt assets were used later by owners who bought them cheaply.

## The checklist, October 2026

Dalio's questions, operationalised in the mechanics note with current
readings. Scores 0 absent, 1 partial, 2 present. This is a resemblance test:
it records whether the conditions past bubbles had are present. It is not a
probability model and does not test whether the investment will earn its
return.

| Indicator | Reading | Score |
|---|---|---|
| Prices high relative to traditional measures | Shiller CAPE 40.6 (September 2026 monthly) against a 1999 peak of 44.2 and a mean of 17.8; Fed: equity premium "well below its historical average" | 2 |
| Prices discounting rapid future appreciation | Forward P/E of 19 looks normal only because consensus has 2026 EPS growing 33%; AI-linked guidance assumes 2027-28 deployments that require labs to raise capital at an undemonstrated scale | 2 |
| Broad bullish sentiment | AAII bears outnumber bulls; fund managers' top tail risk is bond yields. The one soft reading | 1 |
| Purchases financed by leverage | FINRA margin debt $1.48T in September (record $1.50T in June); hyperscalers issuing bonds and equity; ~$81B of listed neocloud debt; Oracle $125B of borrowings | 2 |
| Forward purchases | Oracle RPO $664B, Microsoft $678B, CoreWeave $104B, Broadcom $179B (company-wide); Nvidia supply commitments $279B; ASML expects planned 2027-28 output below customer demand and reports interest in 2029-30 orders, not accepted orders | 2 |
| New buyers entering | Record Q2 2026 IPO proceeds ($104.8B) then a weak Q3; sovereigns, private credit and insurers entering GPU finance; household equity allocation reported at a record (grade D, derivation unverified) | 1 |
| Tightening policy | Fed hiked in September 2026, first since 2023, and its minutes say AI-related investment is "contributing to inflation pressures" alongside energy (Brent averaged $114 in September); 10-year touched 5.31% on 5 October (highest close since May 2002), then 5.09% by 16 October; CPI 3.7%. Partly a response to the boom, partly an oil confounder | 2 |

Twelve points of fourteen across seven indicators, with sentiment and
new-buyer entry the two partial readings. The main objection to this table
is the forward multiple: S&P technology at about 21x earnings against 70x in
2000. The reply is Druckenmiller's "earnings bubble": GPU buyers' capex is
suppliers' revenue, so the E can be the bubble while the P/E looks ordinary.
Which side is right is the payback question below. This scoring is the
report's own operationalisation; the mechanics note, after its cross-check, withdrew its
13-row composite (which summed to 20 of 26) pending consistent rules and
calibration, and records that the four hyperscalers spent 86% of operating
cash flow on cash capex in Q1 2026 and 96% in Q2. In Kindleberger's sequence, soft sentiment with the financing
indicators lit is consistent with the late-euphoria / early profit-taking
boundary. It is also consistent with
a rational response to a productive technology; the checklist cannot tell
those apart, which is why the arithmetic below and the stack page matter
more than this table.

## What the precedents say

| Precedent | Financing | Drawdown | Recovery | Thesis right? |
|---|---|---|---|---|
| Railways 1845-50 | Retail equity, partly paid shares | Examples: −55% (major line), −83% (weaker line); no aggregate index | Not measured | Yes |
| Electrification / 1929 | Margin, holding-company debt | Dow −89% over ~34 months; utilities −55% Sept-Nov 1929 | 25 years | Yes |
| Telecom / fiber 1997-2002 | Bonds, vendor credit and guarantees, loan trusts | Nasdaq telecom ~−89% (Mar 2000 to May 2003) | Not established for the sector | Yes |
| Dot-com 1995-2002 | IPO equity, venture | Nasdaq −78% over 31 months | 15 years | Yes |
| Japan 1986-90 | Bank credit against land | Nikkei −82% | 34 years | No technology thesis |
| Housing 2003-09 | Securitised mortgages | House prices −27% over 67 months; S&P 500 −57% | House prices 10.5 years | No technology thesis |
| Crypto / SPAC 2020-22 | Tokens, retail equity | Bitcoin −77% over ~12 months | 2 years | Not demonstrated |

What the cases support, with their limits. Financing structure shapes how
losses propagate: leverage, maturity mismatch, collateral and guarantees
carried losses beyond equity holders in 1929, telecom, Japan and 2008, while
the equity-funded cases did not produce fast recoveries either (15 years for
the Nasdaq). The cases do not establish a universal recovery order, nor that
equity-led booms cannot coincide with banking stress (the railway mania
had concurrent financial stress). The closest analog to today's circular
deals is telecom vendor financing: at September 2000 Lucent disclosed $5.4B
of undrawn and $1.3B of drawn customer credit; Cisco's FY2001 allowance
expense was $2.8B. These were observed after the March 2000 equity peak.
Nvidia's OpenAI guarantee is a cap of $105B on conditional residual-value
support phased from 2028, a different instrument and an order of magnitude
larger; AMD's warrants and Amazon's $50B investment are different again.
Broad credit spreads gave mixed timing evidence: Baa-Aaa was 1.32 points in
September 1929 and 0.82 in October 2007, but mortgage and funding-market
stress preceded the 2007 equity peak, so the broad spread alone (0.44 points
in September 2026, high-yield OAS 3.2%) is not a sufficient warning either
way. Seven selected busts give no denominator of booms that did not bust.

Which layer matches which precedent: equipment resembles the railway
contractors (sharp, short, little balance-sheet damage); foundry the
incumbent carriers; GPU vendors Lucent, Nortel and Cisco; hyperscalers the
1920s utilities and established railways; neoclouds the CLECs and long-haul
wholesalers; the labs the largest single customer in a chain, with the
qualification that WorldCom's fraud has no analog here and that one customer
tying several vendors' balance sheets together is new.

## The arithmetic

The four largest hyperscalers spent about $231B in 2024 and $381B in 2025 on
each company's own definition and period (Microsoft's fiscal years end in
June, so its figures are offset six months from the others), and 2026
guidance sums to $720-745B on a mixed basis (Amazon raised to ~$220B;
Microsoft's reported figure fell to ~$175B after a lease reclassification
with plans unchanged). Oracle's FY2026 capex was $55.7B and CoreWeave guides
$35-39B for 2026. These totals include ordinary cloud, CPUs and logistics,
not only AI.

The unit-economics note's model is a scenario, not a measurement: an assumed
$750B cohort, two-thirds short-lived compute at life L and one-third
buildings and power at a 15-year life, must repay itself pre-tax at a chosen
return out of owner-level EBITDA. At a six-year GPU life, 50% margin and 10%
cost of capital the cohort needs about $295B of incremental annual revenue;
at a three-year life, $468B.

| GPU life | Required annual revenue, $750B cohort (10%, 50% margin) |
|---|---|
| 3 years | $468B |
| 4 years | $381B |
| 5 years | $330B |
| 6 years | $295B |

Against that, the demand-side note's deduplicated estimate of end-user AI
product revenue is about $55B for 2025 and $170B for 2026 (range
$130-210B; an independent rebuild by payer gave $165B), with scenarios of
$210B, $480B and $800B for 2028. About half of the 2026 figure is the two
labs' reported revenue (C); the allocated remainder is D. It is a working
model, not a measured denominator, and the year exits at a run-rate near
$250B, so the bear path for 2027 is a contraction, not slow growth. Three outside estimates bracket the question: Gartner's
cumulative view (≥$8.5T of revenue needed through 2030 against ≤$3.6T
attributable to owners), IoT Analytics' modelled returns (above a 15%
hurdle now, below it in 2028, negative by 2031, an absorbable write-down),
and SemiAnalysis' operator path ($600-700B of combined OpenAI and Anthropic
revenue by December 2027, $50M of revenue per megawatt against $10-15M of
cost). They disagree by an order of magnitude because they measure different
things: cumulative versus annual, fleet versus inference megawatts, owner
capture versus end-user spend. The comparison is also not like for like: capex includes non-AI
assets, 2026 spending earns over later years, advertising gains and internal
savings pay for compute without a labelled AI dollar, and infrastructure
owners keep less than 100% of end-user spend wherever a lab sits between
them. What survives these caveats: the inputs that decide the answer are
cohort-level and undisclosed: GPU economic life (worth 1.6x on required
revenue), the owner's margin on AI revenue (1.7x between 50% and 30%),
utilisation, commissioning timing, residual values and the share of customer
spending that reaches the infrastructure owner. Market evidence on GPU life
cuts both ways: A100s from 2020 still rent (a listing median of $1.84/hr
mixing 40GB and 80GB variants; the OCPI transaction index is $0.94) and
one-year H100 contract rates rose through early 2026 while the composite
spot stayed flat near $2.80, and on one published benchmark (MiniMax M2.7
at 91 tokens per second per user, using hyperscaler ownership cost rather
than rents) a GB200 serves tokens at $0.19 per million against $0.42 on an
H100; at market rents that gap largely closes. Lab margins are one leaked
figure (OpenAI 33% adjusted gross, 2025, unverified) and one unaudited
"adjusted profit" (Anthropic, Q3 2026).

## Where we are

By the historical checklist the boom is in the financing-escalation stage:
capex has moved from cash flow to bonds, equity, SPVs and vendor credit. The
repricing of the weakest credits began in September (Oracle-tenanted Project
Jupiter loans were reported stressed on 18-19 September) and widened in the
week of 10-17 October (CoreWeave CDS above 1,000bp, project bonds reported from below 88 to about
94 cents, quote versions unresolved). The indicator-reversal stage (IPO window closing, vendor guidance
cuts, forward purchases renegotiated, sector index diverging from
incumbents) has begun in two places: policy (the Fed's September hike, whose
minutes link it partly to AI investment and partly to energy), and the
sector split in which neocloud equity and single-tenant project bonds fell
far more than the hyperscalers while hyperscaler bond spreads widened
earlier in 2026. Rates and oil set the backdrop (the 10-year reached 5.31% on 5 October, its
highest close since May 2002; Brent averaged $114 in September), but during
the week of 9-16 October itself the 10-year fell 15bp, real yields and hike
odds fell and physical Brent fell, while the AI basket dropped 12.7%,
high-yield spreads widened and the financing-sensitive names (Oracle,
CoreWeave, Vertiv) fell 16.5% against 10.5% for the chip names. That week's
repricing was AI-specific and ran through the credit channel. Whether a Blackwell-era
supply glut arrives in 2027 is a scenario, not an observation; the H100
monthly averages are flat, newer chips firmer, A100s softer, with a sharp
two-day H100 drop on 14-16 October inside a flat month.
