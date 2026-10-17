# How bubbles work, and where this one is

*Last updated: 2026-10-17 · Synthesis of
[bubble-mechanics](/research/theory/bubble-mechanics),
[historical-precedents](/research/theory/historical-precedents) and
[ai-unit-economics](/research/theory/ai-unit-economics).*

## The mechanism

Four frameworks describe one machine. Minsky: stability breeds fragility as
borrowers drift from hedge finance (cash flow covers debt service) to
speculative (covers interest only) to Ponzi (needs new money to pay
interest). Kindleberger: displacement, boom, euphoria, profit-taking, panic,
with credit as the fuel. Perez: every technological revolution has an
installation phase ending in a frenzy and a crash, after which the
infrastructure is cheap enough to be used in a deployment phase. Dalio: a
bubble is a price level that discounts unsustainable conditions, and it is
pricked by rising rates and a flood of new issuance.

The distinction that matters for this project: a technology can be real and
the capital that builds it can still be lost. That is the normal case. In six
of the seven precedents the technology thesis was right and build-phase
investors lost most of their money. The overbuilt assets were used, by second
owners who bought them out of bankruptcy, three to ten years later.

## The checklist, October 2026

Dalio's six questions, operationalised with current readings. Scores from
the mechanics note's rubric (0 absent, 1 partial, 2 present).

| Indicator | Reading | Score |
|---|---|---|
| Prices high relative to traditional measures | Shiller CAPE 40.6 against a 1999 peak of 44.2 and a mean of 17.8; Fed says equity premium "well below its historical average" | 2 |
| Prices discounting rapid future appreciation | Forward P/E of 19 looks normal only because consensus has 2026 EPS growing 33%; AI-linked guidance assumes 2027-28 deployments that require labs to raise capital at an undemonstrated scale | 2 |
| Broad bullish sentiment | AAII bears outnumber bulls; fund managers' top tail risk is bond yields. The one soft reading | 1 |
| Purchases financed by leverage | FINRA margin debt at a record $1.50T; hyperscalers issuing bonds and equity; ~$100B of neocloud debt; Oracle $125B of borrowings | 2 |
| Forward purchases | Oracle RPO $664B, Microsoft $678B, CoreWeave $104B, Broadcom $179B; Nvidia supply commitments $279B; ASML customers ordering for 2029-30 | 2 |
| New buyers entering | Record Q2 2026 IPO proceeds ($104.8B); sovereigns, private credit and insurers entering GPU finance; retail equity allocation at a record 46% of financial assets | 2 |
| Tightening policy | Fed hiked in September 2026, first since 2023, with a possible second hike in October; 10-year at 5.1-5.3%, highest since 2002; CPI 3.7% | 2 |

Thirteen of fourteen on this cut. The mechanics note scores 19 of 26 on its
fuller rubric. In Kindleberger's sequence, soft sentiment with every other
indicator lit is the late-euphoria / early profit-taking boundary.

## What the precedents say

| Precedent | Financing | Drawdown | Recovery | Thesis right? |
|---|---|---|---|---|
| Railways 1845-50 | Retail equity | −55% to −80% | Decades (dividends) | Yes |
| Electrification / 1929 | Margin, holding-company debt | Dow −89% | 25 years | Yes |
| Telecom / fiber 1997-2002 | Junk bonds, vendor financing, loan trusts | Telecom index −84% | Never as a sector | Yes |
| Dot-com 1995-2002 | IPO equity | Nasdaq −78% | 15 years | Yes |
| Japan 1986-90 | Bank credit | Nikkei −82% | 34 years | n/a |
| Housing 2003-09 | Securitised mortgages | S&P −57% | 10 years | n/a |
| Crypto / SPAC 2020-22 | Retail equity | Bitcoin −77% | 2 years | Not shown |

Three regularities. Financing decides the damage: equity-funded booms gave
deep equity losses and fast recoveries, credit-funded booms gave banking
losses and decade-long recoveries. The closest analog to today's circular
deals is telecom vendor financing, where Lucent and Nortel carried about $5B
each of customer credit commitments before the top; Nvidia's OpenAI guarantee
alone is capped at $105B. And credit spreads lagged the top in 1929, 2000 and
2007, so today's tight aggregate spreads (Baa-Aaa 0.44pp, high-yield OAS
3.2%) are not evidence of safety.

Which layer matches which precedent: equipment is the railway contractors
(sharp, short, no balance-sheet damage); foundry is the incumbent carriers
(safest asset in the stack); GPU vendors are Lucent, Nortel and Cisco;
hyperscalers are the 1920s utilities and established railways; neoclouds are
the CLECs and long-haul wholesalers; the labs are WorldCom plus the dot-coms,
except that this time one customer ties several vendors' balance sheets
together.

## The arithmetic

The four largest hyperscalers spent $231B in 2024, $381B in 2025 and have
guided about $730B for 2026; Oracle and CoreWeave add $100B or more. The
unit-economics note's model: two-thirds of a cohort is short-lived compute,
one-third is buildings and power; at a six-year GPU life, 50% EBITDA margin
and 10% cost of capital, the 2026 cohort alone needs about $295B of
incremental annual revenue. At a three-year life it needs $468B. The 2024-26
cohorts together need $535-850B.

| GPU life | Required annual revenue, 2026 cohort (10%, 50% margin) |
|---|---|
| 3 years | $468B |
| 4 years | $381B |
| 5 years | $330B |
| 6 years | $295B |

Against that, deduplicated end-user AI product revenue is about $180B in 2026
(demand-side note, range $130-230B), with the base case reaching $480B in
2028. Lab run-rates are higher but unaudited and partly gross of partner
sales. The gap is narrowing fast and is still a gap, and the margin that
infrastructure owners keep of that revenue is lower than 50% wherever a lab
sits in between (OpenAI's reported gross margin is 33%).

The two parameters that matter most are the economic life of a GPU (worth
1.6x on required revenue between six and three years) and the margin on AI
revenue (1.7x between 50% and 30%). Cost of capital matters far less. The
market evidence on GPU life currently cuts both ways: A100s from 2020 still
rent at $1.84/hr and H100 contract rates rose through early 2026, but
Blackwell serves tokens at under half of Hopper's cost.

## Where we are

By the historical checklist the boom is in the financing-escalation stage:
capex has moved from cash flow to bonds, equity, SPVs and vendor credit, and
the week of 10-17 October 2026 produced the first credit repricing in the
weakest layer. The indicator-reversal stage (IPO window closing, vendor
guidance cuts, sector index diverging from incumbents, forward purchases
being renegotiated) has started only in one place: neocloud equity and
single-tenant project bonds fell far more than the hyperscalers that week.
Dalio's two pins, rising rates and a flood of issuance, are both present.
