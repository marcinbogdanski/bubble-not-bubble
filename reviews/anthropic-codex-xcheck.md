# Anthropic — independent Codex cross-check

*As of and sources accessed: 2026-10-17. Read report/methodology.md, tasks/RESEARCH_BRIEF.md and research/stack/anthropic.md. Only this review was written; no git commands were run.*

## Verdict

The core conclusion survives: substantial demand, improving reported economics, and material financing risk; this evidence does not establish either durable profitability or inevitable failure.
The 15 selected rows largely reproduce their sources correctly, but confidential financial figures remain grade C; the coupon/yield interpretation needs correction.
Revise before relying on the note: add known funding overlap, restricted-cash/default provisions, recent capacity and adoption evidence, and a dated, quantitative first Summary bullet.

## Claim re-verification

Selection: rows 2, 3, 4, 6, 7, 9, 12, 16, 18, 21, 22, 27, 31, 32 and 33. These underpin demand, profitability, accounting comparability, fundraising, fixed obligations and creditor exposure. “Matches” means the fetched source supports the attribution, not that a private company's financials were independently audited. I searched for public issuer filings and company/supplier disclosures; no public Anthropic registration statement or executed North Star documents were located. Secondary accounts of confidential documents or meetings therefore remain **reported, unverified, C**, even where several outlets repeat them.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 2 | ~$9bn end-2025; $14bn February; >$30bn April; >$47bn May 2026 run-rate | Same. April 6 supplies both the end-2025 and April figures; February 12 and May 28 supply the other points. | [Series G][G], [April update][APR], [Series H][H] — primary | Yes; these are annualized rates, not annual revenue. | A |
| 3 | >$65bn July; ~$74bn outside projection; $110bn year-end expectation; no new company rate at meeting | CNBC's description says $65bn at end-July, without a strict “greater than.” PYMNTS relays ~$74bn and no updated company disclosure; Reuters attributes $110bn to analysts. | [CNBC description][CNBC], [FT/WSJ relay][P1], [Reuters October 14][Q3] | Substantively; use ~$65bn with this particular CNBC source. ~$74bn lacks a firmly specified endpoint in the cited relay. | C throughout |
| 4 | Q1 $4.7bn; Q2 $11.6bn; Q3 $16.8bn; conflicting relays | Reuters gives exactly $4.7bn/$11.6bn/$16.8bn. The FT relay gives Q1 $4.8bn; Euronews gives Q2 $11.5bn. | [Reuters][Q3], [FT relay][P1], [Euronews][EURO] | Yes; both discrepancies independently reproduced. No public quarterly accounts found. | C |
| 6 | 2025 ~$4.6bn sales, >$8bn operating loss, ~$42bn net loss including ~$34bn remeasurement; $7.33bn compute, $12.65bn operating expenses; $20.28bn year-end liquid assets | All figures reproduced in Reuters' September 28 account of the confidential prospectus. | [Reuters September 28][FY25] | Yes as reported; no primary accounts available for independent reconciliation. | C |
| 7 | Q3 second adjusted profitable quarter; 11% adjusted operating margin; $1.70 sales/compute dollar; positive cash flow without amount | FT relay supports second quarter, 11% and $1.70; Axios reports positive Q3 cash flow, without amount. | [FT relay][P2], [Axios][AX] | Yes as reported; adjusted earnings and cash-flow definitions remain missing. | C |
| 9 | Anthropic gross/cloud sales versus OpenAI net; April normalization up to $8bn | Semafor explicitly describes the differing recognition and up to $8bn added to OpenAI's then run-rate if grossed up. | [Semafor April 10][ACCOUNT] | Yes; not an $8bn deduction from current Anthropic revenue. No public policy reconciliation found. | C |
| 12 | >300,000 businesses September 2025; >500 customers above $1m annualized February 2026; >1,000 April | Same, directly stated on September 2, February 12 and April 6. | [Series F][F], [Series G][G], [April update][APR] | Yes. Customer count and annualized spend thresholds do not establish concentration or retention. | A |
| 16 | $65bn Series H at $965bn post-money | Same, May 28; announcement also explicitly includes $15bn of previously committed hyperscaler investments, including Amazon's $5bn. | [Series H][H] | Yes, with material omitted overlap. | A |
| 18 | June 1 confidential S-1; no priced shares; expected post-midterm debut and >$2tn; ~$2tn/annualized Q3 ≈30x | June 1 submission and unset share count/price confirmed; Reuters supports expected timing and target. $2,000bn/$67.2bn = 29.76x. | [Company S-1 announcement][S1], [Reuters][Q3] | Yes, but “November” is narrower than “after the November midterms.” No public issuer S-1 located by this review. | A submission; C timing, valuation and derived multiple |
| 21 | $8bn prior + $5bn now = $13bn; up to $20bn future = $33bn maximum | Exactly the April 20 announcement's components. | [Amazon agreement][AWS] | Yes; maximum is not funded cash. | A components; B sums |
| 22 | >$100bn AWS/ten years; up to 5GW; nearly 1GW by end-2026; >1m Trainium2 chips; >100,000 Bedrock customers | All directly stated, including that nearly 1GW is capacity coming online by year-end. | [Amazon agreement][AWS] | Yes; future capacity is a plan, not installed capacity at announcement. | A |
| 27 | ≥$518bn/decade, ~80% rigid; Google $111.1bn, AWS $110bn, Microsoft $31.4bn, Broadcom $161.2bn; xAI ≤$84.5bn; AMD >$20bn | Same reported components. Cloud windows differ; xAI largely terminable on 90 days. Component rounding does not reconcile exactly to $518bn. | [Reuters September 29][OBL] | Yes as reported; no public aggregate obligations schedule found. | C |
| 31 | Conditional $42bn convertible facility, none issued August 2; Reuters identifies Anthropic and $125.2bn/five-year lease | Filing confirms ceiling, conditions, lease-only use and no notes issued. Reuters supplies identity/lease and additional liquidity restrictions. | [Broadcom 10-Q, Note 10][AVGO], [Reuters October 1][FAC] | Yes, but important restrictions omitted from Analysis; see below. | A unnamed facility; C identity and lease |
| 32 | ~$29bn maximum backstop; nothing paid; 85%-less-recovery formula | Same. Backstop rises with delivery/deployment and declines with customer lease payments over five-year terms. | [Broadcom 10-Q, Note 10][AVGO] | Yes. This is contingent exposure, not $29bn advanced or a blanket guarantee of every lease. | A terms; Anthropic attribution requires the separate reporting |
| 33 | Proposed $60bn North Star, ~1.5GW; $42bn senior backed by Broadcom; $18bn junior, Blackstone $9bn | All appear in the accessible US version of the FT relay. No primary confirmation of the proposed package found. | [Investing.com October 16, relaying FT][NS] | Yes as a proposal. Replace the inaccessible Australian URL with this accessible version. | C, not independently corroborated by Reuters repeating FT |

## Arithmetic checks

The Analysis mostly refers to figures calculated in the Key claims table rather than displaying formulas. I checked those referenced calculations too. Dollar figures below are billions unless stated otherwise. Arithmetic was independently recomputed with Python; grades inherit uncertain inputs.

| Calculation used or implied | Independent calculation | Result and interpretation |
|---|---|---|
| Sequential revenue growth, claim 5 | (11.6/4.7−1)×100 = 146.8085%; (16.8/11.6−1)×100 = 44.8276% | Correct at 146.8% and 44.8%; C. |
| Nine-month revenue and Q3 annualization | 4.7+11.6+16.8 = 33.1; 16.8×4 = 67.2 | Correct; C. Annualization is neither trailing annual sales nor an exit-month rate. |
| Removing financing remeasurement | 42−34 ≈8 | Correct approximate residual net loss, **not** a derivation of operating loss. Reuters separately reports the operating loss. Rounded expenses minus sales: 12.65−4.6 ≈8.05, consistent with >8; not a cash-flow bridge. [Reuters][FY25] |
| Adjusted profit and compute ratio | 16.8×11% = 1.848; 16.8/1.70 = 9.8824; 1−1/1.70 = 41.1765% | These are useful implied figures, not figures the note calculates. Conditional on consistent definitions, ~$1.85bn adjusted operating profit and ~41.2% of sales after the identified compute cost. Neither establishes free cash flow or a GAAP gross margin. [FT relay][P2] |
| Series G and secondary valuation comparability | 380−30 = 350 | Correct explanation for why a $350bn reference excluding new capital need not be a down round against $380bn post-money. Different dates/security rights still prevent a complete valuation comparison. [Series G][G] |
| Amazon ceiling; supplier total, claim 29 | 8+5 = 13; 13+20 = 33; 33+40+15+5 = 93 | Correct sums; B. Inputs checked in [Amazon][AWS], [Google company statement reported by Reuters][GOOG], [Microsoft/Nvidia][MS], [AMD][AMD]. Mixed historical/new/conditional ceilings are not treasury cash. |
| AWS equity ceiling/spend | 33/(>100) <33% | Correct as a loose upper bound; B. Does not measure how much AWS procurement is financed by Amazon. |
| Ten-year scale comparison, claim 28 | 518/10 = 51.8; 518×80% = 414.4; 51.8/67.2 = 77.0833%; 67.2−51.8 = 15.4 | All arithmetic correct, C. Approximate lower-bound/rounded inputs do not justify precision to $0.1bn. The $15.4bn is a hypothetical subtraction, not cash available for other costs. |
| Commitment component reconciliation | 111.1+110+31.4+161.2+84.5+20 = 518.2 | Consistent with rounded “at least $518bn,” not an exact reconciliation: xAI is an upper limit and AMD a lower threshold. [Reuters][OBL] |
| IPO illustration | 2,000/67.2 = 29.7619x | Correct rounded ~30x, C. It is equity value/sales, not EV/sales; unknown debt and current cash prevent an enterprise-value bridge. |
| North Star tranches | 42+18 = 60; 9/18 =50% | Correct, C. This verifies financing structure, not a new amount to add to compute obligations. |
| Claim 34 annual interest illustration | 9×10% =0.9 | The conditional “if interest-paying at that rate” algebra is true, but the reported offer is a **10% coupon**, with yield above 10% from discounts/fees. At $9bn outstanding face value, annual coupon would be $0.9bn, not >$0.9bn. Amount invested versus face value and draw/amortization terms remain unknown. [FT relay][NS] |
| Opus list-price reduction, claim 37 | 1−4/5 =20%; 1−20/25 =20% | Correct, B. Cache reads also fall 1−0.20/0.50 =60%; Anthropic reports 40% lower typical workload cost. [Opus launch][OPUS] |
| Tokenizer and Fable workload figures | ~30% more tokens; ~25% typical Fable savings | Source-stated estimates, not independently reproducible arithmetic without workload data. Crucially the tokenizer change dates to Claude 4.7+, so it is not a new 30% penalty when moving from Opus 5 to 5.5. [Pricing][PRICE], [Fable announcement][FABLE] |

No other numerical derivations appear in Analysis. The caveats against adding overlapping facilities, counting compute twice through margins, or treating net loss as burn are sound.

## Omissions

1. **Liquidity can deteriorate precisely when the facility is needed (October 1).** Reuters reports restricted cash deposited for Broadcom in April, possible additional collateral, and default provisions that can accelerate leases while constraining facility access. It also reports no notes expected before the IPO. The note already cites this article but relegates cash restrictions and default terms to unknowns. These provisions make the financing a conditional backstop rather than assured emergency liquidity; this strengthens the downside case. Reported, unverified, C. [Reuters][FAC]

2. **Known Series H overlap (May 28).** The primary release resolves part of the uncertainty the Analysis leaves open: see row 16. This improves the cash-financing map; it does not prove today's cash balance. A. [Series H][H]

3. **Financing price trend (October 16).** The fuller FT relay reports Project Big Sky's ~$4.4bn at 8.5% four months earlier. This is relevant evidence of rising marginal financing cost, but differences in collateral, tranche and terms prevent calling it a clean change in Anthropic's credit spread. C. [FT relay][NS]

4. **New Canadian lease (October 16).** Reuters attributes the signed EverWind lease to an Anthropic executive. EverWind confirms an initial 95MW phase planned for late 2027 and 325MW more targeted for 2028, subject to conditions. Its >C$10bn campus-and-wind project cost is the developer's investment, not a disclosed Anthropic lease liability. The primary release leaves the tenant unnamed; identification is B from attributable reporting, while announced phasing is A. This extends geographic/buildout exposure beyond the September snapshot; unknown overlap prevents increasing the $518bn total mechanically. [EverWind][EW], [Reuters][CAN]

5. **Stronger recent enterprise evidence (October 1).** Barclays' rollout targets Claude Code use by 50% of its developers by end-2026, with a majority in 2027. This is more current and concrete than the note's February Code figures, and is counterevidence to an exclusively substitution-focused discussion. It is a customer deployment plan, not disclosed incremental revenue or measured retention. A as an announced target. [Company announcement, quoting Barclays][BAR]

6. **Efficiency evidence makes the pricing argument less one-sided (September 22).** The Opus release attributes lower workload prices partly to reduced serving compute and fewer tokens per task. It supplies the cache and typical-workload reductions checked above. This could support margins even as customer prices fall; company claims do not independently establish realized unit economics. A for what the company states. [Opus launch][OPUS]

The last-30-days search covered September 18–October 17, company news, SEC material, financing, customer adoption and infrastructure announcements. It yielded no public accounts that resolve cash runway or conclusively overturn the note's thesis. Recent safety/governance announcements are relevant context but do not supply a quantified financial adjustment. I did not promote unverified social-media claims to evidence.

## Summary-bullet assessment

| Bullet | Supported by its own evidence? | Usefulness and necessary qualification |
|---|---|---|
| 1 — products, substantial enterprise traction, profitability unproven | Yes: rows 11–12 support adoption; rows 6–8 do not establish independently inspectable sustained profit. | **Too abstract:** no number, date or direct citation. Replace with the concrete sentence in edit 1. “Comfortable profitability” has no defined threshold. |
| 2 — Q3 sales and second adjusted profitable quarter | Yes, with C qualification. S5 supplies revenue and adjusted profitability; S6 explicitly supplies the second consecutive quarter. | Useful, but specify Q3 **2026** and consider including the reported 11% margin. “Suggest” is appropriately conditional. |
| 3 — company run-rate versus later reporting/estimate | Yes. It correctly distinguishes company disclosure, reporting and estimates. | Minor fix: ~$65bn for the cited CNBC description; clarify the ~$74bn estimate's uncertain measurement endpoint. The latest company figure located remains May's. |
| 4 — supplier financing and AWS procurement | Yes: rows 21–22 directly support the numbers. | Add April 20, 2026 and make clear that Amazon's $33bn includes previous funding and possible future money. Incorporate known Series H overlap in Analysis. |
| 5 — rigid payments, switching, North Star risk transfer | Broadly yes: row 27 supports rigidity, row 10 supports contract flexibility, and rows 31–33 support creditor exposure. | “Transfer” is incomplete: creditor financing reallocates/adds exposure while Anthropic retains lease obligations. Add the known default/facility linkage. Technical ability to switch does not establish actual churn. |
| 6 — confidential S-1, expected IPO, unknown cash | Yes with attribution limits. Submission is primary; public-filing absence is only a bounded search finding. November is supported by the note's other relays, although the directly cited Reuters article says after the midterms. | Date the submission June 1. Prefer “after the November midterms” when citing Reuters, or add the November-specific relay; neither timing nor valuation is committed. Some payment windows and restrictions are reported, although a complete schedule and unrestricted cash remain unknown. |

## Your assessment

I agree that Anthropic has a substantial paying market and that improving reported economics are meaningful counterevidence to a simple “all frontier-model revenue is uneconomic” thesis. I differ in the emphasis: the decisive financing risk is the interaction of demand shortfalls, lease acceleration, restricted cash and conditional access to supplier credit, rather than a ten-year average divided by today's sales. Conversely, recent bank deployment plans and documented product-efficiency claims deserve more weight alongside switching risk. Supplier-backed finance can support productive expansion while exposing multiple balance sheets to the same demand outcome; it is not itself proof of a bubble. The evidence supports concern about valuation and contractual fragility, but it cannot quantify sustainable margins, current runway or loss probability without accounts, maturities and executable financing terms. Sources and confidence limits are set out above.

## Recommended edits

1. **Replace Summary bullet 1:** “On February 12, 2026, Anthropic reported Claude Code run-rate revenue above $2.5bn, with enterprise use supplying over half; by April 6, more than 1,000 business customers each spent over $1m annualized. These establish paid adoption, but not sustained company-wide profitability.” Cite [Series G][G] and [April update][APR].

2. **Correct the funding-overlap paragraph:** “Series G includes some previously announced Microsoft/Nvidia investment. Series H's $65bn includes $15bn of previously committed hyperscaler investment, including Amazon's $5bn. These amounts must not be counted again when summing financing announcements; remaining overlaps and current unrestricted cash are unresolved.” Cite [Series G][G] and [Series H][H].

3. **Add after the Broadcom facility discussion:** “Reuters reports that Anthropic posted restricted cash for Broadcom in April 2026, may have to add collateral, and faces defaults that could accelerate leases while restricting facility access. The $42bn ceiling therefore is not assured liquidity in a stress event (reported, unverified).” Cite [Reuters October 1][FAC].

4. **Replace claim 34's interest illustration:** “Reported 10% coupon, with >10% yield including discounts and fees; a fully outstanding $9bn face amount would carry $0.9bn annual coupon, before amortization and other charges. Face amount, draw terms and package-wide cost are unconfirmed.” Cite the [accessible FT relay][NS]; retain C. Add the Big Sky comparison from Omissions with its comparability caveat.

5. **Replace the annual-average interpretation:** “Dividing the reported decade total by ten gives $51.8bn, a scale illustration rather than an annual bill. Comparing this with $67.2bn annualized Q3 sales cannot establish cash headroom or solvency. Reported contract windows already differ; annual maturities, unrestricted cash and realized revenue are needed.” Cite [obligations reporting][OBL] and [Q3 reporting][Q3].

6. **Add recent evidence in both directions:** “On October 1, Barclays announced a rollout targeting Claude Code adoption by 50% of its developers by end-2026. On October 16, Anthropic confirmed through an executive a Canadian lease with EverWind; the developer plans a 95MW initial phase for late 2027. Neither announcement discloses Anthropic's revenue or lease value.” Cite [Barclays rollout][BAR], [Reuters][CAN] and [EverWind][EW].

7. **Replace the tokenizer/pricing passage:** “Opus 5.5 cuts input/output list prices 20% and cache-read prices 60% versus Opus 5; Anthropic reports typical-workload costs 40% lower. The roughly 30% tokenizer expansion applies from Claude 4.7 onward, not newly between these two models. Lower serving compute could offset price cuts, but realized margins are undisclosed.” Cite [Opus launch][OPUS] and [pricing documentation][PRICE].

8. **Tighten remaining Summary wording:** In bullet 2 specify “Q3 2026” and “reported 11% adjusted operating margin”; in bullet 3 use “approximately $65bn at end-July 2026”; in bullet 4 add “announced April 20, 2026.” In bullet 5 replace the last sentence with “The proposed North Star package would expose private-credit investors and Broadcom to Anthropic-backed leases without removing Anthropic's payment obligations.” In bullet 6 replace “a November listing” with “a listing after the November midterms,” and “Payment schedules and available cash” with “A complete annual payment schedule and current unrestricted cash.” Sources: claim table above; these edits preserve the distinction between facts, reports and inference.

[G]: https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
[APR]: https://www.anthropic.com/news/google-broadcom-partnership-compute
[H]: https://www.anthropic.com/news/series-h
[CNBC]: https://www.youtube.com/watch?v=3U_0AKZhi_I
[P1]: https://www.pymnts.com/news/investment-tracker/ipo/2026/anthropic-quarterly-revenue-jumps-45-before-planned-ipo/
[Q3]: https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208
[FY25]: https://www.investing.com/news/stock-market-news/exclusiveanthropics-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-4921382
[P2]: https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-narrows-revenue-gap-with-openai-before-ipo/
[AX]: https://www.axios.com/2026/10/15/anthropic-q3-revenue-cash-flow
[ACCOUNT]: https://www.semafor.com/article/04/10/2026/anthropic-is-gaining-on-openais-revenue-but-hasnt-yet-eclipsed-it
[F]: https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation
[S1]: https://www.anthropic.com/news/confidential-draft-s1-sec
[AWS]: https://www.anthropic.com/news/anthropic-amazon-compute
[OBL]: https://www.investing.com/news/stock-market-news/anthropics-518-billion-ai-buildout-hinges-largely-on-deals-that-cannot-be-canceled-filing-shows-4922031
[AVGO]: https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm
[FAC]: https://www.aol.com/articles/exclusive-broadcom-lend-anthropic-42-100607000.html
[NS]: https://www.investing.com/news/company-news/anthropic-offers-blackstone-over-10-yield-in-60b-ai-chip-financing--ft-reports-4955122
[GOOG]: https://www.streetinsider.com/Reuters/Google%2Bto%2Binvest%2Bup%2Bto%2B%2440%2Bbillion%2Bin%2BAI%2Brival%2BAnthropic/26364234.html
[MS]: https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships
[AMD]: https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/
[OPUS]: https://www.anthropic.com/claude-opus-5-5
[PRICE]: https://platform.claude.com/docs/en/about-claude/pricing
[FABLE]: https://www.anthropic.com/claude-fable-and-mythos-5-1
[EW]: https://everwindfuels.com/2026/10/everwind-announces-10-billion-investment-in-point-tupper-data-centre-campus-and-renewable-energy-portfolio-across-nova-scotia/
[CAN]: https://www.investing.com/news/stock-market-news/anthropic-signs-lease-for-first-canadian-data-center-4954967
[BAR]: https://www.anthropic.com/news/barclays-scales-claude
[EURO]: https://www.euronews.com/2026/10/15/anthropic-revenue-jumps-46-to-168bn-as-ai-firm-eyes-record-2-trillion-ipo-valuation
