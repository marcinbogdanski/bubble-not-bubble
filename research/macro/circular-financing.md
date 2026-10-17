# Circular and vendor financing in the AI stack

*Last updated: 2026-10-17 · Status: draft · Author: Codex (GPT-6) · Reviewer: none*

## Summary

- Suppliers increasingly supply capital, customer equity incentives, capacity backstops and guarantees alongside equipment. These instruments transfer different risks and cannot be summed as spending.
- NVIDIA’s OpenAI lease guarantee is confirmed in filings. Broadcom separately discloses a residual-value backstop and an undrawn convertible-note facility; the reported North Star guarantee remains unverified.
- Headline figures are stale: Amazon subsequently completed its OpenAI investment; Microsoft’s later ownership disclosure is below its recapitalization stake. Neither a commitment nor an equity valuation is cash revenue.
- Semiconductor suppliers remain profitable. CoreWeave’s financing-dependent expansion is loss-making; contracted revenue does not establish returns after depreciation, interest and replacement capex.
- Repeated revenue along a supply chain is normal gross accounting. The danger is treating upstream equipment sales, cloud bookings and lab sales as independent final demand.
- The biggest uncertainty is how much spending would disappear without supplier financing. Public disclosures do not identify that counterfactual or reconcile all overlapping contracts.

## Key claims

Amounts are USD; **bn** = billion, **m** = million. Arrows follow the instrument. The [full deal table](/data/circular-financing-deals.csv) separates dates, from/to, instrument, amount, terms, supported revenue, status, source and grade. A grades disclosure, not execution. Private-company secondary figures are **reported, unverified**.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | NVIDIA → OpenAI equity | $100bn LOI, 10GW, progressive deployment; later $30bn funding announcement; do not add | 2025-09-22; 2026-02-27 | [NLOI], [ROUND] | primary | A |
| 2 | NVIDIA → SB Energy/OpenAI guarantee | $105bn cap; 4.25GW; 20-year leases; commencement 2028/FY2029; default/insolvency shortfall; infrastructure exclusivity | 2026-08-17 | [NGUAR], [NQ] | primary | A |
| 3 | NVIDIA → CoreWeave equity/backstop | Additional $2bn equity at $87.20; $6.3bn initial residual-capacity order through 2032-04-13 | 2026-01-23; 2025-09-09 | [CEQ], [CBACK] | primary | A |
| 4 | NVIDIA/Cisco → xAI | Participation confirmed in $20bn Series E; NVIDIA’s individual check undisclosed; earlier GPU-financing equity up to $2bn reported, unverified | 2026-01-06; 2025-10-08 | [XAI], [XREP] | primary/secondary | A/C |
| 5 | NVIDIA → Nebius | $2bn equity supports NVIDIA cloud infrastructure | 2026-03-11 | [NEQ] | primary | A |
| 6 | NVIDIA/server vendors → Lambda | $480m whole Series D, vendor checks undisclosed; NVIDIA rentals $1.5bn reported, unverified | 2025-02-19; 2025-09-05 | [LEQ], [LRENT] | primary/secondary | A/C |
| 7 | NVIDIA → Intel | $5bn equity announcement at $23.28; CPU/GPU-chiplet co-development | 2025-09-18 | [INTEL] | primary | A |
| 8 | NVIDIA/Microsoft → Anthropic | Up to $10bn/$5bn equity; $30bn Azure purchases and additional capacity up to 1GW support cloud/GPU sales | 2025-11-18 | [NANT] | primary | A |
| 9 | NVIDIA → Groq | $13bn closing + $4bn deferred consideration = $17bn; licence/hiring, no equity or customer contracts acquired | 2025-12; FY2026 filing | [NK] | primary | A |
| 10 | AMD → OpenAI and Meta warrants | Each 160m shares at $0.01; each up to 6GW; purchase/stock/technical conditions; none vested/exercisable; expiries 2030-10-05/2031-02-23 | 2026-06-27 | [AQ] | primary | A |
| 11 | AMD → Anthropic | Up to $5bn future equity; up to 2GW MI450, initial 1GW H1 2027 | 2026-07-22 | [AANT] | primary | A |
| 12 | OpenAI → Broadcom supply | 10GW accelerator/network term sheet; H2 2026–end-2029; dollars undisclosed | 2025-10-13 | [BOAI] | primary | A |
| 13 | Broadcom/Google → Anthropic supply | Approximately 3.5GW TPU capacity beginning 2027; conditional on commercial success | 2026-04-06 | [BTPU] | primary | A |
| 14 | AI XPV financing / Broadcom backstop | $35bn initial transaction; >1GW; five-year leases; $29bn maximum backstop, 85% outstanding lease basis less recoveries; no payments | 2026-08-02 | [BXPV], [BQ] | primary | A |
| 15 | Broadcom → compute customer notes | Up to $42bn convertible facility solely for leases; none issued; filing does not name customer | 2026-08-02 | [BQ] | primary | A |
| 16 | North Star proposed financing | $60bn package; $42bn senior reportedly Broadcom-guaranteed; $18bn junior, Blackstone $9bn, yield >10%; reported, unverified | 2026-10-17 | [NSTAR] | secondary | C |
| 17 | Microsoft → OpenAI | $13bn committed/$11.9bn funded; approximately 25% as-converted versus earlier 27%; $250bn incremental Azure purchases; OpenAI revenue share through 2030, undisclosed rate/cap | 2026-06-30; amendment 2026-04-27 | [MOWN], [MAZ], [MREV] | primary | A |
| 18 | Amazon → Anthropic | $8bn prior + $5bn Series G + $5bn Series H = $18bn invested cost; $15bn facility remaining; $33bn potential total; AWS expansion >$100bn/10 years | 2026-06-30 | [AMQ], [AAMZ] | primary/derived | A/B |
| 19 | Amazon ↔ OpenAI | $28.7bn Series C at June-end + $21.3bn subsequently funded = $50bn; AWS $38bn/7 years plus $100bn/8 years, approximately 2GW Trainium | June-end/subsequent event; 2026-02-27 | [AMQ], [AWS38], [AWS100] | primary | A |
| 20 | Google → Anthropic | Up to 1m TPUs; equity relationship; additional $40bn ($10bn now/$30bn contingent) reported, unverified; current percentage unavailable | 2025-10-23; 2026-04-24 | [GTPU], [GEQ] | primary/secondary | A/C |
| 21 | OpenAI → Oracle | Company describes partnership exceeding $300bn over five years; no direct Oracle loan established | 2025-09-23 | [OSTAR] | primary | A |
| 22 | SoftBank → OpenAI | $64.6bn cumulative, approximately 13%; latest $30bn completed, final $10bn bond-funded; $40bn bridge repaid/cancelled | 2026-10-01 | [SB] | primary | A |
| 23 | Stargate programme | $500bn/four years; $100bn initial intention; SoftBank/OpenAI/Oracle/MGX equity sponsors | 2025-01-22 | [STAR] | primary | A |
| 24 | OpenAI ↔ Cerebras | >$20bn compute, 750MW; ~$1bn loan repayable with service credits; warrant 33,445,026 shares at $0.00001, 10,033,508 exercised July; customer-warrant revenue reduction $46.3m H1 (all customers) | 2026-06-30; July event | [CBS1], [CBQ] | primary | A |
| 25 | OpenAI ↔ CoreWeave | Up to $22.4bn purchases: $11.9bn + $4bn + $6.5bn; CoreWeave issues OpenAI $350m stock, not a cash investment by OpenAI | 2025-03–09 | [OCORE], [CS1] | primary | A |
| 26 | Meta/Blue Owl → Hyperion JV | ~$27bn development; Blue Owl 80%/Meta 20%; initial four-year leases; first 16 operating years residual guarantee, release does not specify cap | 2025-10-21 | [META] | primary | A |
| 27 | Microsoft → Nebius | $17.4bn base/$19.4bn with options; five-year services through 2031; cash flows finance capex, delivery/financing conditions | 2025-09-08 | [NEBMS] | primary | A |
| 28 | Microsoft → IREN | $9.7bn/five years; 20% prepayment finances NVIDIA deployment | 2025-11-03 | [IRENMS] | primary | A |
| 29 | Microsoft → Nscale | Up to $43.8bn through December 2033, excluding optional extensions; delivery/availability conditions | 2026-09-18 disclosure | [NS1] | primary, indexed | A |
| 30 | Microsoft → Lambda | Multibillion-dollar multi-year NVIDIA capacity contract; exact amount/prepayment undisclosed | 2025-11-03 | [LMS] | primary | A |
| 31 | Google → Fluidstack/TeraWulf | Lake Mariner $3.2bn backstop, ~$6.7bn initial rent and ~14% pro-forma warrant stake; separate Abernathy $1.3bn backstop | 2025-08-18; 2025-10-28 | [TW], [TWA] | primary | A |
| 32 | Google → Fluidstack/Cipher | Initial $1.4bn backstop/~5.4% warrant stake; revised $1.73bn including $333m increment; ~$3.8bn initial rent/10 years | 2025-09-25; 2025-11-20 | [CIPH], [CIPHX] | primary | A |
| 33 | Additional vendor equity links | NVIDIA–IREN five-year right: 30m shares × $70 = up to $2.1bn; NVIDIA–Nscale additional $1bn expected mid-November; Crusoe $1.375bn whole round includes NVIDIA/Supermicro | 2026-05-07; 2026-09-25; 2025-10-24 | [IRENN], [NSNEW], [CRUSOE] | primary | A |
| 34 | Explicit equipment/vendor financing | CoreWeave $5.1bn outstanding OEM/software financing; Nscale/Dell ~$2.54bn initial-term equipment rent including $34.8m finance charges | 2026-06-30; 2026-09-04 | [CQ], [NS1] | primary | A |
| 35 | NVIDIA capacity-support model | $36bn, typically six years; third-party customers can replace NVIDIA; additional AI-cloud property guarantee cap $3.5bn | 2026-07-26 | [NQ] | primary | A |
| 36 | Revenue/backlog denominators | NVIDIA Q2 $96.2bn revenue; AMD Q2 $11.536bn; Broadcom RPO $179.2bn; Oracle RPO $664bn; CoreWeave RPO $103.7bn | NVIDIA July 26; AMD June 27; Broadcom August 2; Oracle August 31; CoreWeave June 30, 2026 | [NRESULT], [AQ], [BQ], [ORESULT], [CQ] | primary | A |
| 37 | Profitability counterevidence / vulnerability | NVIDIA H1 operating cash $74.421bn; AMD Q2 operating income ~$2bn; Oracle Q1 ~$6.7bn; CoreWeave Q2 revenue $2.575bn, net loss $626m, net interest $640m | respective latest periods in claim 36 | [NRESULT], [ARESULT], [ORESULT], [CQ] | primary | A |
| 38 | Narrow NVIDIA/AMD attribution scenarios | NVIDIA basket $44bn, 50–100% returned over five years / annualized $384.8bn revenue → 1.1–2.3%; AMD $5bn, 0–100% / five years / $46.144bn → 0–2.2% | scenario 2026-10-17 | claims 1,3,5,8,11,36; assumptions below | derived estimate | C |
| 39 | Backlog-equivalent scenarios | Broadcom $35bn/$179.2bn =19.5% gross, or 4.9–9.8% at assumed 25–50% attributable content; Oracle $300bn/$664bn =45.2%; CoreWeave $6.3bn/$103.7bn =6.1%, plus $22.4bn →27.7% upper scope | scenario 2026-10-17 | claims 3,14,21,25,36; assumptions below | derived estimate | C |
| 40 | Telecom financing precedent | Lucent: $5.391bn undrawn/$1.263bn drawn credit; $0.677bn/$0.771bn debt guarantees; Nortel up to $4.1bn unfunded; Cisco $2.775bn inventory-allowance expense, not customer credit | Lucent September 2000; Nortel December 2000; Cisco FY2001 | [LUC], [NORT], [CISCO] | primary | A |

## Analysis

**Scope and accounting.** The CSV covers requested relationships; private side letters remain incomplete. Purchase contracts close financing loops but do not alone establish vendor financing. Intel and Groq are boundary cases: supplier integration and technology acquisition, respectively.

Investor capital funds lab cloud spending and upstream servers; later subscriptions fund the lab. Adding these sales repeatedly counts intermediate transactions. This alone establishes neither fictitious accounting nor independent demand. Equity, guarantees and backlog are not current revenue. Cerebras deducts customer-warrant costs from revenue and reports pass-through costs. [CBQ]

**Dependency graph.** Arrows show payments; brackets indicate capital/credit support. Delivery runs against payment arrows.

```text
End users → OpenAI / Anthropic → hyperscalers / neoclouds → server OEMs
                                                    → NVIDIA / AMD / Broadcom
                                                    → foundry / memory / power
Microsoft / Amazon / Google [equity] → labs → their investor's cloud
NVIDIA [equity] → OpenAI / Anthropic / xAI / neoclouds → NVIDIA systems
AMD [warrants] → OpenAI / Meta → AMD purchases
AMD [equity] → Anthropic → AMD purchases
OpenAI [loan] → Cerebras [warrant] → OpenAI → Cerebras cloud payments
CoreWeave [stock] → OpenAI → CoreWeave → NVIDIA equipment
NVIDIA [unsold-capacity purchases] → CoreWeave / other AI clouds
SoftBank [equity] → OpenAI → Oracle / Stargate / SB Energy
NVIDIA [lease guarantee] → SB Energy's OpenAI-tenanted campus
Apollo / Blackstone → equipment SPV → Broadcom / Google hardware
Anthropic → SPV lease payments; Broadcom [backstop / conditional notes]
Google [Fluidstack default backstop] → TeraWulf / Cipher project lenders
Microsoft [prepayment / contracted cash flows] → IREN / Nebius / Nscale
Blue Owl / bondholders → Hyperion JV ← Meta [rent / residual guarantee]
```

**Attribution.** Claims 38–39 are conditional estimates, not measured causal shares or comparable accounting ratios.

- **NVIDIA:** the basket adds OpenAI/Anthropic announced equity and incremental CoreWeave/Nebius investments. Assume half to all returns as NVIDIA revenue, evenly over the scenario window, freezing quarterly revenue. Unidentified investments, leverage and guarantees are excluded; supported sales could be much larger. Investee purchases and paid-in timing are undisclosed. Capacity support is potentially overlapping exposure, not another sales numerator. [NLOI] [ROUND] [NQ]
- **AMD:** assume none to all of the Anthropic equity commitment returns as hardware revenue over the same window. The resulting range excludes the potentially much larger purchase programmes incentivized by warrants: no customer-level revenue or warrant fair-value reconciliation permits a defensible percentage for those programmes. Unvested warrants do not prove the absence of supported orders. [AQ] [AANT]
- **Broadcom:** the gross transaction/backlog ratio assumes the entire financed equipment transaction remains in Broadcom RPO. The narrower content range is an explicit sensitivity, not disclosed silicon economics. Google equipment pass-through, already delivered racks and software backlog change the answer. Do not substitute the guarantee cap or note facility for sales, or add North Star without reconciling overlap. [BQ] [BXPV]
- **Oracle:** the ratio assumes the headline partnership amount is an OCI purchase commitment still included in current RPO. Company confirmation of partnership size does not provide that reconciliation. This is indirect exposure to supplier-funded OpenAI, not proof Oracle itself financed that fraction. [OSTAR] [ORESULT]
- **CoreWeave:** direct backstop and broader OpenAI agreement ratios are gross contract-equivalent sensitivities. Recognition to date, capacity resales, variable consideration and overlapping supported capacity reduce the retained backlog numerator. Adding them is only an upper-scope illustration, not a verified RPO split. [CBACK] [OCORE] [CQ]

**Returns and loss allocation.** Supplier profitability contradicts a stack-wide insolvency thesis (claim 37). CoreWeave’s losses and interest burden demonstrate the customer-return problem. Vendors receive cash earlier; cloud equity/lenders absorb utilization, execution and refinancing risks. Guarantees return tail losses upstream when hardware demand and collateral values may also fall.

NVIDIA’s phased PORTS guarantee provides assumption/reletting/sale remedies after default or insolvency. OpenAI’s indemnity may be uncollectible during distress. Broadcom’s backstop also depends on collateral recovery. Lender protection does not remove system risk. [NGUAR] [BQ]

**Historical comparison.** Lucent/Nortel financed customers as external capital constrained expansion. Nortel warned that retreating lenders could leave financing on its books longer. Modern SPVs and guarantees extend this mechanism. Cisco’s inventory charge measures overordering, not vendor loans. Historical commitments and modern caps are neither realized losses nor comparable without adjusting for company scale. [LUC] [NORT] [CISCO]

**Single points of failure.** OpenAI/Anthropic concentrate final demand and fundraising; Microsoft anchors multiple neoclouds; NVIDIA supplies hardware, equity and contingent purchases; Broadcom/Google concentrate TPU financing. Energization delays can block customer payments and funding while construction costs continue. Refinancing and equipment values transmit common shocks: SPVs cannot diversify a simultaneous fall in compute rents.

## Conflicts and open questions

Profitable suppliers and growing usage are the strongest counterevidence. Backstops can bridge construction, and third-party usage displaces supplier obligations. This map cannot establish uneconomic final demand; current chip profits cannot validate customers’ eventual returns.

Specific corrections matter: Microsoft’s original ownership figure was subsequently diluted; its headline funding commitment exceeds cash funded. Amazon’s June-end OpenAI figure excludes a disclosed subsequent completion. Amazon’s Anthropic facility is released against compute milestones, with subsequent equity participation reducing remaining capacity. These are genuine updates, not interchangeable measurements. [MOWN] [AMQ]

North Star’s reported senior guarantee lacks a fetched executed contract. Broadcom’s filed note facility is real but unnamed; identification as Anthropic remains unconfirmed in the fetched primary disclosure. Groq’s reported headline differs from filed consideration; no customer-financing loop was established. [BQ] [NSTAR] [NK]

Unresolved: investee-level NVIDIA sales; guarantee collateral/fees; remaining lab contracts; paid equity; programme overlap. Some SEC access was indexed-only. No comprehensive related-party revenue matrix was verified; economic links do not automatically meet accounting definitions.

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| New supplier equity | AMD–Anthropic up to $5bn | 2026-07-22 | [AANT] | Expands capital/sales coupling |
| Expected funding | NVIDIA–Nscale $1bn expected mid-November | 2026-09-25 | [NSNEW] | Track payment versus pledge |
| Warrant vesting | AMD: none vested/exercisable | 2026-06-27 | [AQ] | Purchase-linked milestones |
| Warrant exercise | OpenAI exercised 10,033,508 Cerebras shares in July | 2026-08-12 disclosure | [CBQ] | Incentives are becoming ownership |
| Guarantee triggers | NVIDIA $105bn phased cap; no verified trigger notice | 2026-08-17/latest reviewed | [NGUAR] | Contingent support becomes cash risk |
| Backstop purchases | CoreWeave $6.3bn initial order; utilization/draw split unavailable | 2025-09-09/latest reviewed | [CBACK] | Detect displacement of external customers |
| Notes/backstop usage | Broadcom: no notes issued, no backstop payments | 2026-08-02 | [BQ] | Distinguish commitment from loss |
| Related-party revenue | No comprehensive investee/customer reconciliation verified | 2026-10-17 | [NQ], [CQ], [BQ] | Enables measured attribution |

## Sources

All accessed **2026-10-17**. Publication/filing dates below; unavailable days and indexed-only SEC access are identified.

1. **NLOI** — NVIDIA, OpenAI strategic partnership, 2025-09-22; primary. https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership-to-Deploy-10-Gigawatts-of-NVIDIA-Systems/default.aspx (accessed 2026-10-17).
2. **ROUND** — OpenAI, Scaling AI for everyone, 2026-02-27; primary. https://openai.com/index/scaling-ai-for-everyone/ (accessed 2026-10-17).
3. **NGUAR** — NVIDIA, Form 8-K: PORTS guarantees, 2026-08-17; primary. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm (accessed 2026-10-17).
4. **NQ** — NVIDIA, Q2 FY2027 10-Q, 2026-08-27; primary. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm (accessed 2026-10-17).
5. **CEQ** — CoreWeave, Form 8-K: NVIDIA equity, 2026-01-26; primary. https://www.sec.gov/Archives/edgar/data/1769628/000176962826000044/crwv-20260123.htm (accessed 2026-10-17).
6. **CBACK** — CoreWeave, Form 8-K: residual capacity, 2025-09-15; primary. https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm (accessed 2026-10-17).
7. **XAI** — xAI, Series E announcement, 2026-01-06; primary. https://x.ai/news/series-e (accessed 2026-10-17).
8. **XREP** — Reuters/Bloomberg, xAI financing, 2025-10-08; secondary. https://uk.marketscreener.com/news/musk-s-xai-nears-20-billion-capital-raise-tied-to-nvidia-chips-bloomberg-news-reports-ce7d5bd2db80f125 (accessed 2026-10-17).
9. **NEQ** — NVIDIA, Nebius partnership, 2026-03-11; primary. https://nvidianews.nvidia.com/news/nvidia-and-nebius-partner-to-scale-full-stack-ai-cloud (accessed 2026-10-17).
10. **LEQ** — Lambda, Series D, 2025-02-19; primary. https://lambda.ai/blog/lambda-raises-480m-to-expand-ai-cloud-platform (accessed 2026-10-17).
11. **LRENT** — Tom’s Hardware/The Information, Lambda rentals, 2025-09-05; secondary. https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-signs-usd1-5-billion-deal-with-cloud-startup-lambda-to-rent-back-its-own-ai-chips-18-000-gpus-will-be-leased-over-4-years-as-lambda-gears-up-for-its-ipo (accessed 2026-10-17).
12. **INTEL** — NVIDIA/Intel, strategic collaboration, 2025-09-18; primary. https://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products (accessed 2026-10-17).
13. **NANT** — Microsoft/NVIDIA/Anthropic, partnerships, 2025-11-18; primary. https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/ (accessed 2026-10-17).
14. **NK** — NVIDIA, FY2026 10-K, Note 2, 2026-02-25; primary. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm (accessed 2026-10-17).
15. **AQ** — AMD, Q2 2026 10-Q, 2026-08-05; primary. https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm (accessed 2026-10-17).
16. **AANT** — AMD/Anthropic, strategic partnership, 2026-07-22; primary. https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/ (accessed 2026-10-17).
17. **BOAI** — OpenAI/Broadcom, accelerator collaboration, 2025-10-13; primary. https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/ (accessed 2026-10-17).
18. **BTPU** — Broadcom, Form 8-K: Google/Anthropic, 2026-04-06; primary. https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm (accessed 2026-10-17).
19. **BXPV** — Broadcom/Apollo/Blackstone, AI XPV platform, 2026-06-09; primary. https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic (accessed 2026-10-17).
20. **BQ** — Broadcom, Q3 FY2026 10-Q, 2026-09-10; primary. https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm (accessed 2026-10-17).
21. **NSTAR** — Investing.com/FT, proposed North Star financing, 2026-10-17; secondary. https://au.investing.com/news/company-news/anthropic-offers-blackstone-over-10-yield-in-60b-ai-chip-financing--ft-reports-4696137 (accessed 2026-10-17).
22. **MOWN** — Microsoft, FY2026 10-K (indexed text; full fetch unavailable), 2026-07-29; primary. https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm (accessed 2026-10-17).
23. **MAZ** — Microsoft, Q1 FY2026 10-Q, 2025-10-29; primary. https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm (accessed 2026-10-17).
24. **MREV** — Microsoft, amended OpenAI partnership, 2026-04-27; primary. https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/ (accessed 2026-10-17).
25. **AAMZ** — Anthropic/Amazon, compute expansion, 2026-04-20; primary. https://www.anthropic.com/news/anthropic-amazon-compute (accessed 2026-10-17).
26. **AMQ** — Amazon, Q2 2026 10-Q, 2026-07-30; primary. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm (accessed 2026-10-17).
27. **AWS38** — OpenAI/AWS, initial agreement, 2025-11-03; primary. https://openai.com/index/aws-and-openai-partnership/ (accessed 2026-10-17).
28. **AWS100** — OpenAI/Amazon, expanded partnership, 2026-02-27; primary. https://openai.com/index/amazon-partnership/ (accessed 2026-10-17).
29. **GTPU** — Anthropic, Google TPU expansion, 2025-10-23; primary. https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services (accessed 2026-10-17).
30. **GEQ** — Reuters, Google investment in Anthropic, 2026-04-24; secondary. https://www.streetinsider.com/Reuters/Google%2Bto%2Binvest%2Bup%2Bto%2B%2440%2Bbillion%2Bin%2BAI%2Brival%2BAnthropic/26364234.html (accessed 2026-10-17).
31. **OSTAR** — OpenAI/Oracle/SoftBank, Stargate expansion, 2025-09-23; primary. https://openai.com/index/five-new-stargate-sites/ (accessed 2026-10-17).
32. **SB** — SoftBank, completed OpenAI follow-on investment, 2026-10-01; primary. https://group.softbank/en/news/press/20261001 (accessed 2026-10-17).
33. **STAR** — SoftBank, Announcing The Stargate Project, 2025-01-22; primary. https://group.softbank/en/news/press/20250122 (accessed 2026-10-17).
34. **CBS1** — Cerebras, May S-1/A, 2026-05 (day not verified); primary. https://www.sec.gov/Archives/edgar/data/2021728/000162828026029503/cerebras-sx1amay2026.htm (accessed 2026-10-17).
35. **CBQ** — Cerebras, Q2 2026 10-Q, 2026-08-12; primary. https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm (accessed 2026-10-17).
36. **OCORE** — CoreWeave, expanded OpenAI agreement, 2025-09-25; primary. https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx (accessed 2026-10-17).
37. **CS1** — CoreWeave, S-1/A: OpenAI stock issuance, 2025-03-20; primary. https://www.sec.gov/Archives/edgar/data/1769628/000119312525058309/d899798ds1a.htm (accessed 2026-10-17).
38. **META** — Meta, Blue Owl Hyperion joint venture, 2025-10-21; updated 2025-11-14; primary. https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/ (accessed 2026-10-17).
39. **NEBMS** — Nebius, Form 6-K: Microsoft contract, 2025-09-08; primary. https://assets.nebius.com/assets/86625727-9e66-46c1-af79-c27d57434e3c/25-25580-1_Nebius%20Group%20N.V._6-K.pdf (accessed 2026-10-17).
40. **IRENMS** — IREN, Microsoft contract, 2025-11-03; primary. https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft (accessed 2026-10-17).
41. **NS1** — Nscale, S-1 (indexed passages; full fetch unavailable), 2026-09-18; primary. https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm (accessed 2026-10-17).
42. **LMS** — Lambda, Microsoft agreement, 2025-11-03; primary. https://lambda.ai/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus (accessed 2026-10-17).
43. **TW** — TeraWulf, Lake Mariner expansion, 2025-08-18; primary. https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-079463/tm2523651d3_ex99-1.htm (accessed 2026-10-17).
44. **TWA** — TeraWulf, Abernathy presentation, 2025-10-28; primary. https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-102858/tm2529509d1_ex99-3.htm (accessed 2026-10-17).
45. **CIPH** — Cipher, Form 8-K: Fluidstack/Google, 2025-09-25; primary. https://investors.cipherdigital.com/static-files/14485cf7-a788-4dcf-9d81-a9d806a695d1 (accessed 2026-10-17).
46. **CIPHX** — Cipher, Fluidstack expansion, 2025-11-20; primary. https://investors.cipherdigital.com/node/10866/pdf (accessed 2026-10-17).
47. **IRENN** — IREN, NVIDIA partnership and results, 2026-05-07; primary. https://iren.gcs-web.com/news-releases/news-release-details/iren-business-update-and-q3-fy26-results (accessed 2026-10-17).
48. **NSNEW** — Nscale, convertible financing, 2026-09-25; primary. https://www.nscale.com/press-releases/pre-ipo-convertible-financing (accessed 2026-10-17).
49. **CRUSOE** — Crusoe, Series E announcement, 2025-10-24; primary. https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-e-funding (accessed 2026-10-17).
50. **NRESULT** — NVIDIA, Q2 FY2027 results, 2026-08-26; primary. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/ (accessed 2026-10-17).
51. **ARESULT** — AMD, Q2 2026 results, 2026-08-04; primary. https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results (accessed 2026-10-17).
52. **ORESULT** — Oracle, Q1 FY2027 results, 2026-09-10; primary. https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/ (accessed 2026-10-17).
53. **CQ** — CoreWeave, Q2 2026 10-Q, 2026-08-12; primary. https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm (accessed 2026-10-17).
54. **LUC** — Lucent, FY2000 10-K, 2000-12 (day not verified); primary. https://www.sec.gov/Archives/edgar/data/1006240/000095012300011855/y43690e10-k405.txt (accessed 2026-10-17).
55. **NORT** — Nortel, FY2000 financial review, later SEC exhibit, 2002 (exhibit; reporting date 2000-12-31); primary. https://www.sec.gov/Archives/edgar/data/72911/000113031902000069/t06303aex99-1.htm (accessed 2026-10-17).
56. **CISCO** — Cisco, FY2001 10-K, 2001 (day not verified); primary. https://www.sec.gov/Archives/edgar/data/858877/000109581101505065/f75710e10-k.txt (accessed 2026-10-17).

[NLOI]: https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership-to-Deploy-10-Gigawatts-of-NVIDIA-Systems/default.aspx
[ROUND]: https://openai.com/index/scaling-ai-for-everyone/
[NGUAR]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
[NQ]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[CEQ]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000044/crwv-20260123.htm
[CBACK]: https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm
[XAI]: https://x.ai/news/series-e
[XREP]: https://uk.marketscreener.com/news/musk-s-xai-nears-20-billion-capital-raise-tied-to-nvidia-chips-bloomberg-news-reports-ce7d5bd2db80f125
[NEQ]: https://nvidianews.nvidia.com/news/nvidia-and-nebius-partner-to-scale-full-stack-ai-cloud
[LEQ]: https://lambda.ai/blog/lambda-raises-480m-to-expand-ai-cloud-platform
[LRENT]: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-signs-usd1-5-billion-deal-with-cloud-startup-lambda-to-rent-back-its-own-ai-chips-18-000-gpus-will-be-leased-over-4-years-as-lambda-gears-up-for-its-ipo
[INTEL]: https://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products
[NANT]: https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/
[NK]: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[AQ]: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
[AANT]: https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/
[BOAI]: https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/
[BTPU]: https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm
[BXPV]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
[BQ]: https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm
[NSTAR]: https://au.investing.com/news/company-news/anthropic-offers-blackstone-over-10-yield-in-60b-ai-chip-financing--ft-reports-4696137
[MOWN]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[MAZ]: https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm
[MREV]: https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/
[AAMZ]: https://www.anthropic.com/news/anthropic-amazon-compute
[AMQ]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[AWS38]: https://openai.com/index/aws-and-openai-partnership/
[AWS100]: https://openai.com/index/amazon-partnership/
[GTPU]: https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services
[GEQ]: https://www.streetinsider.com/Reuters/Google%2Bto%2Binvest%2Bup%2Bto%2B%2440%2Bbillion%2Bin%2BAI%2Brival%2BAnthropic/26364234.html
[OSTAR]: https://openai.com/index/five-new-stargate-sites/
[SB]: https://group.softbank/en/news/press/20261001
[STAR]: https://group.softbank/en/news/press/20250122
[CBS1]: https://www.sec.gov/Archives/edgar/data/2021728/000162828026029503/cerebras-sx1amay2026.htm
[CBQ]: https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm
[OCORE]: https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx
[CS1]: https://www.sec.gov/Archives/edgar/data/1769628/000119312525058309/d899798ds1a.htm
[META]: https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
[NEBMS]: https://assets.nebius.com/assets/86625727-9e66-46c1-af79-c27d57434e3c/25-25580-1_Nebius%20Group%20N.V._6-K.pdf
[IRENMS]: https://iren.gcs-web.com/news-releases/news-release-details/iren-secures-97bn-ai-cloud-contract-microsoft
[NS1]: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm
[LMS]: https://lambda.ai/blog/lambda-announces-multibillion-dollar-agreement-with-microsoft-to-deploy-ai-infrastructure-powered-by-tens-of-thousands-of-nvidia-gpus
[TW]: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-079463/tm2523651d3_ex99-1.htm
[TWA]: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001104659-25-102858/tm2529509d1_ex99-3.htm
[CIPH]: https://investors.cipherdigital.com/static-files/14485cf7-a788-4dcf-9d81-a9d806a695d1
[CIPHX]: https://investors.cipherdigital.com/node/10866/pdf
[IRENN]: https://iren.gcs-web.com/news-releases/news-release-details/iren-business-update-and-q3-fy26-results
[NSNEW]: https://www.nscale.com/press-releases/pre-ipo-convertible-financing
[CRUSOE]: https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-e-funding
[NRESULT]: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/
[ARESULT]: https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results
[ORESULT]: https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/
[CQ]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
[LUC]: https://www.sec.gov/Archives/edgar/data/1006240/000095012300011855/y43690e10-k405.txt
[NORT]: https://www.sec.gov/Archives/edgar/data/72911/000113031902000069/t06303aex99-1.htm
[CISCO]: https://www.sec.gov/Archives/edgar/data/858877/000109581101505065/f75710e10-k.txt
