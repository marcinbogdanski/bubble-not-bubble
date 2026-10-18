# The stack, layer by layer

*Version 0.8, 2026-10-18 · Synthesis of the research notes, corrected after
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
| Foundry (TSMC) | Yes: 66% gross, 59% operating margin | Operating cash flow; capex $60-64B fully covered | New leading-edge and CoWoS capacity mainly serving 2028-29 supply, while customers order only a few quarters ahead and capacity deposits fell 35% in 2025; management forecasts AI accelerator revenue growing at a mid-to-high-50s% annual rate to 2029 but on 15 October called consumer segments "challenged" and said it is "prudent" on 2027; AI accelerators were high-teens % of revenue in FY2025 | Shareholders via utilisation of largely fixed-cost assets; Taiwan is a separate tail | Monthly revenue, capex revisions, utilisation commentary |
| Memory and HBM | Yes, scarcity margins: Micron 87% gross / 81% operating; SK Hynix 76% operating (83% gross) at 100% utilisation | Cash generation (Micron FY2026 OCF $90B vs $31B of PP&E), public equity (SK Hynix ~$26B ADS offering), subsidies; Micron (only) has 26 take-or-pay agreements covering over 35% of revenue through 2030, three-quarters with pricing frameworks, mostly floor-and-ceiling bands, and expects supply much tighter in FY2027-28; SK Hynix's own filing says it has no long-term-contract backlog | Through-cycle returns after prices normalise; 2027-29 capacity milestones (SK Hynix's plan runs to 2033) could coincide with yield gains, customer retrenchment and CXMT (10% of DRAM revenue in Q2 2026, from 4%); shareholder losses already observed: SK Hynix Korean shares −56% from their June peak, the ADS below its offer | Shareholders; the layer has little debt | Fixed DDR5 contract series (P2; the 2026 peak is likely above the $133 August print), HBM share estimates, capex revisions, SK Hynix Q3 call on 28 October |
| Accelerators (Nvidia, AMD, Broadcom) | Yes: Nvidia 75% gross margin (guided to 71-73%), $127B trailing FCF; Broadcom 46% FCF margin | Own cash, plus vendor financing: Nvidia's conditional guarantee capped at $105B on OpenAI leases (phased from 2028), $99B of equity stakes, receivables $63B with DSO at 60 days; AMD's warrants to OpenAI and Meta (160M shares each); Broadcom's disclosed ~$29B lease backstop and conditional customer-note facility of up to $42B | Management says labs backed by Nvidia's balance sheet will be "roughly a quarter" of FY2028 business; Broadcom has six custom-silicon customers and expects Anthropic to be the largest in 2027 and OpenAI second in 2028, with only OpenAI's first 1 GW explicitly binding at AMD; Broadcom's $179B RPO is company-wide, its allocation undisclosed; AVGO −32% from peak | Shareholders through multiple compression; vendors through guarantees and receivables if a lab fails, after collateral recoveries | DSO, supply commitments, customer concentration, guarantee readiness dates |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | Yes, in their core businesses | Operating cash flow plus, in 2026, bonds and equity: Microsoft cash capex 63% of OCF (79% including finance leases); Amazon trailing FCF −$7.6B; Meta Q2 FCF $0.8B; Alphabet Q2 FCF −$5.9B (TTM +$53B), $49.6B of common and mandatory convertible preferred plus bonds including $25B more in August, capex guidance raised twice to $195-205B against $186B of trailing operating cash flow, equity gains of $99B in Q2 ($77B on a private stake reported to be Anthropic) supplying 69% of net income, Cloud backlog $514B within $519.5B of total RPO, just over half of which is expected within 24 months; Amazon raised $67B of long-term-debt proceeds in H1 2026, $25B in July and £4.25B in September, and two-thirds of its Q2 pre-tax income was the mark-up on its Anthropic stake (carried at $190B, about a third of book equity) | Future commitments: Microsoft $329B of signed leases not yet commenced (starting FY2027-33); Meta $279B of uncommenced leases plus $68B signed in July, with $81.7B of commitments due in 2027 (the lease part of the $46B Hyperion maximum exposure, about $12B, overlaps these; the ~$28B residual-value guarantee does not); Alphabet's disclosed datacenter backstops of $43.8B; OpenAI ~41% of Microsoft RPO on the assumption its December balance is unchanged | Shareholders via earnings when depreciation and lease costs land; creditors are well covered by core cash flows and liquidity at 30 June (Microsoft $77B, Amazon $123B, Meta $90B, Alphabet $155B ex equity stakes) | Capex guidance, FCF, lease commitments, equity-method losses on labs |
| Oracle | Software yes; the build no: FCF −$23.7B in FY2026, −$5.4B in Q1 FY2027 with $11.4B of customer advances inside operating cash flow | $125B of borrowings outstanding, a completed $20B equity sale within a ~$40B FY2027 financing plan, customer advances, $44B of lease liabilities and $288B of uncommenced leases; separately, ~$38B of Vantage project loans for Oracle-tenanted sites (reported, not Oracle debt) | RPO $664B, 13% due within 12 months; OpenAI has announced a >$300B partnership, Oracle does not disclose its share, and S&P estimated OpenAI at roughly half of May's $638B RPO; rated BBB− at S&P since 9 July 2026, stable outlook; S&P forecasts mid-4x leverage and nearly −$42B of FY2027 free operating cash flow, leaving limited headroom against its stated downgrade triggers (adjusted leverage above 4.5x, no path to positive FOCF by FY2029); Moody's Baa2 negative and Fitch BBB stable are two notches above junk; on the 10 September call management discussed delay contingencies at the New Mexico and Wisconsin sites while calling construction on track, and Jupiter's air permit is still pending (dismissal-motion hearing 26 October; the main hearing reportedly moved to 7 December, so a decision now likely follows Oracle's mid-December results; the buildings are unpowered and the on-site plant not started; reported, C); ORCL −48% from its 2026 peak | Shareholders, then unsecured bondholders; project lenders separately | CDS (288bp on 15 Oct, then near 300bp), rating outlooks, the customer-prepayment line each quarter, RPO revisions, FCF |
| Neoclouds (CoreWeave and others) | No on a GAAP basis: CoreWeave's net interest was 25% of Q2 revenue; adjusted EBITDA 59% | a selected subtotal of ~$80.7B of listed-layer debt at June including CoreWeave ($35.6B principal, $35.1B carrying; $42.2B adding identified later borrowings before repayments), mixing dates and measures; private facilities (Nscale, Lambda, Crusoe) add to it but are not reconciled; against take-or-pay contracts in which Microsoft (Nscale up to $43.8B, Nebius $17.4-19.4B, IREN $9.7B), Meta, OpenAI and Anthropic recur | DDTL 5.5 lends five years against contracts averaging three; CoreWeave H1 operating cash $3.7B against $14.1B of equipment purchases and $5.2B of principal repayments, with $4.4B / $6.2B / $4.4B due in the rest of 2026 / 2027 / 2028; DDTL 3.0 covenant relief in December 2025 (unlimited equity cures until 28 October 2026, limited cures after); CRWV −56% from peak, converts far out of the money | Equity first; beyond that, by borrower: most DDTLs carry parent guarantees, SPV lenders hold GPU collateral, ~$21B of unsecured notes and converts rank behind secured claims; Nvidia's $6.3B capacity purchase is conditional, not a debt guarantee | CDS (>1,000bp), bond quotes (2032 notes ~78-81c, 14.5-16% yield, dated 15 Oct, grade C-D), renewal pricing as initial contracts expire |
| Frontier labs (OpenAI, Anthropic, xAI) | Not established: OpenAI's reported, unverified adjusted gross margin was 33% (2025) with $25B of 2026 cash burn forecast; Anthropic reports an unaudited 11% adjusted operating margin for Q3 2026 | Investor and supplier equity (Microsoft, Amazon $50B, SoftBank $64.6B cumulative into OpenAI with the final $10B funded by ~9.4% notes, Nvidia, Google, AMD up to $5B), now also debt: $13.3B of related-party Valor GPU financing inside SpaceX for xAI (Valor's founder sits on SpaceX's board), with $28B of non-cancellable commitments, $22B due in 2027; Anthropic's proposed $60B North Star (reported >10% yield on the junior tranche, not closed) | Multi-year commitments far above revenue: OpenAI's aggregate is reported above $1T but overlaps and cannot be summed; its successive cash-flow forecasts for 2026-30 moved from +$14B (Q1 2025) to −$69B and −$179B (Feb 2026) (reported, C), with a disputed September plan at −$278B (D), and end-2025 cash plus the $122B round covers the February plan only into 2028 (C); Microsoft recognised $24.1B of FY2026 revenue from OpenAI including revenue sharing, about 114% of OpenAI's reconstructed $21.2B of sales for the same twelve months (C); Anthropic's reported $518B over a decade (grade C) against a July exit run-rate above $65B (gross) or $67.2B annualising Q3 sales; ~80% of Anthropic's obligations reported non-cancellable while its customers have no long commitments | Investors first; suppliers holding guarantees, RPO and receivables after recoveries | Run-rate reports, funding rounds, contract deferrals, S-1 filings |
| Neolabs and applications | Mostly no | Venture and strategic equity at high multiples | $31B of selected 2025-26 rounds (59% of it Meta's Prometheus financing; not a low-revenue census); exits so far (Cursor to SpaceX at $60B in stock, World Labs) came at higher valuations; one reported failed raise (Poolside) followed by a reported refinancing | Venture investors; new, uncommitted GPU orders are cut first | Down rounds, shutdowns, acqui-hires |
| Power and datacenter real estate | Yes for equipment incumbents and established colocation (Vertiv 19.5% operating margin; GE Vernova Power segment 18.8% with $5.1B of quarterly FCF; Equinix ~50% EBITDA margin excluding one-off fees); unproven for financed campuses | Project bonds, private credit, REIT balance sheets, utility rate bases; three 2025 campus development announcements (Hyperion, Abilene, Frontier/Lighthouse) total at least $82B, not deployed capital; Meta's Hyperion residual-value guarantee threshold (~$28B, declining over time and payable only if Meta does not renew, the property falls short and other conditions are met) roughly covers the $27.3B of Hyperion bonds, so those bondholders depend mainly on Meta's credit | Unpowered shells, merchant campuses and conditional tenant obligations; grid connection is the local constraint (Dominion's queue ~75 GW with ~7-year waits; Jupiter's buildings still unpowered; Virginia moratorium bill filed 16 October), while PJM's July 2026 auction cleared at its price cap 6.8 GW short of the 2028/29 requirement with only 525 MW of new generation; single-tenant bonds reported from below 87 to about 94 cents across two FT versions (price type unstated); VRT −45% from peak | Developers and project bondholders first; guarantees can push losses back to tenants | Project-bond prices, pre-leasing, PJM capacity prices, turbine backlogs |

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
uneconomic. How much accelerator demand depends on that financing remains unquantified:
the note's accounting-scale scenarios (a selected $44B Nvidia equity basket
against its revenue gives 1.1-2.3%) explicitly do not measure it, and the
Claude cross-check's rough estimate of 10-20% narrowly defined is a
reviewer judgement (D).

## Near-term cash risk, by name

Concrete items from the notes that matter inside the forecast horizons,
with the counter-evidence beside them.

| Name | Cash risk | Counter-evidence |
|---|---|---|
| CoreWeave | DDTL 3.0 covenant relief in December 2025 (DSCR test deferred to October 2027; unlimited equity cures until 28 October 2026, limited after); H1 principal repayments $5.2B vs operating cash $3.7B; scheduled principal $4.4B (rest of 2026), $6.2B (2027), $4.4B (2028); $35.5B of leases not yet commenced; converts struck at $97.85 vs $61 stock | Adjusted EBITDA covers net interest 2.4x (not principal); DDTL 4.0 rated A3 at SOFR+225; management reports initial-term debt recovery, A100/H200 renewals and September contracts at ~$40M/MW (company claims, and the company's disclosure controls were not effective at 30 June 2026 per its 10-Q); a 35M-share ATM in place |
| Oracle | FCF −$23.7B (FY2026); customer advances of $11.4B inside Q1 operating cash; $44B lease liabilities, $288B uncommenced | $664B RPO; $20B equity raised; stable outlook at BBB−; legacy software cash flows |
| Meta | $279B uncommenced leases, $68B more signed in July, $349B non-cancellable commitments (categories overlap), $81.7B due in 2027, Hyperion max exposure $46B; 2026 FCF −$17B to +$14B against $23B of dividends and withholding; unpaid capex in payables up from $9.3B to $19.5B | $90B cash and securities; ad-model uplifts of 1.6-5.8% per surface (company measurements); management says it has offers to resell compute at a premium |
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
  pricing is segmented by generation and product (OCPI transaction prices
  as a share of CoreWeave list: B200 0.94, H100 0.45, A100 0.35); the three
  public indices measure different things and cannot be spliced.
- **Cross-cutting**: [debt-markets](/research/macro/debt-markets) (about
  $494B of corporate principal at five large issuers including legacy
  non-AI debt, $572B with selected project securities, now on filed inputs
  with about $46B also counted in the neocloud layer; the earlier $723B
  perimeter is withdrawn; tight aggregate spreads with selective stress), [circular-financing](/research/macro/circular-financing),
  [demand-side](/research/macro/demand-side),
  [public-markets](/research/macro/public-markets) (top ten at 20.9x
  forward earnings, their own average, against 17.9x for the rest; the
  concentration is an earnings risk more than a multiple risk),
  [power-and-datacenters](/research/macro/power-and-datacenters),
  [rates-sovereign-geopolitics](/research/macro/rates-sovereign-geopolitics),
  [china](/research/macro/china) (a margin competitor, not a demand
  substitute: Chinese labs took 69% of OpenRouter tokens in mid-September
  while Western closed models kept 73% of spend; MiniMax prices near cost
  at an 18% gross margin; China's three groups spent about $19B of
  June-quarter capex against $171B for the US four).
