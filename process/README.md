# Process

How the report is kept current. Everything needed to run an update is in
this folder, and it is meant to be read by a human in five minutes.

| File | What it is |
|---|---|
| `README.md` | The rules and the update procedure (this page) |
| `briefs.md` | The prompts given to subagents |
| `scan.sh` | Step 1: Grok lead scan, then Codex verification |
| `archive-gpu-prices.sh` | Appends the day's GPU index prints to `data/gpu-index-daily.csv` |
| `check.py` | Size limits, dead links, data files, front page against register |
| `build_static.py` | Builds `site/` for Cloudflare Pages (see the root README) |

## Rules

1. **Current state only.** An update replaces superseded content; it never
   appends to it. Git holds the history. Prefer too little to too much: a
   lost fact can be re-researched, a bloated repo is slow to clean.
2. **Size limits are hard** and `check.py` enforces them: a note 3,500 words
   (target 2,500, 30 claim rows), a signals entry 400, the front page 1,800,
   all markdown 110,000, `data/` 1.5 MB. Over the limit means cut something.
3. **One home per fact.** A company's figures live in its note; market-wide
   series live in the macro note. Other pages link to the home.
4. **Working files go in `work/`** (ignored by git): scans, verification
   tables, forecast checks, reviews. Empty it when the update is committed.
5. **Kept as history, because the web cannot give it back:** the register's
   History, `data/forecast-observations.csv`, `data/gpu-index-daily.csv` and
   `data/credit-spreads.csv`.
6. **Forecasts** change only on a five-point move in the evidence, with the
   cause logged in the register's History. Vintages are never overwritten.
7. **Reviews** are done by the other vendor in fresh context, applied by a
   separate job, then deleted. The note header records who cross-checked it.

## Update procedure

1. **Scan.** `zsh process/scan.sh SINCE` gives `work/DATE-scan.md` (leads)
   and `work/DATE-verified.md` (checked facts and an Implications table).
2. **Forecast check.** One agent, "Forecast check" brief.
3. **Notes.** One agent per affected note, "Update a note" brief. In results
   season the agent reads the filing itself.
4. **Pages.** The lead updates `report/index.md` (bump the version),
   `report/stack.md`, `report/theory.md` and `forecasts/register.md`.
5. **Changelog.** The lead writes `signals/DATE.md`: what changed, effect on
   forecasts, scheduled next.
6. **Review.** Other-vendor review of the changed pages; apply; delete.
7. **Close.** `zsh process/archive-gpu-prices.sh`, then
   `uv run python process/check.py` must print OK. Empty `work/`. Commit.
   Tell the user: main inputs, changes, which forecasts moved and why.

## Models

- Lead (synthesis, forecasts, pages): Claude Fable.
- Subagents: Claude Opus or Codex `gpt-6-astra` for notes, filings and
  reviews; Codex `gpt-6.1-sol` for verification and mechanical work. Not
  Fable for subagents.
- Grok for the live scan only.
- Codex: `nohup codex exec --skip-git-repo-check -C <repo> -m <model>
  "<prompt>" > <log> 2>&1 &`, one process per job; wait on the process ID,
  not on log text. If a model is at capacity, use the other one.
- Commit by explicit path while agents are still writing.

## Calendar

- **Results:** Microsoft, Alphabet, Amazon, Meta (late Jan, Apr, Jul, Oct);
  Nvidia (late Feb, May, Aug, Nov); Oracle (mid Mar, Jun, Sep, Dec); TSMC
  and ASML (mid Jan, Apr, Jul, Oct); Micron, Broadcom, CoreWeave, AMD, SK
  Hynix, Samsung in between.
- **Monthly:** TSMC revenue (about the 10th); Silicon Data H100 monthly mean
  and DDR5 contract price into `data/forecast-observations.csv`.
- **Daily, when someone is running:** `archive-gpu-prices.sh` (publishers
  keep no public history).
