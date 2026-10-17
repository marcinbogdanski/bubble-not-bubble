# The stack, layer by layer

*Version 0.2, 2026-10-17 · Synthesis of the research notes, corrected after
the [red-team review](/reviews/2026-10-17-codex-redteam-report). Every
figure is sourced and graded in the note it links to. All 25 notes are
present; four have had cross-check corrections applied.*

## One table

"Impairment" is defined in the [forecast register](/forecasts/register):
a further 40% equity decline from the 16 October close for any named
constituent, or a distressed credit event.

| Layer | Profitable now? | How the build is financed | Where it is overextended | Who loses first | First signal |
|---|---|---|---|---|---|
| Equipment (ASML, AMAT, Lam, KLA, TEL) | Yes: ASML 44% operating margin, KLA ~61% gross; all generate FCF above capex | Customer prepayments and own cash; net cash at ASML, AMAT, Lam; modest net debt at KLA | Valuation (ASML ~42x) prices a 2027-28 order book placed by a few customers; China is 20-34% of sales under a live export-control threat | Shareholders; solvency risk low given cash and prepayments | Contract liabilities, KLA/AMAT backlog, customer capex guides (ASML stopped reporting bookings) |
| Foundry (TSMC) | Yes: 66% gross, 59% operating margin, the highest in the stack | Operating cash flow; capex $60-64B fully covered | New leading-edge and CoWoS capacity arriving after today's backlog ships; AI accelerators were high-teens % of revenue in the last full year | Shareholders via utilisation; Taiwan is a separate tail | Monthly revenue, capex revisions, utilisation commentary |
| Memory and HBM | Yes, scarcity margins: Micron 87% gross / 81% operating; SK Hynix 76% operating | Cash generation, public equity and subsidies; longer HBM agreements shift some risk to customers | Through-cycle returns after prices normalise; staggered 2027-28 capacity additions could coincide with yield gains and customer retrenchment; SK Hynix already −56% from its 2026 peak | Shareholders; the layer has little debt | Fixed DDR5 contract series (P2), HBM share estimates, capex revisions |
| Accelerators (Nvidia, AMD, Broadcom) | Yes: Nvidia 75% gross margin, $127B trailing FCF; Broadcom 46% FCF margin | Own cash, plus vendor financing: Nvidia's conditional guarantee capped at $105B on OpenAI leases (phased from 2028), $99B of equity stakes, receivables $63B with DSO at 60 days; AMD's warrants to OpenAI and Meta (160M shares each) | Management says labs backed by Nvidia's balance sheet will be "roughly a quarter of our business next year"; Broadcom has six custom-silicon customers with Anthropic and OpenAI the largest; Broadcom's $179B RPO is company-wide, its allocation undisclosed; AVGO already −32% from peak | Shareholders through multiple compression; vendors through guarantees and receivables if a lab fails, after collateral recoveries | DSO, supply commitments, customer concentration, guarantee readiness dates |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | Yes, in their core businesses | Operating cash flow plus, in 2026, bonds and equity: Microsoft cash capex 63% of OCF (79% including finance leases); Amazon trailing FCF −$7.6B; Meta Q2 FCF $0.8B; Alphabet Q2 FCF −$5.9B, $49.6B of common and mandatory convertible preferred plus bonds, capex guidance raised three times to $195-205B | Future commitments: Microsoft $329B of signed leases not yet commenced (starting FY2027-33); Meta $279B of uncommenced leases plus $68B signed in July and up to $46B of Hyperion exposure; Alphabet's disclosed datacenter backstops of $43.8B; OpenAI ~41% of Microsoft RPO on the assumption its December balance is unchanged | Shareholders via earnings when depreciation and lease costs land; creditors are well covered by core cash flows and $77-123B liquidity balances | Capex guidance, FCF, lease commitments, equity-method losses on labs |
| Oracle | Software yes; the build no: FCF −$23.7B in FY2026, −$5.4B in Q1 FY2027 with $11.4B of customer advances inside operating cash flow | $125B of borrowings outstanding, a $20B equity sale, customer advances, $44B of lease liabilities and $288B of uncommenced leases; separately, ~$38B of Vantage project loans for Oracle-tenanted sites (reported, not Oracle debt) | RPO $664B, 13% due within 12 months; OpenAI has announced a >$300B partnership but Oracle does not disclose its share (45% if all of it were in RPO); rated BBB− at S&P, stable outlook; ORCL −48% from its 2026 peak | Shareholders, then unsecured bondholders; project lenders separately | CDS (282-300bp), rating actions, RPO revisions, FCF |
| Neoclouds (CoreWeave and others) | No on a GAAP basis: CoreWeave's net interest was 25% of Q2 revenue; adjusted EBITDA 59% | ~$81B of listed-layer debt at June (CoreWeave $35.6B principal, ~$42B pro forma), >$110B with private facilities, against take-or-pay contracts concentrated in Microsoft, Meta, OpenAI and Anthropic | Six-year depreciation and five-year loans against three-to-five-year contracts; CoreWeave H1 operating cash $3.7B against $14.1B of capex and $5.2B of principal repayments; covenant relief obtained in December 2025; CRWV −56% from peak, converts far out of the money | Equity, then ~$21B of unsecured notes and converts, then SPV lenders after collateral; Nvidia's $6.3B capacity purchase is conditional, not a debt guarantee | CDS (>1,000bp), bond prices (2032 notes 76-81c), GPU rental index at 2027-29 renewals |
| Frontier labs (OpenAI, Anthropic, xAI) | Not established: OpenAI reported 33% gross margin (2025); Anthropic reports unaudited adjusted profit | Investor and supplier equity (Microsoft, Amazon $50B, Nvidia, Google, AMD up to $5B), now also debt: $13.3B of Valor GPU financing inside SpaceX for xAI; Anthropic's proposed $60B North Star (reported >10% yield on the junior tranche, not closed) | Multi-year commitments far above revenue: OpenAI's aggregate is reported above $1T but overlaps and cannot be summed; Anthropic's reported $518B over a decade (grade C) against a ~$65-67B gross run-rate; ~80% of Anthropic's obligations reported non-cancellable while its customers have no long commitments | Investors first; suppliers holding guarantees, RPO and receivables after recoveries | Run-rate reports, funding rounds, contract deferrals, S-1 filings |
| Neolabs and applications | Mostly no | Venture and strategic equity at high multiples | $31B of reproducible rounds by labs with little disclosed revenue; app margins thin and variable; one reported failed raise (Poolside) | Venture investors; then GPU demand for training | Down rounds, shutdowns, acqui-hires |
| Power and datacenter real estate | Yes for equipment incumbents and established colocation (Vertiv, GE Vernova, Equinix, Digital Realty) | Project bonds, private credit, REIT balance sheets, utility rate bases; selected campus budgets total $82B of commitments | Unpowered shells, merchant campuses and conditional tenant obligations; energisation, not chips, is the regional constraint; single-tenant bonds at 88-94 cents (dealer marks); VRT −45% from peak | Developers and project bondholders first; guarantees can push losses back to tenants | Project-bond prices, pre-leasing, PJM capacity prices, turbine backlogs |

## The shape of it

The stack is profitable at both ends and leveraged in the middle. Equipment,
foundry and Nvidia earn record margins and collect much of their cash early
through prepayments and short payment cycles, with the qualification that
Nvidia's receivables, supply commitments and guarantee are all growing. The
hyperscalers still fund most of their build from operations and hold large
liquidity, but each crossed a line in 2026: Amazon's trailing free cash flow
turned negative, Meta's fell below $1B in a quarter, Alphabet sold equity,
and Microsoft's stock of signed-but-uncommenced leases rose from $93B to
$329B in a year. Oracle and the neoclouds are where the debt sits and where
credit repriced in September and October.

Below them, the labs are the demand the rest is built for. They are growing
very fast on reported numbers, with no audited accounts, gross margins that
do not fund frontier research on the one leaked figure, and multi-year
commitments many times their revenue. OpenAI sits behind Nvidia's guarantee,
AMD's warrants, Amazon's $50B investment, Microsoft's largest RPO line and
an undisclosed share of Oracle's. The
[circular-financing note](/research/macro/circular-financing) maps 51 such
links and is explicit that the map shows transmission channels, not proof
that the demand is uneconomic; what it cannot quantify is how much purchasing
would disappear without the supplier financing.

## Near-term cash risk, by name

Concrete items from the notes that matter inside the forecast horizons,
with the counter-evidence beside them.

| Name | Cash risk | Counter-evidence |
|---|---|---|
| CoreWeave | Covenant relief in December 2025 (DSCR test deferred to October 2027, equity cures to 28 October 2026); H1 principal repayments $5.2B vs operating cash $3.7B; $35.5B of leases not yet commenced; converts struck at $97.85 vs $61 stock | Adjusted EBITDA covers net interest 2.4x; DDTL 4.0 rated A3 and priced at SOFR+225; September contracts reported at ~$40M/MW; a 35M-share ATM in place |
| Oracle | FCF −$23.7B (FY2026); customer advances of $11.4B inside Q1 operating cash; $44B lease liabilities, $288B uncommenced | $664B RPO; $20B equity raised; stable outlook at BBB−; legacy software cash flows |
| Meta | $279B uncommenced leases, $68B more signed in July, $349B non-cancellable commitments (categories overlap), Hyperion max exposure $46B | $90B cash and securities; ad metrics support AI-driven monetisation |
| Anthropic | ~80% of obligations non-cancellable (reported) vs customers without long commitments; North Star unclosed at >10% junior yield; KBRA one notch below IG | Reported $16.8B Q3 revenue and adjusted profit; $65B round; >1,000 customers above $1M |
| Other neoclouds | IREN, Cipher, TeraWulf: $5-8B of debt each with negative or minimal EBITDA; Cipher $3.7B of $4.6B cash restricted; all four 2026 converts out of the money | Nebius 41% AI-cloud EBITDA margin, prepayments 50-60% of GPU capex; Hut 8 non-recourse IG project bonds |

## Layer notes

- **Equipment**: [semiconductor-equipment](/research/stack/semiconductor-equipment).
- **Foundry**: [tsmc-and-foundry](/research/stack/tsmc-and-foundry).
- **Accelerators**: [nvidia](/research/stack/nvidia),
  [amd-broadcom-custom-silicon](/research/stack/amd-broadcom-custom-silicon).
- **Hyperscalers**: [microsoft](/research/stack/microsoft),
  [amazon](/research/stack/amazon), [meta](/research/stack/meta),
  [alphabet](/research/stack/alphabet).
- **Oracle**: [oracle](/research/stack/oracle).
- **Neoclouds**: [coreweave](/research/stack/coreweave),
  [neoclouds-other](/research/stack/neoclouds-other).
- **Labs**: [openai](/research/stack/openai),
  [anthropic](/research/stack/anthropic), [labs-other](/research/stack/labs-other).
- **Memory**: [memory-hbm](/research/stack/memory-hbm).
- **Compute market**: [gpu-pricing-and-utilization](/research/macro/gpu-pricing-and-utilization):
  connected clusters are scarce while standalone GPU-hours stay cheap; the
  three public indices measure different products and cannot be spliced.
- **Cross-cutting**: [debt-markets](/research/macro/debt-markets) (about
  $494B of corporate principal at five large issuers including legacy
  non-AI debt, $572B with selected project securities, a $723B gross
  perimeter including commitments and proposals; tight aggregate spreads
  with selective stress), [circular-financing](/research/macro/circular-financing),
  [demand-side](/research/macro/demand-side),
  [public-markets](/research/macro/public-markets),
  [power-and-datacenters](/research/macro/power-and-datacenters),
  [rates-sovereign-geopolitics](/research/macro/rates-sovereign-geopolitics),
  [china](/research/macro/china).
