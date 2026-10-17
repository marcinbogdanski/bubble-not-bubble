# AI debt markets: where losses sit if the build disappoints

*Last updated: 2026-10-17 · Status: draft · Author: Codex / OpenAI · Reviewer: none*

## Summary

- Credit risk is concentrated in construction, customer-dependent compute financing and residual chip values; profitable hyperscaler businesses provide a substantial cushion.
- Meta’s cited $24.9B is net proceeds: face issuance was $25B. Alphabet’s $49.6B equity/mandatory-preferred raise is not bond debt.
- Identified corporate principal and selected project securities total approximately $572.5B across dated snapshots. Adding construction commitments, subsequent verified USD issuance and the announced Anthropic chip transaction gives a roughly $723B gross financing perimeter, **not AI-only debt outstanding**.
- Developer bonds are claims on project vehicles, not automatically on the named hyperscaler. Lease commencement, termination rights and guarantees determine who pays.
- Reported October project prices and CDS indicate selective stress despite tight aggregate credit spreads. Prices are not realized credit losses.
- Insurers and pensions participate directly and through managed funds; their aggregate AI holdings and banks’ retained underwriting exposures remain unmeasured.
- The largest uncertainty is whether contracted customer payments and recoverable collateral survive together when compute returns disappoint.

## Key claims

Dollar amounts are USD unless another currency is shown; B = billion, bp = basis points. All sources accessed **2026-10-17**. Analyst forecasts are identified as estimates even when their publication is primary.

| # | Claim | Value | As of | Source | Type | Grade |
|---|-------|-------|-------|--------|------|-------|
| 1 | Meta issuance, settled November | $30B; maturities 2030–2065; coupons 4.20–5.75%; Treasury spreads 50–110bp | 2025 | [Term sheet][meta25] | primary | A |
| 2 | Meta issuance, settled May | $25B face, $24.91B net; 2031–2066; coupons 4.55–6.45%; T+53–147bp | 2026-05 | [Terms][meta26], [10-Q][meta] | primary | A |
| 3 | Alphabet issuance | $22.5B USD plus €13.25B; April USD T+32–70bp, November T+30–107bp; respective EUR Bund spreads 66.7–114.8/41.5–122.8bp; maturities 2028–2075 overall | 2025 | [April USD][goog25a], [November USD][goog25], [April EUR][goog25e], [November EUR][goog25n] | primary | B, sums |
| 4 | Alphabet first-half debt issuance | $20B USD + $31.8B foreign-currency equivalent; February USD T+27–95bp, 2029–2066; sterling extends to 2126 | 2026-06-30 | [10-Q][goog], [USD terms][goog26] | primary | A |
| 5 | Alphabet later USD issuance | $25B; 2028–2066; fixed coupons 4.50–6.50%, T+33–130bp | 2026-08-06 | [Term sheet][googaug] | primary | A |
| 6 | Alphabet equity financing | $49.6B aggregate net common/preferred proceeds; preferred mandatorily converts May 2029 | 2026-06 | [10-Q][goog] | primary | A |
| 7 | Amazon issuance | $15B; 2028–2065; coupons 3.90–5.55%; T+30–85bp | 2025-11 | [Term sheet][amzn25] | primary | A |
| 8 | Amazon issuance | March $37B USD, 2028–2076, T+30–130bp fixed; €14.5B, CHF2.8B, C$14B also issued by June; July $25B, T+40–125bp, 2029–2066; September £4.25B, Gilt+53–93bp, 2029–2045 | 2026-09 | [10-Q][amzn], [March][amzn26], [July][amznjul], [September][amznsep] | primary | A |
| 9 | Microsoft direct issuance | Zero debt-issuance cash proceeds in FY2025/FY2026; outstanding principal $46.136B | 2026-06-30 | [10-K][msft] | primary | A |
| 10 | Oracle issuance | January-priced/February-settled $7.75B, 2028–2065, fixed T+57–135bp; September $18B, 2030–2065, T+75–137bp | 2025 | [January][orcl25a], [September][orcl25] | primary | B, sums |
| 11 | Oracle issuance | $25B including floating tranche; 2029–2066; fixed coupons 4.55–6.85%, T+95–195bp; floater SOFR+111bp | 2026-02 | [Term sheet][orcl26] | primary | B, sum |
| 12 | Corporate principal perimeter | Meta $84B; Alphabet $101.085B; Amazon $132.995B; Microsoft $46.136B; Oracle principal schedule $130.105B; sum $494.321B | May/June 2026 | [Meta][meta], [Alphabet][goog], [Amazon][amzn], [Microsoft][msft], [Oracle][orcl] | primary | B, sum |
| 13 | Oracle bank facilities | Original refinanced term commitment $5.63B, SOFR+112.5–162.5bp; scheduled balloon August 2027, extension options; $10B revolver undrawn, expires March 2031; $1.5B commercial paper outstanding | 2026-05-31 | [10-K][orcl] | primary | A |
| 14 | Selected principal payments: 2027/2028/2029/2030 | CoreWeave $6.184/4.416/2.421/3.221B calendar; Oracle $7.210/10.145/5.500/7.250B fiscal; Microsoft $9.250/0/2.001/0B fiscal; Meta $2.750/1.500/1.000/5.000B calendar | June/May 2026; Meta Dec 2025 | [CRWV][crwv], [ORCL][orcl], [MSFT][msft], [Meta][metak] | primary | A |
| 15 | Vantage Texas/Wisconsin loans, reported, unverified | Approximately $38B, JPMorgan/MUFG-led; preliminary benchmark+250bp; planned distribution to loan/private-credit investors | 2025-09-04 report | [Bloomberg][vantage] | secondary | C |
| 16 | Jupiter loans, reported, unverified | $18B; quoted 89–91 cents; syndication stalled, Santander/Jefferies among quoting banks | 2026-09-18 | [Reuters citing FT][jupiter] | secondary | C |
| 17 | Abilene construction financing | $2.3B initial + $7.1B second-phase loans = $9.4B announced; JPMorgan-led | 2025-05-22 | [Arranger announcement][abilene] | primary | B, sum |
| 18 | Hyperion/Beignet | $27.3B private securities; PIMCO-managed accounts majority investors; Meta/Blue Owl ownership 20%/80%; initial lease 4 years, conditional capped residual guarantee first 16 operating years | 2025 transaction | [Counsel][beignet], [Meta][metajv] | primary | A |
| 19 | QTS Fayetteville project notes | $4.6B, 5.700%, due 2036, non-recourse single-asset financing | 2026-04-21 | [Purchasers’ counsel][qts] | primary | A |
| 20 | Hut 8 project notes | River Bend $3.25B + Beacon Point $4.25B = $7.5B, fully amortizing/non-recourse; Beacon 6.129%, due 2042, T+165bp, Baa2 | 2026-Q2 | [Results][hutq], [Beacon terms][hut] | primary | A |
| 21 | Project prices: reported, unverified dealer marks | Beignet below 91; QTS Excalibur below 87; Hut Louisiana about 93, Texas about 91 cents | 2026-10-15 | [FT syndication][prices] | secondary | C |
| 22 | CoreWeave drawn debt and older DDTLs | $35.551B gross; net recourse $31.405B/non-recourse $3.663B; DDTL 1.0/2.0 balances $1.300/$3.190B, effective rates 15%/11%, maturities March 2028/August 2030 | 2026-06-30 | [10-Q][crwv] | primary | A |
| 23 | CoreWeave structured facilities | DDTL 4.0 $8.5B capacity, A3/A(low), SOFR+225bp or about 5.9% fixed, March 2032; DDTL 5.5 $2.6B, SOFR+550bp, about 5-year debt versus 3-year average customer contracts | March/August 2026 | [SEC March release][crwv4], [August release][crwv55] | primary | A |
| 24 | CoreWeave historical lender commitments | $2.3B led by Blackstone/Magnetar, with PIMCO/BlackRock/Carlyle; subsequent $7.5B facility includes CDPQ | 2023/2024 | [Borrower][crwv23], [Blackstone][crwv24] | primary | A |
| 25 | Lambda facilities | Up to $0.5B GPU facility, Macquarie/IDF; new $1.008B DDTL, 6.78%, Baa1/A(low), fully amortizes by May 2033, marketed to insurers | 2024-04 / 2026-10-01 | [Company release][lambda24], [Lambda][lambda26] | primary | A |
| 26 | Crusoe GPU credit | Approximately $0.225B, Upper90-led; BCI, FS, King Street, Liberty Mutual, ORIX participate | 2025-03-27 | [Company release][crusoe] | primary | A |
| 27 | xAI/Valor equipment financing | Apollo-led $3.5B “capital solution” supporting $5.4B compute acquisition/lease; NVIDIA anchor equity investor | 2026-01-07 | [Apollo][xai] | primary | A |
| 28 | Fluidstack-linked project debt | TeraWulf $3.2B secured notes due 2030; Google backstop begins at corresponding lease commencement, with termination-payment or lease-assumption alternatives | 2026-06-30 | [10-Q][wulf] | primary | A |
| 29 | Anthropic chip platform | Announced $35B initial transaction led by Apollo with Blackstone; deployment through Fluidstack sites | 2026-06-09 | [Broadcom][avgo] | primary | A |
| 30 | CoreWeave CDS | Above 1,000bp; Reuters versions imply approximately 63–64% cumulative 5-year default probability | 2026-10-15 | [Reuters quotes][cds], [Explainer][cdsex], [Swedish syndication][cds64] | secondary | C |
| 31 | Oracle CDS | Record 288bp; Reuters explainer rounds to nearly 300bp | 2026-10-15 | [Reuters][cds], [Explainer][cdsex] | secondary | B |
| 32 | Oracle rating action | S&P BBB→BBB−, stable; higher business risk/weaker prospective cash flow | July 2026 | [Teleborsa][orating], [Reuters confirmation][jupiter] | secondary | B |
| 33 | Anthropic rating, reported, unverified | KBRA BB+ issuer/junior rating in June; $4.4B junior within $35B transaction, about 8.5% yield; limited disclosed cash-flow information | 2026-10-16 report | [FT syndication][arating] | secondary | C |
| 34 | North Star proposal, reported, unverified | $60B: $42B senior reportedly Broadcom-guaranteed, $18B junior; Blackstone $9B allocation, 10% coupon/>10% yield; 5-year chip leases, about 1.5GW | 2026-10-16/17 | [Mint citing FT][north], [Reuters, unverified][northreut] | secondary | C |
| 35 | Broad credit context | Baa 6.47% minus Aaa 6.03% = 0.44pp; HY OAS 3.23pp | 2026-09 / 2026-10-15 | [FRED yields][fred], [FRED OAS][fredhy] | primary | B, subtraction |
| 36 | Morgan Stanley external-capital estimate | $1.5T gap against $2.9T spending over four years; private credit/ABF $800B, IG $200B, ABS/CMBS $150B, other $350B | 2025-08-06 | [Bank transcript][msgap] | primary | A, forecast |
| 37 | Morgan Stanley issuance estimate | About $250B AI debt issued YTD; approximately $500B forecast for full year | 2026-06-18 | [Bank transcript][msdebt] | primary | A, estimate |
| 38 | Moody’s estimates | At least $3T data-center investment through 2030; private-credit AUM >$2T in 2026, approaching $4T by 2030, across all sectors | January 2026 | [Bloomberg][moodys], [Moody’s][moodypc] | secondary / primary | C |
| 39 | S&P financing pressure | Hyperscaler capex >$1.3T in 2027; negative free operating cash flow expected across six hyperscalers in 2026/2027 | 2026-08-27 | [Agency release][sp] | primary | A, forecast |
| 40 | Mapped financing perimeter | $572.472B snapshots including $42.6B project securities; construction capacity $65.4B; announced chip transaction $35B; later corporate gross issuance $50B; extended sum $722.872B | mixed dates above | Claims 5,8,12,15–20,22,28–29 | primary / secondary | C |

## Analysis

**What is financed, and who can pay.** Advertising, software, retail and cloud cash flows support hyperscaler debt. Microsoft’s leased suppliers can borrow against its rent despite its absence of direct issuance. Corporate proceeds cannot all be assigned to AI; Alphabet’s mandatory preferred primarily creates dilution and dividends.

**Estimated stack by instrument and holder.** The CSV distinguishes stocks, issuance flows, capacities and proposals. Amounts below are a deliberately incomplete exposure map; corporate principal includes legacy non-AI borrowing, and project issuance can include reserves or refinancing.

| Instrument | Identified amount | Named financing providers / ultimate loss holders | Evidence |
|---|---:|---|---|
| Hyperscaler corporate principal | $494.321B | Bond funds, insurers, pensions, bank lenders; allocations largely undisclosed | Claim 12, A/B |
| CoreWeave drawn debt, including notes, converts, DDTLs and vendor financing | $35.551B | Private-credit accounts, banks, bondholders, equipment financiers | Claims 22–24, A |
| Selected project securities: Beignet, QTS, Hut, TeraWulf | $42.6B | PIMCO accounts and institutional bond investors; Blue Owl/Blackstone often sponsor equity rather than ultimate debt holders | Claims 18–20,28; A/B |
| **Subtotal of dated principal/securities** | **$572.472B** | Holder look-through unavailable | Claim 40, B/C |
| Abilene/Vantage/Jupiter construction capacity, additional | $65.4B | JPMorgan/MUFG-led syndicates and other banks; distribution/retention unverified | Claims 15–17, A/C |
| Anthropic initial chip transaction, additional announced capacity | $35B | Apollo/Blackstone platform investors; funded balance not disclosed here | Claim 29, A |
| July Amazon/August Alphabet USD issuance, additional gross flow | $50B | Institutional bond investors; repayments/FX not rolled forward | Claims 5,8; A/B |
| **Extended gross financing perimeter** | **$722.872B** | Mixed principal snapshots, subsequent gross issuance and commitments | Claim 40, C coverage |

Lambda, Crusoe and xAI examples are outside that subtotal: their facility capacities, remaining draws and overlap with later refinancings are insufficiently reconciled. North Star remains proposed. Adding tenant lease commitments, vendor guarantees or the financing-gap forecast to these totals would count overlapping economic exposure. This is no global debt census.

Blackstone and Magnetar are verified CoreWeave lenders; PIMCO anchors Beignet; Apollo finances equipment vehicles; Blue Owl supplies project equity and organizes capital. CDPQ and BCI demonstrate pension participation; Liberty Mutual and CoreWeave’s disclosed insurance investors demonstrate insurer participation. Asset-manager AUM is not the manager’s own loss-bearing balance sheet. [Blackstone][crwv24], [Crusoe][crusoe], [CoreWeave][crwv4]

**Project credit and GPU credit differ.** Beignet investors depend on Meta rent and conditional residual support; Meta’s guarantee is not an unlimited promise to repay every bond. QTS creditors own project claims, not Microsoft corporate notes. Hut’s Louisiana lease is with Fluidstack, backstopped by Google; the Texas Nvidia tenancy is reported by the FT. Calling both Hut projects Nvidia leases is unsupported. [Meta][metajv], [QTS counsel][qts], [Hut][hutlease], [FT][prices]

CoreWeave’s older DDTLs combine contractual cash receipts with equipment collateral. Its later contract/debt mismatch requires successful renewal, replacement customers or residual recoveries. The cheaper investment-grade facility has different contractual support: its spread cannot be compared with the later facility as a pure time-series repricing. Lambda’s fully amortizing structure is another meaningful protection. [March facility][crwv4], [August facility][crwv55], [Lambda][lambda26]

**Maturity wall and repricing order.** Claim 14 mixes calendars: Oracle years end in May, Microsoft in June. Meta’s new May issue starts beyond the requested window. Construction loans may require takeout when construction completes, well before a project bond’s legal final maturity. Jupiter’s original proposed tenor and Vantage’s final extension conditions were not verified.

CDS, bonds and new-deal discounts reprice first. Floating interest, draw conditions, collateral tests and construction deadlines transmit stress before maturity. Amortizing GPU loans require continuing cash generation. Fixed corporate coupons do not reset when secondary prices fall; their issuers face the new price when refinancing or borrowing again. Fully amortizing Hut bonds reduce balloon-refinancing risk, but retain completion and tenant-performance risk.

**Contagion and the default-cycle scenario.** If returns disappoint, sponsor equity and subordinate capital generally absorb impairment first, followed by secured creditors to the extent collateral and guarantees fail; contractual priority controls the actual waterfall. Private-credit marks can lag traded comparables. Lower marks and redemptions can restrict new lending; warehouse and fund-finance lenders can tighten collateral terms or refuse renewals. Undistributed construction commitments then remain with underwriting banks.

ABS and CMBS route rents, mortgages or equipment receivables through vehicles to institutional investors. Subordination and reserves protect senior claims but cannot diversify a common tenant or unavailable power. Insurer losses initially hit investment income/capital; downgrades can increase capital pressure. Pension losses affect asset values and funding. PIMCO funds are not automatically Allianz general-account investments. The BIS explicitly identifies bank funding lines, guarantees and non-bank investors as transmission channels. [BIS][bis]

A telecom-style default cycle would start with delays and weak compute cash conversion, close refinancing access for marginal operators, then force restructurings, vendor concessions and collateral sales. Surviving buyers could acquire usable power-connected assets at lower cost. Unlike fiber, specialized chips can lose economic relevance during workouts. Systemic banking stress would require meaningful retained leverage, correlated guarantees or funding withdrawals; isolated project price declines do not establish it. This is a conditional mechanism, not a default forecast. [Richmond Fed][telecom], [BIS][bisjan]

## Conflicts and open questions

- **Counterevidence:** Morgan Stanley’s June assessment emphasized strong hyperscaler credit and diversified, operating securitization collateral; BIS initially judged financial-stability risks moderate. S&P’s later cash-flow forecast and October price stress weaken, without disproving, that case. [Morgan Stanley][msdebt], [BIS][bisjan], [S&P][sp]
- Jupiter’s stress report was published in September, not first established in mid-October. Quotes are indications, not verified executed trades or bank accounting losses. [Reuters][jupiter]
- Reuters syndications differ between approximately 63% and 64% CDS-implied default risk. Recovery assumptions, risk premia and liquidity make neither an objective default forecast. [Reuters explainer][cdsex], [Reuters syndication][cds64]
- No primary KBRA report or original S&P Oracle action was retrieved. Anthropic rating/financing details remain reported, unverified. North Star closing, guarantee documentation and final allocations remain unknown.
- Moody’s capex/AUM forecasts, S&P capex projections and Morgan Stanley financing needs measure different universes. No reproducible current AI-only private-credit stock was retrieved from Fitch or Bank of America. Fitch’s joint whitepaper instead highlights leverage layered across holding companies, projects and GPUs. [Fitch joint whitepaper][fitch]
- Exact insurer/pension holdings, bank warehouse exposure, project-loan drawn balances, current secondary spreads and subsequent repayments and foreign-currency issuance are incomplete. Fund redemption pressure is documented; an AI-infrastructure-loss-caused gate was not verified. [CRISIL][flows]

## Signals to watch

| Signal | Current value | As of | Source | Why it matters |
|--------|---------------|-------|--------|----------------|
| CoreWeave CDS | >1,000bp | 2026-10-15 | [Reuters][cds] | Marginal refinancing price |
| Oracle CDS | 288bp | 2026-10-15 | [Reuters][cds] | Tenant/bank concentration |
| Project bonds | Beignet <91; QTS <87; Hut ~91–93 | 2026-10-15 | [FT][prices] | Execution/residual risk |
| Construction syndication | Jupiter $18B, indications 89–91 | 2026-09-18 | [Reuters/FT][jupiter] | Retained underwriting exposure |
| New GPU deals | Lambda $1.008B at 6.78%, closed | 2026-10-01 | [Lambda][lambda26] | Financing remains available selectively |
| Chip financing | North Star $60B proposed, junior yield >10% | 2026-10-16/17 | [Mint/FT][north] | Next funding/guarantee test |
| Ratings | Oracle BBB− stable; Anthropic reportedly BB+ | July/June 2026 | [Oracle report][orating], [FT][arating] | Eligibility and capital sensitivity |
| Aggregate spreads | Baa–Aaa 0.44pp; HY OAS 3.23pp | Sept / Oct 15 2026 | [FRED][fred], [ICE/FRED][fredhy] | Sector versus broad repricing |
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
25. [Newmark/PR Newswire, Construction loan for Abilene][abilene]. 2025-05-22. Accessed 2026-10-17.
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

