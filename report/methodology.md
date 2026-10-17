# Methodology

*Last updated: 2026-10-17*

## The question, made precise

"Is AI a bubble?" is decomposed into questions that can be wrong:

1. **Overbuild**: is capital being deployed faster than demand that can
   service it will appear? Measured per layer of the stack.
2. **Financing**: who funds the build, with what instrument (cash flow, equity,
   bonds, private credit, vendor financing, off-balance-sheet SPVs), and who
   bears the loss if returns disappoint?
3. **Pricing**: are securities (equity, debt) priced for outcomes that the
   evidence makes unlikely?
4. **Resolution**: concrete, dated events whose probability we estimate and
   later score.

Technology can be real and transformative while the capital deployed to build
it does not all earn a return (railways in the 1840s, fiber in 1999). Both can
be true at once; the report keeps them apart.

## Lenses

- **Mechanism**: Minsky and Kindleberger stages (displacement, boom, euphoria,
  profit-taking, panic); Dalio's bubble indicators (prices high relative to
  fundamentals, prices discounting rapid future appreciation, broad bullish
  sentiment, leverage-financed purchases, forward purchases, new entrants,
  tightening policy); Perez's installation-vs-deployment cycle. Each becomes a
  scored indicator with a stated current reading.
- **History**: the closest precedents, what signalled the top, and how long
  the overbuild took to absorb.
- **Plumbing**: where the debt sits, depreciation assumptions, unit economics
  of inference and training, and whether end-user revenue grows fast enough to
  service the capex.

## Evidence rules

- Every number carries a source, an "as of" date and a type. Nothing is
  stated from model memory.
- **Source types**: *primary* (SEC filings, earnings releases and transcripts,
  company statements, central-bank and statistical-agency data, court
  filings), *secondary* (reporting by named outlets), *tertiary* (aggregators,
  social media, analyst commentary). Secondary and tertiary claims about
  private companies are labelled "reported, unverified".
- **Confidence grades** for a claim:
  - **A**: primary source, directly stated.
  - **B**: reputable secondary source, consistent with primary data, or
    derived from primary data by simple arithmetic.
  - **C**: single secondary source, leak, or estimate; plausible but
    unverified.
  - **D**: tertiary, contested, or contradicted by other sources.
- Conflicting evidence is recorded, not resolved by omission.
- No paywalled sources were available at the time of writing. Coverage of
  public companies is therefore strong; coverage of private labs and
  neoclouds relies on reported figures and is graded accordingly.

## Forecast rules

- Each forecast is a question that resolves yes or no by a stated date,
  from a stated public source.
- Horizons: 6, 12 and 24 months from the forecast date. Error bars at 24
  months are large and are stated as such.
- Each forecast records the probability, the date, the reasoning, and every
  later revision with its cause. Forecasts are scored (Brier) once resolved.
- Per-layer summaries estimate the probability that capital deployed in that
  layer is materially impaired (equity drawdown or debt loss) within the
  horizon.

## Agents

The research is produced by AI agents under a lead agent (Claude), steered by
a human. Claude subagents write research notes; Codex (OpenAI) independently
re-researches contentious notes and reviews conclusions; Grok (xAI) scans
x.com for new information, which is then traced to primary sources before use.
Nothing from a social-media scan is cited as evidence on its own. The lead
agent is an Anthropic model and assesses Anthropic by the same rules as every
other lab; the Codex cross-check is the control for that blind spot.

All agent conversations that built the report are published under
[Claude chats](/claude).
