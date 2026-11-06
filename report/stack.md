# The stack, layer by layer

*Version 0.10.1, 2026-11-06 · Synthesis of the research notes. Every figure
is sourced and graded in the note it links to. Each note was cross-checked by a second vendor's model when written; note headers show which later updates were checked.*

## One table

The [forecast register](/forecasts/register) defines impairment for each
layer. Listed-equity tests use a 40% decline from the 16 October close,
not from a peak; credit tests require a distressed event, not a falling
bond price ([public-markets](/research/macro/public-markets)).

| Layer | Profitable now? | How the build is financed | Where it is overextended | Who loses first | First signal |
|---|---|---|---|---|---|
| Equipment (ASML, AMAT, Lam, KLA, TEL) | Yes: ASML 44.4% operating margin; KLA 61.9% gross, $1.3B quarterly FCF ([equipment](/research/stack/semiconductor-equipment)) | Operating cash, customer advances and some borrowing; ASML, AMAT and Lam have cash cushions, KLA modest net debt | Concentrated customers and cancellable backlog; ASML expects planned 2027–28 output below demand. China exposure includes ASML's ~20% annual guide and Lam's 35% latest-quarter sales, with different denominators ([equipment](/research/stack/semiconductor-equipment)) | Shareholders through weaker orders and multiples; cash generation cushions creditors | Deposits, cancellations and capex guides; KLA guides December revenue to $4.7B ±$0.2B ([equipment](/research/stack/semiconductor-equipment)) |
| Foundry (TSMC) | Yes: 66.4% gross, 58.7% operating margin ([foundry](/research/stack/tsmc-and-foundry)) | Operating cash covers investment and dividends; annual capex guide $60–64B ([foundry](/research/stack/tsmc-and-foundry)) | New spending mainly supplies 2028–29; capacity deposits fell 34.8% in 2025 and customers generally do not order far ahead. AI demand exceeds supply, but management remains prudent on consumer demand and 2027 ([foundry](/research/stack/tsmc-and-foundry)) | Shareholders through utilisation of fixed-cost factories; Taiwan remains a separate supply risk | Monthly revenue, capex revisions, loading and deposits |
| Memory and HBM | Yes: Micron 86.8% gross / 80.7% operating; SK Hynix 80% operating; Samsung's broader DS segment 72%, not Memory alone ([memory](/research/stack/memory-hbm)) | Cash generation, equity and subsidies. Micron's 26 take-or-pay agreements cover >35% of estimated revenue through 2030; SK Hynix has >50% of 2027–28 capacity under price-band agreements; Samsung has signed 10 major accounts ([memory](/research/stack/memory-hbm)) | Scarcity supports earnings, but future capacity, yield gains and customer retrenchment threaten normalised returns. Korean shareholder-return plans compete with investment; contract protection differs by supplier | Shareholders first; contracted customers may lose deposits | Fixed DDR5 contract series, inventories, qualified output, cancellations and actual collections |
| Accelerators (Nvidia, AMD, Broadcom) | Nvidia 75% gross margin, $126.9B trailing FCF ([Nvidia](/research/stack/nvidia)); AMD Q3 Data Center revenue $8.5B, group FCF $0.554B; Broadcom 46% FCF margin ([custom silicon](/research/stack/amd-broadcom-custom-silicon)) | Own cash and vendor support: Nvidia's conditional OpenAI lease guarantee capped at $105B; $99B equity holdings and $63.1B receivables ([Nvidia](/research/stack/nvidia)). Broadcom backs up to $43B of an Anthropic financing vehicle; its separate conditional note facility is up to $42B, with overlap unresolved ([custom silicon](/research/stack/amd-broadcom-custom-silicon)) | Concentrated buyers; procurement commitments and guarantees survive weaker demand. AMD's customer warrants produced a $1.2B noncash charge; $4.5B grant-date value remains to reduce qualifying revenue ([custom silicon](/research/stack/amd-broadcom-custom-silicon)) | Shareholders; vendors through receivables and guarantees after recoveries | Collections, margins and support draws; AMD guides Q4 revenue to $17B ±3% ([custom silicon](/research/stack/amd-broadcom-custom-silicon)) |
| Hyperscalers (MSFT, GOOGL, AMZN, META) | Core businesses profitable; Azure +48%, Google Cloud +103% including TPU systems, AWS +39% ([Microsoft](/research/stack/microsoft), [Alphabet](/research/stack/alphabet), [Amazon](/research/stack/amazon)) | September-quarter Microsoft FCF $18.6B, down 27%; $25B general-purpose notes issued: $23B fixed, $2B floating. Alphabet Q3 FCF −$9.1B; nine-month equity $61.9B and net debt proceeds $76.3B. Amazon trailing FCF −$42.4B; nine-month gross long-term-debt proceeds $115.1B and up to approximately $80B of undrawn secured supplier borrowing capacity, drawable at its discretion from 2027 ([Microsoft](/research/stack/microsoft), [Alphabet](/research/stack/alphabet), [Amazon](/research/stack/amazon)). Meta Q3 FCF −$2.1B; preferred and notes supplement operations, while forward equity brings no initial cash ([Meta](/research/stack/meta)) | Microsoft uncommenced leases $364.6B, partly conditional; OpenAI-related quarterly revenue $10.0B, 10.8% of total, includes revenue share and does not establish collection ([Microsoft](/research/stack/microsoft)). Alphabet datacenter/energy backstops $48.0B executed plus $27.7B promised: $75.7B contingent maxima, including Crux, not expected losses ([Alphabet](/research/stack/alphabet)); Amazon's Anthropic stake carries at $238.7B, 38.9% of book equity ([Amazon](/research/stack/amazon)) | Shareholders through dilution, depreciation and investment marks; diversified operating earnings cushion creditors | Cash conversion, lease commencements, customer collections and funding costs |
| Oracle | Q1 FY2027 GAAP operating income $6.7B, software and GPU profit not separated; FY2026 FCF −$23.7B; Q1 FY2027 −$5.4B despite $11.4B significant-financing-component customer advances in operating cash ([Oracle](/research/stack/oracle)) | Investor Day capped further market funding through FY2030 at $20B, excluding refinancing; fully raised as $10B gross equity plus $10B notes at 7.0–8.65% coupons. Borrowings $135.3B pro forma carrying value; $43.8B discounted lease liabilities and $288B undiscounted uncommenced lease commitments are separate ([Oracle](/research/stack/oracle)) | Roughly $220B self-funded-equivalent build depends on about $110B vendor/customer offsets and $90B other cash flows net of other needs, inferred from the slides, grade C. S&P BBB− stable; $664B RPO is not cash ([Oracle](/research/stack/oracle)) | Shareholders, then unsecured parent creditors, who rank behind $107.2B of subsidiary liabilities; new-note Treasury spreads exceeded the BB index OAS, with unmatched durations and conventions. Construction lenders separately bear delays | Quarterly offsets and leverage; latest reported CDS 274.4bp on 28 October (C), no verified 5 November mark; Jupiter application dismissal denied, hearing 7 December ([Oracle](/research/stack/oracle)) |
| Neoclouds (CoreWeave and others) | CoreWeave not GAAP-profitable: Q2 net interest 24.9% of revenue, adjusted EBITDA margin 59% ([CoreWeave](/research/stack/coreweave)); other operators mix profitable facilities with group losses | GPU-backed loans, unsecured notes, converts, equity and prepayments. CoreWeave June debt principal $35.6B; illustrative $42.2B with identified later borrowing, before repayments ([CoreWeave](/research/stack/coreweave)); no comparable current layer total ([other neoclouds](/research/stack/neoclouds-other)) | CoreWeave H1 operating cash $3.7B versus $14.1B equipment purchases and $5.2B principal repayments; DDTL 5.5 lends five years against contracts averaging three ([CoreWeave](/research/stack/coreweave)) | Equity first; secured lenders depend on collateral and borrower recourse, unsecured creditors rank behind them; Nvidia's capacity purchase is no debt guarantee | 5 November CoreWeave CDS reported as high as 1,268bp; 2032 bonds as low as 74.75 cents, Treasury spread touching 1,200bp (reported marks, C); shares $43.66 ([register](/forecasts/register), [CoreWeave](/research/stack/coreweave)); CIFR is 2.9% and CRWV 15.6% from their 40% triggers ([observations](/data/forecast-observations.csv)) |
| Frontier labs (OpenAI, Anthropic, xAI) | OpenAI profitability unestablished; 2026 burn forecast $25B, reported, unverified ([OpenAI](/research/stack/openai)). Anthropic Q3 GAAP operating loss $0.567B, adjusted profit $2.5B at 15% margin ([Anthropic](/research/stack/anthropic)). SpaceX SI operating profit $0.431B, including infrastructure and Cursor ([other labs](/research/stack/labs-other)) | Investor and supplier equity, conditional facilities and equipment finance. Anthropic has $131.8B cash/investments and $77B undrawn conditional partner facilities ([Anthropic](/research/stack/anthropic)). SpaceX related-party equipment finance $12.9B; conditional Apollo lease commitment ~$40B, not funded debt ([other labs](/research/stack/labs-other)) | Anthropic filed commitments $895.4B: $69.8B expected within twelve months after September, $447.5B before end-2030; $213.8B terminable or conditional ([Anthropic](/research/stack/anthropic)). OpenAI's four quantified cloud contracts total ~$710.4B, ~14× its reported run-rate (C), against Anthropic's ~13× annualised Q3 revenue; its February burn plan needs more funding during 2028 even if its $122B round is fully funded ([OpenAI](/research/stack/openai)) | Investors first; suppliers through receivables, idle capacity and contingent support | Filed cash flows, funding receipts, binding amendments and IPO pricing |
| Neolabs and applications | Sustainable independent-lab profitability largely unestablished | Venture and strategic equity; some infrastructure debt | Selected rounds total $31B, 59% for Prometheus; not a low-revenue census. Cursor's $60B stock acquisition closed; World Labs' $8.2B sale remains an agreement ([other labs](/research/stack/labs-other)) | Venture investors; new, uncommitted capacity orders are cut first, an inference from limited cases | Down rounds, closures, acquisitions and paid renewals |
| Power and datacenter real estate | Equipment and established colocation profitable: Vertiv 22.8% operating margin, GE Vernova Power 21.4% EBITDA margin, Equinix 51.4% adjusted EBITDA margin ([power](/research/macro/power-and-datacenters)) | Project bonds, private credit, REIT balance sheets and utility rate bases; Meta's conditional residual guarantees link campus creditors to tenant credit ([Meta](/research/stack/meta)) | Grid and permits constrain delivery. After the 3 November vote, Democrats were called winners of both chambers; 40 of 41 local contests opposed development, mixing binding and advisory votes. Incoming Texas governor proposes an approvals moratorium and tax-break removal; Ohio supports a conditional moratorium requiring operators to cover utility costs and use union labour; Georgia proposes a construction pause. None of these incoming statewide positions is law yet; Texas's existing administrative permit halt is separate ([power](/research/macro/power-and-datacenters)) | Marginal developers and construction lenders first if approvals delay rent; guarantees can transfer losses to tenants, while operating sites may gain scarcity value | Enacted rules, exemptions, energisation, rent commencement and project-credit terms |

## The shape of it

Profitable suppliers sell into a build increasingly funded by outside
capital. Strong margins do not establish the buyers' returns. The
hyperscalers retain large operating businesses, but negative cash flow,
new borrowing and equity issuance make market access part of the build's
funding model. Microsoft's delivery-related capex trim also shows that
supplier execution can constrain spending despite strong demand
([Microsoft](/research/stack/microsoft), [Alphabet](/research/stack/alphabet),
[Amazon](/research/stack/amazon), [Meta](/research/stack/meta)).
Amazon's supplier-loan principal will be classified as debt repayments,
outside its reported FCF measures ([Amazon](/research/stack/amazon)).

The labs differ sharply in disclosure. Anthropic has audited annual
accounts and unaudited interim accounts: revenue was $4.6B in 2025,
$33.2B in nine months of 2026 and $17.0B in Q3. Annualising Q3 gives
$67.8B, not reported ARR. Nine-month operating cash was $6.6B; much
customer spending lacks long commitments, while infrastructure payments
extend far ahead. OpenAI's roughly $50B net run-rate and proposed $20B
raise remain reported, unverified; neither supplies a filed cash-flow
bridge ([Anthropic](/research/stack/anthropic),
[OpenAI](/research/stack/openai)).

Supplier support links these funding risks. Broadcom's $63B Anthropic
vehicle has committed financing, with deliveries expected from 2027;
its backstop and conditional rent-financing notes may overlap and should not be added. Guarantees transfer covered losses;
conditional facilities may become unavailable when customers weaken.
The [circular-financing note](/research/macro/circular-financing) maps
these channels without establishing how much demand would disappear
without them. Gross supplier sales also cannot be added into
[end-user demand](/research/macro/demand-side).

Political constraints can bring losses forward for developers and
construction lenders: permits delay revenue while interest and equipment
costs continue. The election positions still require implementation,
and local votes differ in legal effect. Existing powered sites could
benefit from slower additions. CoreWeave management expects existing
commitments and backlog to be unaffected; this is a counterargument,
not assurance of timely delivery ([power](/research/macro/power-and-datacenters),
[CoreWeave](/research/stack/coreweave)).

The 5 November sell-off already imposed equity losses: Nasdaq-100
26,629.81, down 6.36% that day; the AI basket 82.26 against 100 on
16 October, down 12.00% that day. From their 2026 closing peaks,
Oracle is down 53.59%, CoreWeave 68.36%, Vertiv 53.03% and Broadcom
39.46%; from the 16 October origin they are down 10.2%, 28.9%, 14.4% and 11.3% ([observations](/data/forecast-observations.csv)). Peak losses do not resolve the frozen-origin forecasts
([public-markets](/research/macro/public-markets)). No qualifying credit
event is established in the notes. Construction and weaker GPU credit
remain the likelier sources of first realised credit losses; completed
corporate raises argue against a general funding shutdown. Credit took
part: CoreWeave's CDS was reported as high as 1,268bp, and broad corporate
risk gauges reportedly had their worst day in nearly eight months
(grade C). Index spread prints for 5 November are not yet published
([register](/forecasts/register)).

## Near-term cash risk, by name

**[CoreWeave](/research/stack/coreweave):** June's schedule has $6.2B
principal due in 2027. Restricted equity cures remain available; the
first DDTL 3.0 debt-service test is in October 2027. Adjusted EBITDA
covers net interest 2.36x, not principal. Management cites renewals and
initial-term debt recovery, but cohort cash flows are undisclosed and
June disclosure controls were ineffective. Q3 results are due
10 November.

**[Oracle](/research/stack/oracle):** Preserving opening FY2027 liquidity
requires $42.343B in the central scenario, against about $39.735B net
raised, including $19.826B net in November. Conditional May 2027 ending
cash/securities are $29.29B (range $25.29–32.29B), about $2.61B below the
opening balance. This supports near-term funding under the note's
assumptions, not a guarantee against quarterly shortfalls. The $10B
revolver is conditional; the $19.7B combined revolver/commercial-paper
capacity is not an independent committed cash buffer. Beyond leases, $34.15B unconditional
purchase/other commitments may overlap forecast spending. The annual
filing disclosed a guarantee up to $3.3B of a lessor borrowing maturing
September 2026; its subsequent status is unverified. These are not
amounts to add mechanically to debt or capex. Management targets positive
FCF in H2 FY2028 and at least $30B in FY2029. Vendor principal sits in
financing cash flow, so positive FCF need not mean obligations stop growing.

**[Meta](/research/stack/meta):** $355.7B uncommenced leases and $121.4B
commitments due in 2027 limit flexibility; obligation categories should
not be added together. It raised $14.4B gross of mandatory convertible
preferred at 6.50%, about $14.32B net, arranged a $25B stock forward
with no initial issuer proceeds from that forward, and priced $15B dollar notes for
5 November settlement plus €9B notes for 12 November. Preferred and dollar
notes imply pro forma cash/securities of $111.7B against $99.0B corporate-note
face principal, excluding lease liabilities, euro notes, Q4 cash flow and
forward proceeds. A separate $25B New Mexico civil penalty carries 15%
post-judgment interest; Meta intends to appeal and may need a bond or
collateral, with the requirement unquantified. S&P affirmed
AA− with a negative outlook; Hyperion and El Paso notes also have negative
outlooks. Profitable advertising and reported AI-driven ad gains provide
the operating cushion.

**[Anthropic](/research/stack/anthropic):** Cash and positive operating
cash flow provide a buffer, but management expects significant future
cash use. Its $213.8B conditional or terminable commitments are not all
freely cancellable; lease rent can start before usable compute. Q3
included $5.0B of expensive short-term compute, evidence of a capacity
gap. The filing also flags revenue quality: an estimated 5–7% of nine-month revenue came from customers later found in breach of policy, the top five supply about 25%, and management expects growth to slow. $161.2B of Broadcom lease rent is non-cancellable, cross-defaults link commercial and financing failure, and the D.C. Circuit upheld a supply-chain-risk designation. A $5B quarter-end liquidity floor applies from Q4. Broadcom rent-financing notes, none yet issued, carry 9% PIK interest and conversion at 90% of trailing 30-day VWAP; failed revenue conditions worsen those terms to 13% and 85%. Sustained growth, liquidity or lease-performance failures can end access; on liquidation or change of control, holders may elect cash equal to 150% of principal and accrued interest or conversion ([claims 11, 18](/research/stack/anthropic)). The IPO is filed and unpriced.

**[Other neoclouds](/research/stack/neoclouds-other):** IREN has $9.9B
carrying borrowings before finance leases and still targets $6B of
market-dependent funding for its broader capex plan; its smaller
contracted program includes conditional facilities and unreceived
prepayments. Cipher has $2.2B restricted within $2.9B total cash and
negative adjusted EBITDA. Closed IREN equipment refinancing and signed
Google support for TeraWulf counter a blanket funding-freeze claim;
support is not the same as funded debt.

## Layer notes

- **Equipment**: [semiconductor-equipment](/research/stack/semiconductor-equipment).
- **Foundry**: [tsmc-and-foundry](/research/stack/tsmc-and-foundry).
- **Accelerators**: [nvidia](/research/stack/nvidia),
  [amd-broadcom-custom-silicon](/research/stack/amd-broadcom-custom-silicon).
- **Hyperscalers**: [microsoft](/research/stack/microsoft),
  [amazon](/research/stack/amazon), [meta](/research/stack/meta),
  [alphabet](/research/stack/alphabet).
- **Oracle**: [oracle](/research/stack/oracle).
- **Neoclouds**: [coreweave](/research/stack/coreweave),
  [neoclouds-other](/research/stack/neoclouds-other).
- **Labs**: [openai](/research/stack/openai),
  [anthropic](/research/stack/anthropic), [labs-other](/research/stack/labs-other).
- **Memory**: [memory-hbm](/research/stack/memory-hbm).
- **Compute market**: [gpu-pricing-and-utilization](/research/macro/gpu-pricing-and-utilization):
  October OCPI averages were $2.94/H100-hour and $8.50/B200-hour;
  prices do not measure utilisation, and public indices cannot be spliced.
- **Cross-cutting**: [debt-markets](/research/macro/debt-markets) maps
  $563.7B corporate principal at five issuers and $654.5B including
  CoreWeave and selected project securities; mixed dates, legacy debt,
  later issues excluded and overlap with the neocloud layer.
  [Circular-financing](/research/macro/circular-financing),
  [demand-side](/research/macro/demand-side),
  [public-markets](/research/macro/public-markets),
  [power-and-datacenters](/research/macro/power-and-datacenters),
  [rates-sovereign-geopolitics](/research/macro/rates-sovereign-geopolitics)
  and [china](/research/macro/china) cover financing links, end-user
  returns, market prices, deployment constraints and competition.
