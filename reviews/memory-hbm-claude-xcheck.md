# Memory / HBM: Claude cross-check (second vendor)

Review date: **2026-10-18**. Reviewer: Claude (Opus 5.5), fresh context, first Claude reviewer of `research/stack/memory-hbm.md` (Codex-written, already corrected once after [the Codex cross-check](memory-hbm-codex-xcheck.md)). I fetched 15 URLs, all on 2026-10-18; two of them failed (Micron IR press release behind a Cloudflare challenge; Benzinga 403) and one timed out (Samsung newsroom; its figures were confirmed through search snippets that quote the release). Micron's GAAP tables were checked in the reconciliation pages of the earnings deck, which reproduce the press-release figures. No other file was edited and no git command was run.

## Verdict

Every figure I re-checked reproduces. The arithmetic is clean, and the Micron, SK hynix and Counterpoint numbers that the stack page uses still hold.
Both Codex passes share three blind spots. The supply analysis covers only the big three and leaves out China's CXMT. SK hynix's own semi-annual filing was never opened: it says there is "no order backlog based on long term supply contracts", shows 100% utilisation and lays out a ~KRW1,100tn long-range investment plan. And equity investors are already taking losses: Korean shares are −56% from the June peak and the ADS trades below its $149 offer.
The conclusion that the layer is comfortably profitable today stands. The note's line that impairment "remains a scenario" is true for project returns but already false for shareholders. The note should also say plainly that Micron-style risk transfer to customers is not shown to exist at SK hynix.

## Claim re-verification

The 12 rows below carry the profitability, cash-funding, contract-protection, capacity-calendar, share and P2 conclusions. Grade A means a primary disclosure, and for a forecast it verifies the statement, not the outcome.

| Claim # | Note's value | Your value | Source | Match? | Grade |
|---|---|---|---|---|---|
| 2 | Micron FYQ4 revenue $54.229bn; GAAP GP $47.047bn (86.8%); GAAP OI $43.751bn (80.7%) | $54,229m; $47,047m; $43,751m; 86.76% / 80.68%. Non-GAAP is 87.0% gross / 82.3% operating ($44.6bn) | [Deck][MD] reconciliation pp.41–43; [remarks][MR] pp.7–8 | Yes | A |
| 3 | FYQ4 OCF $43.973bn; PP&E $11.110bn; net capex $10.774bn; adj. FCF $33.199bn | OCF 43,973; PP&E (11,110); sale proceeds 9; incentives 327; net (10,774); adj. FCF 33,199. Q4 deposits received $12.3bn, in financing | [Deck][MD] p.43; [remarks][MR] p.8 | Yes | A |
| 4 | FY2026 OCF $89.675bn; PP&E $30.712bn; incentives $3.316bn; net capex $27.367bn | Same; adj. FCF $62,308m; FY2025 comparatives OCF $17,525m, PP&E $15,857m | [Deck][MD] p.45 | Yes | A |
| 7 | 26 take-or-pay SCAs, >35% of estimated revenue through 2030; three-quarters with pricing framework | Verbatim: "a majority of which have pricing bands with floor and ceiling prices"; the remaining quarter is "negotiated periodically based on market prices"; SCAs now extend into 2031; $32bn of customer commitments, "vast majority" cash deposits | [Deck][MD] slide 11; [remarks][MR] p.3 | Yes. The note's Summary leaves out the floor/ceiling detail that the stack page carries | A |
| 9 | FY27 net capex: Q1 ~$11.5bn, H1 ~$25bn, H2 higher → >~$50bn | Same, "net of anticipated government incentives". Also: capex raised "versus prior plans", the majority of the increase is construction for "late calendar 2028 and beyond", and there is "some pull-forward of equipment spending" | [Remarks][MR] pp.5, 10 | Yes | A (guidance) / B (sum) |
| 10 | ID1 mid-2027; ID2 late-2028; NY 2030; Japan late-2028; Singapore HBM packaging early-2027, NAND H2-2028; Tongluo mid-2027 | All match. Deck adds: output "becomes more meaningful starting a few quarters after initial output" | [Deck][MD] slides 8–9 | Yes | A |
| 12 | SK hynix Q2 revenue KRW79.3187tn; OP KRW60.5426tn; 76% | Same; 76.33% computed. Net profit KRW93.9226tn | [Q2 release][H2] | Yes | A |
| 13 | SK hynix Q2 gross margin ~83%, grade C from Investing.com slide coverage | Primary filing: Q2 revenue W79,318,746m, cost of sales W13,327,390m, GP W65,991,356m = **83.20%**; Q1 by subtraction W41,679,414m / W52,576,287m = 79.27% | [SK hynix semi-annual report 6-K][HK6], interim income statement | Yes; **upgrade to A** | A |
| 16 | "Around 10 LTA customers" (July); 2026 HBM demand secured | Release wording matches. But the same company's semi-annual filing (period to June 30) says: "The Company determines supply volumes and prices on a monthly and quarterly basis by mutual agreement with major customers, and there is no order backlog based on long term supply contracts." | [H2]; [semi-annual 6-K][HK6], "Order Status" | Figure matches. **Conflict not recorded in the note** | A for both statements; how they reconcile is unverified |
| 19 | Y2 KRW35.2tn, cleanroom June-2029; M17 KRW19.1tn, cleanroom Dec-2028 | Same. Groundbreakings July 2027 (Y2) and Feb 2027 (M17); investment periods to Oct 2031 and Apr 2031; equipment "in stages as demand trends develop"; no wafer-capacity figures | [SK hynix announcement][HN] | Yes | A |
| 27 | Counterpoint HBM revenue share Q1 58/21/21, Q2 50/33/18 | Same; page dated Sep 2, 2026; "by Revenue"; rounding footnote. The same page's DRAM table shows **CXMT at 10% of DRAM revenue in Q2 2026, up from 4% in Q2 2025**, and SK hynix's DRAM share down from 39% to 25% | [Counterpoint][CP] | Yes | C |
| 39 | P2: DDR5 8GB SO-DIMM session average $133 on Aug 31; trigger ≤70% of the 2026 monthly peak | Public table still shows 2026-08-31: high 141, low 118, average 133.00, ▲2.31%. The September value (dated 9/30) is Gold+ members only. Rule matches [register][FR] row P2 | [TrendForce][PX], fetched Oct 18 | Yes | B (price) / A (register) |

I did not re-fetch Nvidia (row 31), the SK hynix 424B4 (row 20) or Samsung's slides (rows 22–24). The Codex review verified those against primary filings, and nothing I found contradicts them. The Samsung Q3 guidance ranges (KRW194–196tn sales, KRW107.3–107.5tn OP) were confirmed through search results quoting the official release.

## Arithmetic checks

| Derived figure | Recalculation | Result |
|---|---|---|
| Micron FYQ4 margins | 47,047/54,229 = 86.76%; 43,751/54,229 = 80.68% | Correct |
| Micron FYQ4 net capex, FCF | 11,110 − 9 − 327 = 10,774; 43,973 − 10,774 = 33,199 | Correct |
| Micron FY26 net capex, FCF | 30,712 − 29 − 3,316 = 27,367; 89,675 − 27,367 = 62,308 | Correct |
| "OCF covers gross physical investment" | FY26 89,675 / 30,712 = 2.92× | Correct |
| Micron cash and debt | 38,364 + 5,070 + 30,019 + 27 = 73,480; 491 + 4,688 = 5,179; net cash 68,301 | Correct; matches deck |
| Micron FY27 capex implied | H1 ≈ 25, H2 > H1 → > ~50, i.e. **~1.8× FY26 net capex of 27.4** | Correct. The note never states the growth rate, and it should |
| Micron FYQ3 OCF (CSV) | 89,675 − 8,411 − 11,903 − 43,973 = 25,388 | Matches deck p.42 |
| SK hynix OP margin; net cash | 60.5426/79.3187 = 76.33%; 88 − 18.6 = 69.4 | Correct |
| SK hynix gross margin | 65,991,356/79,318,746 = 83.20% | Supports the C-graded 83%, now A |
| SK hynix HBM mix estimate | 9.4/79.3187 = 11.85% | Arithmetic correct; numerator stays C |
| SK hynix ADS gross | 177.9m × $149 = $26.507bn | Correct |
| Samsung margins, net cash, OCF/PP&E | 107.4/195 = 55.08%; 89.2/127.5 = 69.96%; 189.999 − 22.4087 = 167.59; 105.08/14.11 = 7.45× | Correct |
| Nvidia commitments; Amazon capex | 279 − 119 = 160; 220 − 200 = 20 | Correct |
| Micron FY23 downturn | 15.540/30.758 − 1 = −49.48% | Correct |
| P2 example threshold | 133 × 0.70 = 93.10 | Correct, but conditional. August was still +2.31% and TrendForce forecasts Q4 contract prices up 10–15%, so the 2026 peak is very likely above $133. The $93.10 example probably understates the real threshold |
| Counterpoint Q2 sum | 50 + 33 + 18 = 101 | Rounding, as flagged |

No arithmetic error found.

## Omissions

1. **SK hynix's semi-annual report (Form 6-K, August 2026, period to June 30) was never opened.** This is a primary SEC filing, and four of its items change the analysis. [HK6]
   - *No long-term backlog.* The filing says volumes and prices are set "on a monthly and quarterly basis" and that "there is no order backlog based on long term supply contracts". So the Micron-based risk-transfer argument (take-or-pay, floors, RPO, deposits) cannot be carried over to SK hynix. The July 29 "LTAs with around 10 customers" may postdate June 30 or may carry no binding price and volume. Either way it is unproven protection.
   - *100% utilisation in H1 2026* (available hours = actual hours). The note has no utilisation data, and full utilisation at peak margins is the standard top-of-cycle signature.
   - *A ~KRW1,100tn long-range investment strategy disclosed June 29, 2026.* It covers Yongin ~KRW600tn ("complete the construction of a fourth fab by 2033"), Cheongju ~KRW100tn and a new Southwestern Cluster ~KRW400tn, plus the P&T7 packaging fab (~KRW19tn, April 2026) and Yongin Phases 2–6 (KRW21.6tn, February 2026). The note discusses only Y2/M17 (KRW54tn). The plan is phased and conditional, but for the overbuild question it is the largest memory capital commitment on record and belongs in the note. Grade A for the plan, not for its execution.
   - *Earnings quality and funding.* Q2 finance income was KRW65.86tn, including KRW53.24tn of valuation gains on financial instruments. Kioxia's fair value is the auditor's key audit matter. That is why net profit (KRW93.9tn) exceeds revenue. H1 OCF was KRW91.74tn against KRW18.33tn of PP&E purchases (5.0×). Two customers each took over 10% of H1 revenue (13.35%, 13.03%), against one customer at 27.31% in H1 2025.
2. **China is missing from the supply side, and both reviewers missed it.** Counterpoint's own page, already cited for HBM, shows CXMT at 10% of DRAM revenue in Q2 2026, up from 4% a year earlier [CP]. CXMT listed in Shanghai in July 2026. Reported proceeds are ~CNY29.5bn for DRAM upgrades, and the prospectus reportedly contains no HBM project ([Tom's Hardware][TOM], secondary, C). On October 10–11 CXMT's president claimed a new higher-density cell design, with a server product by year-end. Micron and SKHY fell 4% on October 12 and fell again through October 16 ([24/7 Wall St][W247], secondary, C; the claim itself is unverified). For conventional DRAM, which sets the P2 price, a fast-growing state-backed fourth supplier that does not respond to Western price signals is the most plausible route to oversupply. The note's three-firm framing understates it.
3. **The pricing question has a dated answer that the note does not give.** SK hynix Korean shares closed at KRW1,272,000 on October 16, −56.4% from the KRW2,919,000 close on June 22. The NYSE ADS closed at $136.49, −31.3% from its September 9 close of $198.63 and **−8.4% below the $149 July offer**. All figures are from [Yahoo daily closes][YK] and [YA], C. The ADS and Korean moves diverge by more than a constant exchange rate would allow, which suggests a large won move or a data issue, so reconcile before quoting either in USD terms. The investors who funded the ~$26bn equity raise are already under water. That is the concrete answer to "who bears losses first" and the note never says it.
4. **Micron's forward guidance and supply outlook from the cited remarks.** These are omitted even though the source is already cited [MR]:
   - FQ1 FY27 revenue $61.5bn ± $1.5bn, gross margin ~86.25%, with FQ1 "the floor for gross margins in fiscal 2027" and "a more moderate rate of price increases".
   - Industry DRAM bit growth in the low-20s% and NAND in the mid-20s% for 2027–28, with both "supply constrained".
   - "We do not have line of sight to when supply and demand will return to balance."
   - RPO ~$150bn "based on committed volumes and minimum pricing".
   - Debt cut from $14.6bn to $5.2bn over FY26; a plan to "return 100% of our excess cash to shareholders", with higher returns from Dec 9, 2026.

   These items strengthen the near-term scarcity case. They also show capital going to buybacks as well as fabs, which reduces the overbuild risk at Micron specifically.
5. **Dated events in the next two weeks.** SK hynix holds its Q3 call on October 28, 9:00 Seoul time, per its [6-K of Oct 14][HK7]. Samsung's full Q3 results with a division breakdown are reported for October 29. Both will supersede the note's Q2 Korean figures and should be in the Signals table.
6. **Reported 2027 HBM4 pricing (leads only).** Korean press (Maeil, Chosun Biz via aggregators) report Samsung quoting 2027 HBM4 at ~$4–4.5/Gb against ~$1.50 for HBM3E, and near-final supply deals with Nvidia and Broadcom. This is unverified (C/D) and should not be cited, but it is the next thing to confirm, because a 2–3× HBM price step for 2027 would raise both supplier margins and the buyer cost that the note's Nvidia and Amazon rows describe.

## Summary-bullet assessment

| # | Supported by the note's evidence? | Concrete (figure + date)? | Comment |
|---|---|---|---|
| 1 | Yes | Yes | Add SK hynix's A-grade 83.2% gross margin. The floor-margin sentence is management's expectation for SCA revenue only; say "for SCA revenue at floor prices" |
| 2 | Yes | Yes | Goes stale on Oct 28–29. Add the two scheduled dates |
| 3 | Yes | Yes | Add "a majority of the priced share in floor-and-ceiling bands; the remaining quarter market-priced". Add the SK hynix "no long-term-contract backlog" contrast; without it the bullet reads as industry-wide protection |
| 4 | Yes | Yes | Fine as C. Add the CXMT 10% DRAM share from the same Counterpoint page |
| 5 | Yes | Yes | Fine |
| 6 | Yes for the dates | Yes | Incomplete: leaves out SK hynix's ~KRW1,100tn long-range plan (to 2033+), Micron's capex increase aimed at "late calendar 2028 and beyond", and CXMT's additions |
| 7 | Partly | Yes | The funding facts are right. But "return impairment ... remains a scenario" ignores the observed equity losses (−56% in Korea; ADS below its offer). Separate project-return impairment, which is not yet observed, from shareholder losses, which already have been |

## Your assessment

Memory is comfortably profitable today and, more unusually, liquid: all three producers hold net cash, Micron has cut its debt to $5.2bn and SK hynix funds capex ~5× over from operations. A credit event in this layer is remote. The overextension is not on balance sheets. It sits in three other places: equity prices set at the June–September peak, long-range capex plans sized to today's scarcity (SK hynix's ~KRW1,100tn, Micron's FY27 capex ~1.8× FY26, both weighted to cleanroom construction for 2028+), and prices high enough that end markets are already shrinking in units (Micron's double-digit PC and mobile declines; Samsung DX's loss). Who loses first: equity holders, and that has started. Next come device makers and other downstream buyers squeezed on component cost, then customers holding SCA deposits and contracted inventory if demand falls short. Lenders come last, and there is little debt. Where I differ from the note: (a) it treats Micron's contract protection as the industry template, but SK hynix's own filing says it has no long-term-contract backlog, so the largest HBM supplier looks more cyclically exposed than the note implies; (b) the price-setter for conventional DRAM in a downturn is likely to be CXMT's expansion, which the note never mentions, not a synchronized big-three ramp; (c) the note's carefully hedged "scenario" language undersells how much of the reversal the market has already priced. I agree with both earlier passes that near-term (6–12 month) scarcity is better evidenced than near-term glut, and that P2 at 5% over six months is reasonable given TrendForce's +10–15% Q4 contract forecast.

## Front-page figures

`report/index.md` contains no figures from this note (grep for Micron, SK Hynix, memory, HBM and DRAM returns nothing). The figures below are on `report/stack.md`.

| Page / location | Figure | From this note? | Still holds? |
|---|---|---|---|
| stack, Memory row | Micron 87% gross / 81% operating | Yes (claim 2) | Yes. GAAP 86.8% / 80.7% (non-GAAP 87.0% / 82.3%); label it GAAP, FYQ4 to Sep 3, 2026 |
| stack, "Shape of it" | Micron 81% operating | Yes | Yes (GAAP) |
| stack, Memory row | SK Hynix 76% operating | Yes (claim 12) | Yes for Q2 2026; superseded by Q3 results on Oct 28 |
| stack, Memory row | Micron FY2026 OCF $90B vs $31B of PP&E | Yes (claim 4) | Yes (89.675 / 30.712) |
| stack, Memory row | SK Hynix ~$26B ADS offering | Yes (claim 20) | Yes ($26.5bn gross, ~$26.2bn net). Worth adding that the ADS is 8% below its $149 offer as of Oct 16 |
| stack, Memory row | 26 take-or-pay agreements, >35% of revenue through 2030, three-quarters with pricing frameworks, mostly floor-and-ceiling bands | Yes (claim 7), plus deck wording | Yes. "Mostly" = Micron's "a majority". This is Micron only and should not be read as industry-wide |
| stack, Memory row | Micron expects supply much tighter in FY2027-28 | Deck/remarks (not in the note) | Yes. The CEO said "fiscal 2027 and 2028"; the market-outlook section says "calendar 2027 and 2028" |
| stack, Memory row | "staggered 2027-28 capacity additions" | Yes (claims 10, 18, 19) | **Partly.** The note's own milestones run 2027–2030 (SK Y2 June 2029; Micron NY 2030), and SK hynix's plan runs to 2033. Should read 2027–29 or later |
| stack, Memory row | SK Hynix already −56% from its 2026 peak | No (public-markets note) | Yes as Korean KRW closes (2,919,000 on Jun 22 → 1,272,000 on Oct 16 = −56.4%, C). Specify "Korean shares, KRW" |
| stack, Memory row | "Shareholders; the layer has little debt" | Yes (claims 5, 14, 24) | Yes |
| stack, Memory row / register P2 | DDR5 8GB SO-DIMM $133 on Aug 31; −30% from 2026 monthly peak | Yes (claim 39) | Yes. Still the latest public value on Oct 18; the September print is members-only. The peak is likely above $133 |
| stack, Memory row | HBM share estimates (Counterpoint) | Yes (claim 27) | Yes, C. `data/memory-hbm-market-share-quarterly.csv` still grades every row **B**, which contradicts the note's adopted C |

## Recommended edits

1. **Claim 13, upgrade to A.** Replace the value with: "Q2 2026 gross profit W65,991,356m on revenue W79,318,746m = 83.2% (Q1 79.3%, derived from H1 less Q2)". Set the source to [SK hynix semi-annual report 6-K](https://www.sec.gov/Archives/edgar/data/2120882/000119312526354777/d147827d6k.htm), type primary, grade A.
2. **New claim row (SK hynix contract basis):** "Semi-annual report (period to June 30, 2026): 'The Company determines supply volumes and prices on a monthly and quarterly basis by mutual agreement with major customers, and there is no order backlog based on long term supply contracts.' Reconciliation with the July 29 'LTAs with around 10 customers' is not disclosed." Grade A for both statements.
3. **Replace Summary bullet 3** with: "On September 30, 2026, Micron reported 26 take-or-pay SCAs covering over 35% of estimated revenue through 2030. Three-quarters of that revenue has a defined pricing framework, a majority of it in floor-and-ceiling bands; the remaining quarter is priced periodically at market. This transfers some demand risk to Micron's customers. SK hynix's semi-annual filing, by contrast, reports no order backlog from long-term supply contracts, so the protection is not shown to be industry-wide." [MD][MR][HK6]
4. **New claim rows and an Analysis paragraph under "When supply actually arrives":** "SK hynix disclosed on June 29, 2026 a medium- to long-term investment strategy of approximately KRW600tn at Yongin (a fourth fab by 2033), KRW100tn at Cheongju and KRW400tn at a new Southwestern Cluster, on top of the P&T7 packaging fab (~KRW19tn). Its H1 2026 utilisation was 100%. These are phased plans, not committed spending, but they show capacity intentions sized to the current shortage well beyond the 2027–29 milestones." [HK6], A.
5. **New claim row and an Analysis paragraph on China:** "Counterpoint estimates CXMT's DRAM revenue share at 10% in Q2 2026, up from 4% in Q2 2025 (C). CXMT listed in Shanghai in July 2026, and on October 10–11 it claimed a higher-density cell design with a server product by year-end (reported, unverified); Micron and SK hynix ADS fell about 4% on October 12. A state-supported supplier expanding conventional DRAM is the most direct route to oversupply in the P2 product class, and the big-three milestones above do not capture it." [CP][W247]
6. **Replace Summary bullet 7's last sentence** with: "Project-return impairment after price normalisation is a scenario, not a measured outcome. Equity losses are already observed: SK hynix Korean shares closed −56% below their June 22, 2026 peak on October 16, and its ADS closed at $136.49, 8% below the $149 July offer (Yahoo closes, grade C)." Add the price rows to the claim table and a "Memory equity drawdown" row to Signals.
7. **Add Micron forward guidance to claim 9 or a new row:** "FQ1 FY27 guidance: revenue $61.5bn ± $1.5bn, gross margin ~86.25%, which management calls the floor for FY27 gross margins, with 'a more moderate rate of price increases'. Industry DRAM bit growth low-20s% and NAND mid-20s% in calendar 2027–28, both supply-constrained; management has 'no line of sight to when supply and demand will return to balance'. FY27 capex raised versus prior plans, mostly construction for late-2028+ cleanroom space; implied FY27 net capex above ~$50bn is ~1.8× FY26's $27.4bn." [MR], A/B.
8. **Signals table:** add "SK hynix Q3 results, call October 28, 2026 09:00 KST ([6-K](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526420934/d413172d6k.htm))" and "Samsung full Q3 results with division breakdown, reported for October 29". Update Summary bullet 2 to name both dates.
9. **P2 example (claim 39 and the Analysis):** after "$93.10 only if $133 is the final peak" add: "August's print was still +2.31% and TrendForce forecasts Q4 contract prices up 10–15%, so the 2026 peak is likely higher than $133 and the threshold correspondingly above $93.10. The public table lags by about a month (the September 30 print is members-only), so archive each public refresh when it appears."
10. **Analysis, SK hynix earnings quality:** replace "Use SK hynix's operating profit rather than net profit distorted by nonoperating gains" with: "Use operating profit: Q2 net profit of KRW93.9tn exceeded revenue because finance income was KRW65.9tn, including KRW53.2tn of valuation gains on financial instruments (Kioxia's fair value is the auditor's key audit matter). SK hynix's reported earnings are therefore also exposed to memory-sector valuations through Kioxia." [HK6], A.
11. **Data file:** change the grade column in `data/memory-hbm-market-share-quarterly.csv` from B to C on every row, matching the note's claim 27.
12. **Stack page (for the lead):** in the Memory row, change "staggered 2027-28 capacity additions" to "staggered 2027-29 capacity milestones (SK hynix plans to 2033)". Change "SK Hynix already −56% from its 2026 peak" to "SK Hynix Korean shares −56% from their June 2026 peak; its ADS is below its $149 offer". Add "Micron only" after the floor-and-ceiling clause.

[MD]: https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-26-Earnings-Deck.pdf
[MR]: https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf
[H2]: https://news.skhynix.com/en/q2-2026-business-results/
[HN]: https://news.skhynix.com/en/fab-facility-investment-2026/
[HK6]: https://www.sec.gov/Archives/edgar/data/2120882/000119312526354777/d147827d6k.htm
[HK7]: https://www.sec.gov/Archives/edgar/data/0002120882/000119312526420934/d413172d6k.htm
[CP]: https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share
[PX]: https://www.trendforce.com/price/dram/dram_contract
[FR]: ../forecasts/register.md
[YK]: https://query2.finance.yahoo.com/v8/finance/chart/000660.KS?range=1y&interval=1d
[YA]: https://query2.finance.yahoo.com/v8/finance/chart/SKHY?range=1y&interval=1d
[W247]: https://247wallst.com/investing/2026/10/12/memory-stocks-slide-as-chinas-cxmt-flags-denser-chip-design-micron-and-sk-hynix-fall-4-western-digital-drops-2/
[TOM]: https://www.tomshardware.com/tech-industry/cxmt-closes-up-466-percent-in-shanghai-debut-with-no-hbm-project-in-its-ipo-prospectus
