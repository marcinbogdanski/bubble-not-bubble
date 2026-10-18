# Independent Codex check of version 0.7

*2026-10-18. Fresh-context, non-Anthropic review of the two requested questions. Read the specified report, register, review sections, research notes and market-views signal; independently fetched the sources linked below and recalculated the model. Only this review was written. No git commands were run. Verification of reporting is not verification of confidential accounts or contracts.*

## Verdict

1. Anthropic is now included appropriately as a financing hub, but the page remains mildly softer on its liquidity risk than the evidence warrants; the figures largely check out.
2. F3b at 10/22/38 versus F3 at 15/32/52 is a coherent subjective ordering, not an evidence-calibrated spread; equal treatment does not require equal probabilities.
3. The owner-revenue arithmetic passes; the capture range, deadline and mandatory-doubling inference need correction. Keep the high-bar conclusion as a D-input scenario, with B only for conditional arithmetic.

## Check 1 — Anthropic framing

### Source checks

| Item | Independent source check | Assessment and grade |
|---|---|---|
| $518B commitments; about 80% rigid | [Reuters, 29 September][commitments] reports **at least** $518B over a decade; approximately 80% is non-cancellable **or payable regardless of usage**, from a confidential prospectus. | Numerically supported. “Anthropic reports” should identify Reuters as intermediary. C, reported/unverified; this is not a publicly inspected filing. The rounded rigid amount is about $414B, not a current bill. |
| Google and Amazon roughly $110B each | The same [Reuters report][commitments] gives Google $111.1B and Amazon $110B, with different contract windows. [Anthropic's April announcement][amazon-anthropic] independently confirms an AWS commitment exceeding $100B over ten years. | Rounding is fair. Exact amounts and rigidity remain C; the broader AWS announcement is A for the statement. These components are included in the aggregate, not additive. |
| Broadcom $29B lease backstop | [10-Q, note 10][avgo-q]: maximum potential exposure after full deployment; five-year leases, declining with payments; default formula uses 85% of covered outstanding amounts less rack-sale proceeds. Nothing paid at quarter-end. | A for disclosed terms; C for Anthropic identification through reporting. The front page's blanket C obscures stronger evidence for the instrument. A backstop to a financing partner is not cash or debt forgiveness for the lab. |
| Up to $42B conditional notes | The same [10-Q][avgo-q] limits proceeds to lease obligations and reports no issuance as of 2 August. [Reuters, 1 October][notes] identifies Anthropic and reports restricted collateral and default-related limits on access. | A for unnamed facility; C for private-company attribution/additional restrictions. Neither funded cash nor an unconditional rescue line. Do not add its ceiling to the backstop as independent debt or liquidity. |
| $16.8B Q3 revenue; 11% adjusted operating margin | [Reuters, 14 October][q3] confirms revenue and reported adjusted profitability. The precise 11% is in [PYMNTS' FT relay, 15 October][margin]. The [FT original][ft-q3] exposed its headline but not its body in this check. | Both C, reported/unverified. No numerical overstatement found. The 11% is neither a Reuters-confirmed exact margin nor audited cash generation. Gross revenue and adjusted operating profit are not comparable directly with OpenAI's net run-rate and forecast cash burn. |
| Largest Broadcom XPU customer in 2027 | Hock Tan's prepared remarks in the [Q3 transcript reproduction][avgo-call] explicitly make this forecast, including its continuation into 2028. | Supported **as management's expectation**, not an achieved ranking or proof of capacity installed. B for reproduced remarks, consistent with the custom-silicon note. Does not establish the largest overall compute purchaser or the larger rigid obligation book. |

### Symmetry and F3/F3b

Adding Anthropic to Part 3 and creating F3b repairs the structural asymmetry identified in section 2.4. Both labs combine large procurement commitments, supplier financing and undisclosed future cash requirements. It is appropriate to put them in the same risk category. It is **not established** that Anthropic is an “equal or larger rigid hub”: the public evidence does not provide comparable consolidated, binding-only liability schedules. OpenAI's roughly $1.4T management headline includes a different mixture of plans and commitments; Anthropic's more detailed reported rigidity cannot be treated as proof that its absolute binding exposure is larger. [OpenAI note, claims 16–31](/research/stack/openai); [Anthropic note, claims 27–32](/research/stack/anthropic).

There are reasons to put F3b below F3. Anthropic's reported operating improvement is genuine counterevidence to immediate funding strain, even though unaudited and adjusted. It announced a $65B Series H, including $15B of previously committed supplier funding; that overlap must not be counted again. OpenAI has a larger reported procurement programme and a reported burn outlook. These differences support an ordering, not a numerical probability model. [Anthropic funding announcement][series-h]; [OpenAI note](/research/stack/openai).

The counterweight is substantial: OpenAI announced $122B of committed capital, and independent primary disclosures establish at least $80B funded within that round by 1 October—Amazon $50B and SoftBank $30B. Its confirmed Azure purchase commitment alone is $250B, alongside an AWS programme of $138B and the separately reported Oracle arrangement. Thus OpenAI is neither an unfunded plan nor merely a loose collection of aspirations. Current unrestricted cash and payment schedules remain unresolved for **both** companies. [OpenAI round][openai-round]; [Amazon 10-Q][amzn-q]; [SoftBank completion][softbank]; [Microsoft announcement][azure]; [OpenAI note, claim 20](/research/stack/openai).

Contract rigidity cuts two ways. It worsens downside liquidity but can reduce the ease of a qualifying cancellation. A consensual restructuring or long deferral could still trigger F3b. F3/F3b also count commercially motivated qualifying amendments, not just distress; conversely, a default without such an amendment need not resolve either question Yes. The probability must include public disclosure by the horizon, and exclude supplier delivery delays and slower new signings. These are amendment/disclosure probabilities, not insolvency probabilities.

The curves are internally coherent: cumulative probabilities rise with horizon, and neither event contains the other. Their 5/10/14-point separation is plausible but uncalibrated. I would **retain 15/32/52 and 10/22/38 provisionally**, add an explicit rationale, and avoid inventing tighter estimates from decade-average bills divided by present sales. F3b also should be named in the register's generic private-company resolution list; its current incorporation of F3 makes the intended rule reasonably clear, but explicit inclusion is cleaner.

**Conclusion:** the page is **mildly softer on Anthropic than warranted**, chiefly through presentation: the backstop sounds reassuring without its liquidity limitations, while adjusted operating profit sits beside OpenAI's cash-burn forecast. It is not too hard on Anthropic by including it among exposed labs, and the lower F3b curve is not itself evidence of favoritism. Keep the positive operating evidence, qualify the backstop and the unlike financial measures, and explain the probability ordering. Do not replace the earlier OpenAI-centric story with an unsupported claim that Anthropic has greater binding exposure.

## Check 2 — Part 2 reproduction

### Inputs and provenance

| Input | Verification | Treatment |
|---|---|---|
| $800B / $1.2T / $1.4T capex in 2026–28 | Directly present in [Goldman's 23 September article][goldman], agreeing with signal U10. Sum = $3.4T. | A for the published forecast; C for realization. “Announced plans” overstates its status: these are analyst forecasts of hyperscaler capex, not a consolidated binding AI construction schedule. |
| Annuity ratio | Reproduced from [unit-economics claim 53 and worked model](/research/theory/ai-unit-economics#a-worked-model), including its 2:1 asset mix. | B conditional arithmetic. The unit note calls assumptions C; demand claim 33 calls the application D. The derived sector scenario should retain D uncertainty. |
| 60–100% AI share | Introduced in reviewer section 2.1; not established by Goldman or demand claims 33–40. | Reviewer assumption, D. In particular, 60% is not a verified lower bound and 100% is a deliberately extreme sensitivity. The current front page omits this input. |
| 40–60% infrastructure capture | Demand claim 40 and analysis explicitly call it a sensitivity, not an observed take rate. | D. Separate from the 50% owner EBITDA margin. |
| $180B in 2026; $130–230B range | Demand claims 34–38: $90B labs + $75B cloud + $50B enterprise apps + $10B consumer apps − $45B assumed overlaps = $180B. | D, illustrative annual sales. No verified invoice-level elimination bridge. The endpoints are scenarios, not a statistical confidence interval. |
| Growth base | Demand claims 38–39 use $55B in 2025 and $180/300/480B in 2026/27/28. | 3.27× in 2026; then +66.7% and +60%. “It roughly tripled” mistakenly makes a model backcast sound observed; 2026 is also unfinished as of this review. |

### Calculation

All following amounts are USD. With capital in trillions, owner annual revenue is also in trillions:

```text
A(r,n) = [1 − (1+r)^(-n)] / r
k(L)   = [(2/3)/A(0.10,L) + (1/3)/A(0.10,15)] / 0.50
Rowner = 3.4 × AI_share × k(L)
Rfinal = Rowner / capture
```

Direct calculation gives $295.344B for the $750B six-year cohort and $467.852B for three years: k(6) = 0.393792 and k(3) = 0.623802. Using rounded table values gives 295/750 = 0.393333 and 468/750 = 0.624. The review's 0.393 is harmless rounding, not the material issue.

| Equipment life | AI share | Annual owner revenue | End-user revenue at 60% capture | At 50% | At 40% |
|---|---:|---:|---:|---:|---:|
| 6 years | 60% | $0.803T | $1.339T | $1.607T | $2.008T |
| 6 years | 100% | $1.339T | $2.231T | $2.678T | $3.347T |
| 3 years | 60% | $1.273T | $2.121T | $2.545T | $3.181T |
| 3 years | 100% | $2.121T | $3.535T | $4.242T | $5.302T |

Thus **$0.8–1.3T owner revenue is reproduced** under the six-year assumptions. **$1.6–2.7T final revenue uses 50% capture only.** At the full independent 40–60% range, the six-year envelope is **$1.34–3.35T**. Section 2.1 actually says 50%; it does not make the 40–60% division error. Version 0.7 does not print the final-revenue range or capture assumption, leaving its doubling inference opaque. The range attributed in the checking request should not be described as the full 40–60% result.

Starting with $0.18T of **annual 2026** sales, the required constant annual factor is `(Rfinal / 0.18)^(1/N)`:

| Capture assumption, six-year equipment | By annual 2029 sales: 3 intervals | By annual 2030 sales: 4 intervals |
|---|---:|---:|
| 50% midpoint | 2.07–2.46× each year (+107–146%) | 1.73–1.96× (+73–96%) |
| Full 40–60% envelope | 1.95–2.65× (+95–165%) | 1.65–2.08× (+65–108%) |

Exact doubling gives $1.44T in 2029 and $2.88T in 2030. It misses even the midpoint-capture low endpoint in 2029, but exceeds the midpoint high endpoint in 2030. “Roughly doubling” is reasonable shorthand for the **2030 midpoint scenario**, not a unique requirement by about 2029. It describes an average compound rate, not a necessity to double in every individual year. Substituting an exit run-rate for calendar-year revenue would require another timing bridge.

The report's base yields $192–288B owner revenue in 2028, versus this six-year $803–1,339B illustrative hurdle: about 14–36%, consistent with the review's rounded 15–35%. The bull gives about 24–60%. But that compares a 2028 demand path with an asserted approximately-2029 mature supply hurdle. The base has no stated 2029–30 values. Extending its last 60% growth assumption gives $768B/$1,229B of final sales in 2029/30, below the midpoint scenario; that extension must be labeled rather than silently attributed to the existing forecast.

### Assumptions that prevent a measured sector shortfall

- **Gross capex versus expansion.** Replacement equipment needs capital recovery too, so deleting replacement spend from the denominator would also be wrong. However, replacement can preserve existing revenue rather than require wholly incremental sales. A model must assign retained sales and cash flows between retiring and replacement assets, and avoid charging the same revenue twice. The current claim that every dollar requires incremental revenue overstates the growth inference.
- **Capital perimeter.** Hyperscaler capex includes ordinary cloud and non-datacenter investment. Amazon explicitly includes fulfillment capacity. A 60% haircut allows for some exclusions but does not verify the allocation, asset mix or AI-only denominator. Conversely, direct lab, neocloud and other infrastructure investment outside Goldman's population can add requirements; not all global final AI sales belong to these owners. [Amazon filing][amzn-q]; [unit-economics claims 51–53](/research/theory/ai-unit-economics).
- **Commissioning and earlier receipts.** On 18 October 2026, 2026 is partly historical; the entire programme is not untouched future capital. Capex dates are not service-start dates. Adding annuities is valid while all corresponding tranches operate and earn the assumed level receipts; prior receipts do not invalidate that particular schedule. But treating the full original cost as still unrecovered at a new 2029 start date would be wrong. Construction delays, ramp-up, earlier collections and later capital spending require dated cash flows. No source verifies simultaneous full utilization by 2029. With a three-year life, early-2026 equipment can already retire in 2029: the $1.27–2.12T sum is not automatically a common 2029 bill without replacements or a different commissioning schedule.
- **Annual requirement versus lifetime return.** The model prices level annual cash flows from service entry. Reaching a run-rate in 2029 or 2030 does not establish that earlier shortfalls have been recovered at a 10% discount rate. Delayed receipts generally require later catch-up; later commissioning changes the schedule. Six-year equipment and 15-year infrastructure also have distinct revenue tails. “By about 2029” cannot be derived from capex-year totals alone.
- **Advertising and internal savings.** Incremental advertising cash margin and internal cost savings can support owned infrastructure without separate AI-product invoices. Count incremental cash benefits net of costs and cannibalization, not all legacy ad sales or an economy-wide productivity estimate. The demand note excludes/unquantifies these bridges. Their omission can overstate required separately billed AI revenue; there is no sourced estimate demonstrating that they are too small to matter. They also should not be used as an unexplained plug that makes the model balance.
- **What owners receive.** If a customer pays an app or lab $100 and $50 reaches the infrastructure owner, owner revenue is $50; at the assumed 50% owner EBITDA margin, only $25 is available in this simplified pre-tax capital-recovery calculation. The lab's $100 is not owner revenue, and neither its gross nor operating margin substitutes for the owner's cash margin. A lab that owns or leases equipment needs its own consolidated asset/payment model. Payments to cloud operators, lessors and chip suppliers cannot all be added as independent capture of the same final sale. Debt, equity and supplier financing can bridge timing and generate owner receipts, but are not sustainable end-user revenue.
- **Return proxy and omitted alternatives.** EBITDA is not unlevered free cash flow: taxes, working capital and other reinvestment are omitted. Zero residual value, constant margin, utilization/pricing, the 2:1 capital mix and 15-year long-asset life are assumptions. Better margins, longer lives, residual value, internal benefits or a lower required return can change the answer. The “growth doubles / capex cut / returns disappoint” trilemma is not exhaustive with these inputs free to move. C1/C2 also do not capture every adjustment to post-2028 spending or commissioning.

The unit note's **Outside estimates** table does not independently authenticate a single deadline. It explicitly separates Gartner's cumulative owner receipts, IoT's selected-owner return forecast, Brookings' mature capacity hurdle and Patel's lab receipts. Brookings provides a required-revenue calculation, not an independently forecast demand shortfall. Their differing capital populations, timing and revenue layers prevent a three-to-one vote from upgrading this extrapolation. D2 likewise tests a much smaller combined lab run-rate on mixed accounting bases, not deduplicated end-user revenue or owner capital recovery. [Outside estimates](/research/theory/ai-unit-economics#outside-estimates-side-by-side); [register](/forecasts/register).

**Conclusion:** “Unproven, and the bar is high” is fair if immediately tied to the explicit scenario. The arithmetic supplies a useful stress test and a substantial growth requirement under its assumptions. The sentence asserting that revenue **must** roughly double through 2030, and the exclusive three-outcome claim, are too strong at grade B. Keep B for the reproducible operations; the sector application and growth deadline remain D. A matched commissioning, replacement and cash-benefit model is needed to turn that sensitivity into an empirical payback finding.

## Recommended edits

1. **Replace Part 2 with the following (retain links to the two research notes):**

   > **2. Is capital being deployed faster than returns can service it? Unproven; an illustrative payback scenario sets a high bar.** Applying our six-year equipment-life model to an assumed 60–100% AI share of Goldman's $3.4T hyperscaler-capex forecast for 2026–28 gives $0.80–1.34T of annual owner revenue while the cohorts operate together. This assumes two-thirds equipment, one-third 15-year infrastructure, a 50% owner EBITDA margin and a 10% discount rate. At 50% end-user-to-owner capture, that corresponds to $1.61–2.68T of annual end-user revenue; the full 40–60% capture sensitivity gives $1.34–3.35T. From our illustrative $180B in 2026, the midpoint-capture case implies 73–96% annual growth through 2030, or 107–146% through 2029. These are conditional growth rates, not an established deadline or measured shortfall (arithmetic B; sector assumptions D). Replacement spending, commissioning, existing revenue, advertising gains and internal savings require reconciliation. Our base path assumes +67% then +60% through 2028; it is not a matched cohort-return forecast. Slower growth would put pressure on returns or spending unless margins, asset lives or other cash benefits compensate.

2. **Replace the Anthropic parenthesis in Part 3:**

   > (Reuters reports at least $518B of Anthropic commitments over a decade, about 80% non-cancellable or payable regardless of use; reported, unverified, C. Broadcom's $29B maximum backstop protects a financing partner; it does not provide unconditional liquidity to Anthropic. Filing terms A; customer attribution C.)

   This preserves the correctly reported scale without implying that supplier credit removes the lab's obligation. Sources: [Reuters][commitments], [Broadcom filing][avgo-q], [Reuters financing report][notes].

3. **Replace the lab comparison in the demand bullet:**

   > Anthropic's reported $16.8B Q3 revenue and 11% adjusted operating margin are encouraging but unaudited; adjusted profit is not a cash-flow measure. OpenAI's roughly $50B net annualised revenue and February forecast of $25B cash burn in 2026 are on different bases and dates. These private-company figures remain reported, unverified, C; they do not establish a comparable current cash-generation ranking.

   Sources: [Reuters revenue reporting][q3], [FT relay][margin], [OpenAI note, claims 3 and 7](/research/stack/openai).

4. **Retain F3/F3b numbers; add this rationale beside them in the register:**

   > F3b is below F3 because Anthropic's reported operating improvement and funding provide a plausible near-term cushion against qualifying commitment changes. OpenAI's substantial confirmed funding is a counterweight to its larger reported programme and burn outlook. Both companies' payment schedules and current unrestricted cash remain unknown. The probability gap is judgmental; these forecasts concern disclosed $10B+ binding amendments, not insolvency, and rigidity can worsen liquidity while making cancellations harder.

5. **In the register's private-company resolution rule, replace its parenthetical list:**

   > (D1, D2, F3, F3b, F5, lab and neolab layers)

[commitments]: https://www.investing.com/news/stock-market-news/anthropics-518-billion-ai-buildout-hinges-largely-on-deals-that-cannot-be-canceled-filing-shows-4922031
[avgo-q]: https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm
[notes]: https://www.aol.com/articles/exclusive-broadcom-lend-anthropic-42-100607000.html
[q3]: https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208
[margin]: https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-narrows-revenue-gap-with-openai-before-ipo/
[ft-q3]: https://www.ft.com/content/11632d03-358c-454b-af95-d06d4072932b
[avgo-call]: https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/
[series-h]: https://www.anthropic.com/news/series-h
[amazon-anthropic]: https://www.anthropic.com/news/anthropic-amazon-compute
[openai-round]: https://openai.com/index/accelerating-the-next-phase-ai/
[amzn-q]: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[softbank]: https://group.softbank/en/news/press/20261001
[azure]: https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/
[goldman]: https://www.goldmansachs.com/insights/articles/can-ai-investment-drive-s-and-p-500-earnings-even-higher
