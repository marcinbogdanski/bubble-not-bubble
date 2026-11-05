# AI debt markets: where losses sit if the build disappoints

*Last updated: 2026-11-05 · Cross-checked by: Codex gpt-6-astra, Claude Opus 5.5 · Data: [ai-debt-stack.csv](/data/ai-debt-stack.csv), [credit-spreads.csv](/data/credit-spreads.csv)*

## Summary

- Credit access is selective. Microsoft priced $25B at fixed-rate issue yields of 4.869–6.356%; Oracle closed $10B at 7.062–8.667%. Both sit well below the stressed CoreWeave secondary-market yields (claims 26, 30–31). These are different issuers, securities and observation times, not a matched spread series.
- Meta's negative outlook now reaches Beignet and Sopaipilla, both still A+. This is observable transmission of tenant risk into project credit, not a default (claims 14–15, 27).
- Trepp's datacenter CMBS senior averages widened while comparable broader CMBS medians held steady. Every sampled underlying loan remained current; the publication uses pre-window marks through 23 October (claim 33).
- The mapped principal subtotal is $654.497B, including legacy corporate borrowing and mixed snapshot dates. It excludes subsequent issues and undrawn commitments; neocloud overlaps prevent adding the layer totals (claims 9, 11).
- Borrowing is extending through SPVs, vendor support and equipment finance. Committed financing and contingent guarantees cannot be added as separate funded exposures (claims 18, 28, 34).
- Without defaults, long IG bonds can generate large dollar marks; filed fair values sit $53.323B below the matched face perimeter. First realized credit losses remain likelier in construction and weaker GPU credit (claims 10, 19; judgement).
- The largest uncertainty remains who retains the debt and whether customer payments, guarantees and equipment values weaken together.

## Key claims

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | AI-related IG bond issuance | $330B in H1 2026, 10× full-year 2023; 10% of IG issuance against 2% in 2023. Broad AI value-chain issuers, not AI-only use of proceeds | 2026-06-30 (published 2026-10-05) | [KC Fed, Chart 1][kcfed] | primary | A |
| 2 | Weighted-average maturity of IG bonds issued 2025 to August 2026 | Hyperscalers 16 years; utilities 17; market average 10. None published for the full $330B pool | 2026-08 (published 2026-10-05) | [KC Fed, Chart 4][kcfed] | primary | A |
| 3 | Global AI-related debt issuance, Morgan Stanley data | $466B year to date against $101B in the same period of 2025. Scope differs from KC Fed and IFR; issuance is not outstanding debt | 2026-10-20 | [FT via Financial Post][ft20] | secondary | B attribution |
| 4 | US public AI bonds and loans underwritten | Almost $330B YTD, almost $100B of it datacenter/neocloud; five datacenter IPOs pulled or delayed. Not the KC Fed sample | 2026-10-23 | [IFR][ifr25] | secondary | B |
| 7 | S&P hyperscaler cash-flow view | Negative free operating cash flow forecast for all six covered hyperscalers in 2026–27, recovery in 2029. Company results and funding plans are in the [Microsoft](/research/stack/microsoft), [Alphabet](/research/stack/alphabet), [Amazon](/research/stack/amazon) and [Oracle](/research/stack/oracle) notes; agency forecasts are not company guidance | 2026-08-27 forecast; results 2026-10-28/29 | [S&P][sp]; linked issuer notes | primary forecast / primary results | A |
| 8 | External financing need and private-credit scale | Morgan Stanley: $1.5T gap against $2.9T of spending over four years (private credit/ABF $800B, IG $200B, ABS/CMBS $150B, other $350B). Moody's: at least $3T of datacenter investment through 2030; private-credit AUM >$2T in 2026, approaching $4T by 2030, all sectors | 2025-08-06 / 2026-01 | [Morgan Stanley][msgap], [Bloomberg via Insurance Journal][moodys], [Moody's][moodypc] | primary / secondary | A forecast (Morgan Stanley); C (Moody's) |
| 9 | Mapped corporate principal, five issuers | $563.746B, including legacy debt, excluding leases. September face balances for Meta, Alphabet, Amazon and Microsoft; Oracle retains its May all-borrowings principal schedule because its August carrying value is not comparable. Components and dates in CSV; later issues excluded | 2026-09-30 / Oracle 2026-05-31 | [Meta](/research/stack/meta), [Alphabet](/research/stack/alphabet), [Amazon](/research/stack/amazon), [Microsoft](/research/stack/microsoft), [Oracle](/research/stack/oracle); [CSV](/data/ai-debt-stack.csv) | primary / derived | A inputs; B sum; C mixed-date coverage |
| 10 | Filed debt fair value against matched face, four issuers | $323.210B fair value against $376.533B face/perimeter: $53.323B below. September Meta, Alphabet notes and Microsoft; August Oracle. Alphabet excludes $1.221B other debt from the face comparator. Period-end estimates, not traded marks; rate/credit split undisclosed | 2026-08-31 / 2026-09-30 | [Meta 10-Q][meta3q], [Alphabet 10-Q][goog3], [Microsoft 10-Q][ms-q], [Oracle 10-Q][orclq] | primary / derived | A values; B arithmetic; C attribution |
| 11 | Dated subtotal of mapped principal | $563.746B corporate + $35.551B CoreWeave + $55.2B selected project securities = $654.497B. CoreWeave, Hut 8 and WULF Compute overlap the neocloud total. September Amazon/Alphabet stocks include their summer issuance; do not add it again. November corporate issues, construction commitments, chip platforms and undrawn facilities remain separate | mixed 2026-05 to 2026-11 disclosures | Claims 9, 14–16, 26; [CSV](/data/ai-debt-stack.csv) | derived | B arithmetic; C coverage |
| 12 | Construction loan packages | $65.4B in total: Vantage Texas/Wisconsin ~$38B, JPMorgan/MUFG-led, preliminary benchmark+250bp, final commitment and draws unverified (reported, unverified); Jupiter $18B (reported, unverified); Abilene $2.3B + $7.1B = $9.4B, JPMorgan-led | 2025-09-04 / 2026-09-18 / 2025-05-22 | [Bloomberg Línea][vantage], [Reuters citing FT][jupiter], [Newmark phase 1][abilene1], [Newmark phase 2][abilene2] | secondary / primary | C Vantage and Jupiter; B Abilene sum |
| 13 | Jupiter loans and procedure | $18B quoted at 89–91 cents, syndication stalled (reported, unverified). Force-majeure notice reported 2026-09-24; Oracle said on 2026-10-13 scope is unchanged. Permit hearing 2026-12-07, after the reported 2026-11-23 deadline; effect on that deadline unestablished | 2026-09-18 quote; orders filed 2026-10-16 | [Reuters citing FT][jupiter], [Axios][jupnotice], [Oracle][juporacle], [NMED scheduling order][juporder] | secondary / primary | C quote and notice; A procedural dates and company statement |
| 14 | Beignet / Hyperion project notes | $27.3B amortizing notes due May 2049; A+ affirmed, outlook negative. S&P ties construction-phase credit to Meta, with a one-notch adjustment for security-package weakness and no direct asset pledge. Lease and conditional residual-value support terms in the Meta note | 2026-11-02 | [S&P][beignet-new]; [Meta note](/research/stack/meta) | primary | A |
| 15 | Sopaipilla / El Paso project notes | About $12.6B amortizing notes due November 2048; A+ affirmed, outlook negative. Meta is an irreplaceable material counterparty; construction-phase rating follows Meta with a one-notch security adjustment. Not new issuance in this window; rents and guarantees are not extra project principal | 2026-11-02 | [S&P][sopaipilla]; [Meta exposure](/research/stack/meta) | primary | A |
| 16 | Other selected project notes | QTS Fayetteville $4.6B, 5.700%, due 2036, non-recourse single-asset; Hut 8 River Bend $3.25B + Beacon Point $4.25B = $7.5B, fully amortizing, non-recourse (Beacon 6.129%, due 2042, T+165bp, Baa2); WULF Compute $3.2B secured notes, 7.75%, due 2030-10-15, Google backstop from lease commencement | 2026-04-21 / 2026-Q2 / 2026-06-30 | [Paul Hastings][qts], [Hut 8 Q2 results][hutq], [Beacon Point terms][hut], [TeraWulf 10-Q Notes 8, 10][wulfhtml] | primary | A |
| 18 | Anthropic chip-platform financing | $63B committed SPV financing, deliveries expected from 2027. Banks arrange first lien; Blackstone provides committed second lien. Broadcom supplies contingent residual-value support, not cash investment or an unconditional guarantee of the entire transaction. Backstop formula/cap in the custom-silicon note; funded balance undisclosed | 2026-10-26/27 | [Banks][xpu], [Broadcom 8-K][avgo-k]; [custom-silicon note](/research/stack/amd-broadcom-custom-silicon) | primary | A |
| 19 | No-default repricing sensitivity | 5.5% semiannual par bonds, +100bp / +200bp on $330B: 16–17-year bullets lose $32.5–33.7B / $60.9–62.8B; 16-year-average ladder $29.3B / $54.6B. Illustrative neocloud pool ~$80.7B, five-year 10% coupon: −$13.8B at +500bp; default at 50% recovery ~−$40B. Scenarios, not current marks or measured loss forecasts | scenario 2026-10-18 | Claims 1, 2; [neocloud pool](/research/stack/neoclouds-other) | derived | B arithmetic; C assumptions |
| 20 | Bank exposure, Chicago Fed | Banks with ≥$100B assets: ~$450B AI-adjacent C&I commitments, $150B outstanding; outstanding ~0.8% of assets and ~9% of tier 1; commitments ~25% of tier 1. Cites MSCI ~$14.9B bank datacenter lending in the year to 2025-Q3. Not AI-only; nonbank lending unquantified | late 2025 (published 2026-02) | [Chicago Fed Insights][chifed] | primary | A |
| 21 | Nonbank liquidity, IMF | 4 of 10 sampled BDCs (~$90B of $300B assets) have commitments above liquidity buffers; insurers and pensions nearly doubled their illiquid share over a decade, private credit a main driver. Not AI-specific | 2026-10 | [IMF GFSR, Chapter 1][imf] | primary | A |
| 22 | Named lender and holder channels | Blackstone/Magnetar and CDPQ (CoreWeave facilities); BCI/Liberty Mutual (Crusoe). New chip SPV: BofA, Citi, Morgan Stanley and Blackstone. SpaceX lease commitments include Apollo, BlackRock, Goldman Sachs and KKR-advised accounts. Participation does not establish retained beneficial ownership | announcements through 2026-10-26 | [Blackstone][crwv24], [Crusoe][crusoe], [banks][xpu], [SpaceX][spacex] | primary | A named participation |
| 24 | Circular relationships, BIS authors | 46.4% by value of AI-to-AI investment deals in 2021–2025 also involved commercial supply-chain relationships; not a share of current AI debt | 2026-10-01 | [BIS Bulletin 137][bis137] | primary | A |
| 25 | Five-year CDS, latest dated snapshots | CoreWeave 1,148bp (S&P GMI, 26 October 11:42 GMT); Oracle 274.365bp (Bloomberg, 28 October, published 3 November); Meta 114.79bp (Markit, 22 October). Different vendors/times, not synchronized closes; alternative Oracle tick unresolved | 2026-10-22 to 2026-10-28 | [CoreWeave note](/research/stack/coreweave), [Seoul Economic Daily][orcl-cds], [Reuters][metacds25] | secondary | B reporting; C market marks |
| 26 | CoreWeave debt and market stress | Principal and secured-facility terms in linked note. Latest reported unsecured 2031 low 79.5 cents; 2030/2032 yields >15%. Reported, unverified against TRACE; coupon/CUSIP and fixing time unspecified. No disclosed default established by these marks | report 2026-11-05 | [CoreWeave note](/research/stack/coreweave) | primary / secondary | A filed terms; C quotes |
| 27 | Corporate rating actions | Meta AA−/negative; Broadcom A−/stable after positive outlook. Ratings affirmed, not downgraded. Oracle S&P BBB−/stable; no below-IG action established. Meta cash-flow forecasts conflict between secondary reports; see issuer note | Meta 2026-10-30; Broadcom 2026-10-29; Oracle 2026-11-02 issue expectations | [S&P project actions][sopaipilla], [Cbonds][avgo-rating], [Reuters][meta-rating-reuters], [Oracle FWP][orcl-new-fwp]; [Meta](/research/stack/meta) | primary / secondary | A S&P/issue expectations; B reported action |
| 28 | Neocloud financing access | IREN equipment refinance closed; TeraWulf executed Google support for anticipated Anthropic project financing. Neither leased revenue nor a backstop is a drawn loan. Debt balances, refinance amount and contract terms remain in the owning note | 2026-10-28 / 2026-11-04 | [Neocloud note](/research/stack/neoclouds-other); [IREN][iren-fin], [TeraWulf][wulf-new] | primary | A |
| 29 | Server and network accounting lives | Meta 5–5.5 years; Microsoft 2–6 years. Accounting estimates, not measured GPU economic life | 2025-12-31 / 2026-06-30 | [Meta note](/research/stack/meta), [Microsoft note](/research/stack/microsoft) | primary | A |
| 30 | Microsoft new-issue bond pricing | $25B across ten series, two floating-rate. Eight fixed-rate issue YTMs 4.869–6.356%; Treasury spreads +25–105bp; maturities 2028–2066. Priced 29 October; 4 November 8-K files issuance documents. Issue yields, not subsequent trading yields | 2026-10-29 pricing; 2026-11-04 filing | [Microsoft FWP][ms-fwp], [8-K][ms-close] | primary | A |
| 31 | Oracle new-issue bond pricing | $10B notes, closed 4 November alongside equity described in issuer note. 2029/2031/2033/2037/2046 YTMs 7.062/7.464/7.851/8.015/8.667%; Treasury spreads +240/275/305/310/335bp. Executes the Investor Day funding plan, not an additional requirement | 2026-11-02 pricing; 2026-11-04 close | [Oracle FWP][orcl-new-fwp], [8-K][orcl-new-close]; [Oracle note](/research/stack/oracle) | primary | A |
| 32 | Meta new corporate note offering | $15B: $3.25B/5.850%/2031; $3.25B/6.250%/2033; $4B/6.550%/2036; $1.75B/7.350%/2046; $2.75B/7.500%/2056. Estimated net $14.9B. Coupons, not yields. Expected delivery 5 November; prospectus alone does not establish settlement | prospectus 2026-11-04 | [Meta prospectus][meta-notes]; [Meta note](/research/stack/meta) | primary | A terms |
| 33 | Datacenter CMBS evaluated spreads | Senior originally-AAA fixed-rate average T+182bp, +21bp that week; floating SOFR+199bp, +24bp. VDCM 2025-AZ A: T+205bp, price 94.6; SWCH 2025-DATA A: SOFR+243bp. All sampled loans current, none in special servicing. Equal-weighted senior averages; other SASB/conduit medians essentially unchanged that week | observations through 2026-10-23; published 2026-10-27 | [Trepp original][trepp] | primary data-provider calculations | A |
| 34 | Additional secured financing channels | AirTrunk A$4.25B green loan for SYD3 development; capacity, not revenue. Amazon discretionary secured hardware facility and SpaceX conditional GPU finance lease are detailed in their notes; neither announcement establishes a current drawn balance | 2026-10-26 to 2026-10-30 | [AirTrunk][airtrunk-new]; [Amazon](/research/stack/amazon), [SpaceX](/research/stack/labs-other) | primary | A announcements |

## Analysis

**Access and cash conversion.** Advertising, software, retail and cloud cash flows still support hyperscaler borrowing, but capex increasingly requires external finance. The latest company cash flows differ substantially; the issuer notes own those results (claim 7). S&P's sector forecast is not a uniform quarterly observation. Oracle's new funding executes its announced bridge, while its targeted cash-flow recovery still depends on delivery, customer prepayments and vendor finance.

The Microsoft and Oracle term sheets demonstrate functioning IG markets at markedly different borrowing costs (claims 30–31). Meta's note prospectus also shows access, but expected delivery is not completed settlement (claim 32). Its common-stock forward offering supplies no initial cash to Meta; the preferred greenshoe is completed funding. Amounts and timing are detailed in the [Meta note](/research/stack/meta); the [forward prospectus][meta-forward] and [note prospectus][meta-notes] distinguish the cash flows. Announced supplier equity participation does not prove receipt of proceeds.

**Map, not census.** The principal subtotal combines September corporate balances with Oracle's May principal schedule and CoreWeave's June debt (claims 9, 11). It includes legacy borrowing. Summer Amazon and Alphabet issuance is inside their September balances and must not be added again. November corporate deals remain separate flows. Sopaipilla's disclosed notes are included as project principal; the agency action is not a fresh issue. Construction commitments, chip SPVs, leases and guarantees are excluded from the subtotal because funded balances and overlaps are incomplete.

**Where risk travels.** S&P explicitly links the construction-phase ratings of Beignet and Sopaipilla to Meta, with weaker security than a direct asset pledge (claims 14–15). That makes the outlook changes concrete evidence of counterparty transmission. Conditional residual-value support should not be read as an unconditional debt guarantee. Broadcom's support of the Anthropic chip SPV similarly redistributes loss risk while connecting the supplier to its customer's payment performance (claim 18).

IREN's closed refinance and TeraWulf's executed Google support show that collateral and strong counterparties still attract funding (claim 28). Amazon's hardware facility and SpaceX's lease commitment extend the same financing channel, but their announcements do not disclose current draws (claim 34). Nvidia/Nscale guarantee discussions remain **reported, unverified**, grade C; the [neocloud note](/research/stack/neoclouds-other) tracks them. Talks do not support adding a signed guarantee.

**Marks before losses.** Trepp supplies a better identified project-credit signal than unattributed indicative bond quotes: senior datacenter CMBS widened relative to the broader sample, with every underlying loan still current (claim 33). This supports sector repricing, not a distressed-event claim. CDS and secondary bond prices likewise price risk without proving missed payments (claims 25–26). Fixed coupons do not reset; higher rates bite at new borrowing or refinancing.

Long maturities expose IG investors to duration and repeated hardware replacement cycles (claims 2, 29). The illustrative $330B pool loses roughly $29–34B at a one-percentage-point yield increase, without default (claim 19). The filed fair-value shortfall is a different, observed measure; neither separates rates from credit. Construction and GPU lenders face completion, collateral and renewal risk before maturity. Named providers establish participation, not retained positions; bank commitments and nonbank liquidity mismatches describe possible transmission channels (claims 20–22), not measured AI losses. The circular relationships documented by BIS reinforce the risk of correlated payments and collateral (claim 24).

## Open questions

- **Comparable balances.** A current all-borrowings principal schedule for Oracle is needed to replace the May component without mixing carrying and face values. The subtotal remains a dated map.
- **Pricing.** CoreWeave's latest reported bond low lacks a coupon/CUSIP and fixing time. Oracle CDS vendor snapshots disagree; no synchronized close or unsupported exact tick is substituted.
- **Settlement and drawdowns.** Meta's note closing, forward-sale cash receipt, new facility draws and final SPV distributions need subsequent disclosures. Vendor commitments alone do not establish cash delivered.
- **Agency forecasts.** Secondary reports conflict on Meta's projected cash deficit. The rating action is verified; disputed forecasts are not used in the loss arithmetic.
- **Counterevidence.** IG issuance, IREN's refinance and current CMBS loans argue against a general funding shutdown. Whether this access survives weaker cash conversion is unresolved.
- **Holders and construction.** Retained bank/insurer/fund positions, Vantage's final terms and Jupiter's deadline effect remain unverified. They determine whether project stress stays local or propagates.

## Signals to watch

| Signal | Current value | As of | Why it matters |
|--------|---------------|-------|----------------|
| IG new-issue pricing | Microsoft T+25–105bp; Oracle T+240–335bp | 2026-10-29 / 2026-11-02 | Access survives at different costs; compare matched tenors next |
| Weak-issuer market stress | CoreWeave CDS 1,148bp; reported bond yields >15% | 2026-10-26 / report 2026-11-05 | Refinancing pressure, not a default trigger |
| Datacenter CMBS | Fixed T+182bp; floating SOFR+199bp; loans current | 2026-10-23 marks, 2026-10-27 publication | Watch spread persistence and actual arrears |
| Tenant-linked project ratings | Beignet and Sopaipilla A+/negative | 2026-11-02 | Meta credit quality transmits to project creditors |
| Jupiter construction | Loans reported at 89–91 cents; permit hearing 7 December | quote 2026-09-18; order 2026-10-16 | Completion deadlines can constrain funding |
| Commitments becoming cash | SPV, hardware facility and lease draws undisclosed | 2026-11-05 review | Avoid counting commitments as outstanding debt |
| BDC investment schedules | Q3 releases due in November | 2026-11 | Position-level marks and non-accruals |
| Corporate ratings | Oracle BBB−/stable; Meta AA−/negative; Broadcom A−/stable | 2026-10-29 to 2026-11-02 | Outlook actions remain distinct from downgrades |

[kcfed]: https://www.kansascityfed.org/research/economic-bulletin/beyond-valuations-long-term-financial-risks-from-the-ai-build-out/
[ft20]: https://financialpost.com/financial-times/ai-debt-worries-spark-surge-in-default-insurance-trading
[msgap]: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/credit-markets-ai-financing-gap-vishy-tirupattur-vishwas-patkar
[ifr25]: https://www.ifre.com/bonds/2502504/coreweave-rout-freezes-data-centre-financing
[sp]: https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says
[moodys]: https://www.insurancejournal.com/news/national/2026/01/12/853930.htm
[moodypc]: https://www.moodys.com/web/en/us/insights/credit-risk/outlooks/private-credit-2026.html
[meta3q]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm
[orclq]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
[vantage]: https://www.bloomberglinea.com/negocios/bancos-alistan-deuda-por-us38000-millones-para-centros-de-datos-de-oracle/
[jupiter]: https://www.aol.com/articles/oracles-18-billion-data-center-220302000.html
[abilene1]: https://www.nmrk.com/insights/press-releases/newmark-arranges-2-3-billion-construction-financing-for-206-mw-build-to-suit-data-center
[abilene2]: https://www.prnewswire.com/news-releases/newmark-facilitates-7-1-billion-construction-loan-to-develop-ai-data-center-302463532.html
[jupnotice]: https://www.axios.com/2026/09/24/oracle-force-majeure-blue-owl-openai
[juporacle]: https://www.oracle.com/news/announcement/project-jupiter-is-expected-to-generate-13-billion-in-economic-impact-2026-10-13/
[juporder]: https://www.env.nm.gov/opf/wp-content/uploads/sites/13/2026/07/2026-10-16-AQB-26-57-2nd-Amnd-Sch-Order-filed.pdf
[qts]: https://www.paulhastings.com/en-GB/news/paul-hastings-advises-the-initial-purchasers-on-qts-data-centers-usd4-6-billion-notes-offering
[hutq]: https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results
[hut]: https://www.hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data
[wulfhtml]: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm
[chifed]: https://chicagofed.org/publications/chicago-fed-insights/2026/ai-tail-risk-for-banks
[imf]: https://www.imf.org/-/media/files/publications/gfsr/2026/october/english/ch1.pdf
[crwv24]: https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/
[crusoe]: https://crusoe.ai/newsroom/upper90-closes-usd225m-credit-facility-to-crusoe-to-expand-ai-cloud/
[bis137]: https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms
[metacds25]: https://www.marketscreener.com/news/meta-s-credit-risk-indicator-jumps-to-record-high-after-results-ce785cdedd89fe23
[ms-q]: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm
[ms-fwp]: https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm
[meta-notes]: https://www.sec.gov/Archives/edgar/data/1326801/000119312526448015/d135326d424b5.htm
[sopaipilla]: https://spratings.spglobal.com/ratings/%5Blang%5D/regulatory/article/-/view/type/HTML/id/3653386
[xpu]: https://www.blackstone.com/news/press/bank-of-america-blackstone-citi-and-morgan-stanley-announce-landmark-63-billion-financing-structure-to-enable-ai-compute/
[avgo-k]: https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm
[spacex]: https://ir.spacex.com/updates/releases-details/2026/SPACEX-SECURES-40-BILLION-IN-THE-LARGEST-GPU-FINANCING-EVER-2026-EnDqGhTAB3/
[orcl-cds]: https://en.sedaily.com/international/2026/11/03/oracle-curbs-borrowing-as-credit-risk-eases-microsoft-bonds
[avgo-rating]: https://cbonds.com/news/4148325/
[meta-rating-reuters]: https://www.investing.com/news/stock-market-news/sp-global-revises-outlook-on-meta-to-negative-on-cashflow-concerns-4988756
[iren-fin]: https://investor.wedbush.com/wedbush/article/bizwire-2026-10-28-iren-and-wingspire-equipment-finance-complete-363-million-financing-for-high-density-ai-compute-assets
[trepp]: https://www.trepp.com/trepptalk/data-center-cmbs-caught-in-the-ai-sell-off
[goog3]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm
[beignet-new]: https://spratings.spglobal.com/ratings/%5Blang%5D/regulatory/article/-/view/type/HTML/id/3653391
[wulf-new]: https://investors.terawulf.com/news-events/press-releases/detail/148/terawulf-secures-google-credit-backstop-for-project-financing-in-support-of-19-billion-anthropic-lease-executes-definitive-fluor-epc-agreement
[ms-close]: https://www.sec.gov/Archives/edgar/data/789019/000119312526447173/d178557d8k.htm
[orcl-new-fwp]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526443918/d87441dfwp.htm
[orcl-new-close]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526447507/d131790d8k.htm
[airtrunk-new]: https://airtrunk.com/airtrunk-secures-a4-25b-green-loan-for-syd3-western-sydney-expansion-supporting-australias-digital-economy/
[meta-forward]: https://www.sec.gov/Archives/edgar/data/1326801/000119312526436410/d94886d424b5.htm
