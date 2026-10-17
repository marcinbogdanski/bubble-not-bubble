# Is AI a bubble? A live, evidence-backed assessment

*Version 0.5, 2026-10-18. Built by AI agents from primary sources, steered
by a human, on 26 research notes with graded claim tables, after two
three independent red-team reviews ([v0.1](/reviews/2026-10-17-codex-redteam-report),
[v0.2](/reviews/2026-10-17-codex-redteam-report-v02),
[v0.4](/reviews/2026-10-17-codex-redteam-report-v04)). Rules:
[Methodology](/report/methodology). Glossary at the end.*

## The short answer

The question splits into three.

**1. Are the signals that past bubbles showed present? Several are.** On
the report's own uncalibrated seven-indicator heuristic, 12 points of 14
(September 2026 readings): CAPE 40.6 against a 1999 peak of 44.2 (Shiller,
A); margin debt $1.48T (FINRA, A); record forward purchases (Oracle RPO
$664B, Microsoft $678B, Nvidia supply commitments $279B; filings, A); capex
financing moving from cash flow to bonds, equity, SPVs and vendor credit
(filings, A); a central bank hiking into 3.7% inflation (Fed, BLS, A).
Sentiment and new-buyer entry are partial. This is a resemblance test. It
does not establish that AI assets are overpriced, and the strongest
counter-argument is that the S&P 500 trades at a forward P/E of 19 because
earnings surged; the live question is whether those earnings are the bubble,
since GPU buyers' capex is suppliers' revenue. [Theory](/report/theory)

**2. Is capital being deployed faster than returns can service it? Not
established either way.** This is the question that matters, and public
disclosures do not settle it. Our payback model is a scenario (unit-economics
note, model arithmetic): a $750B cohort, two-thirds short-lived compute at a
six-year life and one-third buildings at 15 years, needs about $295B of
incremental annual pre-tax owner EBITDA-level revenue at 50% margin and 10%
cost of capital, or $468B at a three-year life. The best available demand
figure, about $180B of deduplicated end-user AI revenue in 2026 (range
$130-230B), is a grade-D working model, and the two are not like for like.
What is missing is cohort-level cash returns: GPU economic life, utilisation,
owner margins, residual values and the share of customer spending that
reaches the infrastructure owner. Demand is real and growing fast; whether
fast enough is open.

**3. Where is the fragility, and who bears it? Concentrated in the middle of
the stack, and partly repriced already.** The strongest-supported finding.
Oracle (FY2026 free cash flow −$23.7B, $125B of borrowings, BBB−), CoreWeave
(net interest 25% of revenue, covenant relief in December 2025, CDS above
1,000bp), the wider listed neocloud layer (about $81B of debt at June including
CoreWeave, on mixed bases; private facilities such as Nscale's add to it
but have not been reconciled) and the
frontier labs (multi-year commitments many times revenue, financed partly by
their suppliers). From 2026 peaks to 16 October: Oracle −48%, CoreWeave
−56%, SK Hynix −56%, Vertiv −45%; the Nasdaq-100 −6.5%. Losses would fall on
equity holders first everywhere; beyond that, who loses depends on each
borrower's collateral, guarantees and recoveries, not on a fixed order.
[Stack](/report/stack)

## The four facts that carry the answer

- **The incumbents still generate cash, with less margin than before.**
  Microsoft FCF $67B (FY to June 2026) with cash capex at 63% of operating
  cash flow; Alphabet TTM FCF $53B though Q2 2026 was −$5.9B; Amazon TTM FCF
  −$7.6B at June; Meta Q2 FCF $0.8B (10-K/10-Qs, A). Each holds tens of
  billions of liquidity; dividends and buybacks paid in FY2026 (Microsoft
  $48.7B) could be cut. S&P's 27 August 2026 forecast expects all six
  hyperscalers it rates to have negative free operating cash flow in 2026
  and 2027, recovering in 2029 (rating-agency report, B).
- **The hyperscalers are borrowing to build.** Amazon received $67B of
  long-term-debt proceeds in H1 2026 and issued $25B in July and £4.25B in
  September (10-Q and releases, A); Meta's full-year FCF is between −$17B
  and +$20B on two sensitivities (meta note, B); Alphabet's $195-205B 2026
  capex guidance exceeds its $186B of trailing operating cash flow (10-Q,
  A).
- **The intermediaries are cash-strained now, not hypothetically.** CoreWeave:
  H1 2026 operating cash $3.7B against $14.1B of equipment purchases and
  $5.2B of principal repayments; the 30 June schedule has $4.4B more
  principal due in the rest of 2026, $6.2B in 2027 and $4.4B in 2028 (10-Q,
  A). Oracle: Q1 FY2027 (to August) operating cash flow included $11.4B of
  customer advances with a financing component (10-Q, A).
- **Demand is growing fast.** Azure +43% (June quarter), Google Cloud +82%
  (Q2), 30M paid Copilot seats, and nearly 90% of FY2026 Microsoft Cloud
  revenue from customers other than frontier labs, so the labs are one
  concentrated channel rather than the whole market (filings and calls, A);
  Anthropic reporting $16.8B of Q3
  revenue at an 11% adjusted operating margin, OpenAI about $50B of net
  annualised revenue and 1.2B weekly users, against its own February
  forecast of $25B of 2026 cash burn (reported, unverified, C).
- **Investment returns are unknown.** No company discloses cohort-level
  returns on AI capacity. Depreciation lives are 5-6 years; rental evidence
  on old chips cuts both ways (A100s still rent, but at about a third of H100
  rates; Blackwell cuts cost per token by more than half on the one benchmark
  we have). Lab margins rest on one leaked figure (OpenAI 33% adjusted gross,
  2025) and one unaudited "adjusted profit" (Anthropic, Q3 2026).

## Forecasts

Definitions and the full set of 18 questions plus layer estimates are in the
[register](/forecasts/register). Exact labels; 6 / 12 / 24 months.

| Event | 6m | 12m | 24m |
|---|---|---|---|
| M1: equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT closes at or below 60 (indexed to 100 at the 16 October close) | 12% | 25% | 38% |
| F2: Oracle rated below investment grade by any major agency | 12% | 28% | 42% |
| F1: CoreWeave distressed credit event, or an acquisition closing below $40 a share | 15% | 25% | 38% |
| F3: OpenAI cancels, cuts, or defers by a year or more, a binding compute commitment, by $10B+ | 15% | 32% | 52% |
| Headline: M1 plus distressed credit events at two distinct corporate or sponsor groups (one severe unwind, not every bad outcome) | 6% | 13% | 20% |

## What we do not know, and what would tell us

| Unknown | The observable test |
|---|---|
| Economic life of a GPU under 2026 conditions (1.6x on required revenue) | H100 monthly index (P1) through a Blackwell-era supply increase; used-H100 prices; depreciation-policy changes |
| The labs' real numbers: no audited accounts, different bases (OpenAI net, Anthropic gross), undisclosed commitment terms | An S-1 on EDGAR; same-basis run-rates at two dates (D1, D2); a lab down round (F5) |
| Firmness of the take-or-pay contracts behind neocloud debt | A disclosed deferral or cancellation (F3); CoreWeave principal schedule met from operations; renewal pricing on 2027 expiries |
| Who holds the project bonds and GPU-backed loans, and at what marks | A $1B+ project or SPV distress (F4); dealer marks moving from the current below-88-to-94 cents range |
| How much purchasing would disappear without supplier financing (51 mapped links) | Guarantee readiness dates (Nvidia Ohio from 2028); warrant vesting; backstop purchases |
| Whether the hyperscalers cut (C1, C2) or keep building | First calendar-2027 capex guidance with Q4 2026 results |

## The bull case, stated fairly

- Cash cushions: Microsoft $77B of liquidity, Amazon $123B, Meta $90B,
  Alphabet $155B excluding equity stakes; dividends and buybacks are
  discretionary.
- Breadth: nearly 90% of Microsoft Cloud revenue is from customers other
  than frontier labs; the Census Bureau's business survey showed 19.8% of
  employer businesses using AI in May 2026 (a later 23.8% reading is
  unreproduced); Anthropic reports over 1,000 customers above $1M a year.
- Volume: Google's tokens processed rose from 9.7T to 3.2 quadrillion a
  month in two years across all surfaces.
- AI pays for itself inside existing products: Meta attributes ad gains to
  AI ranking; internal savings need no labelled AI revenue.
- Suppliers collect early: equipment deposits, TSMC's cash flow, Nvidia's
  $127B of trailing FCF. CoreWeave's management reports initial-term
  returns and A100/H200 renewals (company claims, not audited).

## The bear case, stated fairly

- CoreWeave needed covenant relief on its DDTL 3.0 facility; its converts are
  far out of the money; DDTL 5.5 lends five years against contracts averaging
  three; its unsecured issuance window is effectively shut at 14-16% yields.
- Oracle's operating cash flow is supported by customer advances; $44B of
  lease liabilities and $288B of uncommenced leases sit on top of $125B of
  debt.
- Meta's $279B of uncommenced leases plus $68B signed in July overlap with,
  and dwarf, the $46B Hyperion headline.
- Anthropic reports roughly 80% of its obligations as non-cancellable while
  its customers can switch models.
- Demand quality: Ramp's sample shows flat token spending; consumer-app
  retention is weak; one reported failed raise (Poolside).
- Several names have already fallen 45-56% from their 2026 peaks.

## Glossary

RPO: remaining performance obligations, contracted revenue not yet
recognised. FCF: free cash flow, operating cash flow less capital
expenditure. CDS: credit default swap; the annual cost in basis points
(bp, hundredths of a percent) of insuring debt. DSO: days sales
outstanding, how long customers take to pay. DDTL: delayed-draw term loan.
SPV: special-purpose vehicle. CAPE: cyclically adjusted price/earnings
ratio.

## Status

All 26 research notes have been cross-checked by a second model (Codex
gpt-6-astra, fresh context) against primary sources and corrected; every
note's status is "reviewed" and its header names the reviewer. Claude-side
reviews of the Codex-written notes are the next step. No paywalled sources were used, so
private-company figures are reported and unverified and graded as such. The
lead agent is an Anthropic model; Anthropic's note was written by Codex.
Version history and every change are in the
[register](/forecasts/register) and the [reviews](/reviews/2026-10-17-codex-redteam-report-v02).
Start points for agents: [llms.txt](/llms.txt), raw markdown of every page,
the [data](/data/) folder.
