# How bubbles work, and where this one is

*Version 0.3, 2026-10-17 · Synthesis of
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
| Forward purchases | Oracle RPO $664B, Microsoft $678B, CoreWeave $104B, Broadcom $179B (company-wide); Nvidia supply commitments $279B; ASML says customers want to place 2029-30 orders | 2 |
| New buyers entering | Record Q2 2026 IPO proceeds ($104.8B) then a weak Q3; sovereigns, private credit and insurers entering GPU finance; household equity allocation reported at a record (grade C) | 1 |
| Tightening policy | Fed hiked in September 2026, first since 2023; 10-year touched 5.31% on 5 October, highest since 2002, then fell to 5.09% by 16 October; CPI 3.7% | 2 |

Twelve points of fourteen across seven indicators, with sentiment and
new-buyer entry the two partial readings; the fuller 13-row rubric in the
mechanics note sums to 20 of 26 and scores forward P/E and broad credit
stress at zero. In Kindleberger's sequence, soft sentiment with the financing
indicators lit is consistent with the late-euphoria / early profit-taking
boundary. It is also consistent with
a rational response to a productive technology; the checklist cannot tell
those apart, which is why the arithmetic below and the stack page matter
more than this table.

## What the precedents say

| Precedent | Financing | Drawdown | Recovery | Thesis right? |
|---|---|---|---|---|
| Railways 1845-50 | Retail equity | −55% to −80% | Decades (dividends) | Yes |
| Electrification / 1929 | Margin, holding-company debt | Dow −89% | 25 years | Yes |
| Telecom / fiber 1997-2002 | Junk bonds, vendor financing, loan trusts | Telecom index −84% | Never as a sector | Yes |
| Dot-com 1995-2002 | IPO equity | Nasdaq −78% | 15 years | Yes |
| Japan 1986-90 | Bank credit | Nikkei −82% | 34 years | No technology thesis |
| Housing 2003-09 | Securitised mortgages | S&P 500 −57%; house prices −27% | S&P ~5.5 years; house prices 10.5 years | No technology thesis |
| Crypto / SPAC 2020-22 | Retail equity | Bitcoin −77% | 2 years | Not demonstrated |

Three regularities, with their limits. Financing shapes the damage:
equity-funded booms gave deep equity losses with no banking crisis, credit-
funded booms gave bank and vendor losses and the longest recoveries, though
equity-funded recoveries were not fast (15 years for the Nasdaq). The
closest analog to today's circular deals is telecom vendor financing: in
September 2000 Lucent had $5.4B of undrawn and $1.3B of drawn customer
credit commitments, and in December 2000 Nortel $4.1B unfunded; these were
observed after the March 2000 equity peak, not before it. Nvidia's OpenAI
guarantee is a cap of $105B on conditional residual-value support phased
from 2028, a different instrument and an order of magnitude larger. Credit
spreads lagged the top in 1929, 2000 and 2007 (Baa-Aaa 1.32, 0.69 and 0.82
points), so today's 0.44 points and high-yield OAS of 3.2% are not evidence
of safety; they are also not evidence of a top. Seven busts give no
denominator of booms that did not bust.

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
product revenue is about $55B for 2025 and $180B for 2026 (range
$130-230B), with scenarios of $210B, $480B and $800B for 2028. The note
grades those allocations D: they are a working model, not a measured
denominator. The comparison is also not like for like: capex includes non-AI
assets, 2026 spending earns over later years, advertising gains and internal
savings pay for compute without a labelled AI dollar, and infrastructure
owners keep less than 100% of end-user spend wherever a lab sits between
them. What survives these caveats: the inputs that decide the answer are
cohort-level and undisclosed: GPU economic life (worth 1.6x on required
revenue), the owner's margin on AI revenue (1.7x between 50% and 30%),
utilisation, commissioning timing, residual values and the share of customer
spending that reaches the infrastructure owner. Market evidence on GPU life
cuts both ways: A100s from 2020 still rent (an aggregator quoted $1.84/hr
median; the pricing note found $1.79 on 2 October and could not reproduce
the earlier figure) and H100 contract rates rose through early 2026, while
on one published benchmark (MiniMax M2.7, FP8) a GB200 serves tokens at
$0.19 per million against $0.42 on an H100. Lab margins are one leaked
figure (OpenAI 33% adjusted gross, 2025, unverified) and one unaudited
"adjusted profit" (Anthropic, Q3 2026).

## Where we are

By the historical checklist the boom is in the financing-escalation stage:
capex has moved from cash flow to bonds, equity, SPVs and vendor credit. The
repricing of the weakest credits began in September (Oracle-tenanted Project
Jupiter loans were reported stressed on 18-19 September) and widened in the
week of 10-17 October (CoreWeave CDS above 1,000bp, project bonds at 88-94
cents). The indicator-reversal stage (IPO window closing, vendor guidance
cuts, forward purchases renegotiated, sector index diverging from
incumbents) has begun in two places: policy (the Fed's September hike and
its October minutes), and the sector split in which neocloud equity and
single-tenant project bonds fell far more than the hyperscalers while
hyperscaler bond spreads widened earlier in 2026. Whether a Blackwell-era
supply glut arrives in 2027 is a scenario, not an observation; the H100
monthly averages are flat, newer chips firmer, A100s softer, with a sharp
two-day H100 drop on 14-16 October inside a flat month.
