# AGENTS.md

Operating context for agents working in this repo: what is available and
where the boundaries are. It is not exhaustive: infer the user's intent and
use your judgement. How an update is run is in `process/README.md`.

## Project

- Deep research into the economics of AI ("is it a bubble or not?"),
  published as a web report.
- Public at https://bubble.bogdanski.ai as a static site on Cloudflare
  Pages. The user builds and publishes manually (see README), so edits are
  not live until then. Do not publish.
- Source: https://github.com/marcinbogdanski/bubble-not-bubble
- Agent session logs (e.g. `~/.claude`) are private: never publish them or
  copy them into the repo.

## Repo layout

- `report/`: the published pages (index = the answer, theory, stack,
  methodology). Short; they cite research notes.
- `forecasts/`: the forecast register with its revision history.
- `research/`: one note per company, layer or topic, following
  `research/TEMPLATE.md`. Subfolders: `theory/`, `stack/`, `macro/`.
- `signals/`: one short changelog entry per update.
- `data/`: CSV series, each with a `# source:` header line. Served at `/data/`.
- `process/`: the update procedure, agent briefs and scripts.
- `work/`: scratch for the current update. Ignored by git; emptied after.

Every `.md` under `report/`, `research/`, `forecasts/`, `signals/` is a page
on the site, rendered at its path and raw at `/raw/<path>.md`; `/llms.txt`
indexes them. Nothing else is published, so do not link to other folders
from a page.

## Keep the repo small

Accumulation is the main enemy. Agents can generate millions of tokens, and
the instinct to keep everything as evidence is wrong here.

- Notes and pages hold the current state. An update replaces; it does not
  append. Git holds the history.
- Delete what has served its purpose: scans, verification tables and
  reviews live in `work/` and go when the update is committed.
- Prefer too little to too much. Lost information can be re-researched.
- The exceptions, which cannot be recovered from the web, are listed in
  `process/README.md`.
- `uv run python process/check.py` enforces size limits and link integrity.
  It must pass before a commit. Do not raise a limit to make it pass.

## Tools

All three CLIs are installed, each with a non-interactive mode: `grok -p`,
`codex exec`, `claude -p`.

- **Grok:** live x.com access. Good for "what is being said about X". Its
  output is a lead, never a citation.
- **Codex:** persistent and detail-oriented. `gpt-6-astra` for notes,
  filings and reviews; `gpt-6.1-sol` for verification and mechanical work.
- **Claude:** broad view and good judgement. Opus for subagents; the lead's
  own model (Fable) for synthesis, forecasts and the pages only.

Neither subscription has a short usage window now, so agents can run in
parallel. Use them generously and use one vendor to check the other.
Subagents never spawn subagents, never run git, and write only the files
they are given.

A full Google Chrome is available when search and fetch tools cannot reach a
page: prefer the Claude or Codex Chrome extension (the user's real profile),
or drive a separate instance over the debugging port with its profile in a
temp folder.

## The VM

The whole VM is cleared for agentic use. The one concern is spill.

- **This repo:** commit whenever you reach a usable step, by explicit path
  while agents are writing. Don't push: there are no GitHub credentials here.
- **Packages:** `uv` within this repo.
- **Temporary files:** `work/`, your own temp folder, or `/tmp`.
- **API keys:** some are in `~/.zshrc`, if any.
- **Elsewhere on the VM:** read-only is fine, e.g. to check tool logs.

## Never pause to ask "shall I continue?"

Once a goal has been agreed, carry the work through to it. Do not end a turn
with "I made a step, shall I make the next?": the user checks in
occasionally and such a question can idle the project for hours. Pause only
for a real problem: a destructive or irreversible action, a scope change, or
a dependency only the user can unblock.

## Ask the user before

- Installing VM-wide packages.
- Anything that needs `sudo`. You don't have it.
- Creating files outside this folder, other than temp or cache files.
