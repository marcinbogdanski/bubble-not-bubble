# Is AI a bubble? A live, evidence-backed assessment

*Version 0.7a, 2026-10-18. Built by AI agents from primary sources, steered
by a human, on 26 research notes with graded claim tables, after three
Codex red-team reviews and a first
[Claude review](/reviews/2026-10-18-claude-opus-review) (the lead and that
reviewer share a vendor; its Anthropic findings and arithmetic were then
[checked by Codex](/reviews/2026-10-18-codex-check-v07)). Rules: [Methodology](/report/methodology). Glossary at the end.*

## The short answer

The question splits into three.

**1. Are the signals that past bubbles showed present? Several are, and the
financing ones are AI-specific.** On the report's own uncalibrated
seven-indicator heuristic, 12 points of 14: record forward purchases (Oracle
RPO $664B, Microsoft $678B, Nvidia supply commitments $279B; filings, A);
capex financing moving from cash flow to bonds, equity, SPVs and vendor
credit, with the four hyperscalers spending 96% of operating cash flow on
cash capex in Q2 2026 (filings, A); a Fed that hiked in September and whose
minutes say AI-related investment is itself "contributing to inflation
pressures", alongside an energy shock (Brent averaged $114 in September; Fed
and EIA, A). CAPE at 40.6 and margin debt at $1.48T (A) are market-wide rather than
AI-specific; the forward-P/E objection is taken up in
[theory](/report/theory). This is a resemblance test: it does not establish
that AI assets are overpriced.

**2. Is capital being deployed faster than returns can service it?
Unproven; an illustrative payback scenario sets a high bar.** Our model
(two-thirds equipment at a six-year life, one-third buildings at 15 years,
50% owner EBITDA margin, 10% discount rate; unit-economics note) says a $750B
cohort needs about $295B of annual owner revenue while it operates, $468B at
a three-year life. Applied to a 60-100% AI share of Goldman's $3.4T
hyperscaler-capex forecast for 2026-28, the 2026-28 cohorts need $0.8-1.3T a
year of owner revenue once they all operate; at 50% end-user-to-owner
capture that is $1.6-2.7T of annual end-user AI revenue, against a grade-D
estimate of about $180B in 2026. Reaching it by 2029-30 would take growth of
roughly 70-150% a year (arithmetic reproducible, B; inputs and sector
application D). It roughly tripled in 2026; our own base path assumes +67%
then +60%. The scenario omits replacement capex that preserves existing
revenue, advertising and internal-savings benefits, commissioning timing and
residual values, any of which could move it; cohort-level returns, GPU
economic life and owner margins remain undisclosed. Capex cuts (C1, C2
below) are the self-correcting path, and none is expected near term.

**3. Where is the fragility, and who bears it? Failure risk sits in the
middle of the stack; most of the dollars at risk sit at the top.** Likeliest
to fail: Oracle (FY2026 free cash flow −$23.7B, $125B of borrowings, BBB− at
S&P since July; filings and rating action, A), CoreWeave (net interest 25% of
Q2 revenue, $5.2B of H1 principal repaid against $3.7B of operating cash,
DDTL 3.0 covenant relief in December 2025, 5-year CDS above 1,000bp on 15
October; 10-Q A, CDS B), the other listed neoclouds (about $81B of debt in
the layer including CoreWeave, on mixed bases) and the frontier labs, OpenAI
and Anthropic alike (Reuters reports at least $518B of Anthropic commitments
over a decade, about 80% non-cancellable or payable regardless of use,
reported C; Broadcom's filed $29B maximum backstop protects a financing
partner and gives Anthropic no liquidity). Equity has repriced: the weakest names are down 45-56% from 2026 peaks,
the Nasdaq-100 6.5%, though some of that is a rates and oil move, not AI
information. Credit has only begun to: CoreWeave's unsecured notes yield
14-16% and no AI-related debt has yet defaulted. If returns disappoint
without defaults, the largest losses land elsewhere: on equity in Nvidia and
the hyperscalers (the top ten are 40.6% of the S&P 500) and on the $330B of
AI-related investment-grade bonds issued in 2026 at 16-17-year maturities
against 5-6-year chips (Kansas City Fed, A). [Stack](/report/stack)

## The four facts that carry the answer

- **The incumbents generate cash but are now borrowing to build.** Microsoft
  FCF $67B (FY to June 2026) with cash capex at 63% of operating cash flow;
  Alphabet TTM FCF $53B though Q2 was −$5.9B; Amazon TTM FCF −$7.6B after
  $67B of long-term-debt proceeds in H1 and $25B more in July; Meta Q2 FCF
  $0.8B (10-K/10-Qs, A). S&P's 27 August forecast expects negative free
  operating cash flow at all six hyperscalers it rates in 2026 and 2027
  (rating-agency release, A for the stated forecast).
- **The intermediaries are cash-strained now.** CoreWeave's 30 June schedule
  has $4.4B more principal due in the rest of 2026, $6.2B in 2027 and $4.4B
  in 2028 (10-Q, A), its unsecured issuance window is effectively shut, and
  its CEO and CFO concluded its disclosure controls were not effective at 30
  June 2026 because of material weaknesses (10-Q, A), which qualifies every
  management claim about returns and renewals. Oracle's Q1 FY2027 operating
  cash flow included $11.4B of customer advances (10-Q, A).
- **Demand is growing fast and is broad, while backlog is concentrated.**
  Azure +43%, Google Cloud +82%, 30M paid Copilot seats; nearly 90% of
  Microsoft's FY2026 Cloud revenue came from customers other than frontier
  labs, yet OpenAI was about 45% of its December 2025 commercial RPO
  (filings and calls, A). Anthropic's reported $16.8B of Q3 revenue at an 11%
  adjusted operating margin is unaudited, and adjusted profit is not cash
  flow; OpenAI's roughly $50B of net annualised revenue and its February
  forecast of $25B of 2026 cash burn are on different bases and dates. None
  of these ranks the two on cash generation (reported, unverified, C).
- **Investment returns are unknown.** No company discloses cohort-level
  returns on AI capacity. Depreciation lives are 5-6 years; A100s still
  rent at about a third of H100 rates; one benchmark has a GB200 serving
  tokens at under half an H100's cost (A/C).

## Forecasts

Definitions, rules and the full set of 20 questions, 10 layer estimates and
two headline events are in the [register](/forecasts/register); 6 / 12 / 24
months from 17 October 2026.

| Event | 6m | 12m | 24m |
|---|---|---|---|
| M1: equal-weighted basket of NVDA, AVGO, TSM, ORCL, CRWV, AMD, MU, VRT falls 40% from its 16 October level | 10% | 22% | 30% |
| M1a: the five chip names alone fall 40% | 6% | 14% | 25% |
| M1b: ORCL, CRWV, VRT alone fall 40% | 20% | 35% | 50% |
| F1: CoreWeave distressed credit event, or an acquisition closing below $40 a share | 8% | 20% | 35% |
| F2: Oracle rated below investment grade by any major agency | 12% | 28% | 42% |
| F3: OpenAI cancels, cuts, or defers by a year or more, a binding compute commitment of $10B+ | 15% | 32% | 52% |
| F3b: the same for Anthropic | 10% | 22% | 38% |
| Credit-led unwind: M1 plus distressed credit events at two distinct obligor groups | 3% | 9% | 16% |
| Equity-led unwind: M1 with at most one such event (the 2000 pattern) | 7% | 13% | 14% |

Nearest markets ([sources](/signals/2026-10-18-market-views)): Polymarket's
"AI bubble burst" (three of six triggers from all-time highs) shows 6.9% by
end-2026 and 16.5% by June 2027, closest to M1a; CoreWeave's CDS implies
8-10% default at 6 months and 28-33% at 2 years (risk-neutral), bracketing
F1; Goldman's capex path is consistent with C1. No market prices an Oracle
downgrade or a lab commitment cut.

## Strongest arguments each way

| Topic | Bull (source, grade) | Bear (source, grade) |
|---|---|---|
| Valuation | S&P technology ~21x earnings vs 70x in 2000; semiconductor earnings +178% y/y (Timmer, B) | GPU buyers' capex is suppliers' revenue, so the E can be the bubble while the P/E looks ordinary (Druckenmiller via FT, B) |
| Demand path | SemiAnalysis: OpenAI plus Anthropic revenue $600-700B by December 2027; up to $50M revenue per MW against $10-15M of cost (estimate, C) | Gartner: $8.5T of cumulative revenue needed through 2030 for a 12% return, at most $3.6T attributable to owners (B) |
| Supply | TSMC and ASML say demand exceeds planned supply through 2028; B200 rents +15% in 30 days to $8.12 (A/B) | Nvidia guides its own gross margin down to 71-73%; by 2028 the H100 is 5.5 years old (A) |
| Credit | Liquidity: Microsoft $77B, Amazon $123B, Meta $90B, Alphabet $155B; buybacks could be cut (A) | IMF: ~$300B of hyperscaler equity and ~$650B of debt into AI firms that committed ~$1.4T back to their backers, "wrong-way risk"; AI is 10% of 2026 IG issuance (A) |
| Demand quality | Census: 19.8% of employer businesses using AI (May 2026, A); Anthropic >1,000 customers above $1M a year (C) | Anthropic token use +90% July to September, spending +19% (Ramp, B); Barclays: enterprise hardware strength is memory prices, AI ~5% of IT budgets (B) |
| Intermediaries | CoreWeave management reports initial-term recovery and renewals; Nebius 49.7% AI-cloud EBITDA margin (company claims, C) | CoreWeave controls not effective; converts far out of the money; DDTL 5.5 lends five years against three-year contracts; project bonds at below 88 to 94 cents (A/C) |

## What we do not know, and what would tell us

| Unknown | The observable test |
|---|---|
| Economic life of a GPU under 2026 conditions (1.6x on required revenue) | H100 monthly index (P1, an age test by 2028); used-H100 prices; depreciation-policy changes |
| The labs' real numbers: no audited accounts, different bases (OpenAI net, Anthropic gross), undisclosed commitment terms | An S-1 on EDGAR; same-basis run-rates at two dates (D1, D2); a lab down round (F5) |
| Firmness of the take-or-pay contracts behind neocloud and lab debt | A disclosed deferral or cancellation (F3, F3b); CoreWeave's principal schedule met from operations; any cure or amendment after DDTL 3.0's unlimited equity-cure window closes on 28 October 2026 |
| Who holds the project bonds and GPU-backed loans, and at what marks | A $1B+ project or SPV distress (F4); dealer marks moving from the current below-88-to-94 cents range |
| How much purchasing would disappear without supplier financing (51 mapped links) | Guarantee readiness dates (Nvidia Ohio from 2028); warrant vesting; backstop purchases |
| Whether the hyperscalers cut (C1, C2) or keep building | First calendar-2027 capex guidance with Q4 2026 results |
| How much of the October repricing was AI information versus rates and oil | Spreads of AI names against the index as the 10-year and Brent move |

## Glossary

RPO: contracted revenue not yet recognised. FCF: operating cash flow less
capex. CDS: cost in basis points (bp, 0.01%) of insuring debt. DDTL:
delayed-draw term loan. SPV: special-purpose vehicle. CAPE: cyclically
adjusted P/E. IG: investment grade.

## Status

All 26 research notes were cross-checked by a second model against primary
sources and corrected; the reviews of this page are under reviews and every
change is logged in the register's history. No paywalled sources were used,
which biases the evidence toward leaked lab figures and away from sell-side
and rating-agency credit work. Agents start at [llms.txt](/llms.txt).
