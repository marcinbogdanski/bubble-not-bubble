# Is AI a bubble? A live, evidence-backed assessment

*Version 0.2, 2026-10-17. Revised after an independent
[red-team review](/reviews/2026-10-17-codex-redteam-report) by Codex of
version 0.1; its findings and our changes are listed at the end. Memory,
Alphabet and GPU-pricing notes are still in progress. Built by AI agents from
primary sources, steered by a human. See [Methodology](/report/methodology).*

## The short answer

The question splits into three, and they have different answers.

**1. Does the market show bubble-stage dynamics? Yes.** Twelve of fourteen
on the Dalio checklist as we operationalise it: CAPE 40.6 (September) against
a 1999 peak of 44.2; margin debt $1.48T (record $1.50T in June); forward
purchases at records (Oracle RPO $664B, Microsoft $678B, Nvidia supply
commitments $279B); capex financing migrating from cash flow to bonds,
equity, SPVs and vendor credit; new classes of buyer; a central bank hiking
into 3.7% inflation. Sentiment is the only soft reading. This is a
resemblance test. It says the conditions past bubbles had are present, not
that the investment will fail. [Theory](/report/theory)

**2. Is capital being deployed faster than returns can service it? Not
established either way, and this is the question that matters.** Our
payback model is a scenario, not a measurement: a $750B cohort with
two-thirds short-lived compute needs about $295B of incremental annual
revenue at a six-year GPU life, 50% margin and 10% cost of capital, or $468B
at a three-year life. Against it, deduplicated end-user AI revenue is
estimated at about $180B for 2026 (range $130-230B, graded D by the note
that built it), and the two lab run-rates are reported and unverified
(OpenAI ~$50B net; Anthropic ~$65-67B gross). The comparison is not like for
like: capex includes ordinary cloud, revenue excludes advertising gains and
internal savings, and 2026 spending earns over later years. The two inputs
that would settle it, the economic life of a GPU and the margin on AI
revenue, are the two nothing public discloses. Demand is real and growing
fast; whether it is growing fast enough is open.

**3. Where is the fragility, and who bears it? Concentrated in the middle
of the stack, and partly repriced already.** Oracle (FY2026 free cash flow
−$23.7B, $125B of borrowings, BBB−, CDS near 300bp), CoreWeave (net
interest 25% of revenue, covenant relief in December 2025, CDS above
1,000bp), the other neoclouds (~$81B of listed debt, over $110B with private
facilities, against contracts concentrated in four counterparties) and the
labs (multi-year commitments many times revenue, financed partly by their
suppliers). From 2026 peaks to 16 October: Oracle −48%, CoreWeave −56%, SK
Hynix −56%, Vertiv −45%, Broadcom −32%; the Nasdaq-100 −6.5%. The equipment
makers, TSMC and Nvidia earn record margins and collect much of their cash
early, with the caveat that Nvidia's receivables, supply commitments and
guarantee are all growing. [Stack](/report/stack)

**Forecasts** (6 / 12 / 24 months, definitions in the
[register](/forecasts/register); price questions are measured from the
16 October close so none is already triggered):

| Event | 6m | 12m | 24m |
|---|---|---|---|
| Equal-weighted AI-infrastructure basket falls a further 40% | 12% | 25% | 38% |
| Oracle rated below investment grade | 12% | 28% | 42% |
| CoreWeave distressed credit event | 10% | 20% | 35% |
| OpenAI cancels or defers a commitment of $10B+ | 20% | 40% | 60% |
| A frontier lab down round | 10% | 20% | 35% |
| Hyperscaler 2027 capex guidance below 2026 | 7% | 7% | 7% |
| 2000-style unwind (basket event plus distress at two distinct obligors) | 8% | 18% | 30% |

## What we know

Verified against primary sources during the review.

- **Capex**: the four largest hyperscalers spent about $231B in 2024 and
  $381B in 2025 on their own definitions, and 2026 guidance sums to
  $720-745B (Amazon raised to ~$220B; Microsoft's reported figure fell to
  ~$175B after a lease reclassification with plans unchanged). Oracle's
  FY2026 capex was $55.7B; CoreWeave guides $35-39B.
- **Commitments are stocks, not flows**: Microsoft's $329B of signed leases
  not yet commenced (10-K, note 13) start between FY2027 and FY2033.
  Nvidia's $105B cap (8-K of 17 August 2026) is conditional residual-value
  support on OpenAI's Ohio leases, phased from 2028 and net of recoveries,
  not cash lent today. Neither falls due inside the forecast window.
- **Vendor financing is explicit and large**: Nvidia holds $99B of equity
  stakes, DSO rose from 45 to 60 days on terms up to a year, and management
  says labs it backs will be "roughly a quarter of our business next year".
  AMD pays OpenAI and Meta in warrants on 160M shares each. Amazon has put
  $50B into OpenAI ($28.7B by June plus $21.3B since) and $18B into Anthropic
  with a $15B facility remaining. Lucent and Nortel carried $4-7B each in
  2000.
- **Oracle**: RPO $664B with 13% due within a year (10-Q); OpenAI has
  confirmed a partnership above $300B over five years; Oracle does not
  disclose its share of RPO. FY2026 operating cash flow $32.0B less capex
  $55.7B. Q1 FY2027 operating cash flow included $11.4B of customer
  advances.
- **CoreWeave**: $35.6B of debt principal at June (10-Q), about $42B pro
  forma after September; Q2 net interest $640M on revenue $2.58B; first-half
  operating cash $3.7B against $14.1B of capex and $5.2B of principal
  repayments; $35.5B of leases not yet commenced.
- **Credit in the week of 10-17 October**: CoreWeave 5-year CDS
  1,038-1,195bp; its 2032 notes traded from 76 to about 81 cents (14.6%);
  Oracle CDS 282-300bp; Hyperion bonds ~92 cents, Project Excalibur below
  88. The 10-year Treasury yield fell during the week, from 5.24% to 5.09%,
  after touching 5.31% on 5 October.
- **Compute prices are not falling**: the Silicon Data H100 neo-cloud index
  was $2.83/hr on 16 October, up from about $1.86 in February 2025;
  on-demand H100 medians are flat to +18% year on year. The GPU-pricing note
  will fix the series; overcapacity is not visible in this market yet.

## What we do not know

- The economic life of a GPU under 2026 conditions. It moves required
  revenue by 1.6x. Burry's claim that Oracle's and Meta's earnings would be
  overstated by 21-27% in 2028 is a grade-D scenario we have not verified.
- The labs' real numbers: no audited accounts, run-rates on different bases
  (OpenAI net, Anthropic gross), undisclosed terms on every large commitment.
- Contract firmness: the deferral and termination rights in the Microsoft,
  Meta, OpenAI and Anthropic take-or-pay agreements that back the neocloud
  debt.
- Who ultimately holds the project bonds and GPU-backed loans (insurers,
  pensions, private-credit funds, bank warehouses) and at what marks.
- How much purchasing would disappear without supplier financing. The
  circular-financing map shows 51 links; it cannot show the counterfactual.

## What would change the answer

Toward "not a bubble": lab revenue growth sustained through 2027 on net
accounting; the H100 index holding through a Blackwell-era supply increase;
hyperscaler free cash flow recovering while capex still grows; OpenAI and
Anthropic publishing audited numbers that close the margin gap; custom
silicon delivering the 30-44% cost advantages claimed (grade C today).

Toward "bursting": a 2027 capex guidance cut by any hyperscaler; an OpenAI
commitment deferral; a GPU-backed loan default; the H100 index below $1.50;
a lab down round; Oracle cut to junk; the Fed continuing to hike.

## The bull case, stated fairly

- Cash cushions: Microsoft $67B of FCF and $77B of liquidity; Amazon $123B
  of liquidity; Meta $90B of cash and securities; dividends and buybacks are
  discretionary.
- Enterprise evidence beyond leaks: 30M paid Copilot seats; Census Bureau
  23.8% of businesses using AI; Anthropic reporting over 1,000 customers
  above $1M a year.
- Volume: Google's tokens processed rose from 9.7T to 3.2 quadrillion a
  month in two years; Azure grew 43%, Google Cloud 82%.
- AI can pay for itself inside existing products: Meta attributes ad gains
  to AI ranking, and internal cost savings need no labelled AI revenue.
- Suppliers are paid early, so losses concentrate where contracts fail, not
  across the whole chain.

## The bear case, stated fairly

- CoreWeave already needed covenant relief; its converts are far out of the
  money; five-year loans sit against three-year contracts.
- Oracle's operating cash flow is supported by customer advances; its lease
  commitments ($288B uncommenced) sit on top of $125B of debt.
- Meta's commitments ($279B uncommenced leases plus $68B in July) are far
  larger than its Hyperion headline.
- Anthropic reports roughly 80% of its obligations as non-cancellable while
  its customers can switch models.
- Demand quality: Ramp's sample shows flat token spending; consumer-app
  retention is weak; one reported failed raise (Poolside).
- Several names have already fallen 45-56% from their 2026 peaks; the
  repricing is not only a future possibility.

## Changes from version 0.1

The red-team found 36 errors or overstatements. The material ones: a
"$600-700B" middle-layer debt figure that mixed borrowers and scopes
(removed); "most of Oracle's RPO is OpenAI" (Oracle does not disclose it);
the $180B demand estimate presented as known (it is a grade-D scenario); the
checklist scored 13/14 (12/14 on the note's own scores); "$329B moved off
Microsoft's capex line" (it is a stock of future leases); Anthropic
commitments "ten times revenue" (seven to eight, over a decade); layer
forecasts that were already triggered by observed drawdowns (rebased to the
16 October close); the headline event allowing one restructuring to count
twice (now two distinct obligors). Vintage 0.1 probabilities are preserved
in the register's history.

Start points for agents: [llms.txt](/llms.txt), the raw markdown of every
page, and the [data](/data/) folder.
