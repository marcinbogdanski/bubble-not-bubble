# AI debt markets: where losses sit if the build disappoints

*Last updated: 2026-10-25 · Cross-checked by: Codex gpt-6-astra, Claude Opus 5.5 · Data: [ai-debt-stack.csv](/data/ai-debt-stack.csv), [credit-spreads.csv](/data/credit-spreads.csv)*

## Summary

- Debt now funds much of the build. AI-related investment-grade (IG) issuance was $330B in H1 2026, 10% of IG issuance against 2% in 2023 (claim 1). Morgan Stanley data via the FT put global AI-related issuance at $466B year to date against $101B a year earlier (claim 3).
- Profitability is not self-funding. S&P expects negative free operating cash flow at all six covered hyperscalers in 2026–27, recovering only in 2029; it warned on 2026-10-19 that financing links can obscure liabilities, without a rating action (claim 7).
- Mapped stack: $494.321B of corporate principal at five issuers, including legacy debt; $572.472B with CoreWeave and selected project securities (claims 9, 11). About $46B also sits in the neocloud ~$80.7B; do not add them.
- Stress is priced, but nothing has defaulted. Latest dated CDS: CoreWeave 1,065.84bp and Oracle 308.25bp on 2026-10-21; Meta a record 114.79bp on 2026-10-22 (claim 25). Project bonds were quoted at 87–94 cents (claim 17); Jupiter loans at 89–91 (claim 13). Access is selective, not shut (claims 4, 28).
- Without defaults, the largest dollar losses could be marks on long IG bonds: a 100/200bp widening on $330B costs about $29–34B / $55–63B (claim 19). Filed fair values already sit $45.811B below face at four issuers (claim 10). First realised credit losses are likelier in construction loans and sub-IG GPU credit (judgement).
- Maturity mismatch: hyperscaler and utility bonds average 16 and 17 years; server lives are 5–5.5 years at Meta and 2–6 at Microsoft (claims 2, 29). CoreWeave's DDTL 5.5 lends five years against three-year contracts (claim 26).
- Biggest uncertainty: whether customer payments and collateral fail together, and who holds the paper. Evidence shows channels (insurers, pensions, BDCs, banks), not positions (claims 20–22).

## Key claims

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | AI-related IG bond issuance | $330B in H1 2026, 10× full-year 2023; 10% of IG issuance against 2% in 2023. Broad AI value-chain issuers, not AI-only use of proceeds | 2026-06-30 (published 2026-10-05) | [KC Fed, Chart 1][kcfed] | primary | A |
| 2 | Weighted-average maturity of IG bonds issued 2025 to August 2026 | Hyperscalers 16 years; utilities 17; market average 10. None published for the full $330B pool | 2026-08 (published 2026-10-05) | [KC Fed, Chart 4][kcfed] | primary | A |
| 3 | Global AI-related debt issuance, Morgan Stanley data | $466B YTD against $101B in the same period of 2025 (FT); $23B in September against $113B in June; US IG AI issuance ~$306B January–August, reportedly nil in September. June bank estimate: ~$250B YTD, ~$500B forecast for the year. Scopes and cutoffs differ | 2026-10-20 | [FT via Financial Post][ft20], [Axios/FT][axiosdebt], [Coinpaper relay][coin], [Morgan Stanley, June][msdebt] | secondary / tertiary; primary for June estimate | B FT attribution; C nine-month/US composite; A June estimate |
| 4 | US public AI bonds and loans underwritten | Almost $330B YTD, almost $100B of it datacenter/neocloud; five datacenter IPOs pulled or delayed. Not the KC Fed sample | 2026-10-23 | [IFR][ifr25] | secondary | B |
| 5 | CDS trading turnover, seven names (Oracle, SpaceX, Alphabet, Amazon, Meta, Broadcom, Nvidia) | >$9B average weekly notional in September against <$2B in July. Turnover, not net protection bought | 2026-09 | [FT via Financial Post][ft20] | secondary | B |
| 6 | Broad US credit indicators | Moody's Baa 6.47% minus Aaa 6.03% = 44bp (monthly yield differential); ICE BofA US HY OAS 323bp (daily). Different constructions; no historical tightness benchmark supplied | 2026-09 / 2026-10-15 | [FRED Baa/Aaa][fred], [FRED HY OAS][fredhy] | primary | A observations; B subtraction |
| 7 | S&P hyperscaler cash-flow view | Capex above $1.3T by 2027; negative free operating cash flow in 2026–27 for Alphabet, Amazon, Microsoft, Meta, Oracle and SpaceX; recovery not until 2029. 2026-10-19 commentary: interconnected financing can obscure liabilities; no hidden-debt estimate; no rating changes warranted | 2026-08-27; commentary 2026-10-19 | [S&P Global Ratings][sp], [Reuters via Boursorama][sp19] | primary forecast / secondary commentary | A forecast; B commentary |
| 8 | External financing need and private-credit scale | Morgan Stanley: $1.5T gap against $2.9T of spending over four years (private credit/ABF $800B, IG $200B, ABS/CMBS $150B, other $350B). Moody's: at least $3T of datacenter investment through 2030; private-credit AUM >$2T in 2026, approaching $4T by 2030, all sectors | 2025-08-06 / 2026-01 | [Morgan Stanley][msgap], [Bloomberg via Insurance Journal][moodys], [Moody's][moodypc] | primary / secondary | A forecast (Morgan Stanley); C (Moody's) |
| 9 | Corporate principal, five issuers | Meta $84B; Alphabet $101.085B; Amazon $132.995B; Microsoft $46.136B; Oracle $130.105B (including $1.468B commercial paper and $5.137B term loan); sum $494.321B. Includes legacy pre-AI debt; excludes leases | 2026-05-31 / 2026-06-30 | [Meta 10-Q][meta], [Alphabet 10-Q][goog], [Amazon 10-Q][amzn], [Microsoft 10-K Note 10][msft], [Oracle 10-K][orcl] | primary | A inputs; B sum |
| 10 | Filed debt fair value against face, four issuers | $310.41B fair value against $356.221B face/perimeter: $45.811B below. Meta $73.31B/$84B (September); Alphabet $94.9B/$101.085B and Microsoft $36.5B/$46.136B (June); Oracle $105.7B/$125B (August). Period-end estimates, not traded marks; rate/credit split not disclosed | 2026-06-30 to 2026-09-30 | [Meta Q3 10-Q Note 9][meta3q], [Alphabet][goog], [Microsoft][msft], [Oracle August 10-Q][orclq] | primary / derived | A values; B sum; C attribution |
| 11 | Dated subtotal of mapped principal | $494.321B corporate + $35.551B CoreWeave + $42.6B selected project securities = $572.472B. $46.251B (CoreWeave, Hut 8, WULF Compute) also sits in the neocloud ~$80.7B: do not add. Kept separate: $65.4B construction packages, $35B chip transaction, $12.5B El Paso financing, $50B later Amazon/Alphabet USD issuance, $4.2B CoreWeave convertible. No combined outstanding-exposure total | mainly 2026-06-30; later flows 2026-07 to 2026-09 | Claims 9, 12, 14–16, 18, 26, 28; [Amazon July term sheet][amznjul], [Alphabet August term sheet][googaug] | derived | B arithmetic; C coverage |
| 12 | Construction loan packages | $65.4B in total: Vantage Texas/Wisconsin ~$38B, JPMorgan/MUFG-led, preliminary benchmark+250bp, final commitment and draws unverified (reported, unverified); Jupiter $18B (reported, unverified); Abilene $2.3B + $7.1B = $9.4B, JPMorgan-led | 2025-09-04 / 2026-09-18 / 2025-05-22 | [Bloomberg Línea][vantage], [Reuters citing FT][jupiter], [Newmark phase 1][abilene1], [Newmark phase 2][abilene2] | secondary / primary | C Vantage and Jupiter; B Abilene sum |
| 13 | Jupiter loans and procedure | $18B quoted at 89–91 cents, syndication stalled (reported, unverified). Force-majeure notice reported 2026-09-24; Oracle said on 2026-10-13 scope is unchanged. Permit hearing 2026-12-07, after the reported 2026-11-23 deadline; effect on that deadline unestablished | 2026-09-18 quote; orders filed 2026-10-16 | [Reuters citing FT][jupiter], [Axios][jupnotice], [Oracle][juporacle], [NMED scheduling order][juporder] | secondary / primary | C quote and notice; A procedural dates and company statement |
| 14 | Hyperion / Beignet project securities | $27.3B private securities; PIMCO-managed accounts majority investors; Meta 20% / Blue Owl 80%; leases start 2029, ~$12.31B initial commitment, four-year terms renewable to 20 years; conditional RVG over the first 16 operating years, declining threshold ~$28B; no liability booked | 2025-10 transaction; 2026-06-30 filing | [Clifford Chance][beignet], [Meta announcement][metajv], [Meta Q2 10-Q Note 5][meta] | primary | A |
| 15 | Meta Louisiana/Texas venture exposure and El Paso | Combined maximum exposure $68.404B = $4.732B equity + $18.476B lease commitments + $3.703B future funding + $41.493B conditional RVGs; no RVG liability booked. El Paso (Sopaipilla): Meta 20% / BlackRock funds 80%, ~$12.5B financing announced; reported ~7.5%, 2048, A+/AA−(EXP) pricing. Rents and RVGs are not extra project principal | 2026-09-30; El Paso 2026-07 | [Meta Q3 10-Q Note 5][meta3q], [Meta El Paso announcement][elpaso], [IBTimes UK][elpasoprice] | primary / secondary | A components; B sum; C pricing |
| 16 | Other selected project notes | QTS Fayetteville $4.6B, 5.700%, due 2036, non-recourse single-asset; Hut 8 River Bend $3.25B + Beacon Point $4.25B = $7.5B, fully amortizing, non-recourse (Beacon 6.129%, due 2042, T+165bp, Baa2); WULF Compute $3.2B secured notes, 7.75%, due 2030-10-15, Google backstop from lease commencement | 2026-04-21 / 2026-Q2 / 2026-06-30 | [Paul Hastings][qts], [Hut 8 Q2 results][hutq], [Beacon Point terms][hut], [TeraWulf 10-Q Notes 8, 10][wulfhtml] | primary | A |
| 17 | Project-bond indicative prices | FT 2026-10-15 version: Beignet <91, QTS <87, Hut Louisiana ~93 / Texas ~91 cents. 2026-10-16 version: <92, <88, ~94 / ~92. Unresolved; identifiers and timestamps unknown. Derived: at modified duration 7.5–11, an 8–12-point discount equals roughly 75–160bp of combined Treasury and spread rise | 2026-10-15 / 2026-10-16 | [FT via Yahoo][prices], [FT via BizNews][pricesalt] | secondary / derived | C marks; B arithmetic; C attribution |
| 18 | Chip-platform financing | Anthropic AI XPV: $35B initial transaction, Apollo-led with Blackstone; funded balance and debt/equity split undisclosed. North Star proposal (reported, unverified): $60B, $42B senior reportedly Broadcom-guaranteed, $18B junior; Blackstone $9B at a 10% coupon / >10% yield; five-year chip leases, ~1.5GW; not closed | 2026-06-09 / 2026-10-17 | [Broadcom][avgo], [Mint citing FT][north], [Reuters via Yahoo][northreut] | primary / secondary | A announcement; C North Star |
| 19 | No-default repricing sensitivity | 5.5% semiannual par bonds, +100bp / +200bp on $330B: 16–17-year bullets −$32.5B to −$33.7B / −$60.9B to −$62.8B; 16-year-average ladder −$29.3B / −$54.6B; 10-year bullet −$24.0B / −$45.9B; range ~$29–34B / ~$55–63B. On $494.3B: −$48.7B to −$50.4B / −$91.2B to −$94.1B. Neocloud ~$80.7B (five-year, 10% coupon): −$13.8B at +500bp, −$24.8B at +1,000bp; all default at 50% recovery ~−$40B | scenario, 2026-10-18 | Claims 1, 9, 28; [KC Fed][kcfed] | derived | B arithmetic; C assumptions and ranking |
| 20 | Bank exposure, Chicago Fed | Banks with ≥$100B assets: ~$450B AI-adjacent C&I commitments, $150B outstanding; outstanding ~0.8% of assets and ~9% of tier 1; commitments ~25% of tier 1. Cites MSCI ~$14.9B bank datacenter lending in the year to 2025-Q3. Not AI-only; nonbank lending unquantified | late 2025 (published 2026-02) | [Chicago Fed Insights][chifed] | primary | A |
| 21 | Nonbank liquidity, IMF | 4 of 10 sampled BDCs (~$90B of $300B assets) have commitments above liquidity buffers; insurers and pensions nearly doubled their illiquid share over a decade, private credit a main driver. Not AI-specific | 2026-10 | [IMF GFSR, Chapter 1][imf] | primary | A |
| 22 | Named lenders and holder channels | Blackstone and Magnetar (CoreWeave facilities, with CDPQ); Blackstone Credit & Insurance (DDTL 4.0); PIMCO accounts (Beignet); BCI and Liberty Mutual (Crusoe). KC Fed names insurer, pension and private-credit channels, AI holdings unquantified; Open Markets argues exposure reaches policyholders and retirement funds | 2023 to 2026-10-16 | [Blackstone][crwv24], [DDTL 4.0][crwv4], [Crusoe][crusoe], [KC Fed][kcfed], [Open Markets][omi] | primary / advocacy | A named participation; B advocacy |
| 23 | Blackstone AI book | Q3 AUM $1,368.3B, inflows $63.3B, firmwide. Management: AI debt/equity ~7% of AUM, mostly datacenters, initial 15–20-year leases, 96% IG counterparties. Not proof against credit loss | 2026-10-22 | [Blackstone results][bx25], [call transcript][bxcall25], [Reuters][bxreut25] | primary / secondary | A results; B attribution |
| 24 | Circular relationships, BIS authors | 46.4% by value of AI-to-AI investment deals in 2021–2025 also involved commercial supply-chain relationships; not a share of current AI debt | 2026-10-01 | [BIS Bulletin 137][bis137] | primary | A |
| 25 | Five-year CDS, latest dated snapshots | CoreWeave 1,065.84bp and Oracle 308.25bp (FactSet via CNBC; Oracle 315bp CNBC / 322bp FT on 2026-10-19); Meta 114.79bp Markit / ~119.3bp ICE intraday, a record. Distinct vendor snapshots, not closes | 2026-10-21 / 2026-10-22 | [CoreWeave note](/research/stack/coreweave), [Oracle note](/research/stack/oracle), [Reuters][metacds25], [Bloomberg via Yahoo][metaice25] | secondary | B reporting; C marks |
| 26 | CoreWeave debt, bonds and facilities | $35.551B principal; $4.413B due in the rest of 2026. 9.75% 2031 notes 15.97% / 79.25 and 9.625% 2032 low 77.5 / 15.70% on 2026-10-20. DDTL 4.0 ~$7.5B rising to $8.5B, A3, SOFR+225bp, non-recourse; DDTL 5.5 $2.6B, Ba2/BB+, SOFR+550bp, ~5-year debt against ~3-year average contracts; $4.2B 2.875% convertible due 2033 | 2026-06-30; marks 2026-10-20; convertible 2026-09-22 | [CoreWeave note](/research/stack/coreweave) | primary / secondary | A filings; C marks |
| 27 | Oracle rating | S&P BBB→BBB−, stable outlook | 2026-07 | [Oracle note](/research/stack/oracle) | secondary | B |
| 28 | Neocloud debt and new facilities | Listed-layer debt ~$80.7B including CoreWeave, mixed dates and bases. New: Nebius $3.5B 364-day secured facility, SOFR+2.75% stepping to 3.50%; TeraWulf ~$150M added committed revolver capacity; Lambda $1.008B DDTL at 6.78%, Baa1/A(low), two IG offtakers, commissioning-linked draws. Capacities, not cash drawn | 2026-06-30 to 2026-10-23 | [Neocloud note](/research/stack/neoclouds-other) | primary / derived | A terms; B sum |
| 29 | Server and network accounting lives | Meta 5–5.5 years; Microsoft 2–6 years. Accounting estimates, not measured GPU economic life | 2025-12-31 / 2026-06-30 | [Meta note](/research/stack/meta), [Microsoft note](/research/stack/microsoft) | primary | A |

## Analysis

**Who pays, and from what.** Advertising, software, retail and cloud cash flows service hyperscaler debt. That cushion is strong, but S&P expects all six covered hyperscalers to run negative free operating cash flow in 2026–27 (claim 7). The build is partly borrowed. Morgan Stanley put the external gap at $1.5T, with $800B expected from private credit and asset-backed finance (claim 8).

**Issuance and access.** The KC Fed, Morgan Stanley and IFR series cover different issuers and cutoffs (claims 1, 3, 4). None measures outstanding debt. The Morgan Stanley data show a sharp September slowdown, and IFR reports delayed datacenter financing. Yet lenders still commit to well-supported structures: Lambda's amortizing loan with IG offtakers, Nebius's secured bank line, TeraWulf's revolver (claim 28), CoreWeave's convertible (claim 26). Access is selective, not shut.

**The mapped stack and its overlaps.** The $572.472B subtotal (claim 11) mixes snapshot dates and includes legacy corporate debt. It is a map, not a census. CoreWeave, Hut 8 and WULF Compute debt also appears in the neocloud total, so the two cannot be added. Construction packages, chip platforms, El Paso and later issuance are flows or capacities and stay outside it. Leases, guarantees and project principal overlap: Meta's $68.404B maximum exposure includes $41.493B of conditional RVGs supporting the same projects the bonds finance (claim 15).

**Project credit differs from GPU credit.** Hyperion bondholders depend mainly on Meta's credit. The ~$28B RVG threshold roughly covers the $27.3B of securities, but pays only on non-renewal and other conditions; Meta is not an unconditional guarantor (claim 14). QTS creditors hold project claims, not Microsoft notes. Hut's amortizing notes cut balloon risk but keep completion and tenant risk (claim 16). GPU loans depend on equipment collateral and renewals: CoreWeave's DDTL 5.5 lends five years against three-year contracts (claim 26).

**Maturity mismatch.** Hyperscaler and utility bonds average 16 and 17 years (claim 2). Server lives are 5–5.5 years at Meta and 2–6 at Microsoft (claim 29), accounting estimates rather than resale values. Long-dated creditors rely on cash generation across several hardware generations after replacement capex; diversified issuers' bonds do not rest on the first chip cohort. For project and equipment debt, amortization, contracts, residual values and guarantees set the mismatch security by security.

**How stress transmits.** CDS, bonds and new-deal discounts reprice first (claims 17, 25). Floating rates, draw conditions, collateral tests and construction deadlines pass stress on before maturity. Fixed coupons do not reset; issuers meet the new price when they borrow again. An 8–12-point project-bond discount fits 75–160bp of combined rate and spread rise at assumed duration (claim 17), so it does not on its own show distress. The broad indicators (claim 6) are built differently, and nothing here benchmarks them as tight.

**Where losses land without defaults.** Equity takes first loss. Among creditors, the largest dollar marks can be on long IG bonds: about $29–34B at +100bp on $330B, about $55–63B at +200bp (claim 19). That compares with $13.8B for a +500bp neocloud repricing and ~$40B if every listed neocloud defaulted at 50% recovery. Filed fair values already sit $45.811B below face at four issuers (claim 10); filings do not split rates from credit. Marks are unrealised for holders who keep the bonds. Realised credit losses are likelier first in undistributed construction loans and sub-IG GPU credit. That is a mechanism-based judgement, not a measured forecast.

**Holders and contagion.** Named providers show participation, not current beneficial ownership (claim 22). The Chicago Fed sizes large-bank exposure against tier 1 capital (claim 20). The IMF flags liquidity mismatches at BDCs and rising illiquid holdings at insurers and pensions (claim 21). The BIS finds 46.4% of AI-to-AI investment deals also carry supply links (claim 24), so demand, financing and collateral can fail together. A telecom-style cycle would run from delays and weak cash conversion to closed refinancing, restructurings and collateral sales; unlike fiber, chips can lose relevance during workouts. Systemic bank stress would need retained leverage, correlated guarantees or funding withdrawal; isolated price falls do not establish it. This is a conditional mechanism, not a default forecast. [Richmond Fed][telecom], [BIS][bis]

## Open questions

- **Issuance measures.** KC Fed, Morgan Stanley/FT and IFR differ in issuers, scope and cutoff; the $466B YTD figure is not reconciled to the earlier nine-month figure (claims 1, 3, 4). A matched series would settle it.
- **Project marks.** The two FT versions in claim 17 disagree. TRACE prints with identifiers and timestamps would settle them.
- **Loss ranking.** Whether the biggest losses fall on IG marks or on construction and GPU credit depends on an unobserved spread shock and assumed duration; no source measures the loss distribution (claim 19).
- **Holders.** No census of insurer, pension or fund holdings of AI instruments exists here; Schedule D, N-PORT and BDC schedules could bridge it. Redemption requests rose, but no AI-caused gate is verified ([CRISIL][flows]). Fitch flags leverage layered across holding companies, projects and GPUs ([Fitch][fitch]).
- **Counterevidence.** Morgan Stanley in June stressed strong hyperscaler credit and diversified collateral; BIS judged risks moderate in January ([Morgan Stanley][msdebt], [BIS][bisjan]). S&P's forecast and October stress weaken that case without disproving it.
- Vantage's final terms and the legal effect of Jupiter's deadline are unverified.

## Signals to watch

| Signal | Current value | As of | Why it matters |
|--------|---------------|-------|----------------|
| AI credit CDS and bond yields | CoreWeave 1,065.84bp, Oracle 308.25bp; Meta 114.79bp; CoreWeave 2031 yield 15.97% | 2026-10-21 / 2026-10-22 | Earliest market read of funding stress; prices alone are not defaults |
| Project-bond prints | Indicative 87–94 cents, two unresolved versions | 2026-10-16 | Separates rate and duration effects from credit distress |
| Jupiter permit and loans | $18B at 89–91 cents; permit hearing 2026-12-07 | 2026-09-18 / 2026-10-16 | First test of an Oracle-tenanted construction loan |
| AI debt issuance flow | $466B YTD; $23B in September against $113B in June | 2026-10-20 | Whether the September slowdown persists |
| New GPU and neocloud facilities | Nebius $3.5B; Lambda $1.008B; TeraWulf ~$150M | 2026-10-23 | Selective access; watch draws, security and covenants |
| BDC Q3 schedules of investments | Due early-to-mid November | 2026-11 | Position-level marks and non-accruals on datacenter and GPU loans |
| Rating actions | Oracle BBB− stable at S&P | 2026-07 | A cut would put Oracle debt below IG |
| Broad credit spreads | Baa–Aaa 44bp; HY OAS 323bp | 2026-09 / 2026-10-15 | Whether AI stress spreads to the wider credit market |

[kcfed]: https://www.kansascityfed.org/research/economic-bulletin/beyond-valuations-long-term-financial-risks-from-the-ai-build-out/
[ft20]: https://financialpost.com/financial-times/ai-debt-worries-spark-surge-in-default-insurance-trading
[axiosdebt]: https://www.axios.com/2026/10/16/wall-street-limit-ai-spending-debt
[coin]: https://coinpaper.com/37113/ai-debt-issuance-falls-from-113b-to-23b-while-oracle-loans-trade-below-par
[msdebt]: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/ai-debt-surge-carolyn-campbell-vishwas-patkar
[msgap]: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/credit-markets-ai-financing-gap-vishy-tirupattur-vishwas-patkar
[ifr25]: https://www.ifre.com/bonds/2502504/coreweave-rout-freezes-data-centre-financing
[fred]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA,AAA&cosd=2026-09-01&coed=2026-09-30
[fredhy]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-10-15&coed=2026-10-15
[sp]: https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says
[sp19]: https://www.boursorama.com/bourse/actualites/les-principaux-hyperscalers-pourraient-avoir-un-endettement-lie-a-l-ia-plus-important-qu-on-ne-le-pense-actuellement-met-en-garde-s-p-global-83db047e4cfe79ccfdc7bad05d42e61b
[moodys]: https://www.insurancejournal.com/news/national/2026/01/12/853930.htm
[moodypc]: https://www.moodys.com/web/en/us/insights/credit-risk/outlooks/private-credit-2026.html
[meta]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
[meta3q]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm
[goog]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
[googaug]: https://www.sec.gov/Archives/edgar/data/1652044/000119312526338750/d159970dfwp.htm
[amzn]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[amznjul]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926081334/tm2619352d3_fwp.htm
[msft]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[orcl]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
[orclq]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
[vantage]: https://www.bloomberglinea.com/negocios/bancos-alistan-deuda-por-us38000-millones-para-centros-de-datos-de-oracle/
[jupiter]: https://www.aol.com/articles/oracles-18-billion-data-center-220302000.html
[abilene1]: https://www.nmrk.com/insights/press-releases/newmark-arranges-2-3-billion-construction-financing-for-206-mw-build-to-suit-data-center
[abilene2]: https://www.prnewswire.com/news-releases/newmark-facilitates-7-1-billion-construction-loan-to-develop-ai-data-center-302463532.html
[jupnotice]: https://www.axios.com/2026/09/24/oracle-force-majeure-blue-owl-openai
[juporacle]: https://www.oracle.com/news/announcement/project-jupiter-is-expected-to-generate-13-billion-in-economic-impact-2026-10-13/
[juporder]: https://www.env.nm.gov/opf/wp-content/uploads/sites/13/2026/07/2026-10-16-AQB-26-57-2nd-Amnd-Sch-Order-filed.pdf
[beignet]: https://www.cliffordchance.com/insights/thought_leadership/trends/2026/energy-and-resources-insights-2026.html
[metajv]: https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
[elpaso]: https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/amp/
[elpasoprice]: https://www.ibtimes.co.uk/meta-blackrock-ai-data-centre-deal-1811227
[qts]: https://www.paulhastings.com/en-GB/news/paul-hastings-advises-the-initial-purchasers-on-qts-data-centers-usd4-6-billion-notes-offering
[hutq]: https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results
[hut]: https://www.hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data
[wulfhtml]: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm
[prices]: https://ca.finance.yahoo.com/news/investors-dump-data-centre-bonds-132608292.html
[pricesalt]: https://www.biznews.com/global-investing/investors-dump-data-centre-bonds
[avgo]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
[north]: https://www.livemint.com/ai/artificial-intelligence/anthropic-offers-blackstone-double-digit-yield-in-chip-financing-deal-what-the-60-billion-deal-entails-11792204532812.html
[northreut]: https://finance.yahoo.com/technology/ai/articles/anthropic-offers-blackstone-double-digit-010109537.html
[chifed]: https://chicagofed.org/publications/chicago-fed-insights/2026/ai-tail-risk-for-banks
[imf]: https://www.imf.org/-/media/files/publications/gfsr/2026/october/english/ch1.pdf
[crwv24]: https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/
[crwv4]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex991.htm
[crusoe]: https://crusoe.ai/newsroom/upper90-closes-usd225m-credit-facility-to-crusoe-to-expand-ai-cloud/
[omi]: https://www.openmarketsinstitute.org/publications/report-brace-for-impact-protecting-people-and-the-economy-when-the-ai-bubble-burst
[bx25]: https://www.blackstone.com/blackstone3q26earningspressrelease/
[bxcall25]: https://stockanalysis.com/stocks/bx/transcripts/714082-q3-2026/
[bxreut25]: https://uk.marketscreener.com/news/blackstone-s-profit-falls-as-choppy-market-tempers-investment-exits-ce785cdedb8bf323
[bis137]: https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms
[metacds25]: https://www.marketscreener.com/news/meta-s-credit-risk-indicator-jumps-to-record-high-after-results-ce785cdedd89fe23
[metaice25]: https://finance.yahoo.com/technology/ai/articles/meta-credit-risk-gauge-hits-125603234.html
[telecom]: https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/economic_quarterly/2003/fall/pdf/wolman.pdf
[bis]: https://www.bis.org/publications/qr-202603/financing-ai-infrastructure-boom-on-and-off-balance-sheet-borrowing
[bisjan]: https://www.bis.org/publications/bulletin-120-financing-ai-boom-cash-flows-debt
[flows]: https://integraliq.crisil.com/en/homepage/what-we-think/all-our-thinking/reports/2026/09/us-private-credit-trends-momentum-eases-in-the-second-quarter.html
[fitch]: https://your.fitch.group/rs/732-CKH-767/images/APLMA_Fitch_L%26W_Data%20Centre%20Whitepaper.pdf
