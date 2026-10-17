# AI debt markets: where losses sit if the build disappoints

*Last updated: 2026-10-18 · Author: Codex / OpenAI · Status: reviewed · Reviewer: Codex (gpt-6-astra) cross-check, applied 2026-10-17*

## Summary

- Credit risk depends on construction delivery, customer payments and equipment resale values. S&P’s **2026-08-27 forecast** projects capex above $1.3T by 2027 and expects all six covered hyperscalers to have negative free operating cash flow in 2026–2027, with recovery only in 2029; profitability alone does not establish capacity to self-fund the build. [S&P][sp]
- Meta’s May 2026 bond issue raised $25B face value and $24.91B net cash. Alphabet’s June 2026 common-stock and mandatory-preferred financing raised $49.6B net; preferred conversion is scheduled on/about May 15, 2029 unless earlier converted. [Meta][meta], [Alphabet][goog]
- The note assembles approximately $572.5B of dated corporate principal and selected project securities, mainly from May–June 2026 snapshots, conditional on the verification limits in claim 12. Construction packages, chip-platform capital and subsequent issuance are displayed separately because they do not measure comparable outstanding debt. [Claims 12 and 40](#key-claims)
- AI-related IG issuance expanded substantially (claims 50–51), while later issuance weakened (claim 53). The measures have different coverage. [KC Fed][kcfed]
- Hyperion’s 2025 structure illustrates project versus tenant debt: Meta signed initial four-year leases and conditional, capped residual-value support for the first 16 operating years. This is not an unlimited Meta guarantee of project bonds. [Meta][metajv]
- Wood/Jefferies, relayed October 17, reports Oracle CDS widening from 186bp on September 11 to 288bp, and CoreWeave from 749bp to 1,118bp. Endpoint quote dates are unspecified. These paths reinforce selective stress, not realized defaults or rating-downgrade probabilities. [ET/ANI][wood]
- Institutional participation is established: CDPQ joined CoreWeave’s $7.5B May 2024 facility; BCI and Liberty Mutual Investments joined Crusoe’s $0.225B March 2025 GPU financing. Open Markets warns about pensions and PE-owned insurers, but supplies no holdings census. Current allocations, aggregate insurer/pension exposure and banks’ retained underwriting positions remain unquantified. [Blackstone][crwv24], [Crusoe][crusoe], [Open Markets][omi]
- Long bonds outlast server accounting lives (claims 52,56–57), suggesting repeated replacement capex before repayment; actual chip economic life remains unverified. CoreWeave’s five-year debt/three-year customer-contract mismatch is a separate renewal risk (claim 23). [KC Fed][kcfed], [Meta][metak], [Microsoft historical policy][mslife], [CoreWeave][crwv55]

## Key claims

Dollar amounts are USD unless another currency is shown; B = billion, bp = basis points. Existing sources accessed **2026-10-17**; new sources and hardware-life comparators checked **2026-10-18**. Analyst forecasts are identified as estimates even when their publication is primary.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Meta issuance, settled November | $30B; maturities 2030–2065; coupons 4.20–5.75%; Treasury spreads 50–110bp | 2025 | [Term sheet][meta25] | primary | A |
| 2 | Meta issuance, settled May | $25B face, $24.91B net; 2031–2066; coupons 4.55–6.45%; T+53–147bp | 2026-05 | [Terms][meta26], [10-Q][meta] | primary | A |
| 3 | Alphabet issuance | $22.5B USD plus €13.25B; April USD T+32–70bp, November T+30–107bp; respective EUR Bund spreads 66.7–114.8/41.5–122.8bp; maturities 2028–2075 overall | 2025 | [April USD][goog25a], [November USD][goog25], [April EUR][goog25e], [November EUR][goog25n] | primary | B, sums |
| 4 | Alphabet first-half debt issuance | $20B USD + $31.8B foreign-currency equivalent; February USD T+27–95bp, 2029–2066; sterling extends to 2126 | 2026-06-30 | [10-Q][goog], [USD terms][goog26] | primary | A |
| 5 | Alphabet later USD issuance | $25B; 2028–2066; fixed coupons 4.50–6.50%, T+33–130bp | 2026-08-06 | [Term sheet][googaug] | primary | A |
| 6 | Alphabet equity financing | $49.6B aggregate net common/preferred proceeds; preferred mandatorily converts on/about May 15, 2029 unless earlier converted | 2026-06 | [10-Q][goog] | primary | A |
| 7 | Amazon issuance | $15B; 2028–2065; coupons 3.90–5.55%; T+30–85bp | 2025-11 | [Term sheet][amzn25] | primary | A |
| 8 | Amazon issuance | March $37B USD, 2028–2076, T+30–130bp fixed; €14.5B, CHF2.8B, C$14B also issued by June; July $25B, T+40–125bp, 2029–2066; September £4.25B, Gilt+53–93bp, 2029–2045 | 2026-09 | [10-Q][amzn], [March][amzn26], [July][amznjul], [September][amznsep] | primary | A |
| 9 | Microsoft direct issuance | Zero debt-issuance cash proceeds in FY2025/FY2026; outstanding principal $46.136B | 2026-06-30 | [10-K][msft] | primary | A |
| 10 | Oracle issuance | January-priced/February-settled $7.75B, 2028–2065, fixed T+57–135bp; September $18B, 2030–2065, T+75–137bp | 2025 | [January][orcl25a], [September][orcl25] | primary | B, sums |
| 11 | Oracle issuance | $25B including floating tranche; 2029–2066; fixed coupons 4.55–6.85%, T+95–195bp; floater SOFR+111bp | 2026-02 | [Term sheet][orcl26] | primary | B, sum |
| 12 | Corporate principal perimeter, partially cross-checked | Meta $84B; Alphabet $101.085B; Amazon $132.995B directly reproduced by review; Microsoft $46.136B not independently reproduced; Oracle $130.105B from indexed principal schedule, full-document retrieval failed; conditional sum $494.321B | May/June 2026 | [Meta][meta], [Alphabet][goog], [Amazon][amzn], [Microsoft filing index][msftindex], [Oracle indexed filing][orclindex] | primary | A for directly retrieved balances; B for conditional sum; see verification note below |
| 13 | Oracle bank facilities | Original refinanced term commitment $5.63B, SOFR+112.5–162.5bp; scheduled balloon August 2027, extension options; $10B revolver undrawn, expires March 2031; $1.5B commercial paper outstanding | 2026-05-31 | [10-K][orcl] | primary | A |
| 14 | Selected principal payments: 2027/2028/2029/2030 | CoreWeave $6.184/4.416/2.421/3.221B calendar; Oracle $7.210/10.145/5.500/7.250B fiscal; Microsoft $9.250/0/2.001/0B fiscal; Meta $2.750/1.500/1.000/5.000B calendar | June/May 2026; Meta Dec 2025 | [CRWV][crwv], [ORCL][orcl], [MSFT][msft], [Meta][metak] | primary | A |
| 15 | Vantage Texas/Wisconsin preliminary package, reported, unverified | Approximately $38B, JPMorgan/MUFG-led; preliminary benchmark+250bp; Wisconsin arrangements still under discussion; planned distribution to loan/private-credit investors; final commitment and draw status unverified | 2025-09-04 report | [Bloomberg Línea][vantage] | secondary | C |
| 16 | Jupiter loans, reported, unverified | $18B; quoted 89–91 cents; syndication stalled, Santander/Jefferies among quoting banks | 2026-09-18 | [Reuters citing FT][jupiter] | secondary | C |
| 17 | Abilene construction financing | $2.3B initial + $7.1B second-phase loans = $9.4B announced; JPMorgan-led | phase 1 date unverified here; phase 2 announced 2025-05-22 | [Newmark phase 1][abilene1], [Newmark phase 2][abilene2] | primary | B, sum |
| 18 | Hyperion/Beignet | $27.3B private securities; PIMCO-managed accounts majority investors; Meta/Blue Owl ownership 20%/80%; initial lease 4 years, conditional capped residual guarantee first 16 operating years | 2025 transaction | [Counsel][beignet], [Meta][metajv] | primary | A |
| 19 | QTS Fayetteville project notes | $4.6B, 5.700%, due 2036, non-recourse single-asset financing | 2026-04-21 | [Purchasers’ counsel][qts] | primary | A |
| 20 | Hut 8 project notes | River Bend $3.25B + Beacon Point $4.25B = $7.5B, fully amortizing/non-recourse; Beacon 6.129%, due 2042, T+165bp, Baa2 | 2026-Q2 | [Results][hutq], [Beacon terms][hut] | primary | A |
| 21 | Project prices: reported, unverified indicative marks; versions unresolved | Original note’s October 15 FT/Yahoo attribution: Beignet <91; QTS Excalibur <87; Hut Louisiana ~93/Texas ~91 cents. October 16 FT/BizNews version: <92; <88; ~94/~92 respectively. No single precise mark certified; bond identifiers/timestamps needed | 2026-10-15/16 publication dates | [FT/Yahoo, original attribution][prices], [FT/BizNews, alternate version][pricesalt] | secondary | C; same FT reporting, not independent confirmation |
| 22 | CoreWeave drawn debt and older DDTLs | $35.551B gross; net recourse $31.405B/non-recourse $3.663B after discounts/issuance costs; DDTL 1.0/2.0 balances $1.300/$3.190B, effective rates 15%/11% (not necessarily cash coupons), maturities March 2028/August 2030; June snapshot, not October balance | 2026-06-30 | [10-Q][crwv] | primary | A |
| 23 | CoreWeave structured facilities | DDTL 4.0 initially ~$7.5B, rising to $8.5B upon asset stabilization, A3/A(low), SOFR+225bp or ~5.9% fixed, March 2032; DDTL 5.5 $2.6B, Ba2/BB+ (below investment grade), SOFR+550bp, ~5-year debt versus 3-year average customer contracts | 2026-03-31 / 2026-08-10 | [SEC March release][crwv4], [August release][crwv55] | primary | A, announced terms/ratings |
| 24 | CoreWeave historical lender commitments | $2.3B led by Blackstone/Magnetar, with PIMCO/BlackRock/Carlyle; subsequent $7.5B facility includes CDPQ | 2023/2024 | [Borrower][crwv23], [Blackstone][crwv24] | primary | A |
| 25 | Lambda facilities | Up to $0.5B GPU facility, Macquarie/IDF; new $1.008B DDTL, 6.78%, Baa1/A(low), fully amortizes by May 30, 2033; three deployments for two investment-grade offtakers; draws tied to commissioning; marketed to insurers, final holdings/full funding not disclosed | 2024-04 / 2026-10-01 | [Company release][lambda24], [Lambda][lambda26] | primary | A, announced terms |
| 26 | Crusoe GPU credit | Approximately $0.225B, Upper90-led; BCI, FS, King Street, Liberty Mutual, ORIX participate | 2025-03-27 | [Company release][crusoe] | primary | A |
| 27 | xAI/Valor equipment financing | Apollo-led $3.5B “capital solution” supporting $5.4B compute acquisition/lease; NVIDIA anchor equity investor | 2026-01-07 | [Apollo][xai] | primary | A |
| 28 | Fluidstack-linked project debt | TeraWulf subsidiary WULF Compute LLC: $3.2B secured notes, 7.75%, due October 15, 2030; Google backstop begins at corresponding lease commencement, with termination-payment or lease-assumption alternatives; Google affiliate undertaking to collateral agent follows recognition-agreement timing | 2026-06-30 | [10-Q, Notes 8 and 10][wulfhtml] | primary | A |
| 29 | Anthropic chip platform | Announced $35B initial AI XPV transaction led by Apollo with Blackstone; Fluidstack sites; funded balance, debt/equity split and complete guarantee terms undisclosed—not verified debt outstanding | 2026-06-09 | [Broadcom][avgo] | primary | A, announcement only |
| 30 | CoreWeave CDS | Above 1,000bp; Reuters explainer gives ~63% cumulative 5-year model-implied default probability; cited 64% Swedish version inaccessible to review; curve, recovery assumption and contract identifier not retrieved | 2026-10-15 | [Reuters quotes][cds], [Explainer][cdsex], [Unverified Swedish version][cds64] | secondary | C, composite claim |
| 31 | Oracle CDS | Record 288bp; Reuters explainer rounds to nearly 300bp | 2026-10-15 | [Reuters][cds], [Explainer][cdsex] | secondary | B |
| 32 | Oracle rating action | S&P BBB→BBB−, stable; higher business risk/weaker prospective cash flow | July 2026 | [Teleborsa][orating], [Reuters confirmation][jupiter] | secondary | B |
| 33 | Anthropic rating, reported, unverified | KBRA BB+ issuer/junior rating in June; $4.4B junior within $35B transaction, about 8.5% yield; limited disclosed cash-flow information | 2026-10-16 report | [FT syndication][arating] | secondary | C |
| 34 | North Star proposal, reported, unverified | $60B: $42B senior reportedly Broadcom-guaranteed, $18B junior; Blackstone $9B allocation, 10% coupon/>10% yield; 5-year chip leases, about 1.5GW | 2026-10-16/17 | [Mint citing FT][north], [Reuters, unverified][northreut] | secondary | C |
| 35 | Broad credit context: distinct measures | Monthly Baa 6.47% minus Aaa 6.03% = 0.44pp (44bp) yield-quality differential, not matched-maturity OAS; daily US HY OAS 3.23pp (323bp) | 2026-09 / 2026-10-15 | [FRED yields][fred], [FRED OAS][fredhy] | primary | A, observations; B, subtraction/conversion |
| 36 | Morgan Stanley external-capital estimate | $1.5T gap against $2.9T spending over four years; private credit/ABF $800B, IG $200B, ABS/CMBS $150B, other $350B | 2025-08-06 | [Bank transcript][msgap] | primary | A, forecast |
| 37 | Morgan Stanley issuance estimate | About $250B AI debt issued YTD; approximately $500B forecast for full year | 2026-06-18 | [Bank transcript][msdebt] | primary | A, estimate |
| 38 | Moody’s estimates | At least $3T data-center investment through 2030; private-credit AUM >$2T in 2026, approaching $4T by 2030, across all sectors | January 2026 | [Bloomberg][moodys], [Moody’s][moodypc] | secondary / primary | C |
| 39 | S&P financing pressure | Capex projected >$1.3T by 2027; negative free operating cash flow in 2026/2027 for Alphabet, Amazon, Microsoft, Meta, Oracle and SpaceX; recovery not projected until 2029 | 2026-08-27 | [Agency release][sp] | primary | A, forecast |
| 40 | Dated financing subtotal and separately classified amounts | $494.321B corporate + $35.551B CoreWeave + $42.6B selected project securities = $572.472B conditional historical subtotal. Separately: $65.4B announced/reported construction packages (including preliminary Vantage); $35B announced chip transaction; $50B later Amazon/Alphabet USD issuance; $4.2B September CoreWeave issuance; no combined outstanding-exposure total | mixed dates, principally May/June 2026 snapshots; later flows July–September 2026 | Claims 5,8,12,15–20,22,28–29,41 | primary / secondary | B, arithmetic on stated inputs; C, coverage/preliminary packages; claim 12 limits apply |
| 41 | CoreWeave subsequent convertible borrowing | $4.2B principal including exercised purchaser option; 2.875%, due 2033; $4.137B net before estimated offering expenses; $0.5662B capped-call cost; $4.137B − $0.5662B = $3.5708B remaining before those expenses | 2026-09-22 | [SEC 8-K][crwvsep] | primary | A, terms/proceeds; B, subtraction |
| 42 | Jupiter contract dispute, reported, unverified | Force-majeure notice reported; Oracle maintained schedule; contractual effect unverified | 2026-09-24 | [Axios][jupnotice] | secondary | C |
| 43 | Oracle’s Jupiter response | Company states project scope unchanged beyond April 2026 power-plan update; this does not independently establish financing or permitting resolution | 2026-10-13 | [Oracle announcement][juporacle] | primary | A for company statement |
| 44 | Circular investment relationships, BIS authors’ research | 46.4% by value of AI-to-AI investment deals in 2021–2025 also involved commercial supply-chain relationships; historical investment-deal statistic, not share of current AI debt | published 2026-10-01 | [BIS Bulletin 137][bis137] | primary | A for reported research finding |
| 45 | Oracle quarterly cash-flow funding | OCF $23.103B including $11.363B customer advances with significant financing component; capex $28.499B; reported FCF −$5.396B. Illustrative OCF minus advances minus capex: $23.103B − $11.363B − $28.499B = −$16.759B, not reported FCF | quarter ended 2026-08-31; released 2026-09-10 | [Oracle results][orclresults], [August 10-Q][orclq] | primary | A, disclosures; B, illustrative subtraction |
| 46 | Oracle equity funding | $19.909B common-equity proceeds from at-the-market program, net of issuance costs | quarter ended 2026-08-31 | [August 10-Q][orclq] | primary | A |
| 47 | Meta future lease obligations | $278.99B leases not yet commenced at June 30; another $68B data-center leases signed in July; undiscounted obligations, separate from current project debt | 2026-06-30 / 2026-07 | [Meta 10-Q, Note 9][meta] | primary | A |
| 48 | Oracle future lease commitments | $288B additional leases not on August balance sheet; expected commencement fiscal Q2 2027–fiscal 2029, terms 15–19 years; undiscounted contractual obligations | 2026-08-31 | [August 10-Q][orclq] | primary | A |
| 49 | CoreWeave immediate principal payments | $4.413B in remaining portion of calendar 2026, per June maturity schedule; not an October remaining balance | 2026-06-30 | [10-Q, Note 10][crwv] | primary | A |
| 50 | AI-related share of IG issuance | 2% in 2023 → 10% in 2026; broad AI value-chain issuers, not AI-only use of proceeds | through 2026-Q2; published 2026-10-05 | [Sharma & George, KC Fed, Chart 1][kcfed] | primary | A for authors’ analysis |
| 51 | AI-related IG issuance volume | $330B YTD, 10× full-year 2023 | through 2026-Q2; published 2026-10-05 | [KC Fed, Chart 1][kcfed] | primary | A for authors’ estimate |
| 52 | Weighted-average IG bond maturity | Hyperscalers 16 years; utilities 17; market average 10 | bonds issued 2025–August 2026; published 2026-10-05 | [KC Fed, Chart 4][kcfed] | primary | A for authors’ analysis |
| 53 | Global AI-related debt issuance | September $23B versus June $113B | 2026; reported 2026-10-16 | [Axios, citing FT][axiosdebt] | secondary | B |
| 54 | Oracle CDS path | Five-year protection 186bp on September 11 → 288bp; endpoint observation date unspecified | since 2026-09-11; reported 2026-10-17 | [ET/ANI quoting Christopher Wood, Jefferies][wood] | secondary | B for attributed marks |
| 55 | CoreWeave CDS path | 749bp → 1,118bp over the same interval; 2032 bond yield 14.8%; endpoint observation date unspecified | since 2026-09-11; reported 2026-10-17 | [ET/ANI quoting Wood/Jefferies][wood] | secondary | B for attributed marks |
| 56 | Meta hardware accounting lives | Servers/network assets 5–5.5 years; most extended to 5.5 effective January 1, 2025; buildings 25–30 years | 2025-12-31; filed 2026-01-29 | [Meta 10-K, Note 1][metak] | primary | A for accounting estimates, not measured economic life |
| 57 | Microsoft historical hardware accounting policy | Server/network lives extended from 4 to 6 years effective FY2023; historical comparator, not a new 2026 GPU-life measurement | FY2024 annual report | [Microsoft, Note 1][mslife] | primary | A for historical accounting policy |
| 58 | Holder-channel evidence and limit | Institutional channels identified; AI-specific allocations unquantified. Open Markets warns about insurer/endowment exposure | KC Fed 2026-10-05; Open Markets 2026-10-16 | [KC Fed][kcfed], [Open Markets][omi]; named deals in claims 18,24–26 | primary institutional analysis / advocacy | A for Fed analysis and named disclosures; B for advocacy attribution |

**Claim 12 verification limits.** The cross-check directly reproduced Meta, Alphabet and Amazon balances. Oracle’s principal schedule was available only in an indexed SEC extract; the full annual report did not fetch. Microsoft’s filing index was accessible, but the reviewer could not independently reproduce its principal. The conditional sum is correct arithmetic, not certification of all five balances or an October debt census. [Independent cross-check](../../reviews/debt-markets-codex-xcheck.md), [Oracle indexed filing][orclindex], [Microsoft filing index][msftindex]

## Analysis

**What is financed, and who can pay.** Advertising, software, retail and cloud cash flows support hyperscaler debt. Microsoft’s leased suppliers can borrow against its rent despite its absence of direct issuance. Corporate proceeds cannot all be assigned to AI; Alphabet’s mandatory preferred primarily creates dilution and dividends. S&P’s August forecast (claim 39) expects negative free operating cash flow across its six-company universe through 2027, with recovery only in 2029. Operating profitability is therefore support, not evidence that the build can be self-funded. [S&P][sp]

Oracle’s quarter ended August 31, 2026 provides a funding bridge: $23.103B OCF included $11.363B of customer advances with a significant financing component, against $28.499B capex and reported FCF of −$5.396B. Excluding those advances gives an illustrative −$16.759B OCF-minus-capex figure, not reported FCF. These prepayments create deferred revenue and interest expense; they improve liquidity but are distinct from cash generated by delivered services. Oracle also raised $19.909B net common equity, real loss-absorbing capital (claims 45–46). [Results][orclresults], [10-Q][orclq]

**Issuance flows and market access.** The Fed excludes private AI labs; its issuer perimeter differs from claim 53. Neither series measures outstanding debt or forms a directly comparable monthly series. Together with the closed Lambda facility and CoreWeave convertible, the evidence supports more selective access; it does not establish that financing has stopped. [KC Fed][kcfed]; claims 25,41,53

**Estimated stack by instrument and holder.** The CSV distinguishes stocks, issuance flows, capacities and proposals. The dated subtotal below is an incomplete historical map, conditional on claim 12’s verification limits; corporate principal includes legacy non-AI borrowing, and project issuance can include reserves or refinancing.

| Instrument | Identified amount | Named financing providers / ultimate loss holders | Evidence |
|---|---:|---|---|
| Hyperscaler corporate principal, partially cross-checked | $494.321B | Bond funds, insurers, pensions, bank lenders; allocations largely undisclosed | Claim 12, A/B; verification note applies |
| CoreWeave drawn debt, including notes, converts, DDTLs and vendor financing | $35.551B | Private-credit accounts, banks, bondholders, equipment financiers | Claims 22–24, A |
| Selected project securities: Beignet, QTS, Hut, TeraWulf | $42.6B | PIMCO accounts and institutional bond investors; Blue Owl/Blackstone often sponsor equity rather than ultimate debt holders | Claims 18–20,28; A/B |
| **Conditional subtotal of dated principal/securities** | **$572.472B** | Holder look-through unavailable; claim 12 retrieval limits apply | Claim 40, B arithmetic/C coverage |

Separate announcements and issuance flows below are not added to that subtotal or to each other as a measure of outstanding exposure:

| Category | Identified amount | Status / financing providers | Evidence |
|---|---:|---|---|
| Abilene/Vantage/Jupiter construction packages | $65.4B | Mix of announced financing and reported packages; Vantage preliminary, final commitment/draw status unverified; JPMorgan/MUFG-led syndicates and other banks | Claims 15–17, B/C |
| Anthropic initial chip transaction | $35B | Announced platform capital; Apollo/Blackstone investors; funded balance and debt/equity split undisclosed | Claim 29, A for announcement |
| July Amazon/August Alphabet USD issuance | $50B | Gross borrowing flow; repayments/FX not rolled forward | Claims 5,8; A/B |
| September CoreWeave convertible issuance | $4.2B | Gross borrowing flow; conversion option is part of its pricing | Claim 41, A |

Lambda, Crusoe and xAI examples are outside that subtotal: their facility capacities, remaining draws and overlap with later refinancings are insufficiently reconciled. North Star remains proposed. Tenant lease commitments, vendor guarantees and financing-gap forecasts can overlap with project debt; they cannot be added as independent exposures. No global debt census or updated net debt balance is inferred. CoreWeave’s September 22 convertible sale (claim 41) demonstrates continuing financing access, but its 2.875% coupon cannot be compared with straight-debt yields without valuing the conversion option. [8-K][crwvsep]

**Future contractual lease obligations, shown separately.** These undiscounted commitments matter to tenants’ ability to support outside borrowers; they may overlap with financing already mapped and are not added to project debt.

| Tenant | Not-yet-commenced/additional obligations | As of | Evidence |
|---|---|---|---|
| Meta | $278.99B at June 30; another $68B signed in July | 2026-06-30 / 2026-07 | Claim 47, [10-Q][meta], A |
| Oracle | $288B outside August balance sheet; fiscal Q2 2027–2029 commencement, 15–19-year terms | 2026-08-31 | Claim 48, [10-Q][orclq], A |

Blackstone and Magnetar are verified CoreWeave lenders; PIMCO anchors Beignet; Apollo finances equipment vehicles; Blue Owl supplies project equity and organizes capital. CDPQ and BCI, institutional investment managers, establish pension-sector participation in the named financings, not direct pension balance-sheet allocations; Liberty Mutual Investments and CoreWeave’s disclosed insurance investors establish insurer-sector participation. Asset-manager AUM is not the manager’s own loss-bearing balance sheet. [Blackstone][crwv24], [Crusoe][crusoe], [CoreWeave][crwv4]

**Who holds the paper.** KC Fed’s purchase chart covers all corporate bonds; its private-placement discussion identifies insurer, pension and private-credit channels. Open Markets’ October 16 report argues exposure reaches retirement funds, endowments and policyholders through PE-owned insurers; that verifies the advocacy position, not each portfolio’s exposure. [KC Fed][kcfed], [Open Markets][omi]

The named providers above establish participation, not present beneficial ownership. An insurer may hold an asset directly or through a managed fund; a pension can be a fund investor rather than lender of record; a private-credit manager can arrange capital without retaining all the risk. A security-level bridge requires identifiers, current positions, fund investors, insurer general-account disclosures and the contractual waterfall. Neither new source verifies aggregate AI holdings or a quantified BBB−/BB GPU-mezzanine allocation. General corporate-bond purchase data cannot fill that gap.

**Maturity mismatch: long bonds, shorter-lived chips.** Compare claim 52’s 16–17-year bonds with the roughly five-to-six-year hardware accounting lives in claims 56–57. These server/network estimates are broader than GPUs and do not measure actual resale value or the date chips cease to earn revenue. Meta also reports much longer building lives. [Meta][metak], [Microsoft historical policy][mslife]

Our inference is that long-duration creditors rely on cash generation across successive hardware generations after replacement capex. Rapid obsolescence, weaker rents or expensive replacement can erode that cushion before legal maturity. Long fixed-rate borrowing also reduces immediate rollover pressure, and diversified corporate issuers have durable assets and other revenues; their bonds are not automatically secured solely by the first chip cohort. For equipment/project debt, amortization, contracts, residual values and guarantees determine the mismatch security by security. Claim 23’s contract-renewal gap is separate from hardware useful life.

**Project credit and GPU credit differ.** Beignet investors depend on Meta rent and conditional residual support; Meta’s guarantee is not an unlimited promise to repay every bond. QTS creditors own project claims, not Microsoft corporate notes. Hut’s Louisiana lease is with Fluidstack, backstopped by Google; the Texas Nvidia tenancy is reported by the FT. Calling both Hut projects Nvidia leases is unsupported. [Meta][metajv], [QTS counsel][qts], [Hut][hutlease], [FT][prices]

CoreWeave’s older DDTLs combine contractual cash receipts with equipment collateral. Its later contract/debt mismatch requires successful renewal, replacement customers or residual recoveries. The cheaper investment-grade facility has different contractual support: its spread cannot be compared with the later facility as a pure time-series repricing. DDTL 4.0 initially permits about $7.5B, rising to $8.5B upon stabilization; DDTL 5.5 is rated Ba2/BB+ (claim 23). Lambda’s October facility instead pairs full amortization with two investment-grade offtakers and commissioning-linked draws (claim 25), counterevidence against an indiscriminate shutdown; closing the commitment does not show it was fully drawn. [March facility][crwv4], [August facility][crwv55], [Lambda][lambda26]

Claim 42 makes lease-commencement protection an immediate verification priority. [Axios][jupnotice] Oracle’s October 13 statement says Jupiter’s scope is unchanged beyond its April power-plan update (claim 43); this does not establish resolution of financing or permitting risks. [Oracle][juporacle]

**Maturity wall and repricing order.** CoreWeave’s June 30 schedule includes $4.413B of principal payments in the remaining part of 2026 (claim 49), an immediate liquidity requirement omitted by a 2027–2030-only view; it is not an October remaining balance. [10-Q][crwv] Claim 14 mixes calendars: Oracle years end in May, Microsoft in June. Meta’s new May issue starts beyond the requested window. Construction loans may require takeout when construction completes, well before a project bond’s legal final maturity. Jupiter’s original proposed tenor and Vantage’s final extension conditions were not verified.

The Jefferies paths in claims 54–55 provide an earlier starting point for repricing. ET/ANI reproduces Wood’s figures, but the original Jefferies note and endpoint fixing times were not retrieved. Their endpoints must not be dated as October 17 closes or combined with Reuters’ separate observations into a certified daily series. CDS prices include risk premia, recovery assumptions and liquidity; neither path directly establishes default or fallen-angel odds. [ET/ANI][wood]

CDS, bonds and new-deal discounts reprice first. Floating interest, draw conditions, collateral tests and construction deadlines transmit stress before maturity. Amortizing GPU loans require continuing cash generation. Fixed corporate coupons do not reset when secondary prices fall; their issuers face the new price when refinancing or borrowing again. Fully amortizing Hut bonds reduce balloon-refinancing risk, but retain completion and tenant-performance risk.

The two FT project-price versions in claim 21 remain unresolved; the alternate October 16 figures were fetched from the republication’s HTML. Neither version supplies authenticated dealer/TRACE observations here. Par discounts combine rate duration, credit, liquidity, amortization and other terms, so they do not isolate credit losses. The September Baa–Aaa monthly yield differential and October 15 daily HY OAS (claim 35) have different constructions; the note supplies no historical benchmark for calling either broadly “tight.” CDS provides separate credit-repricing evidence, not a documented portfolio-wide loss estimate. [FT/BizNews][pricesalt], [Reuters][cds], [FRED yields][fred], [HY OAS][fredhy]

**Contagion and the default-cycle scenario.** BIS authors’ October 1 research finds that 46.4% by value of AI-to-AI investment deals in 2021–2025 also involved commercial supply-chain relationships (claim 44). This historical investment statistic is not a current debt share; it supports the inference that customer demand, financing and collateral support may fail together. Circularity can also secure scarce inputs and does not itself prove fictitious demand. [BIS Bulletin 137][bis137]

If returns disappoint, sponsor equity and subordinate capital generally absorb impairment first, followed by secured creditors to the extent collateral and guarantees fail; contractual priority controls the actual waterfall. Private-credit marks can lag traded comparables. Lower marks and redemptions can restrict new lending; warehouse and fund-finance lenders can tighten collateral terms or refuse renewals. Undistributed construction commitments then remain with underwriting banks.

ABS and CMBS route rents, mortgages or equipment receivables through vehicles to institutional investors. Subordination and reserves protect senior claims but cannot diversify a common tenant or unavailable power. Insurer losses initially hit investment income/capital; downgrades can increase capital pressure. Pension losses affect asset values and funding. PIMCO funds are not automatically Allianz general-account investments. The BIS explicitly identifies bank funding lines, guarantees and non-bank investors as transmission channels. [BIS][bis]

A telecom-style default cycle would start with delays and weak compute cash conversion, close refinancing access for marginal operators, then force restructurings, vendor concessions and collateral sales. Surviving buyers could acquire usable power-connected assets at lower cost. Unlike fiber, specialized chips can lose economic relevance during workouts. Systemic banking stress would require meaningful retained leverage, correlated guarantees or funding withdrawals; isolated project price declines do not establish it. This is a conditional mechanism, not a default forecast. [Richmond Fed][telecom], [BIS][bisjan]

## Conflicts and open questions

- **Loss concentration and cash-flow cushion—note versus review:** the original note judged risk concentrated in construction, customer-dependent compute and residual chip values, with profitable hyperscalers providing a substantial cushion. The cross-check accepts those mechanisms but says their share of aggregate expected losses was not measured and profitability alone is too reassuring without cash-flow coverage. Claims 39 and 45–48 now supply funding and obligation evidence; they still do not quantify the loss distribution. [Independent review](../../reviews/debt-markets-codex-xcheck.md), [S&P][sp], [Oracle][orclq], [Meta][meta]
- **Mixed total—note versus review:** the original note considered the extended gross financing perimeter useful with caveats. The reviewer agrees every original sum and rounding was arithmetically correct, but judges that adding stocks, gross flows and provisional packages creates an economically non-comparable headline. Both views are recorded; the revised presentation keeps the conditional historical subtotal and separate categories, without an October outstanding-exposure total. [Review, arithmetic and assessment](../../reviews/debt-markets-codex-xcheck.md)
- **Repayment-source risk—note versus review:** the original note called joint failure of customer payments and recoverable collateral the largest uncertainty. The review treats this as an illustrative mechanism rather than a ranked, quantified finding, and emphasizes that apparent diversification across instruments can hide the same customers. The review also stresses continued issuance and Lambda’s protections as counterevidence to a general financing shutdown. Both assessments agree that this evidence establishes neither a systemic banking crisis nor a realized default wave. [Review](../../reviews/debt-markets-codex-xcheck.md), [CoreWeave][crwv55], [Lambda][lambda26], [BIS authors][bis137]
- **Project marks:** the original note attributed Beignet <91, QTS <87 and Hut Louisiana/Texas ~93/~91 cents to October 15 FT/Yahoo reporting. The cross-check reproduced <92, <88 and ~94/~92 in the October 16 FT/BizNews version, also fetched when applying this review. The original version was not independently retrieved; different versions/timestamps may explain the difference. Both remain grade C indications from the same reporting, pending bond identifiers and observation times. [Original attribution][prices], [Alternate version][pricesalt]
- **Broad-market comparison—note versus review:** the original Summary described aggregate spreads as tight. The reviewer accepts the specified observations but requires a historical benchmark for that characterization and distinguishes monthly yield-quality differentials from daily option-adjusted spreads. The revised Summary reports the dated indicators without a claim about historical tightness. [Review](../../reviews/debt-markets-codex-xcheck.md), [FRED yields][fred], [HY OAS][fredhy]
- **Counterevidence:** Morgan Stanley’s June assessment emphasized strong hyperscaler credit and diversified, operating securitization collateral; BIS initially judged financial-stability risks moderate. S&P’s later cash-flow forecast and October price stress weaken, without disproving, that case. [Morgan Stanley][msdebt], [BIS][bisjan], [S&P][sp]
- Jupiter’s stress report was published in September, not first established in mid-October. Quotes are indications, not verified executed trades or bank accounting losses. [Reuters][jupiter]
- The original note combined Reuters syndications as approximately 63–64% CDS-implied default risk. The review reproduced about 63% but could not fetch the Swedish 64% version; that value remains unverified. Recovery assumptions, risk premia and liquidity make neither an objective default forecast. [Reuters explainer][cdsex], [Reuters syndication][cds64]
- No primary KBRA report or original S&P Oracle action was retrieved. Anthropic rating/financing details remain reported, unverified. North Star closing, guarantee documentation and final allocations remain unknown.
- Moody’s capex/AUM forecasts, S&P capex projections and Morgan Stanley financing needs measure different universes. No reproducible current AI-only private-credit stock was retrieved from Fitch or Bank of America. Fitch’s joint whitepaper instead highlights leverage layered across holding companies, projects and GPUs. [Fitch joint whitepaper][fitch]
- KC Fed’s issuance and maturity samples have different cutoffs; its broad issuer definition differs from claim 53’s global debt perimeter. Hardware accounting lives are not observed GPU economic lives, and Jefferies’ endpoint fixing dates/original note remain unverified (claims 50–57).
- Exact insurer/pension holdings, bank warehouse exposure, project-loan drawn balances, current secondary spreads and subsequent repayments and foreign-currency issuance are incomplete. Fund redemption pressure is documented; an AI-infrastructure-loss-caused gate was not verified. [CRISIL][flows]

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| CoreWeave CDS | >1,000bp | 2026-10-15 | [Reuters][cds] | Marginal refinancing price |
| Oracle CDS | 288bp | 2026-10-15 | [Reuters][cds] | Tenant/bank concentration |
| CDS path / quote provenance | Oracle 186→288bp; CoreWeave 749→1,118bp since September 11; endpoint dates unspecified | reported 2026-10-17 | [ET/ANI][wood] | Dated risk repricing; original note/fixing times still needed |
| Issuance and maturity coverage | Claims 50–53: different universes and cutoffs | Q2 / August / September 2026 | [KC Fed][kcfed]; claim 53 | Track matched issuance series and hardware replacement needs |
| Project bonds, unresolved versions | Oct 15 original attribution: Beignet <91/QTS <87/Hut Louisiana ~93, Texas ~91; Oct 16 alternate: <92/<88/~94/~92 cents; no certified mark | 2026-10-15/16 publication dates | [FT/Yahoo][prices], [FT/BizNews][pricesalt] | Indicative discounts also reflect rates/liquidity/terms; identifiers and timestamps needed |
| Construction syndication | Jupiter $18B, indications 89–91 | 2026-09-18 | [Reuters/FT][jupiter] | Retained underwriting exposure |
| New GPU deals | Lambda $1.008B commitment at 6.78%, closed; two investment-grade offtakers; commissioning-linked draws | 2026-10-01 | [Lambda][lambda26] | Selective financing access; commitment is not full funding |
| Subsequent CoreWeave issuance | $4.2B convertible notes, 2.875%, due 2033 | 2026-09-22 | [8-K][crwvsep] | Financing access continues; gross issuance, not net debt change |
| CoreWeave immediate maturities | $4.413B principal in remaining 2026 at June snapshot | 2026-06-30 | [10-Q][crwv] | Near-term liquidity before the selected maturity window |
| Chip financing | North Star $60B proposed, junior yield >10% | 2026-10-16/17 | [Mint/FT][north] | Next funding/guarantee test |
| Ratings | Oracle BBB− stable; Anthropic reportedly BB+ | July/June 2026 | [Oracle report][orating], [FT][arating] | Eligibility and capital sensitivity |
| Broad credit indicators | Monthly Baa–Aaa yield differential 44bp; daily HY OAS 323bp | Sept / Oct 15 2026 | [FRED][fred], [ICE/FRED][fredhy] | Different measures; no historical tightness benchmark supplied |
| Redemptions/gates | Requests increased; AI-caused gate unverified | Q2 2026, reported Sept | [CRISIL][flows] | Lending capacity/liquidity mismatch |

## Sources

1. [Meta pricing term sheet][meta25]. 2025-10-30. Accessed 2026-10-17.
2. [Meta pricing term sheet][meta26]. 2026-04-30. Accessed 2026-10-17.
3. [Meta Q2 10-Q][meta]. 2026-07-30. Accessed 2026-10-17.
4. [Alphabet April USD term sheet][goog25a]. 2025-04-28. Accessed 2026-10-17.
5. [Alphabet November USD term sheet][goog25]. 2025-11-03. Accessed 2026-10-17.
6. [Alphabet April EUR term sheet][goog25e]. 2025-04-29. Accessed 2026-10-17.
7. [Alphabet November EUR term sheet][goog25n]. 2025-11-03. Accessed 2026-10-17.
8. [Alphabet Q2 10-Q][goog]. 2026-07-23. Accessed 2026-10-17.
9. [Alphabet February term sheet][goog26]. 2026-02-09. Accessed 2026-10-17.
10. [Alphabet August term sheet][googaug]. 2026-08-06. Accessed 2026-10-17.
11. [Amazon November term sheet][amzn25]. 2025-11-17. Accessed 2026-10-17.
12. [Amazon Q2 10-Q][amzn]. 2026-07-31. Accessed 2026-10-17.
13. [Amazon March term sheet][amzn26]. 2026-03-10. Accessed 2026-10-17.
14. [Amazon July term sheet][amznjul]. 2026-07-07. Accessed 2026-10-17.
15. [Amazon sterling term sheet][amznsep]. 2026-09-09. Accessed 2026-10-17.
16. [Microsoft FY2026 10-K][msft]. 2026-07-29. Accessed 2026-10-17.
17. [Oracle January term sheet][orcl25a]. 2025-01-30. Accessed 2026-10-17.
18. [Oracle September term sheet][orcl25]. 2025-09-24. Accessed 2026-10-17.
19. [Oracle February term sheet][orcl26]. 2026-02-02. Accessed 2026-10-17.
20. [Oracle FY2026 10-K][orcl]. 2026-06-22. Accessed 2026-10-17.
21. [CoreWeave Q2 10-Q][crwv]. 2026-08-12. Accessed 2026-10-17.
22. [Meta annual 10-K][metak]. 2026-01-29. Accessed 2026-10-17.
23. [Bloomberg Línea, Banks prepare Oracle-linked financing][vantage]. 2025-09-04. Accessed 2026-10-17.
24. [Reuters/AOL, Oracle data-center debt under pressure, citing FT][jupiter]. 2026-09-18. Accessed 2026-10-17.
25. [Newmark/PR Newswire, Construction loan for Abilene, phase 2][abilene2]. 2025-05-22. Accessed 2026-10-17.
26. [Clifford Chance, Energy & resources insights: Hyperion transaction][beignet]. 2026, exact date unavailable. Accessed 2026-10-17.
27. [Meta, Hyperion joint venture announcement][metajv]. 2025-10-21; updated 2025-11-14. Accessed 2026-10-17.
28. [Paul Hastings, QTS notes offering][qts]. 2026-04-21. Accessed 2026-10-17.
29. [Hut 8, Q2 results][hutq]. 2026-08-04. Accessed 2026-10-17.
30. [Hut 8, Beacon Point financing][hut]. 2026-06-09. Accessed 2026-10-17.
31. [Financial Times/Yahoo, Investors dump data centre bonds as AI borrowers face ‘Darwin moment’][prices]. 2026-10-15. Accessed 2026-10-17.
32. [CoreWeave, DDTL 4.0, SEC exhibit][crwv4]. 2026-03-31. Accessed 2026-10-17.
33. [CoreWeave, DDTL 5.5, SEC exhibit][crwv55]. 2026-08-10. Accessed 2026-10-17.
34. [CoreWeave, Magnetar/Blackstone facility][crwv23]. 2023-08-03. Accessed 2026-10-17.
35. [Blackstone, CoreWeave debt facility][crwv24]. 2024-05-17. Accessed 2026-10-17.
36. [Lambda/Business Wire, GPU-backed facility][lambda24]. 2024-04-04. Accessed 2026-10-17.
37. [Lambda, Senior secured fixed-rate financing][lambda26]. 2026-10-01. Accessed 2026-10-17.
38. [Crusoe/Upper90, GPU credit facility][crusoe]. 2025-03-27. Accessed 2026-10-17.
39. [Apollo, Valor/xAI compute infrastructure capital solution][xai]. 2026-01-07. Accessed 2026-10-17.
40. [TeraWulf Q2 10-Q, notes and Google recognition agreements][wulf]. 2026-08-05. Accessed 2026-10-17.
41. [Broadcom, Apollo and Blackstone AI XPV platform][avgo]. 2026-06-09. Accessed 2026-10-17.
42. [Reuters/Economic Times, AI credit default swap spreads widen sharply][cds]. 2026-10-15. Accessed 2026-10-17.
43. [Reuters/Economic Times, Why CDS unnerve AI investors][cdsex]. 2026-10-15. Accessed 2026-10-17.
44. [Reuters/MarketScreener, AI credit insurance reaches records (Swedish syndication)][cds64]. 2026-10-15. Accessed 2026-10-17.
45. [Teleborsa, S&P downgrades Oracle][orating]. 2026-07-10. Accessed 2026-10-17.
46. [Financial Times/Yahoo, Anthropic secured highest junk rating][arating]. 2026-10-16. Accessed 2026-10-17.
47. [Mint, Anthropic/Blackstone chip financing, citing FT][north]. 2026-10-17. Accessed 2026-10-17.
48. [Reuters/Yahoo, Anthropic offers Blackstone double-digit yield, FT reports][northreut]. 2026-10-16. Accessed 2026-10-17.
49. [FRED, Moody’s Baa and Aaa corporate yields, monthly CSV][fred]. 2026-09 observation. Accessed 2026-10-17.
50. [FRED/ICE BofA, US HY option-adjusted spread CSV][fredhy]. 2026-10-15 observation. Accessed 2026-10-17.
51. [Morgan Stanley, How Credit Markets Could Finance AI’s Trillion Dollar Gap][msgap]. 2025-08-06. Accessed 2026-10-17.
52. [Morgan Stanley, Inside the AI Debt Surge][msdebt]. 2026-06-18. Accessed 2026-10-17.
53. [Bloomberg/Insurance Journal, Data centers need investment through 2030][moodys]. 2026-01-12. Accessed 2026-10-17.
54. [Moody’s, Private Credit Outlook 2026][moodypc]. 2026-01-21. Accessed 2026-10-17.
55. [S&P Global Ratings, AI infrastructure investment outlook][sp]. 2026-08-27. Accessed 2026-10-17.
56. [Hut 8/PublicNow, River Bend lease][hutlease]. 2025-12-17. Accessed 2026-10-17.
57. [BIS, Financing the AI infrastructure boom: on- and off-balance-sheet borrowing][bis]. 2026-03. Accessed 2026-10-17.
58. [Richmond Fed, Boom and Bust in Telecommunications][telecom]. 2003, Fall. Accessed 2026-10-17.
59. [BIS Bulletin, Financing the AI boom: from cash flows to debt][bisjan]. 2026-01-07. Accessed 2026-10-17.
60. [Fitch/APLMA/Latham & Watkins, Network effects, Data Centre Financing][fitch]. 2026, exact date unavailable. Accessed 2026-10-17.
61. [CRISIL, US private credit trends: Momentum eases][flows]. 2026-09, exact date unavailable. Accessed 2026-10-17.
62. [CoreWeave, September convertible issuance, SEC 8-K][crwvsep]. Completed 2026-09-22; earliest reported event 2026-09-17. Accessed 2026-10-17.
63. [Axios, Oracle moves to shield itself from AI buildout risks][jupnotice]. 2026-09-24. Accessed 2026-10-17.
64. [Oracle, Project Jupiter economic impact and scope announcement][juporacle]. 2026-10-13. Accessed 2026-10-17.
65. [BIS authors, Circular relationships among AI firms, Bulletin 137][bis137]. 2026-10-01. Accessed 2026-10-17.
66. [Oracle, Q1 fiscal 2027 results][orclresults]. 2026-09-10. Accessed 2026-10-17.
67. [Oracle, August 2026 10-Q][orclq]. Quarter ended 2026-08-31. Accessed 2026-10-17.
68. [Financial Times/BizNews, Investors dump data centre bonds][pricesalt]. 2026-10-16; alternate version, same FT reporting as source 31. Accessed 2026-10-17 via HTML fetch; web text extraction exposed only headline/date.
69. [Newmark, Initial Abilene construction financing, phase 1][abilene1]. Publication date not independently retrieved. Cross-check verified the amount; source was found in primary-site search, but full-page fetch returned 403 on 2026-10-17.
70. [Microsoft, FY2026 10-K filing index][msftindex]. 2026-07-29. Cross-check accessed 2026-10-17; body/principal not independently reproduced.
71. [Oracle, FY2026 indexed annual report][orclindex]. 2026-06-22. Cross-check obtained indexed principal schedule on 2026-10-17; full-document retrieval failed.
72. [Independent debt-markets cross-check](../../reviews/debt-markets-codex-xcheck.md). Codex, 2026-10-17; applied 2026-10-17.

73. [Sharma, Padma, and Pierce George, Beyond Valuations: Long-Term Financial Risks from the AI Build-Out][kcfed]. Federal Reserve Bank of Kansas City, Economic Bulletin, 2026-10-05. Charts 1, 3 and 4 and endnotes. Accessed 2026-10-18.
74. [Axios issuance report][axiosdebt]. Madison Mills, 2026-10-16, citing FT. Accessed 2026-10-18.
75. [Rising borrowing costs signal funding risks for global AI expansion: Jefferies report][wood]. Economic Times/ANI, 2026-10-17. Full HTML retrieved directly; original Jefferies note not retrieved. Accessed 2026-10-18.
76. [Brace for Impact: Protecting People and the Economy when the AI Bubble Bursts][omi]. Open Markets Institute, 2026-10-16. Advocacy report; not a holdings census. Accessed 2026-10-18.
77. [Microsoft FY2024 annual report, Note 1][mslife]. Historical useful-life policy, effective FY2023. Accessed 2026-10-18.
78. [Meta 2025 10-K, Note 1][metak]. 2026-01-29; source 22 rechecked for hardware/building lives on 2026-10-18.

[meta25]: https://www.sec.gov/Archives/edgar/data/1326801/000119312525258837/d61769dfwp.htm
[meta26]: https://www.sec.gov/Archives/edgar/data/1326801/000119312526197902/d148113dfwp.htm
[meta]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
[goog25a]: https://www.sec.gov/Archives/edgar/data/1652044/000119312525100802/d806252dfwp.htm
[goog25]: https://www.sec.gov/Archives/edgar/data/1652044/000119312525263045/d41216dfwp.htm
[goog25e]: https://www.sec.gov/Archives/edgar/data/1652044/000119312525103574/d946828dfwp.htm
[goog25n]: https://www.sec.gov/Archives/edgar/data/1652044/000119312525262837/d74700dfwp.htm
[goog]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
[goog26]: https://www.sec.gov/Archives/edgar/data/1652044/000119312526043127/d297481dfwp.htm
[googaug]: https://www.sec.gov/Archives/edgar/data/1652044/000119312526338750/d159970dfwp.htm
[amzn25]: https://www.sec.gov/Archives/edgar/data/1018724/000110465925113283/tm2530638d2_fwp.htm
[amzn]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[amzn26]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926025948/tm266670d5_fwp.htm
[amznjul]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926081334/tm2619352d3_fwp.htm
[amznsep]: https://www.sec.gov/Archives/edgar/data/1018724/000110465926106322/tm2624614d4_fwp.htm
[msft]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[orcl25a]: https://www.sec.gov/Archives/edgar/data/1341439/000119312525017365/d901407dfwp.htm
[orcl25]: https://www.sec.gov/Archives/edgar/data/1341439/000119312525215807/d49252dfwp.htm
[orcl26]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526033882/d44245dfwp.htm
[orcl]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
[crwv]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
[metak]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[vantage]: https://www.bloomberglinea.com/negocios/bancos-alistan-deuda-por-us38000-millones-para-centros-de-datos-de-oracle/
[jupiter]: https://www.aol.com/articles/oracles-18-billion-data-center-220302000.html
[abilene]: https://finance.yahoo.com/news/newmark-facilitates-7-1-billion-171000176.html
[beignet]: https://www.cliffordchance.com/insights/thought_leadership/trends/2026/energy-and-resources-insights-2026.html
[metajv]: https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
[qts]: https://www.paulhastings.com/en-GB/news/paul-hastings-advises-the-initial-purchasers-on-qts-data-centers-usd4-6-billion-notes-offering
[hutq]: https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results
[hut]: https://www.hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data
[prices]: https://ca.finance.yahoo.com/news/investors-dump-data-centre-bonds-132608292.html
[crwv4]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex991.htm
[crwv55]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm
[crwv23]: https://www.coreweave.com/blog/coreweave-secures-2-3-billion-debt-financing-magnetar-capital-blackstone
[crwv24]: https://www.blackstone.com/news/press/coreweave-secures-7-5-billion-debt-financing-facility-led-by-blackstone-and-magnetar/
[lambda24]: https://markets.financialcontent.com/prnews/article/bizwire-2024-4-4-lambda-announces-500m-gpu-backed-facility-to-expand-cloud-for-ai
[lambda26]: https://lambda.ai/blog/lambda-closes-1-billion-senior-secured-fixed-rate-financing
[crusoe]: https://crusoe.ai/newsroom/upper90-closes-usd225m-credit-facility-to-crusoe-to-expand-ai-cloud/
[xai]: https://www.apollo.com/wealth/insights-news/pressreleases/2026/01/apollo-backs-5-4-billion-valor-and-xai-data-center-compute-infrastructure-transaction-with-3-5-billion-capital-solution-3214463
[wulf]: https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001083301-26-000166/0001083301-26-000166.pdf
[avgo]: https://investors.broadcom.com/news-releases/news-release-details/broadcom-apollo-and-blackstone-establish-landmark-strategic
[cds]: https://economictimes.indiatimes.com/tech/artificial-intelligence/ai-credit-default-swap-spreads-widen-sharply/articleshow/134958105.cms
[cdsex]: https://economictimes.indiatimes.com/markets/us-stocks/news/why-are-credit-default-swaps-unnerving-ai-investors/articleshow/134967395.cms
[cds64]: https://se.marketscreener.com/nyheter/priset-p-kreditskydd-inom-ai-rusar-nar-fortroendet-for-datacenter-sviktar-ce785dd3d888f127
[orating]: https://www.teleborsa.it/News/2026/07/10/oracle-declassata-a-bbb-da-s-p-per-aumento-del-rischio-e-calo-del-flusso-di-cassa-59.html
[arating]: https://finance.yahoo.com/technology/ai/articles/anthropic-secured-highest-junk-credit-040018773.html
[north]: https://www.livemint.com/ai/artificial-intelligence/anthropic-offers-blackstone-double-digit-yield-in-chip-financing-deal-what-the-60-billion-deal-entails-11792204532812.html
[northreut]: https://finance.yahoo.com/technology/ai/articles/anthropic-offers-blackstone-double-digit-010109537.html
[fred]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA,AAA&cosd=2026-09-01&coed=2026-09-30
[fredhy]: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-10-15&coed=2026-10-15
[msgap]: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/credit-markets-ai-financing-gap-vishy-tirupattur-vishwas-patkar
[msdebt]: https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/ai-debt-surge-carolyn-campbell-vishwas-patkar
[moodys]: https://www.insurancejournal.com/news/national/2026/01/12/853930.htm
[moodypc]: https://www.moodys.com/web/en/us/insights/credit-risk/outlooks/private-credit-2026.html
[sp]: https://press.spglobal.com/2026-08-27-AI-Infrastructure-Investment-To-Exceed-1-3-Trillion-By-2027,-S-P-Global-Ratings-Says
[hutlease]: https://ebs.publicnow.com/view/BD5482EC294A1654616EF4B574388EFCA461061B
[bis]: https://www.bis.org/publications/qr-202603/financing-ai-infrastructure-boom-on-and-off-balance-sheet-borrowing
[telecom]: https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/economic_quarterly/2003/fall/pdf/wolman.pdf
[bisjan]: https://www.bis.org/publications/bulletin-120-financing-ai-boom-cash-flows-debt
[fitch]: https://your.fitch.group/rs/732-CKH-767/images/APLMA_Fitch_L%26W_Data%20Centre%20Whitepaper.pdf
[flows]: https://integraliq.crisil.com/en/homepage/what-we-think/all-our-thinking/reports/2026/09/us-private-credit-trends-momentum-eases-in-the-second-quarter.html


[abilene1]: https://www.nmrk.com/insights/press-releases/newmark-arranges-2-3-billion-construction-financing-for-206-mw-build-to-suit-data-center
[abilene2]: https://www.prnewswire.com/news-releases/newmark-facilitates-7-1-billion-construction-loan-to-develop-ai-data-center-302463532.html
[msftindex]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm
[orclindex]: https://www.sec.gov/ixviewer/ix.html?doc=%2FArchives%2Fedgar%2Fdata%2F1341439%2F000119312526277521%2Forcl-20260531.htm
[pricesalt]: https://www.biznews.com/global-investing/investors-dump-data-centre-bonds
[wulfhtml]: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm
[crwvsep]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000432/crwv-20260917.htm
[jupnotice]: https://www.axios.com/2026/09/24/oracle-force-majeure-blue-owl-openai
[juporacle]: https://www.oracle.com/news/announcement/project-jupiter-is-expected-to-generate-13-billion-in-economic-impact-2026-10-13/
[bis137]: https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms
[orclresults]: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
[orclq]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm

[kcfed]: https://www.kansascityfed.org/research/economic-bulletin/beyond-valuations-long-term-financial-risks-from-the-ai-build-out/
[axiosdebt]: https://www.axios.com/2026/10/16/wall-street-limit-ai-spending-debt
[wood]: https://economictimes.indiatimes.com/markets/us-stocks/news/rising-borrowing-costs-signal-funding-risks-for-global-ai-expansion-jefferies-report/articleshow/135012567.cms
[omi]: https://www.openmarketsinstitute.org/publications/report-brace-for-impact-protecting-people-and-the-economy-when-the-ai-bubble-burst
[mslife]: https://www.microsoft.com/investor/reports/ar24/
