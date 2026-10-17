# The stack, layer by layer

*Last updated: 2026-10-17 · Synthesis of the research notes; every figure
below is sourced and graded in the note it links to. Memory, Alphabet, GPU
pricing and power notes are still in progress and are marked as such.*

## One table

"Impairment" means a 40%+ equity drawdown from the 2026 peak or a loss to
creditors. Probabilities are in the [forecast register](/forecasts/register).

| Layer | Profitable now? | How the build is financed | Where it is overextended | Who loses first | First signal |
|---|---|---|---|---|---|
| Equipment (ASML, AMAT, Lam, KLA, TEL) | Yes, the most profitable layer: ASML 44% operating margin | Customer prepayments and own cash; net cash balance sheets | Valuation (ASML ~42x) prices a 2027-28 order book that a few customers placed with down payments | Shareholders; no solvency risk | Contract liabilities, KLA/AMAT backlog, customer capex guides (ASML stopped reporting bookings) |
| Foundry (TSMC) | Yes: 66% gross, 59% operating margin | Operating cash flow; capex $60-64B fully covered | Leading-edge and CoWoS capacity arriving after today's backlog ships; AI accelerators are only high-teens % of revenue | Shareholders via utilisation; Taiwan is a separate tail | Monthly revenue, capex revisions, utilisation commentary |
| Memory and HBM | *Note pending* | | Nvidia's $279B supply commitments are mostly memory; the most cyclical layer historically | | Contract DRAM prices, capex revisions |
| Accelerators (Nvidia, AMD, Broadcom) | Yes: Nvidia 75% gross margin, $127B trailing FCF; Broadcom 46% FCF margin | Own cash, but now also vendor financing: Nvidia's $105B OpenAI lease guarantee, $99B of equity stakes, DSO 45 to 60 days; AMD pays OpenAI and Meta in 160M-share warrants | A quarter to a third of demand comes from loss-making labs and debt-financed neoclouds; Broadcom's $179B RPO rests on six customers | Shareholders through multiple compression; vendors through guarantees if a lab fails | DSO, supply commitments, customer concentration, guarantee triggers |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | Yes, in their core businesses | Operating cash flow, increasingly plus bonds and equity: Microsoft capex 63% of OCF; Amazon trailing FCF negative; Meta Q2 FCF $0.8B; Alphabet $49.6B equity raise | Off-balance-sheet build (Microsoft $329B of uncommenced leases; Meta's Hyperion SPV with residual guarantee) and OpenAI concentration (~41% of Microsoft RPO) | Shareholders via earnings when depreciation and lease costs land; creditors are safe | Capex guidance, FCF, lease commitments, equity-method losses on labs |
| Oracle | Software yes; the build no: FCF −$23.7B in FY2026 | $125B of borrowings, a $20B equity sale, customer advances, $38B of project loans | RPO $664B, over $300B of it OpenAI, booked before power, customer liquidity or margins are secured; rated BBB− | Shareholders, then unsecured bondholders and project lenders | CDS (288bp), rating actions, RPO revisions, FCF |
| Neoclouds (CoreWeave and others) | No on a GAAP basis: CoreWeave interest is 25% of revenue | ~$100B+ of layer debt against take-or-pay contracts with four counterparties; needs $35B+ a year of fresh capital at CoreWeave alone | Six-year depreciation against three-to-five-year contracts; refinancing at 15-16% unsecured yields | Equity, then unsecured notes, then SPV lenders (Blackstone, Magnetar, banks), then Nvidia via its $6.3B backstop | CDS (>1,000bp), bond prices, GPU rental index at 2027-29 renewals |
| Frontier labs (OpenAI, Anthropic, xAI) | No: OpenAI reported 33% gross margin; Anthropic reports adjusted profit, unaudited | Investor and supplier equity, now also debt (xAI $13.3B, Anthropic's proposed $60B North Star at >10% junior coupon) | Over $1T of OpenAI commitments and $518B of Anthropic commitments against ~$50B and ~$65-74B run-rates | Investors (SoftBank, Microsoft, Amazon, Nvidia), then suppliers holding guarantees and RPO | Run-rate reports, funding rounds, contract deferrals, S-1 filings |
| Neolabs and applications | Mostly no | Venture and strategic equity at high multiples | $31B+ raised by labs with little revenue; app margins thin and variable | Venture investors; then GPU demand for training | Down rounds, shutdowns, acqui-hires |
| Power and datacenter real estate | *Note pending* | Project bonds and private credit; single-tenant bonds already trade at 87-93 cents | | Project bondholders and developers | Project-bond prices, pre-leasing, turbine backlogs |

## The shape of it

The stack is profitable at both ends and leveraged in the middle. Equipment,
foundry and Nvidia earn record margins today and are paid first, partly in
advance. The hyperscalers are still funding most of their build from
operations, but each has crossed a line in 2026 that it had not crossed
before: Amazon's trailing free cash flow turned negative, Meta's fell to
under $1B in a quarter, Alphabet sold $49.6B of equity, and Microsoft moved
$329B of future datacenter leases off its capex line. Oracle and the
neoclouds are the layer where the debt actually sits, and they are the layer
whose credit repriced in the week of 10-17 October.

Below them, the labs are the demand that everything above is built for. They
are growing very fast on reported numbers, with no audited accounts, with
gross margins that do not fund frontier research, and with commitments that
exceed their revenue by a factor of ten or more. A single counterparty,
OpenAI, sits behind Nvidia's guarantee, AMD's warrants, Amazon's $50B
investment, Microsoft's largest RPO line and most of Oracle's backlog. The
[circular-financing note](/research/macro/circular-financing) draws the
graph; the [precedents note](/research/theory/historical-precedents)
observes that in 2000 no single customer tied three vendors' balance sheets
together.

## Layer notes

- **Equipment**: [semiconductor-equipment](/research/stack/semiconductor-equipment).
  ASML guides 2026 sales of €44-45B (+36%), says 2027-28 capacity "will not
  fully meet" demand, and holds ~€10B net cash. In 2001 its sales fell 40%
  and gross margin went to 2%. The layer would survive a cut; its share
  prices would not.
- **Foundry**: [tsmc-and-foundry](/research/stack/tsmc-and-foundry). Q3
  2026 revenue $46.7B (+41% in USD), capex guided $60-64B against far larger
  operating cash flow. HPC is 68% of revenue, but AI accelerators were
  high-teens percent in the last full year.
- **Accelerators**: [nvidia](/research/stack/nvidia),
  [amd-broadcom-custom-silicon](/research/stack/amd-broadcom-custom-silicon).
  Nvidia's management says labs backed by its balance sheet will be "roughly
  a quarter of our business next year" and guides gross margin down to
  71-73%. AMD's two largest deals are 6 GW each and paid for partly in
  warrants worth up to ~$96B per customer at the top hurdle. Broadcom expects
  Anthropic to be its largest custom-silicon customer in 2027.
- **Hyperscalers**: [microsoft](/research/stack/microsoft),
  [amazon](/research/stack/amazon), [meta](/research/stack/meta), Alphabet
  pending. Combined 2026 capex guidance is roughly $730B, up from $381B in
  2025 and $231B in 2024.
- **Oracle**: [oracle](/research/stack/oracle). The only large builder
  that cannot fund its build from operations, and the one most dependent on
  one customer.
- **Neoclouds**: [coreweave](/research/stack/coreweave),
  [neoclouds-other](/research/stack/neoclouds-other). Pricing shows no
  stress yet (H100 on-demand medians flat to up year on year; Nebius says it
  could sell all 2027 capacity today). Credit does: CoreWeave's 2032 notes
  trade near 78 cents.
- **Labs**: [openai](/research/stack/openai), [anthropic](/research/stack/anthropic),
  [labs-other](/research/stack/labs-other).
- **Cross-cutting**: [debt-markets](/research/macro/debt-markets) (about
  $572B of identified AI-related principal, a $723B gross financing
  perimeter, tight aggregate spreads with selective stress),
  [demand-side](/research/macro/demand-side) (deduplicated AI product
  revenue ~$55B in 2025 and ~$180B in 2026; base case $480B in 2028),
  [china](/research/macro/china).
