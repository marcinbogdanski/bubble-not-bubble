# Independent cross-check: AI debt markets (Claude)

*Review date and information cutoff: 2026-10-18. Reviewer: Claude (Anthropic), fresh context, no subagents. Reviewed `report/methodology.md`, `tasks/RESEARCH_BRIEF.md`, `research/macro/debt-markets.md`, `data/ai-debt-stack.csv`, `data/circular-financing-deals.csv`, `reviews/debt-markets-codex-xcheck.md` and `report/index.md` Part 3. Fetch budget: 15 used, 4 of them failed (Axios 403, a TradersUnion relay 403, Economic Times via WebFetch blocked, and IMF via curl access-denied; the last two were then retrieved another way). SEC fetches used a generic User-Agent. All external sources accessed 2026-10-18. No file other than this review was edited.*

## Verdict

All 12 re-checked rows match their sources. Microsoft's $46.136B and Oracle's $130.105B, which the Codex check could not reproduce, now come straight from the filings, so the $494.3B / $572.5B arithmetic rests on retrieved primary inputs (A inputs, B sum).
The note leaves out material primary data it could have used: Meta's own ~$28B Hyperion residual-value threshold and its ~$13B El Paso guarantee with ~$12.5B of El Paso debt; filed fair values that already put four issuers' debt about $39B below face; Microsoft's $443.5B of lease payments; and the IMF and Chicago Fed evidence on who holds the debt. The two CSVs also carry at least five of the same instruments.
The front page's "largest losses at the top" claim holds for equity. For IG bonds it holds only as a mark-to-market statement: 100bp / 200bp of widening on $330B costs about $29-34B / $55-63B, against ~$81B of neocloud debt in total. As a ranking it is grade C, and the note itself never makes the claim.

## Claim re-verification

Dollar figures in billions unless stated.

| # | Claim (note row) | Note's figure | Re-verified figure | Source | Match | Grade |
|---|---|---|---|---|---|---|
| 1 | Corporate principal perimeter (12) | Meta 84 + Alphabet 101.085 + Amazon 132.995 + Microsoft 46.136 + Oracle 130.105 = 494.321; MSFT and ORCL "not reproduced" | **Microsoft 46.136** "Total face value" (Note 10; also the principal line in contractual obligations, FY27 9.250 / thereafter 36.886). **Oracle 130.105** "Total senior notes and other borrowings", which *includes* $1.468B of commercial paper and a $5.137B term loan; the future-principal schedule also totals 130.105. Meta 84.000 and Alphabet 101.085 reproduced. Amazon not re-fetched (Codex reproduced it). | [MSFT 10-K][msft], [ORCL 10-K][orcl], [Meta 10-Q][meta], [Alphabet 10-Q][goog] | Yes. The verification limit can be removed. | A for each input; B for the sum. Scope: all corporate debt including legacy pre-AI issues, Oracle CP and term loan; leases excluded |
| 2 | Dated subtotal (40) | 494.321 + 35.551 + 42.6 = 572.472 | Arithmetic correct. Scope caveat the note does not state: CoreWeave (35.551), Hut 8's project notes (7.5) and WULF Compute's notes (3.2) are also inside the neocloud note's ~$80.7B. If the front page's "$81B" were added to $572B, about $46B would be counted twice. | Note claims 18-20, 22, 28; `research/stack/neoclouds-other.md` row 39 | Yes (arithmetic); overlap with neocloud total not flagged | B |
| 3 | KC Fed AI share and volume of IG issuance (50-51) | 2% (2023) → 10% (2026); $330B YTD through Q2, 10× 2023 | Same: "year-to-date issuances of investment-grade bonds … are $330 billion", "10 times the issuances for the whole of 2023", data "through the second quarter of 2026". Perimeter: hyperscalers, chipmakers, utilities, industrials, neoclouds, data-centre operators. No classification rule is given. | [KC Fed][kcfed] | Yes | A (authors' estimate). Note: this is H1-2026 *issuance*, not a cumulative stock |
| 4 | KC Fed maturities (52) | Hyperscalers 16y, utilities 17y, market 10y; issued 2025-Aug 2026 | Same. The 16-17-year figures apply to the **hyperscaler and utility subsets only**. No weighted maturity is given for the full $330B (chipmakers, industrials, neoclouds). The bulletin gives no duration, spread or loss estimates. | [KC Fed, Chart 4][kcfed] | Yes. The front page applies the figure to the whole $330B, which the source does not support. | A |
| 5 | September issuance drop (53) | Sept $23B vs June $113B, "Axios citing FT" | Axios returned 403. Relays of the same FT story give the data provider as **Morgan Stanley**, the perimeter as global AI-related debt (public bonds and private placements per one relay; undefined in another), a 9-month total of ~$466B, and US IG AI-related issuance of ~$306B Jan-Aug that "stopped entirely in September". | [Coinpaper relay, 2026-10-11][coin]; search relays | Figures match; provider unnamed in note | B for the attributed pair (FT, Morgan Stanley data); the $466B and $306B are C (relay only) |
| 6 | Meta May 2026 financing (2) | $25B face, $24.91B net; 2031-2066; 4.55-6.45% | Same: "May 2026 Notes 2031-2066 4.55%-6.45% … 25,000"; "Proceeds from issuance of long-term debt, net 24,910". Total face 84,000 (59,000 at Dec). **Fair value of notes $79.75B at June 30.** | [Meta 10-Q, Note 8][meta] | Yes | A |
| 7 | Alphabet 2026 financings (4, 6) | $49.6B net common + mandatory preferred; conversion on/about May 15 2029; debt face 101.085 | Same: "aggregate net proceeds of $49.6 billion … including capital expenditures to scale AI infrastructure"; conversion "on or about May 15, 2029"; a further **$40B at-the-market equity programme** (not in note). Face 101,085 vs 49,085 at Dec 2025. **Fair value of notes $94.9B.** Backstops: $43.8B credit derivatives + $7.6B financial guarantees. | [Alphabet 10-Q][goog] | Yes; ATM programme omitted | A |
| 8 | Oracle and CoreWeave CDS paths (54-55) | ORCL 186→288bp; CRWV 749→1,118bp since Sept 11; 2032 bond 14.8% | Verbatim: "increased from 186 basis points on September 11 to 288 basis points, while CoreWeave's spread surged from 749 basis points to 1,118 basis points during the same period"; "yield on CoreWeave's bond maturing in 2032 had reached 14.8 per cent". End date not given. Report title: GREED & fear, "K-shaped stresses, AI tremors and the Houthis". | [ET/ANI][wood] (retrieved by direct HTTP) | Yes | B (attributed sell-side marks via a wire relay) |
| 9 | CoreWeave DDTL 4.0 (23) | ~$7.5B rising to $8.5B; A3/A(low); SOFR+225 / ~5.9%; March 2032 | Same, plus details the note omits: "**First of a kind non-recourse facility**", "secured by substantially all assets of CoreWeave Compute Acquisition Co. VIII", A (low) is from **DBRS**, "anchored by **Blackstone Credit & Insurance** and included participation from … **insurance investors**". | [CoreWeave 8-K ex.99.1, 2026-03-31][crwv4] | Yes; recourse status and holder detail omitted | A (announced terms) |
| 10 | CoreWeave DDTL 5.5 (23) | $2.6B; Ba2/BB+; SOFR+550; ~5y vs ~3y contracts | Same (Ba2 Moody's, BB+ Fitch; borrower CoreWeave Financing DDTL V-V; JPM/MUFG). Lenders "willing to underwrite renewal risk". Also discloses a **$3.1B DDTL 5.0** closed earlier in 2026, absent from the note and the CSV. | [CoreWeave 8-K ex.99.1, 2026-08-10][crwv55] | Yes; DDTL 5.0 omitted | A |
| 11 | Hyperion structure (18) | $27.3B securities; Meta 20%/Blue Owl 80%; 4-year leases; "conditional capped residual guarantee first 16 operating years" | 10-Q: ~$27B development cost funded pro rata; leases **commence 2029**, initial commitment **~$12.31B**, 4-year terms renewable to 20; RVG with "an **aggregate threshold of approximately $28 billion** that decreases over time"; on termination or non-renewal Meta pays the shortfall between fair value and threshold; "RVG payments are not probable", so no liability is recorded. Equity-method, not consolidated. **El Paso (July 2026 subsequent event): 20% interest, RVG "maximum aggregate exposure of approximately $13 billion."** | [Meta 10-Q, Notes 5 and 13][meta] | Structure matches. The cap is quantified in the filing but not in the note, and it roughly equals the $27.3B of Beignet principal. | A |
| 12 | Holder evidence (13, 58) | Channels identified; allocations unquantified | KC Fed: mutual funds, ETFs and insurers "remain the largest buyers of corporate bonds"; "Insurers, private credit firms, and pension funds have acquired long-duration bonds through private placements"; banks became net buyers after 2023-24. No percentages. DDTL 4.0 adds a named insurer-channel anchor (row 9). | [KC Fed, Chart 3][kcfed], [crwv4] | Yes | A for channels; nothing is quantified |

Front-page items checked as a by-product:

- **IMF map.** Verbatim: "Fourteen publicly disclosed transactions since 2023 account for approximately $300 billion of aggregate equity investments led by hyperscalers in financially weaker AI firms, supplemented by $650 billion in debt, in exchange for $1.4 trillion in future revenue commitments"; "About $320 billion of the $650 billion debt is taken on by investees … including debt backed by investor guarantees, contingent financing, and other off-balance-sheet debt" ([IMF GFSR Oct 2026, ch.1, pp.3-4][imf]). It matches the front page (A). The IMF map sits in the circular-financing note, not in this note. The IMF's own "10 percent" is the **hyperscalers'** share of **global** IG issuance, a different perimeter from the KC Fed's 10%.
- **Oracle $125B (August).** Consistent with the filed May figure of $130.105B (A) and with `research/stack/oracle.md` row 10 ($125.337B). The August 10-Q was not re-fetched.
- **Project bonds "below 88 to about 94 cents".** Not re-fetched; it remains the October 16 FT/BizNews version (C).

## CSV and double-counting check

**CSV against the note.** Every amount in `data/ai-debt-stack.csv` matches the note's claim table. The CSV correctly warns "DO NOT SUM ROWS". Defects:

1. **Oracle commercial paper is mislabelled.** The row reads "commercial paper; separate disclosure excluded from perimeter, 1500". The 10-K's $130,105M total *includes* "Commercial paper notes 1,468". The CP is inside the perimeter, and the amount is $1,468M.
2. **Beignet row date** is "2026-10-17", which is the access date. The transaction is from October 2025.
3. **Abilene phase 1** ($2,300M) is dated 2025-05-22 and sourced to the phase-2 Yahoo URL. Use the Newmark phase-1 page (`[abilene1]` in the note).
4. **Missing instruments the repository already documents.** These are El Paso / Sopaipilla debt (~$12.5B per Meta's announcement, `research/stack/meta.md` row 29), CoreWeave DDTL 5.0 ($3.1B), and Meta's two RVGs (~$28B Hyperion, ~$13B El Paso) as contingent rows.

**Instruments carried in both CSVs** (same instrument, or the same cash flow seen from two sides). Neither CSV records the cross-reference.

| Instrument | ai-debt-stack.csv | circular-financing-deals.csv | Relationship |
|---|---|---|---|
| Hut 8 River Bend project notes | 3,250 (USD m) | CF067, amount "USD 3.25bn project notes" | **Same instrument, same amount** |
| AI XPV / Anthropic initial tranche | 35,000 | CF021 USD 35bn; CF022 Broadcom $29B backstop on the same tranche | **Same instrument**; the backstop is a second claim on the same loss |
| North Star / Anthropic | 60,000 / 42,000 / 18,000 | CF024 USD 60bn / 42bn / 18bn; CF023 Broadcom $42B facility "unreconciled" | **Same proposed instrument** |
| Valor / xAI capital solution | 3,500 | CF068 USD 3.5bn | **Same instrument** |
| Hyperion / Beignet | 27,300 securities | CF037 ~USD 27bn development, "debt investors include PIMCO" | Same project; CF037 bundles the debt with equity and the RVG |
| WULF Compute notes | 3,200 notes | CF042 Google USD 3.2bn backstop | Different instruments, same rent stream: the backstop supports the cash that services the notes. Adding them double-counts the exposure. |
| CoreWeave vendor financing | inside 35,551 gross debt | CF049 USD 5.1bn outstanding | CF049 is a **subset** of the CoreWeave stock |
| Abilene and Jupiter construction loans | 9,400 and 18,000 capacity | CF030 / CF032 Stargate programme and Oracle-OpenAI contract | Programme overlap, not the same instrument |

Summing the two CSVs would double-count at least $3.25B + $35B + $3.5B + $27.3B ≈ $69B of instruments, before the proposed North Star $60B and the backstop layers. Neither page sums them today. A shared `instrument_id` or `also_in` column would stop it happening by accident.

## Dollars-at-risk test

**Method.** Price change of a par bond with a 5.5% coupon (semiannual) for an instant parallel spread shock, computed by full repricing (convexity included). The 5.5% sits within the 2026 coupon ranges in claims 2, 5 and 11. Durations follow from the note's maturities: 16-year bullet, modified duration 10.6; 17-year, 11.0; 10-year (market average), 7.6. A 5/10/20/29-year ladder with a 16-year average has duration 9.6, because bonds dispersed around a 16-year average carry lower duration than a 16-year bullet. Bases: $330B (KC Fed H1-2026 AI-related IG issuance, a lower bound on the outstanding AI-related IG stock) and $494.3B (filed corporate principal, which includes legacy and Oracle BBB− debt).

| Scenario | Base | +100bp | +200bp |
|---|---|---|---|
| 16-17-year bullets (KC Fed hyperscaler/utility maturities) | $330B | −$32.5B to −$33.7B (−9.9% to −10.2%) | −$60.9B to −$62.8B (−18.5% to −19.0%) |
| 16-year-average ladder | $330B | −$29.3B (−8.9%) | −$54.6B (−16.5%) |
| 10-year (market-average maturity) | $330B | −$24.0B | −$45.9B |
| 16-17-year bullets | $494.3B corporate principal | −$48.7B to −$50.4B | −$91.2B to −$94.1B |
| *Comparator:* all listed neocloud debt, face | ~$80.7B (mixed bases) | n/a | n/a |
| *Comparator:* neocloud debt, 5-year 10% coupon, +500bp / +1,000bp, no defaults | $80.7B | −$13.8B (at +500bp) | −$24.8B (at +1,000bp) |
| *Comparator:* every listed neocloud defaults, 50% recovery | $80.7B | −$40B | n/a |
| *Observed:* filed fair value below face. Meta −4.25 (94.9%), Alphabet −6.18 (93.9%), Microsoft −9.64 (79.1%), all June 30; Oracle −19.3 (84.6%), Aug 31 | $356B face | **−$39.4B already**, mostly rates on fixed coupons | n/a |

Sources: arithmetic in this review (B); inputs [KC Fed][kcfed], filings [meta], [goog], [msft]. Oracle's fair value is from `research/stack/oracle.md` row 26 (Aug 10-Q, not re-fetched). The neocloud total is `research/stack/neoclouds-other.md` row 39.

**Result.**

- **Equity half: supported.** Equity takes first loss by contract, and the top-of-stack equity base is far larger than any bond figure here. It was not dollarised in this review because market capitalisations were not retrieved.
- **IG-bond half: supported only as mark-to-market.** A 100bp widening marks the $330B down by about $29-34B, roughly 40% of the *entire* face of listed neocloud debt. That already exceeds a no-default neocloud repricing of +500bp (~$14B), and is comparable to every listed neocloud defaulting at 50% recovery (~$40B). At 200bp (~$55-63B) the IG mark exceeds even that default case.
- **Limits of the claim.**
  - The loss is unrealised for hold-to-maturity insurers and pensions, the KC Fed's private-placement buyers. Without a default it reverses at maturity.
  - Much of it would be rates, not AI. The observed $39B is mostly that.
  - The note gives no evidence that AA-rated hyperscaler spreads would widen 100-200bp in a no-default scenario. Tertiary reports put JPMorgan's hyperscaler index near 148bp on October 16 and say BofA data showed about +30bp in September. Both are unverified leads.
  - The front page attaches the 16-17-year maturity to all $330B. The KC Fed gives it only for hyperscalers and utilities.
- **Grade.** B for the arithmetic, C for the ranking: it depends on an assumed spread shock and an approximate duration, and it is stated nowhere in the note.

The same arithmetic explains the project-bond marks. With modified duration of 7.5-11, an 8-12-point discount implies roughly 75-160bp of combined Treasury-plus-spread rise since issue. That is consistent with duration and new-issue concessions (El Paso reportedly priced about 0.4pp over Hyperion), not with distressed credit pricing.

## Holders

**Verifiable now:**

- Channels only. The KC Fed names insurers, private-credit firms and pension funds as buyers of long-duration private placements, and mutual funds/ETFs and insurers as the largest corporate-bond buyers ([KC Fed][kcfed], A).
- Named deal participants: PIMCO accounts in Beignet; Blackstone Credit & Insurance plus "insurance investors" in DDTL 4.0; CDPQ in the 2024 CoreWeave facility; BCI and Liberty Mutual in Crusoe's facility (primary, A, participation only).
- **Banks' direct exposure (missed by the note).** The Chicago Fed (Cohen, Killen and Lau, February 2026, FR Y-14Q data, banks ≥$100B) finds about "$450 billion in commitments ($150 billion of which was outstanding)" of AI-adjacent C&I exposure in late 2025. Outstanding exposure is about "0.8% of bank total assets"; C&I outstanding averages 9% of tier 1 capital and commitments "closer to 25%". MSCI counts "$14.9 billion of bank lending" to data centres in the year to Q3 2025. Indirect exposure through lending to nonbanks is "difficult to quantify with regulatory data" ([Chicago Fed][chifed], A).
- **Nonbank liquidity (missed).** IMF GFSR October 2026: "among 10 BDCs with $300 billion in total assets, 4, representing about $90 billion in assets, have commitments exceeding their available liquidity buffers". Pension funds and insurers "have nearly doubled their share of illiquid investments", and private credit is "one of the main drivers", with IG status supporting "favorable capital treatment" ([IMF][imf], A). None of this is AI-specific.

**Reported, unverified (C):**

- An NAIC September report, relayed by Forbes on October 8, puts insurers' private-credit exposure at ~$1.21T (~13% of cash and invested assets) and privately rated bonds at ~$512B at end-2025.
- The NAIC is reportedly reviewing ratings on data-centre holdings, using its discretion authority effective January 1, 2026.
- HPS Corporate Lending Fund reportedly received Q3 repurchase requests for 11.5% of shares and paid 5%; BCRED's requests were about 10%.

**Not verifiable from public aggregates:** insurer, pension or bank holdings of specific AI instruments; banks' retained shares of the Jupiter and Vantage syndications; GPU-loan marks. These can be closed security by security with disclosures the note does not use:

1. **Insurer statutory filings.** NAIC Schedule D Part 1 (year-end, by CUSIP) and Part 3 (quarterly acquisitions) would show which insurers hold Beignet (2025 CUSIPs appear in year-end 2025 statements) and which bought QTS, Hut 8 or Sopaipilla in Q2-Q3 2026.
2. **Fund holdings.** SEC N-PORT filings for PIMCO, BlackRock and other mutual funds give CUSIP-level positions and values. They can test whether "PIMCO-managed accounts" means public funds or separate accounts.
3. **BDC 10-Q schedules of investments.** Position-level fair values for BCRED, Blue Owl, HPS and Ares funds, including any CoreWeave DDTL, Crusoe or Lambda participations. Q3 filings are due around early-to-mid November.
4. **Fed Financial Stability Report.** The May 8, 2026 report was not used; the November edition is due.
5. **Bank 10-Qs.** Q3 results came out October 13-14 and 10-Qs follow in early November. Look for loans held for sale at fair value (undistributed construction loans), loans to nondepository financial institutions, and unfunded commitments. Also Jefferies' fiscal-Q3 10-Q (quarter to August 31), given its reported role quoting Jupiter.
6. **TRACE.** 144A trades in Beignet, Sopaipilla, QTS and Hut 8 notes are disseminated by FINRA. That would resolve the two unreconciled FT mark versions (claim 21).

## Omissions

From the last 30 days (2026-09-18 to 10-18):

- **IMF GFSR, October 2026** ([imf], A). Hyperscalers' share of global IG issuance rose "to 10 percent from less than 1 percent" since 2024. IG issuance was 40% of euro-area, UK and US bond issuance on a duration-weighted basis in Q1 2026, competing with sovereigns. The circular map and the BDC/insurer liquidity findings above. The note cites the BIS but not the IMF.
- **Fuller issuance context for claim 53** ([coin], C). The data provider is Morgan Stanley; ~$466B of global AI-related debt in nine months; ~$306B of US IG AI issuance Jan-Aug, reportedly nil in September. The ~$466B also tests Morgan Stanley's June forecast of ~$500B for the year (claim 37).
- **Oracle's August 10-Q fair value.** $105.7B against $125.0B of notes (84.6%, down from 89.3% in May). It is in the Oracle note, filed September 11, and is the single largest observed IG mark-to-market in the stack.
- **Market-level leads, unverified (C/D):** JPMorgan hyperscaler bond index ~148bp, "widest since July" (October 16); Deutsche Bank (October 15) says AI financing costs are "manageable" but Oracle's long bonds yield 8-8.5%; LSEG counts >$228B of 2026 bonds from Alphabet, Amazon, Meta and Oracle as of October 13; Meta's latest deal reportedly drew a third less demand.
- **Forbes / NAIC insurer reporting** (October 8) and private-credit redemption data (above).

Older but material, and missing from this note even though the repository has them:

- **El Paso / Sopaipilla.** ~$12.5B of project debt (Meta announcement via `research/stack/meta.md` row 29); reported ~7.5%, 2048, S&P A+ / Fitch AA-(EXP) (C); a ~$13B RVG in Meta's 10-Q (A). After Beignet it is the largest single project bond in the stack, and its reported ~0.4pp premium over Hyperion is a clean repricing observation.
- **Meta's ~$28B Hyperion RVG threshold and $12.31B lease commitment** (10-Q, A).
- **Microsoft's $443.506B of lease payments including interest** (including $329.1B uncommenced; 10-K, A). It is in the Microsoft note but missing from the note's tenant-obligation table, which shows only Meta and Oracle.
- **Microsoft's current useful-life policy.** "Servers and network equipment, two to six years" (FY2026 10-K). The note cites the FY2024 report instead.
- **Chicago Fed bank exposure** (February 2026, A).
- **CoreWeave DDTL 5.0** ($3.1B) and DDTL 4.0's non-recourse status.
- **Alphabet's $40B ATM equity programme** (10-Q, A), which adds to the loss-absorbing equity at the top.

## Summary-bullet assessment

| Bullet | Assessment | Change |
|---|---|---|
| 1 S&P negative FOCF | Accurate (Codex verified). | None |
| 2 Meta / Alphabet financings | Accurate (re-verified). Lists deals without saying what they mean for the debt stack. | Add the fair values (Meta $79.75B vs $84B; Alphabet $94.9B vs $101.1B) and Alphabet's $40B ATM |
| 3 $572.5B perimeter | Arithmetic right. The "verification limits" caveat is now obsolete. The overlap with the neocloud total goes unmentioned. | Edit 1 |
| 4 Issuance | Too vague for a summary: it cites claim numbers instead of figures. | Edit 6 |
| 5 Hyperion | Correct but leaves out the filed RVG size, which is the decisive fact for bondholders. Omits El Paso. | Edit 2 |
| 6 CDS paths | Accurate; the end-date caveat is correctly stated. | None |
| 7 Holders | Accurate but thin. Misses the Chicago Fed, the IMF and DDTL 4.0's insurer anchor. | Edit 9 |
| 8 Maturity mismatch | Direction right. The 16-17 years applies to the hyperscaler and utility subsets; the Microsoft comparator is out of date. | Edit 7 |
| Missing | The note never states where dollar losses land, although the front page relies on it for that. | Edit 5 |

## Your assessment

**Where the first loss appears.** Equity is already absorbing first loss: CoreWeave's stock is down 56% from its peak, Oracle's is falling, and the weakest names are down 45-56%. The first *credit* loss, meaning a principal shortfall or a realised mark, is most likely in the middle of the stack, in one of two places:

1. **Undistributed bank construction loans to power-constrained campuses.** Jupiter's $18B package was quoted at 89-91 with syndication stalled. Banks holding such loans for sale must mark them to fair value, so a loss can surface in a quarterly filing without any default.
2. **Sub-IG GPU-backed private credit to neoclouds that lack an investment-grade offtaker.** The weakest structures lend five years against three-year contracts (DDTL 5.5), or carry covenant relief (CoreWeave DDTL 3.0, whose unlimited equity-cure window closes October 28, 2026).

Long-dated hyperscaler IG and Meta-backed project bonds (Beignet and El Paso, backed by a ~$28B and ~$13B RVG) are where the largest *marks* sit, but they are the least likely place for a first *credit* loss.

**Earliest public signal, in likely order of arrival:**

1. **Daily:** CDS and TRACE prints on CoreWeave notes and 144A project bonds. Already moving, but these are prices, not losses.
2. **Within four business days of an event:** an 8-K from CoreWeave or another listed neocloud or miner disclosing a waiver, amendment, forbearance, equity cure or acceleration (Items 1.01 / 2.04). The first date to watch is after October 28.
3. **Early-to-mid November:** BDC Q3 10-Q schedules of investments showing data-centre or GPU loans marked below ~90 or on non-accrual, and bank 10-Qs showing held-for-sale marks.
4. **Event-driven:** rating actions on the structured facilities (Moody's, Fitch, KBRA, DBRS) or an NAIC override of a private rating.

Of these, the 8-K and the BDC marks are the earliest signals that would show a realised loss rather than a repricing.

## Recommended edits

1. **Claim 12, Summary bullet 3 and the "Claim 12 verification limits" paragraph.** Replace the verification paragraph with: "Claude's 2026-10-18 cross-check retrieved Microsoft's FY2026 10-K (Note 10, total face value $46.136B) and Oracle's FY2026 10-K (total senior notes and other borrowings $130.105B, including $1.468B of commercial paper and a $5.137B term loan) directly. All five inputs are now primary (A); the $494.321B sum is B. The perimeter includes pre-AI legacy debt and excludes leases." In claim 12 change the grade to "A inputs; B sum". In Summary bullet 3 delete ", conditional on the verification limits in claim 12" and add: "CoreWeave, Hut 8 and WULF Compute debt (~$46B) also sits inside the neocloud note's ~$80.7B; do not add the two totals."
2. **Claim 18 and Summary bullet 5.** Replace the bullet with: "Hyperion: Meta holds 20%, leases commence in 2029 with a ~$12.31B initial commitment over four-year terms, and Meta provides residual-value guarantees with an aggregate threshold of about $28B that declines over time. On termination or non-renewal Meta pays the shortfall between fair value and that threshold, and records no liability because payment is not probable. The cap is close to the $27.3B of Beignet securities, so bondholders depend mainly on Meta's credit, but it is not an unconditional guarantee of the bonds. [Meta 10-Q, Note 5]"
3. **New claim 59 (El Paso).** "Meta El Paso venture: Meta 20% / BlackRock funds 80%; ~$12.5B debt financing; Meta RVG maximum aggregate exposure ~$13B (10-Q subsequent event, A). Notes issued by Sopaipilla Investor LLC reportedly priced ~7.5%, due 2048, S&P A+ / Fitch AA-(EXP), about 0.4pp over Hyperion (reported, unverified, C)." Add $12.5B to the separately classified project list. Do not add it to $572.5B without a dated balance.
4. **New claim 60 (filed debt fair values).** "Fair value of notes versus face: Meta $79.75B / $84.0B (94.9%); Alphabet $94.9B / $101.085B (93.9%); Microsoft $36.5B / $46.136B (79.1%), all June 30; Oracle $105.7B / $125.0B (84.6%), August 31. About $39B below face in total, mostly from rates on fixed coupons; unrealised for holders who keep the bonds to maturity. Filings A; sum B."
5. **New Analysis paragraph, "Where the dollars of loss land without defaults", after "Maturity wall and repricing order".** "Equity absorbs first loss by contract. Among creditors, without defaults the largest dollar losses are mark-to-market losses on long-dated IG bonds: at modified duration ~9.6-11.0, a 100bp spread widening marks the KC Fed's $330B of H1-2026 AI-related IG issuance down by about $29-34B and 200bp by about $55-63B (arithmetic B; scenario C). That compares with ~$81B of listed neocloud debt in total, ~$14B for a +500bp no-default neocloud repricing, or ~$40B if every listed neocloud defaulted at 50% recovery. These IG marks are unrealised for hold-to-maturity insurers and pensions and include rate effects; realised credit losses are more likely first in undistributed construction loans and sub-IG GPU credit."
6. **Summary bullet 4.** Replace with: "AI-related IG issuance reached $330B in H1 2026, 10% of IG issuance against 2% in 2023 (KC Fed, A). Morgan Stanley data reported by the FT show global AI-related debt issuance falling to $23B in September from $113B in June (B), with US IG AI issuance reportedly halted in September (C)." In claim 53 name "Morgan Stanley data via FT" and add the ~$466B nine-month total as C.
7. **Claims 52 and 57, and Summary bullet 8.** In claim 52 add: "applies to the hyperscaler and utility subsets; no weighted maturity is given for the full $330B." Replace claim 57 with: "Microsoft FY2026 10-K: servers and network equipment depreciated over two to six years (A, accounting estimate)."
8. **Claim 23.** Append: "DDTL 4.0 is non-recourse, secured by substantially all assets of CoreWeave Compute Acquisition Co. VIII; A (low) is from DBRS; anchored by Blackstone Credit & Insurance with insurance investors. CoreWeave also closed a $3.1B DDTL 5.0 earlier in 2026 (August 10 release)." Add DDTL 5.0 to the CSV as a capacity row.
9. **Holders (Summary bullet 7, claim 58 and "Who holds the paper").** Add: "Chicago Fed (FR Y-14Q, banks ≥$100B): ~$450B of AI-adjacent C&I commitments ($150B outstanding) in late 2025; outstanding exposure ~0.8% of total assets; commitments ~25% of tier 1 capital; ~$14.9B of bank data-centre CRE lending in the year to Q3 2025; indirect lending to nonbanks unquantified (A). IMF GFSR October 2026: 4 of 10 BDCs (~$90B of $300B assets) have commitments exceeding liquidity buffers; insurers and pensions have nearly doubled their illiquid share, driven by private credit (A, not AI-specific)." Add "NAIC: insurers' private-credit exposure ~$1.21T, privately rated bonds ~$512B at end-2025 (reported via Forbes, C)" to Conflicts as unverified.
10. **Tenant-obligation table.** Add the row: "Microsoft | $443.506B operating and finance lease payments including interest, of which $329.1B uncommenced | 2026-06-30 | 10-K contractual obligations, A".
11. **Signals to watch.** Add rows: "BDC Q3 10-Q schedules (data-centre/GPU loan marks, non-accruals), due early-to-mid November"; "CoreWeave 8-Ks after the DDTL 3.0 equity-cure window closes on 28 October"; "TRACE prints for Beignet, Sopaipilla, QTS and Hut 8 144A notes (resolves claim 21)"; "Schedule D / N-PORT holdings of named project CUSIPs"; "JPMorgan hyperscaler index spread (~148bp reported October 16, unverified)".
12. **Claim 21 interpretation.** Add to the project-credit paragraph: "At modified duration 7.5-11, an 8-12-point discount equals roughly 75-160bp of combined Treasury and spread rise since issue. That is consistent with duration and new-issue concessions, not on its own with distressed credit pricing."
13. **`data/ai-debt-stack.csv`.**
    - Relabel the Oracle CP row to `"stock: commercial paper; INCLUDED in 130105 perimeter","1468"`.
    - Change the Beignet date to `2025-10` and the instrument text to say the date is the transaction date.
    - Point the Abilene phase-1 source to the Newmark phase-1 URL.
    - Add an `also_in` column: Hut 8 River Bend = CF067; AI XPV = CF021/CF022; North Star = CF024/CF023; Valor = CF068; Beignet = CF037; WULF Compute = CF042 (same rent stream); CoreWeave gross debt contains CF049.
    - Make the reverse references in `circular-financing-deals.csv`.
14. **Front page, Part 3, last two sentences.** Replace "If returns disappoint without defaults, the largest losses land elsewhere: … (Kansas City Fed, A)." with: "If returns disappoint without defaults, the largest losses are mark-to-market and land at the top: on equity in Nvidia and the hyperscalers (the top ten are 40.6% of the S&P 500) and on long-dated investment-grade bonds. AI-related IG issuance was $330B in the first half of 2026 alone, and hyperscaler and utility issues average 16-17-year maturities against 5-6-year chips (Kansas City Fed, A). A 100bp spread widening would mark that $330B down by roughly $29-34B, and 200bp by $55-63B, against about $81B of listed neocloud debt in total (our arithmetic, B; scenario C). Holders who keep the bonds lose nothing without a default, and filed fair values were already about $39B below face at Meta, Alphabet, Microsoft and Oracle, mostly from rates (filings, A)."

## Sources

All accessed 2026-10-18.

1. [Sharma and George, "Beyond Valuations", Kansas City Fed Economic Bulletin, 2026-10-05][kcfed]
2. [Coinpaper relay of FT / Morgan Stanley issuance data, 2026-10-11][coin] (tertiary; Axios original returned 403)
3. [Economic Times / ANI, Jefferies GREED & fear CDS figures, 2026-10-17][wood] (HTML retrieved by direct HTTP)
4. [CoreWeave 8-K ex.99.1, DDTL 4.0, 2026-03-31][crwv4]
5. [CoreWeave 8-K ex.99.1, DDTL 5.5, 2026-08-10][crwv55]
6. [Microsoft FY2026 10-K][msft]
7. [Oracle FY2026 10-K][orcl]
8. [Alphabet Q2 2026 10-Q][goog]
9. [Meta Q2 2026 10-Q][meta]
10. [Chicago Fed Insights, "AI tail risk for banks", February 2026][chifed]
11. [IMF, Global Financial Stability Report, October 2026, chapter 1][imf] (PDF retrieved via WebFetch after curl was denied)
12. Search-result leads only, not cited as evidence: Forbes 2026-10-08 (NAIC figures); Octus (HPS redemptions); IBTimes / Global Data Center Hub (El Paso pricing and ratings); Startup Fortune and Benzinga (JPMorgan index, LSEG totals, Deutsche Bank).

[kcfed]: https://www.kansascityfed.org/research/economic-bulletin/beyond-valuations-long-term-financial-risks-from-the-ai-build-out/
[coin]: https://coinpaper.com/37113/ai-debt-issuance-falls-from-113b-to-23b-while-oracle-loans-trade-below-par
[wood]: https://economictimes.indiatimes.com/markets/us-stocks/news/rising-borrowing-costs-signal-funding-risks-for-global-ai-expansion-jefferies-report/articleshow/135012567.cms
[crwv4]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex991.htm
[crwv55]: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm
[msft]: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[orcl]: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
[goog]: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
[meta]: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
[chifed]: https://chicagofed.org/publications/chicago-fed-insights/2026/ai-tail-risk-for-banks
[imf]: https://www.imf.org/-/media/files/publications/gfsr/2026/october/english/ch1.pdf
