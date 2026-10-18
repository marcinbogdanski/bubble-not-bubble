# Oracle: independent Claude cross-check

*Review date and evidence cutoff: 2026-10-18. Reviewer: Claude (Opus), fresh context, no subagents. Reviewed `research/stack/oracle.md` (Codex, corrected once after [the Codex cross-check](/reviews/oracle-codex-xcheck)) against `report/methodology.md` and `tasks/RESEARCH_BRIEF.md`, and the Oracle figures used in `report/index.md` Part 3, `report/stack.md` and forecast F2. USD billions unless stated otherwise. Oracle's fiscal year ends May 31. No other file was edited.*

*Evidence handling: 15 fetches were used (one failed against Fitch, two against local news sites, one SEC download refused). Items marked **(fetched)** were read in full or in the relevant part. Items marked **(search)** rest on search-result extracts of the named page and are graded one step lower than a fetch of the same page would be.*

## Verdict

The note's numbers hold: all 12 load-bearing rows re-verified against the Q1 FY2027 10-Q and the Q1 and Q4 FY2026 releases, with no transcription error. The front page's Oracle figures are correct, except that "CDS 282-300bp" has no source for 282.
The note under-reports the ratings mechanics, which decide F2. S&P's own triggers (adjusted leverage sustained above 4.5x, or no path to positive FOCF by FY2029) sit against an S&P FY2027 forecast of "mid-4x" and −$42B FOCF, so there is almost no headroom. S&P also estimates OpenAI at about half of RPO, and the note omits that.
Oracle is overextended relative to its rating and its own cash generation, not relative to its liquidity. FY2027 is fundable if customers keep prepaying. I put F2 at **8% / 24% / 40%**, slightly below the register's 12/28/42 at the near horizons.

## Claim re-verification

| # | Claim (note row) | Note's figure | Re-verified figure | Source | Match | Grade |
|---|---|---|---|---|---|---|
| 1 | FY2026 FCF (rows 7–8) | OCF 31.977 − capex 55.663 = −23.686 | Same. The release states "$32.0 billion, up 54%" and FCF −$23.7B; net cash outlay after prepayments and short-term financing was 47.726 | [Q4 FY26 release][E4] (fetched) | Yes | A |
| 2 | Q1 FY2027 cash flow (rows 6–8) | OCF 23.103; capex 28.499; FCF −5.396 | Same; trailing four quarters Q2 FY26–Q1 FY27: OCF 46.940, capex 75.660, FCF −28.720 (my sum) | [Q1 FY27 release][E5]; [10-Q][Q] (fetched) | Yes | A; B for TTM sum |
| 3 | Customer advances (row 9; front page "$11.4B") | 11.363 | The cash-flow line "Increase in deferred revenues from customer prepayments with significant financing component" is 11,363. The 10-Q says "No prepayments ... were received during the first quarter of fiscal 2026." Total deferred revenue is 30.789, of which 16.103 is non-current, against 5.479 at May 31 | [10-Q][Q] (fetched) | Yes | A |
| 4 | OCF excluding advances and net outlay (rows 9, 50) | 11.740; 17.966; bridge −6.226 | 23.103−11.363 = 11.740; 28.499−11.363+0.830 = 17.966 | [Q1 release][E5] | Yes | A inputs; B arithmetic |
| 5 | Borrowings and liquidity (row 10; front page "$125B") | 125.337; cash and securities 37.077 | 7.625 + 117.712 = 125.337; 36.369 + 0.708 = 37.077. Senior notes and other borrowings are 125.0, fair value 105.7 | [10-Q][Q] (fetched) | Yes | A; B sums |
| 6 | RPO and conversion (rows 1–2; front page "$664B") | 664; 13% / 37% / 34% | "Remaining performance obligations were $664 billion as of August 31, 2026 ... approximately 13% ... next twelve months, 37% ... month 13 to month 36, 34% ... month 37 to month 60" | [10-Q][Q] (fetched) | Yes | A |
| 7 | Leases (row 11) | Operating 34.621; finance 9.185; 288 uncommenced, 15–19 years | Same. "$288 billion of additional lease commitments, substantially all related to data center arrangements, that are generally expected to commence between the second quarter of fiscal 2027 and fiscal 2029 and for terms of fifteen to nineteen years" | [10-Q, Note 6][Q] (fetched) | Yes | A |
| 8 | ATM and FY27 plan (row 17) | 20 ATM completed; ~40 FY27 plan | 10-Q: "we fully utilized the ATM Program and issued approximately 141 million shares ... for net proceeds of $19.9 billion." Q4 release: "In fiscal year 2027, Oracle expects to raise approximately $40 billion ..." and "**Oracle does not expect to issue additional debt in calendar year 2026**" (the second quote is not in the note) | [10-Q][Q]; [Q4 release][E4] (fetched) | Yes, with an omission | A |
| 9 | FY27 guidance (row 16) | Revenue ≥90; EPS 8.10; capex 90–95; net ≤70 | The release gives revenue "at least $90 billion" and EPS $8.10, but no capex. Capex 90–95 with net ≤70 comes from the call summary and from S&P (via PPC Land) | [Q1 release][E5]; [transcript page][T] (fetched, summary only); [PPC Land][SPX] | Yes | A revenue/EPS; B capex |
| 10 | S&P action (row 24; front page "BBB− since July") | BBB/A-2 → BBB−/A-3, stable, July 9, 2026 | Same, with triggers and forecasts added (see Rating path) | [PPC Land, July 18][SPX] (fetched); [Fortune, Sept 18][FOR] (fetched) | Yes | B (S&P text still not obtained) |
| 11 | Moody's / Fitch (row 23) | Moody's Baa2 negative "Dec 2025"; Fitch BBB stable, Feb 2, 2026 | Moody's **affirmed Baa2 negative on Feb 2, 2026**, alongside the equity announcement. The note's December 2025 date is stale. Fitch BBB/F2 stable, Feb 2, 2026. No later action by either agency was found | [Newsquawk][MDY] (search); [FinancialJuice][MDY2] (search); [Fitch disclosure][FIT] per note | Partly: Moody's date is wrong | B |
| 12 | CDS (row 25; front page "282-300bp") | 288bp, Oct 15 | 288bp (record, +26bp) on Oct 15; Reuters' later version says "near 300bp", about +31bp on the week; Jefferies via ET/ANI has 186→288bp from Sept 11. **No source found for 282bp** | [Reuters/MarketScreener][C] per note; [GuruFocus][GF] (search); `signals/2026-10-18-market-views.md` P9 | 288 and ~300 yes; 282 unsourced | B |
| 13 | OpenAI share undisclosed (rows 3, 34; front page) | >300 over five years; no named share | The 10-Q text contains no mention of OpenAI and no customer-concentration note. The 10-K risk factors say only: "In certain OCI offerings, we are more concentrated among a number of large customers." **S&P estimates OpenAI at roughly half of the $638B May RPO** (not in the note) | [10-Q][Q]; [10-K][K] (fetched, partial); [PPC Land][SPX] | Yes for Oracle's disclosure; omission on S&P | A disclosure; B S&P estimate |
| 14 | Dividends (rows 12, 51) | FY26 5.787; Q1 1.565 | Same: Q1 1.565 = common 1.484 + preferred 0.081 | [Q4 release][E4]; [10-Q][Q] | Yes | A |

Not re-verified: the FY2027 and FY2028 scheduled principal of 7.210 and 10.145 (row 12), because the 10-K fetch truncated before Note 6. The 10-Q is consistent with them: $3.1B of scheduled debt repaid in Q1, current borrowings of 7.625 at August 31, and $4.6B reclassified to current. Row 34's "no customer ≥10% of FY26 revenue" was also not found in the portion of the 10-K I could read. Rows 40, 44 and 45 (permit pending, restricted cash 2.6, unconditional obligations 34.150 including 6.176 in FY28) match the 10-Q and Oracle's October 15 release text.

## FY2027 funding arithmetic

**Two consistent bases.** Gross capex is funded by OCF *including* customer advances. Oracle's "net cash capex" (capex − customer prepayments + net manufacturer-financing repayments) is funded by OCF *excluding* advances. Mixing the two double counts. The CFO's framing (call summary, B) is $70B of Oracle's own capex plus $20–25B "repaid by customers".

**Inputs (A unless marked):**
- Opening unrestricted liquidity, May 31, 2026: 31.289 + 0.605 = **31.894**. At August 31 it was **37.077**, after $2.6B of cash was reclassified to restricted.
- FY27 capex guidance: gross 90–95; net cash capex ≤70 (B). Q1 actual: gross 28.499, net 17.966.
- OCF including advances: Q1 23.103. OCF excluding advances: Q1 11.740, up 44% on Q1 FY26's 8.140.
- **FY27 OCF excluding advances: 40–47, central 44 (C).** The ceiling is Q1 × 4 = 47.0 (Q1 was 25% of FY26 OCF). The central figure applies Q1's +44% to FY26's 31.977 (46.0) and haircuts it because FY26 Q3–Q4 may already contain some prepayments: the 7.937 FY26 capex-to-net-outlay gap mixes the two and is not split. Interest is already inside OCF; Q1 interest expense was **1.428**, up 55% year on year (A).
- Dividends: Q1 paid 1.565. After 141M ATM shares, quarterly common at $0.50 is about 1.55, plus 0.081 preferred: **FY27 ≈ 6.4** (B/C), against 5.787 in FY26.
- Debt maturities: FY27 scheduled **7.210** (10-K, per note; not re-verified), of which ~3.1 was paid in Q1. The 10-Q's liquidity text also shows $1.1B of commercial paper repaid in Q1.
- Restructuring: the 2026 plan was up to **$2.1B**, supplemented by about **$0.7B** after August 31 (10-Q, A). The cash is mostly in OCF; I flag it but do not add it.
- Financing: the $20B ATM (net 19.909) is done. About $20B of the ~$40B FY27 plan remains, and Oracle "does not expect to issue additional debt in calendar year 2026". The remainder therefore falls in January–May 2027, as debt, equity or both.

**FY27 external funding requirement (net basis, to preserve opening liquidity):**

| | Low OCF (40) | Central (44) | High OCF (47) |
|---|---|---|---|
| Net cash capex | 70 | 70 | 70 |
| − OCF excluding advances | −40 | −44 | −47 |
| + dividends | +6.4 | +6.4 | +6.4 |
| + scheduled principal | +7.2 | +7.2 | +7.2 |
| **= requirement** | **43.6** | **39.6** | **36.6** |
| + restricted-cash reclass already incurred | +2.6 | +2.6 | +2.6 |

**What covers it (central case):** ATM 19.9 + remaining plan ~20 ≈ 40, which roughly matches the ~42 requirement. Unrestricted liquidity ends FY27 near **29–30**, against 31.9 at the start. A Q2–Q4 roll-forward from August 31 gives the same answer. Net capex still to spend is 70 − 17.966 = 52.0; OCF excluding advances adds ~32.3; dividends take ~4.9 and maturities ~4.1. That is a Q2–Q4 deficit of ~28.7, so 37.1 − 28.7 = **8.4 with no new raise** and **~28.4 with the remaining ~$20B**. The note's own scenario (36.0 required, ending at 35.9) uses the high-OCF case and historical dividends. The two reconcile.

**What does not cover it:** the $10B revolver (due March 2031) is a backstop, not funding. The A-3 short-term rating from S&P effectively shuts Oracle out of most of the commercial-paper market (my inference, C), which fits the Q1 CP repayment.

**The swing factor is customer funding, not Oracle's OCF.** If the $20–25B of customer-funded capex does not arrive, net capex moves toward the 90–95 gross figure. The requirement then rises to **~60–67**. That means roughly $40B+ more than the ATM, or running cash down to the revolver, inside a fiscal year in which S&P already projects FOCF of about −$42B. The 10-Q does not say who prepaid the $11.4B. S&P's estimate that OpenAI is about half of RPO makes OpenAI the natural candidate, but that is inference (C).

**Beyond FY27 (C):** the $288B of uncommenced leases at 15–19 years implies roughly **$15–19B a year** of rent once fully commenced (288/17 ≈ 17, undiscounted, my arithmetic). Commencement runs from FY27 Q2 to FY29. That cost lands in OCF before the corresponding revenue unless sites go live on time, and it compares with total FY26 OCF of 32.0. FY28 adds 10.145 of maturities, and the 6.176 of FY28 unconditional purchase obligations partly overlaps capex. Neither FY28 capex guidance nor S&P's FY28 figures were found.

## Rating path and F2 view

F2 resolves Yes if any agency rates Oracle below investment grade. S&P is one notch away; Moody's and Fitch are two. In practice F2 is the probability of an S&P cut to BB+, plus a small tail of a two-notch move elsewhere.

| Agency | Current | Last action | Stated downgrade triggers | Oracle against the trigger |
|---|---|---|---|---|
| **S&P** | BBB− / A-3, stable | July 9, 2026: cut from BBB/A-2 | Adjusted leverage **sustained above 4.5x**; Oracle **not on a path to positive FOCF by FY2029**; a negative view of Oracle's AI strategy or of the AI industry. Upgrade "unlikely" within two years; it needs leverage toward mid-3x | S&P's own FY27 forecast is leverage in the "mid-4x area" (down from 4.8x) and FOCF of "nearly −$42bn" including prepayment benefits, peaking in FY27 and positive "by 2029". Fortune's reading of S&P is positive FCF only in FY2028. **Headroom is essentially zero on leverage and one year on the FOCF path.** OpenAI concentration is named as a rationale (about half of RPO) |
| **Moody's** | Baa2, negative | Feb 2, 2026 affirmation; outlook negative since July 2025 | Primary text not obtained. Secondary reports say leverage "could approach 5x temporarily", the build must be funded "with a meaningful proportion of equity", and counterparty risk on the "largest AI infrastructure customer" is significant | A negative outlook held for 15 months is ripe for resolution. A cut to Baa3 is plausible, but it would not resolve F2 |
| **Fitch** | BBB / F2, stable | Feb 2, 2026 affirmation | Single secondary source: EBITDA leverage sustained above 3.5x; lease-adjusted above 4.0x; (CFO−capex)/debt below 15%; a departure from the balanced debt/equity mix | Fitch forecast pre-dividend FCF of −$26B in FY26 (actual −23.7) and −$18B in FY27, far milder than S&P's −42. TTM (CFO−capex)/debt is −28.7/125.3 = **−23%**, already far through its sensitivity, so Fitch is looking through the build |

**My proxy metrics (C, not agency-comparable):** Q1 EBITDA ≈ operating income 6.728 + depreciation 3.156 + amortisation 0.202 = 10.086, or ~40.3 annualised. Gross borrowings / EBITDA ≈ **3.1x**; adding recognised leases (169.1) gives ≈ **4.2x** before any rent add-back; net of cash, ≈ 3.3x. S&P's mid-4x figure is higher because it is forward-looking and counts leases as they commence: $288B of commitments coming onto the balance sheet over FY27 Q2–FY29 is what pushes adjusted leverage up even as EBITDA grows. The rating outcome turns on whether OCI revenue from the new sites (Abilene, Shackelford, Port Washington, Saline, Jupiter) starts in step with the lease liabilities.

**Market pricing:** five-year CDS at 288–300bp implies a risk-neutral hazard of ~4.8% a year at 40% recovery: about 9% over two years and 21% over five (my arithmetic, C). That is high-yield-like pricing. The market already treats Oracle roughly as a BB credit, and agencies usually lag markets.

**My F2: 8% at 6 months, 24% at 12 months, 40% at 24 months** (register: 12/28/42).

- **Lower at 6 months (8 vs 12).** S&P moved to *stable* only three months ago. S&P normally signals with a negative outlook or CreditWatch before a cut into speculative grade, absent a discrete shock. Oracle will issue no debt in calendar 2026, so there is no bond-deal review. The Q1 10-Q shows liquidity of 37.1 and a working equity channel ($19.9B in a single quarter). The visible 6-month catalysts are Q2 results (mid-December), the Jupiter permit decision (deadline November 23) and OpenAI financing news. Any of them would more likely move S&P's outlook than the rating.
- **Similar at 12 and 24 months.** Headroom is zero. Lease commencement mechanically raises adjusted leverage through FY28–29. The remaining ~$20B raise in January–May 2027 forces a fresh agency review. S&P names OpenAI concentration explicitly. Conditional on an F3-type OpenAI cancellation or deferral, I put P(F2) at ~45% within 12 months and ~60% within 24 months. Without one it is ~12% and ~20% (leverage drift, delays, funding stress). Weighted by the register's F3 (32% / 52%), that gives ≈22% and ≈41%. I round to 24 and 40 to allow for a Moody's or Fitch two-notch tail and for the CDS signal.
- **What would move me up:** S&P revising the outlook to negative; a quarter in which the customer-prepayment line falls while capex holds; the January–May 2027 raise done as secured or project-level debt, or at spreads near current CDS; NMED denying or dismissing the Jupiter permit.
- **What would move me down:** another large equity raise; FY27 net capex below $70B; OpenAI closing committed financing that covers its 2027 payments; Q2 OCI revenue showing the Abilene ramp.

## OpenAI dependence

- **What Oracle discloses (A):** nothing customer-specific. The Q1 FY2027 10-Q text has no mention of OpenAI, no 10%-customer disclosure and no concentration-of-credit-risk note. The 10-K risk factor says only that "in certain OCI offerings, we are more concentrated among a number of large customers, which could increase these risks." The note's row 34 ("no customer ≥10% of FY26 revenue") could not be located in the part of the 10-K I read. It should be quoted with a page reference or softened.
- **What others estimate:** S&P (July 2026) puts OpenAI at roughly half of the $638B May RPO (B, via PPC Land). In September 2025 S&P estimated OpenAI could exceed a third of Oracle's revenue by FY2028 (B, via Investing.com). OpenAI's own announcement gives >$300B over five years (A as announcement). Against the $664B August RPO that is ≤45%; against May it is ~47%. The S&P half is consistent if other OpenAI orders exist. Management also said Q1 added >$30B of AI contracts whose structure does not raise capital needs (A). Reporting that non-OpenAI backlog "more than doubled" was a search lead only.
- **Customer funding:** the $11.4B of Q1 prepayments and the $75B "prepaid and customer supplied hardware portions of our large AI contracts" (Q4 release, A) are unattributed. Prepayments are performance obligations: they lower Oracle's funding need but bind it to deliver.
- **Site ownership and project finance:**

| Site | Developer / owner and finance | Status | Grade |
|---|---|---|---|
| Abilene, TX (1.2GW) | Crusoe; JV with Blue Owl-managed funds and Primary Digital; $15B JV financing (May 2025) | Two buildings live since 2025; final (eighth) building topped out. In March 2026 Bloomberg and Reuters reported a dropped 600MW nearby expansion; Oracle said the agreement was on track | A announcement; C reports |
| Shackelford Co., TX and Port Washington, WI | Vantage; **~$38B construction loan** (23.25 TX + 14.75 WI), JPMorgan/MUFG, ~SOFR+250bp, four-year tenor | Bloomberg (April 15, 2026): syndication "nearly done" after months, with some lenders still placing under $1B. October reports say some lenders are selling slices to non-bank buyers at a discount. On the Q1 call management acknowledged delays at the Wisconsin and New Mexico sites but said they would not affect FY27 guidance | C (reported, unverified) |
| Saline Twp., MI | Related Digital with Blackstone-affiliated equity; **$16B** financing with fixed-rate debt anchored by PIMCO-managed funds (April 24, 2026); Blue Owl withdrew in December 2025 | First of three buildings nearing completion (Oracle, June 1, 2026) | A announcement (search); **missing from the note** |
| Doña Ana Co., NM (Project Jupiter, 2.45GW) | STACK (Blue Owl) with BorderPlex; **~$18B bank loan**; FT: quoted at 89–91c (Santander, Jefferies) | Force-majeure notice (Sept 24) to protect deferral if the 2028 opening slips; flood statement (Sept 30) says schedule maintained. Reporting says the Energy Transfer gas pipeline was denied twice and slipped to February 1, 2027, and Oracle switched to Bloom fuel cells. On October 14 New Energy Economy moved to dismiss the air-permit application; the hearing officer (retired Judge James Browning) set an **October 26** hearing on the motion; NMED's decision deadline is reported as **November 23**. Oracle's October 15 35% emissions-cut proposal answers that motion | A Oracle statements; B/C local and FT-derived reporting |

- **Loss allocation.** Project loans are not Oracle debt, but Oracle's leases are what service them. If a site is late, lenders face construction carry while Oracle has force-majeure deferral. If OpenAI does not pay, Oracle keeps the lease and loses the revenue. The 89–91c Jupiter quote is the market pricing that asymmetry.

## Omissions

Last 30 days (September 18 – October 18, 2026):

1. **Delay acknowledged by management.** On the September 10 call, management said New Mexico and Wisconsin delays would not affect FY27 guidance, and reporting has Jupiter's power in-service date at February 2027. This conflicts with the note's reliance on the September 30 "maintained planned schedule" statement and belongs in Conflicts. (B transcript summary; C reporting.)
2. **Jupiter permit litigation dates**: the October 14 motion to dismiss, the October 26 hearing and the November 23 NMED deadline (B/C, Source NM and Albuquerque Journal via search). The note says only "pending".
3. **Equity stress**: ORCL −8.8% on October 14 to $130.55 in the CoreWeave bond scare, a further ~4.6% on October 16, and a fall on October 8 after the FT's OpenAI revenue report (B, CNBC, 24/7 Wall St., MarketBeat via search).
4. **Insider activity, September 2026** (EDGAR Form 4 extracts via search, B): Sicilia sold under a 10b5-1 plan (10,882 shares at $139.94 on Sept 16; 22,562 at $151.59 on Sept 22). Henley made large open-market sales in June 2026 at ~$156–164. Director Rusckowski **bought** 25,000 shares at ~$139.35 on Sept 29. Ellison cancelled his sale plan on Sept 12. The note's sale example (Catz, June 2025) is 15 months old.
5. **AI World** (October 25–28) is still ahead. No new guidance or financing has been announced since September 10, and no Oracle 8-K or prospectus supplement after August 31 was found (search only; EDGAR was not browsed).

Structural omissions:

6. **S&P's triggers and forecasts** (adjusted leverage >4.5x; positive-FOCF path by FY2029; FY27 mid-4x and −$42B FOCF) and **S&P's OpenAI estimate of about half of RPO**. These are the facts that decide F2.
7. **"No additional debt in calendar year 2026"** (Q4 release, A). It puts the remaining ~$20B in January–May 2027, which is a dated test of market access.
8. **The A-3 short-term rating**, and what it means for commercial-paper access.
9. **The Saline Township $16B project** (Related/Blackstone/PIMCO), missing from the site table.
10. **Interest expense up 55% to 1.428 in Q1**; restructuring plan of up to $2.1B plus $0.7B.
11. **Agency disagreement**: FY27 pre-dividend FCF of −$18B (Fitch, February) against FOCF of −$42B (S&P, July). Also S&P's positive-FOCF year: FY2029 (PPC Land) versus FY2028 (Fortune's reading).
12. **Implied rent run-rate** of the $288B commitments, ~$15–19B a year once commenced: the mechanism that drives S&P's leverage path.
13. **Moody's affirmation date**: February 2, 2026, not December 2025.

## Summary-bullet assessment

| Bullet | Supported? | Treatment |
|---|---|---|
| 1. FY26 deficit −23.686 | Yes (A) | Keep |
| 2. Q1 FCF −5.396 despite 11.363 advances | Yes (A) | Keep; add "OCF excluding advances 11.7 against capex 28.5" so the size of the customer funding is visible |
| 3. Borrowings 125.3; net 88.3; $288B leases | Yes (A) | Keep; add the commencement window (FY27 Q2–FY29) and the 55% rise in interest expense |
| 4. OpenAI >$300B; share undisclosed | Yes on Oracle's disclosure | Incomplete: add S&P's estimate of about half of RPO and the 10-K large-customer risk factor |
| 5. ATM done; ~$40B plan | Yes (A) | Add "no further debt in calendar 2026", so ~$20B falls in January–May 2027 |
| 6. CDS 288bp; S&P BBB− stable | Yes (B) | Too soft. It omits that S&P's trigger (4.5x) sits at its own FY27 forecast (mid-4x), and that Moody's is negative |
| 7. Jupiter permit pending | Yes (A) | Understates: management acknowledged delays, and the permit faces an October 26 dismissal hearing and a November 23 deadline |
| (missing) Bottom line | n/a | After the Codex pass the Summary has no judgement. The project needs one on "overextended" and on who bears losses (see edit 5) |

## Your assessment

**Is Oracle overextended?** Yes, in a specific and checkable sense: its contracted obligations have outrun its own cash generation and its rating headroom. They have not outrun its liquidity.

- Oracle has committed to ~$93B of gross capex in FY27 against ~$44B of OCF before customer money. It has $288B of leases commencing over the next ~2.5 years, $34B of purchase obligations and $125B of debt. S&P's FY27 leverage forecast already sits at its downgrade trigger.
- Its plan works only if three outside parties keep performing: customers prepaying ~$20–25B a year, equity and bond markets taking ~$40B a year, and a customer S&P puts at about half of backlog paying on schedule. That customer's reported revenue was revised down by about $20B this month (FT, C). Oracle has no slack if any one of the three falters, and the January–May 2027 raise will test the second.
- Against this: liquidity of $37B, a demonstrated equity channel, legacy software earnings, 97.9% reported GPU utilisation, OCI growth of 121%, and the flexibility to defer discretionary capex. There is no evidence of insolvency or imminent default. "Conditional fragility" (the Codex view) and "overextended" describe the same facts; the difference is emphasis. I would use "overextended relative to its rating and its own cash flow".

**First thing that would show it is failing:** the **customer-prepayment line in the Q2 FY2027 cash-flow statement** (quarter ending November 30, reported mid-December). Watch it alongside net cash capex. If prepayments fall well below the ~$5–6B a quarter needed to bridge the $20–25B gap while gross capex holds near $23B a quarter, then customers, most likely OpenAI, are no longer funding their share. The cost moves onto Oracle's balance sheet, the FY27 requirement rises toward $60B, and S&P's FOCF path breaks. That would show up before any RPO cut or rating action. An S&P outlook revision to negative would be the second signal.

## Recommended edits

1. **Summary bullet 4: append:** "Oracle's filings name no customer and report no customer concentration for OCI beyond a risk-factor statement that 'in certain OCI offerings, we are more concentrated among a number of large customers.' S&P estimated in July 2026 that OpenAI accounts for roughly half of RPO (rating-agency estimate, B)." Add a key-claims row with the PPC Land and Fortune sources pending S&P's own text.

2. **Replace Summary bullet 6:** "S&P cut Oracle to BBB−/A-3 (stable) on July 9, 2026. Its stated downgrade triggers are adjusted leverage sustained above 4.5x, or no path to positive free operating cash flow by FY2029; its own FY2027 forecast is leverage in the mid-4x area and FOCF of about −$42bn, so headroom is minimal (B). Moody's affirmed Baa2 with a negative outlook on February 2, 2026, and Fitch affirmed BBB stable the same day; both are two notches above speculative grade. Five-year CDS was a record 288bp on October 15 and near 300bp later that week (B)."

3. **Summary bullet 5: append:** "Oracle 'does not expect to issue additional debt in calendar year 2026', so the remaining ~$20bn of the FY2027 plan falls in January–May 2027 (A)."

4. **Replace Summary bullet 7:** "On the September 10 call management acknowledged delays at the New Mexico and Wisconsin sites while maintaining FY2027 guidance (B). Project Jupiter's air permit remained pending on October 15: a motion to dismiss is set for hearing on October 26, NMED's decision deadline is reported as November 23, and Oracle proposed a 35% cut in permitted emissions in response (A Oracle statement; B/C reporting). Exposure grows if lease commencements (FY2027 Q2–FY2029) run ahead of billable capacity."

5. **Add a closing Summary bullet:** "Judgement (C): Oracle is overextended relative to its rating and its own cash generation, not relative to its liquidity. FY2027 is fundable (≈$40bn needed to preserve opening liquidity; the $20bn ATM plus ~$20bn planned covers it) provided customers keep funding $20–25bn of capex. If they do not, the need rises to ≈$60bn. Shareholders bear the first loss; project lenders bear site delays; unsecured bondholders are exposed only if capital access fails."

6. **Row 23: replace** "Baa2 negative / BBB stable; Fitch affirmation Feb 2, 2026 | Dec 2025 / Feb 2026" **with** "Moody's Baa2 negative, affirmed Feb 2, 2026 (negative since Jul 2025); Fitch BBB/F2 stable, affirmed Feb 2, 2026, forecasting FY27 pre-dividend FCF of about −18 | Feb 2, 2026". Grade B for Moody's until the primary text is obtained.

7. **Add key-claims rows:**
   - (a) S&P triggers and forecasts, July 9, 2026, B.
   - (b) "Oracle does not expect to issue additional debt in calendar year 2026", Q4 release, A.
   - (c) Q1 FY27 interest expense 1.428 against 0.923, 10-Q, A.
   - (d) 2026 Restructuring Plan up to 2.1 plus ~0.7 supplement, 10-Q, A.
   - (e) Total deferred revenue 30.789, of which 16.103 is non-current, 10-Q, A.
   - (f) Saline Township $16bn Related/Blackstone/PIMCO financing, Apr 24, 2026, A announcement.
   - (g) Vantage $38bn syndication update: "nearly done" in April 2026; October reports of discounted sales to non-bank buyers, C.
   - (h) September 2026 Form 4s: Sicilia 10b5-1 sales; Rusckowski purchase of 25,000 shares, A once fetched from EDGAR.

8. **Funding section: replace the flat-assumption scenarios with a roll-forward from August 31:** "From August 31 liquidity of 37.1: remaining net capex 52.0 (70 − 17.966), less Q2–Q4 OCF excluding advances of about 32 (FY27 range 40–47), plus dividends of about 4.9 at the post-ATM run rate, plus remaining scheduled principal of about 4.1, leaves about 8 without new financing and about 28 with the remaining ~$20bn. On a full-year basis the requirement to preserve opening liquidity is about 37–44 (central 40). If the $20–25bn customer-funded portion does not arrive, the requirement is about 60–67." Keep the B/C labels. Note that the A-3 rating limits commercial-paper access.

9. **Site table: add a row:** "Saline Township, Michigan | Related Digital with Blackstone-affiliated equity; $16bn financing with fixed-rate debt anchored by PIMCO-managed funds (April 2026), after Blue Owl withdrew (December 2025) | Oracle tenant serving OpenAI; first of three buildings nearing completion (June 2026)." **Add to the Jupiter row:** "$18bn bank loan; force-majeure notice protects deferral if the 2028 opening slips; gas pipeline in-service reportedly February 2027."

10. **Conflicts: add two bullets.**
    - "Schedule: Oracle/STACK's September 30 statement maintained Jupiter's schedule, while management acknowledged New Mexico and Wisconsin delays on September 10 and reporting places pipeline gas at February 2027."
    - "Agency forecasts diverge: S&P projects FY2027 FOCF of about −$42bn with positive FOCF by FY2029 (Fortune reads FY2028); Fitch projected FY2027 pre-dividend FCF of about −$18bn."

11. **Signals table: add rows.**
    - S&P outlook (stable since July 9).
    - Customer prepayments per quarter (Q1: 11.363; ~5–6 a quarter needed).
    - Jupiter permit (October 26 dismissal hearing; November 23 deadline).
    - January–May 2027 financing (size, instrument, spread).
    - Lease commencements (288 uncommenced).

12. **Front page (`report/index.md`) and `report/stack.md`:**
    - Change "CDS 282-300bp" to "CDS 288bp (15 October, record) to near 300bp". I found no source for 282.
    - Change "OpenAI's share undisclosed" to "OpenAI's share undisclosed by Oracle; S&P estimates about half".
    - In Part 3 consider adding: "S&P's own FY2027 leverage forecast sits at its 4.5x downgrade trigger."

13. **Register F2:** consider 8/24/40 with the rationale in the Rating path section. The main reasons are S&P's three-month-old stable outlook, the absence of debt issuance before January 2027, and S&P's habit of revising the outlook before cutting into speculative grade. 12- and 24-month risk is driven by zero headroom, lease commencement and the OpenAI correlation. At minimum, add to the rationale that F2 is in practice a one-notch S&P question and that S&P's triggers are already at its forecast.

14. **Row 34:** quote the 10-K sentence and page for "no customer ≥10% of FY26 revenue", or replace it with the risk-factor quotation in edit 1.

## Sources

Fetched (accessed 2026-10-18):

- [Q]: Oracle Form 10-Q, quarter ended Aug 31, 2026: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
- [K]: Oracle Form 10-K FY2026 (partial: Item 1 and risk factors): https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
- [E5]: Oracle Q1 FY2027 release, Sept 10, 2026: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
- [E4]: Oracle Q4 FY2026 release, June 10, 2026: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx
- [SPX]: PPC Land, "S&P cuts Oracle to BBB- as AI buildout widens cash deficit to $42bn", July 18, 2026: https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/
- [FOR]: Fortune (K. Koharki), Sept 18, 2026: https://fortune.com/2026/09/18/sp-kept-oracle-investment-grade-its-own-numbers-dont-support-that-call/
- [INV25]: Investing.com, agency actions, Sept 24, 2025: https://www.investing.com/news/stock-market-news/oracles-credit-ratings-affirmed-amid-ai-infrastructure-expansion-93CH-4253750
- [T]: Motley Fool Q1 FY2027 call page (summary only): https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/

Search extracts only (graded one step lower):

- [MDY]: Newsquawk, Moody's affirms Baa2, Feb 2, 2026: https://www.newsquawk.com/headlines/moody-s-affirms-oracle-s-orcl-baa2-rating-on-equity-announcement-outlook-remains-negative-02-02-2026
- [MDY2]: FinancialJuice: https://x.com/financialjuice/status/2018302863517086102
- [FIT]: Fitch disclosure (per note S17) and Investing.com: https://www.investing.com/news/stock-market-news/oracle-stock-rises-after-fitch-affirms-bbb-rating-amid-debt-plans-4478591
- [GF]: GuruFocus, CDS record: https://www.gurufocus.com/news/9124975/credit-default-swaps-surge-for-us-tech-firms-amid-ai-sector-strain-oracle-orcl-spreads-hit-record-high
- [C]: Reuters via MarketScreener (note S19): https://se.marketscreener.com/nyheter/cds-spreadar-inom-ai-vidgas-kraftigt-ce785dd3d980f124
- CNBC, Oct 14, 2026: https://www.cnbc.com/2026/10/14/coreweave-stock-bond-yields-ai-debt.html ; 24/7 Wall St.: https://247wallst.com/investing/2026/10/15/oracle-fell-nearly-9-as-coreweaves-bond-scare-spread/ ; MarketBeat, Oct 16: https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-falls-46-heres-what-happened-2026-10-16/
- Source NM, Oct 15, 2026: https://sourcenm.com/2026/10/15/oracle-says-it-will-cut-project-jupiter-emissions-after-new-mexico-org-seeks-to-toss-permit-case/ ; Albuquerque Journal: https://www.abqjournal.com/news/new-challenge-to-project-jupiter-air-permit/3143387
- Jupiter loans/force majeure: https://tradersunion.com/news/financial-news/show/3392215-oracle-new-mexico-data-centre-debt ; https://news.bloomberglaw.com/ip-law/oracle-cites-force-majeure-to-shield-itself-on-big-data-center
- Bloomberg, Apr 15, 2026, $38B syndication: https://www.bloomberg.com/news/articles/2026-04-15/oracle-tied-38-billion-debt-takes-months-for-market-to-swallow ; October follow-up: https://startupfortune.com/banks-are-now-trying-to-offload-the-ai-data-center-debt-they-just-underwrote/
- Related Digital, Saline financing, Apr 24, 2026: https://www.related.com/press-releases/2026-04-24/related-digital-announces-financing-16-billion-oracle-data-center-project ; Oracle, June 1, 2026: https://www.oracle.com/news/announcement/related-digital-oracle-openai-walbridge-and-governor-whitmer-celebrate-construction-of-stargate-campus-in-saline-township-2026-06-01/
- Abilene: https://datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas ; https://tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion
- Q1 call delay remarks (secondary/AI-generated summaries): https://betafinch.com/episodes/ORCL_2027_Q1_en
- EDGAR Form 4s (Sept 2026), e.g.: https://www.sec.gov/Archives/edgar/data/0001341439/000134143926000096/form4.xml and the sibling accessions 000134143926000083–000134143926000099
