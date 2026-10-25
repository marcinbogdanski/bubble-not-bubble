# Update playbook (phase 3: ongoing)

How the report is kept current. Not yet automated; run by the lead agent
when the user asks or on a cadence to be agreed.

## Weekly scan (about 30 minutes of agent time)

1. **Lead scan.** `scripts/scan.sh YYYY-MM-DD` runs Grok over x.com and the
   web for the past 7 days (topics listed in the script) and saves the raw
   output to `tasks/grok/YYYY-MM-DD-scan.md`. Grok output is a lead, never a
   citation.
2. **Verification.** The same script then runs Codex (`gpt-6.1-sol`) to trace
   each item to a primary or reputable secondary source and write
   `signals/YYYY-MM-DD.md` (format: see `signals/2026-10-17.md`) plus any new
   rows in `data/credit-spreads.csv`.
3. **Propagation.** The lead agent reads the signals entry's "Implications"
   section and, for each affected note, either edits the claim table directly
   (small, sourced change) or assigns a Codex/Claude agent to update the note.
   Each edited note gets a new "Last updated" date.
4. **Forecast check.** For each register question, check whether anything
   resolved or whether the evidence moved a probability by 5 points or more.
   Append to the register's History with the cause; never overwrite.
5. **Front page.** Update "What we know" figures that changed, bump the
   version, add a line to "Changes".
6. Commit.

## Earnings season (late October, late January, late April, late July)

Microsoft, Alphabet, Amazon, Meta, Oracle (Sept/Dec/Mar/Jun quarters),
Nvidia (late Nov/Feb/May/Aug), TSMC (mid-Jan/Apr/Jul/Oct), ASML, Broadcom,
AMD, CoreWeave, Micron, SK Hynix, Samsung. For each: assign one agent to
update the company note's claim table and CSV from the release, 10-Q and
call transcript, and to list which forecasts (C1-C4, D3, F2) it touches.

## Daily (for P1 and P1b to be scoreable)

- Append the Silicon Data SDH100RT H100 print and the OCPI H100 and B200
  prints to `data/gpu-index-daily.csv` (date, series, value, source URL,
  accessed). Neither publisher keeps a public history; OCPI's API holds a
  rolling three months.
- Run `zsh scripts/archive-gpu-prices.sh` daily to archive OCPI H100, H200,
  B200 and A100 plus the Silicon Data H100 display; it preserves publisher
  dates, skips existing rows and records inaccessible series as `unavailable`.

## Monthly

- TSMC monthly revenue (around the 10th): update `data/tsmc-monthly-revenue.csv`
  and check C4.
- Silicon Data H100 monthly mean and TrendForce DDR5 contract price: record
  in `data/forecast-observations.csv` for P1 and P2.
- FINRA margin debt, Shiller CAPE, FRED spreads: refresh the theory
  checklist readings.

## Review cadence

- Every substantive front-page revision gets a fresh-context red-team by a
  different vendor's model before it is marked a new version.
- Notes written by Claude are cross-checked by Codex and vice versa; the
  cross-check is applied to the note and the note's status set to
  "reviewed".
