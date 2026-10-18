# The stack, layer by layer

*Version 0.7e, 2026-10-18 · Synthesis of the research notes, corrected after
the [red-team review](/reviews/2026-10-17-codex-redteam-report). Every
figure is sourced and graded in the note it links to. All 26 notes have
been cross-checked and corrected (status: reviewed).*

## One table

"Impairment" is defined in the [forecast register](/forecasts/register):
a further 40% equity decline from the 16 October close for any named
constituent, or a distressed credit event.

| Layer | Profitable now? | How the build is financed | Where it is overextended | Who loses first | First signal |
|---|---|---|---|---|---|
| Equipment (ASML, AMAT, Lam, KLA, TEL) | Yes: ASML 44% operating margin, KLA ~61% gross; all generate FCF above capex | Customer prepayments and own cash; net cash at ASML, AMAT, Lam; modest net debt at KLA | Earnings and valuations depend on a 2027-28 order book placed by a few customers, and ASML expects planned 2027-28 output to fall short of demand; China is 20-34% of sales under a live export-control threat | Shareholders; solvency risk low given cash and prepayments | Contract liabilities, KLA/AMAT backlog, customer capex guides (ASML stopped reporting bookings) |
| Foundry (TSMC) | Yes: 66% gross, 59% operating margin | Operating cash flow; capex $60-64B fully covered | New leading-edge and CoWoS capacity arriving after today's backlog ships; AI accelerators were high-teens % of revenue in the last full year | Shareholders via utilisation; Taiwan is a separate tail | Monthly revenue, capex revisions, utilisation commentary |
| Memory and HBM | Yes, scarcity margins: Micron 87% gross / 81% operating; SK Hynix 76% operating | Cash generation (Micron FY2026 OCF $90B vs $31B of PP&E), public equity (SK Hynix ~$26B ADS offering), subsidies; Micron has 26 take-or-pay agreements covering over 35% of revenue through 2030, three-quarters with pricing frameworks, mostly floor-and-ceiling bands, and expects supply much tighter in FY2027-28 | Through-cycle returns after prices normalise; staggered 2027-28 capacity additions could coincide with yield gains and customer retrenchment; SK Hynix already −56% from its 2026 peak | Shareholders; the layer has little debt | Fixed DDR5 contract series (P2), HBM share estimates, capex revisions |
| Accelerators (Nvidia, AMD, Broadcom) | Yes: Nvidia 75% gross margin (guided to 71-73%), $127B trailing FCF; Broadcom 46% FCF margin | Own cash, plus vendor financing: Nvidia's conditional guarantee capped at $105B on OpenAI leases (phased from 2028), $99B of equity stakes, receivables $63B with DSO at 60 days; AMD's warrants to OpenAI and Meta (160M shares each); Broadcom's disclosed ~$29B lease backstop and conditional customer-note facility of up to $42B | Management says labs backed by Nvidia's balance sheet will be "roughly a quarter" of FY2028 business; Broadcom has six custom-silicon customers and expects Anthropic to be the largest in 2027 and OpenAI second in 2028, with only OpenAI's first 1 GW explicitly binding at AMD; Broadcom's $179B RPO is company-wide, its allocation undisclosed; AVGO −32% from peak | Shareholders through multiple compression; vendors through guarantees and receivables if a lab fails, after collateral recoveries | DSO, supply commitments, customer concentration, guarantee readiness dates |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | Yes, in their core businesses | Operating cash flow plus, in 2026, bonds and equity: Microsoft cash capex 63% of OCF (79% including finance leases); Amazon trailing FCF −$7.6B; Meta Q2 FCF $0.8B; Alphabet Q2 FCF −$5.9B (TTM +$53B), $49.6B of common and mandatory convertible preferred plus bonds, capex guidance raised twice to $195-205B against $186B of trailing operating cash flow, Cloud backlog $514B, just over half recognised within 24 months; Amazon $67B of long-term debt drawn in H1 2026 plus $25B in July | Future commitments: Microsoft $329B of signed leases not yet commenced (starting FY2027-33); Meta $279B of uncommenced leases plus $68B signed in July (the $46B Hyperion maximum exposure overlaps these); Alphabet's disclosed datacenter backstops of $43.8B; OpenAI ~41% of Microsoft RPO on the assumption its December balance is unchanged | Shareholders via earnings when depreciation and lease costs land; creditors are well covered by core cash flows and liquidity (Microsoft $77B, Amazon $123B, Meta $90B, Alphabet $155B ex equity stakes) | Capex guidance, FCF, lease commitments, equity-method losses on labs |
| Oracle | Software yes; the build no: FCF −$23.7B in FY2026, −$5.4B in Q1 FY2027 with $11.4B of customer advances inside operating cash flow | $125B of borrowings outstanding, a completed $20B equity sale within a ~$40B FY2027 financing plan, customer advances, $44B of lease liabilities and $288B of uncommenced leases; separately, ~$38B of Vantage project loans for Oracle-tenanted sites (reported, not Oracle debt) | RPO $664B, 13% due within 12 months; OpenAI has announced a >$300B partnership, Oracle does not disclose its share, and S&P estimates it at about half of the backlog; rated BBB− at S&P since 9 July 2026, stable outlook, with S&P's cut triggers (adjusted leverage above 4.5x, no path to positive free operating cash flow by FY2029) at its own FY2027 forecast; Moody's Baa2 negative and Fitch BBB stable are two notches above junk; on the 10 September call management discussed delay contingencies at the New Mexico and Wisconsin sites while calling construction on track, and Jupiter's air permit is still pending (dismissal motion heard 26 October, decision deadline reported as 23 November); ORCL −48% from its 2026 peak | Shareholders, then unsecured bondholders; project lenders separately | CDS (288bp on 15 Oct, then near 300bp), rating outlooks, the customer-prepayment line each quarter, RPO revisions, FCF |
| Neoclouds (CoreWeave and others) | No on a GAAP basis: CoreWeave's net interest was 25% of Q2 revenue; adjusted EBITDA 59% | a selected subtotal of ~$80.7B of listed-layer debt at June including CoreWeave ($35.6B principal, $35.1B carrying; $42.2B adding identified later borrowings before repayments), mixing dates and measures; private facilities (Nscale, Lambda, Crusoe) add to it but are not reconciled; against take-or-pay contracts in which Microsoft (Nscale up to $43.8B, Nebius $17.4-19.4B, IREN $9.7B), Meta, OpenAI and Anthropic recur | DDTL 5.5 lends five years against contracts averaging three; CoreWeave H1 operating cash $3.7B against $14.1B of equipment purchases and $5.2B of principal repayments, with $4.4B / $6.2B / $4.4B due in the rest of 2026 / 2027 / 2028; DDTL 3.0 covenant relief in December 2025 (unlimited equity cures until 28 October 2026, limited cures after); CRWV −56% from peak, converts far out of the money | Equity first; beyond that, by borrower: most DDTLs carry parent guarantees, SPV lenders hold GPU collateral, ~$21B of unsecured notes and converts rank behind secured claims; Nvidia's $6.3B capacity purchase is conditional, not a debt guarantee | CDS (>1,000bp), bond quotes (2032 notes ~78-81c, 14.5-16% yield, dated 15 Oct, grade C-D), renewal pricing as initial contracts expire |
| Frontier labs (OpenAI, Anthropic, xAI) | Not established: OpenAI's reported, unverified adjusted gross margin was 33% (2025) with $25B of 2026 cash burn forecast; Anthropic reports an unaudited 11% adjusted operating margin for Q3 2026 | Investor and supplier equity (Microsoft, Amazon $50B, Nvidia, Google, AMD up to $5B), now also debt: $13.3B of Valor GPU financing inside SpaceX for xAI; Anthropic's proposed $60B North Star (reported >10% yield on the junior tranche, not closed) | Multi-year commitments far above revenue: OpenAI's aggregate is reported above $1T but overlaps and cannot be summed; its successive cash-flow forecasts for 2026-30 moved from +$14B (Q1 2025) to −$69B, −$179B (Feb 2026) and −$278B (Sept 2026, disputed), and end-2025 cash plus the $122B round covers the February plan only into 2028 (reported, C); Microsoft billed OpenAI $24.1B in FY2026, about equal to OpenAI's revenue for the same twelve months; Anthropic's reported $518B over a decade (grade C) against a July exit run-rate above $65B (gross) or $67.2B annualising Q3 sales; ~80% of Anthropic's obligations reported non-cancellable while its customers have no long commitments | Investors first; suppliers holding guarantees, RPO and receivables after recoveries | Run-rate reports, funding rounds, contract deferrals, S-1 filings |
| Neolabs and applications | Mostly no | Venture and strategic equity at high multiples | $31B of reproducible rounds by labs with little disclosed revenue; app margins thin and variable; one reported failed raise (Poolside) | Venture investors; then GPU demand for training | Down rounds, shutdowns, acqui-hires |
| Power and datacenter real estate | Yes for equipment incumbents and established colocation (Vertiv, GE Vernova, Equinix, Digital Realty); unproven for financed campuses | Project bonds, private credit, REIT balance sheets, utility rate bases; three announced campus development budgets (Hyperion, Abilene, Frontier/Lighthouse) total $82B, not deployed capital | Unpowered shells, merchant campuses and conditional tenant obligations; PJM's July 2026 auction fell 6.8 GW short of its 2028/29 requirement, so energisation is the regional constraint; single-tenant bonds quoted from below 88 to about 94 cents (dealer indications, 15 Oct); VRT −45% from peak | Developers and project bondholders first; guarantees can push losses back to tenants | Project-bond prices, pre-leasing, PJM capacity prices, turbine backlogs |

## The shape of it

The suppliers at the top of the stack are profitable and the intermediaries
in the middle are leveraged; the labs at the bottom are growing fast with
profitability not established. Equipment, foundry, memory and Nvidia earn
high margins today (Micron 81% operating, TSMC 59%, ASML 44%, Nvidia 75%
gross and guided lower) and collect much of their cash early through
prepayments and short payment cycles, with the qualification that Nvidia's
receivables, supply commitments and guarantee are all growing and Broadcom
now carries a lease backstop and a conditional note facility of its own. The
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
an undisclosed share of Oracle's. Anthropic sits behind Broadcom's $29B
lease backstop and conditional notes, Google's and Amazon's reported ~$110B
commitments each, and is expected to be Broadcom's largest custom-silicon
customer in 2027 (reported, C); its reported $518B of commitments are about
80% non-cancellable. The
[circular-financing note](/research/macro/circular-financing) maps the
links (round-trip flows, contingent credit support and customer prepayments
are different things; "circular" fits only the first) and is explicit that
the map shows transmission channels, not proof that the demand is
uneconomic. A narrow estimate of supplier-supported 2026 accelerator demand
is 10-20%, broad 17-35% (grade D); the filed, paid-in, chip-traceable part
is under 5%, almost all of it through OpenAI and Anthropic.

## Near-term cash risk, by name

Concrete items from the notes that matter inside the forecast horizons,
with the counter-evidence beside them.

| Name | Cash risk | Counter-evidence |
|---|---|---|
| CoreWeave | DDTL 3.0 covenant relief in December 2025 (DSCR test deferred to October 2027; unlimited equity cures until 28 October 2026, limited after); H1 principal repayments $5.2B vs operating cash $3.7B; scheduled principal $4.4B (rest of 2026), $6.2B (2027), $4.4B (2028); $35.5B of leases not yet commenced; converts struck at $97.85 vs $61 stock | Adjusted EBITDA covers net interest 2.4x (not principal); DDTL 4.0 rated A3 at SOFR+225; management reports initial-term debt recovery, A100/H200 renewals and September contracts at ~$40M/MW (company claims, and the company's disclosure controls were not effective at 30 June 2026 per its 10-Q); a 35M-share ATM in place |
| Oracle | FCF −$23.7B (FY2026); customer advances of $11.4B inside Q1 operating cash; $44B lease liabilities, $288B uncommenced | $664B RPO; $20B equity raised; stable outlook at BBB−; legacy software cash flows |
| Meta | $279B uncommenced leases, $68B more signed in July, $349B non-cancellable commitments (categories overlap), Hyperion max exposure $46B | $90B cash and securities; ad metrics support AI-driven monetisation |
| Anthropic | ~80% of obligations non-cancellable (reported) vs customers without long commitments; North Star unclosed at >10% junior yield; KBRA one notch below IG | Reported $16.8B Q3 revenue and adjusted profit; $65B round; >1,000 customers above $1M |
| Other neoclouds | IREN, Cipher, TeraWulf: $5-8B of debt each with negative or minimal EBITDA; Cipher $3.7B of $4.6B cash restricted; all four 2026 converts out of the money | Nebius 49.7% AI-cloud adjusted EBITDA margin (40.6% group) though operating cash less capex was −$3.4B; prepayments material; Hut 8 non-recourse IG project bonds |

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
  non-AI debt, $572B with selected project securities, both dated May-June
  2026 snapshots; tight aggregate spreads with selective stress), [circular-financing](/research/macro/circular-financing),
  [demand-side](/research/macro/demand-side),
  [public-markets](/research/macro/public-markets) (the $494B/$572B
  corporate and project principal figures in the debt note carry its stated
  verification limits; its earlier $723B perimeter is withdrawn),
  [power-and-datacenters](/research/macro/power-and-datacenters),
  [rates-sovereign-geopolitics](/research/macro/rates-sovereign-geopolitics),
  [china](/research/macro/china).
