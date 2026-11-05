# Briefs for subagents

Paste the section into the agent's prompt with today's date and its file
paths. Common to all: read `report/methodology.md` first; write only the
files named; never run git; never spawn subagents; for SEC requests use a
generic User-Agent (`research-bot contact@example.com`), never a personal
email; no paywalled sources; a social-media post is a lead, not a source.

## Verify a scan (Codex gpt-6.1-sol)

Trace each lead in `work/DATE-scan.md` to a primary or reputable secondary
source. Write `work/DATE-verified.md`: per topic, a table (Item | Figure as
verified | Source link | Type | Grade | Confirmed, partly, or not), then
"Scheduled and not yet released", then "Implications": one row per affected
note or forecast (File or forecast ID | What to change | Source link).
Append dated CDS, bond and yield observations to `data/credit-spreads.csv`.
Drop leads you cannot confirm; do not pad.

## Update a note (Codex gpt-6-astra or Claude Opus, one agent per note)

Inputs: the note, `research/TEMPLATE.md`, and the note's rows in the
Implications table of `work/DATE-verified.md`. For a results season, read
the filing itself (10-Q, release, call) and take figures from it.
Replace, do not append: overwrite the superseded value in its claim row,
update Summary, Analysis and Signals only where the picture changes, and set
"Last updated". Add a row only for a new metric, and cut a weaker row to
stay inside the limits (30 rows, 3,500 words hard). No "updated from",
no "previously", no dated chains of snapshots. Time series go to the note's
CSV in `data/`. A figure owned by another note is linked, not restated.
Report: rows changed, rows added and cut, word count, forecasts touched.

## Write a new note (Claude Opus or Codex gpt-6-astra)

Follow `research/TEMPLATE.md`. Every number comes from a page fetched during
the task, with its link in the claim row. Prefer filings, releases,
transcripts, statistical agencies and central banks; then named outlets.
Private-company figures from leaks are grade C at best and labelled
"reported, unverified". Search for the strongest contradicting evidence and
record it under Open questions. Watch fiscal years, currencies, run-rate
versus trailing, bookings versus revenue, guidance versus actual.

## Forecast check (Claude Opus)

Inputs: `forecasts/register.md`, `data/forecast-observations.csv`. Fetch the
latest close for every named constituent, compute M1, M1a and M1b against
the frozen 2026-10-16 baselines, and state for every question: resolved or
not, distance to trigger, and whether the evidence in `work/DATE-verified.md`
moves it by five points or more, with the reason. Append one observation row
per series to `data/forecast-observations.csv`. Write
`work/DATE-forecast-check.md`. Do not edit the register.

## Review (other vendor than the author, fresh context)

Inputs: the changed pages and the notes they cite. Try to break the
argument: figures that do not match the note or its source, arithmetic,
omissions that change a conclusion, summary lines the evidence does not
support. Write `work/DATE-review-<page>.md` as numbered edits with
replacement text. Do not edit the page. A separate job applies the edits;
the review file is then deleted.
