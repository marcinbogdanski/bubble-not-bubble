# AGENTS.md

Operating context for agents working in this repo. It describes what is
available and the boundaries, not how to do the work. It is not exhaustive:
infer the user's intent and use your judgement.

## Project

- Deep research into the economics of AI ("is it a bubble or not?"),
  published as a live web report (FastAPI, `main.py`).
- It is public at https://bubble.bogdanski.ai as a static site on Cloudflare
  Pages. The user publishes manually (`npm run deploy`, see README), so edits
  are not live until then. `npm run preview` serves the static build locally.
- Source: https://github.com/marcinbogdanski/bubble-not-bubble
- Claude chats for this repo are published on the site (`/claude`). Keep
  secrets out of conversations.

## Repo layout

- `report/`: the published pages (index = the answer, methodology, and the
  synthesis pages). Short, cites research notes.
- `research/`: one markdown note per company, layer or topic, following
  `research/TEMPLATE.md` and the evidence rules in `report/methodology.md`.
  Subfolders: `theory/`, `stack/`, `macro/`.
- `forecasts/`: the forecast register with update history.
- `signals/`: dated log (`YYYY-MM-DD.md`) of new information and what changed.
- `data/`: CSV time series with a `# source:` header line. Served at `/data/`.
- `reviews/`: independent reviews of notes and conclusions by other agents.
- `tasks/`: task status (`tasks.md`) and briefs for subagents.

Every `.md` under `report/`, `research/`, `forecasts/`, `signals/` is a page
on the site, rendered at its path and raw at `/raw/<path>.md`; `/llms.txt`
indexes them for agents.

## Tools

### Agents

All three CLIs are installed. Each has a non-interactive mode:
`grok -p`, `codex exec`, `claude -p`.

- **Grok CLI:** has live x.com access. Good for broad questions like "what is
  the community feedback on X".
- **Codex CLI:** frontier-level agent. Observed to be persistent and
  detail-oriented.
- **Claude CLI:** frontier-level agent. Observed to take a broad view of a
  topic and to have good judgement.

Use subagents generously. Play to each agent's strengths, and especially use
them to double-check work for blind spots.

- **Model choice (Claude):** the account has a 5-hour usage window that a
  wide fan-out on the lead's own model exhausts in under an hour. Tier it:
  Opus for research notes, Sonnet for mechanical work (extraction, link and
  lead verification, formatting), the lead's own model only for synthesis,
  forecasts and red-team reviews. Subagents must not spawn subagents.
- **Model choice (Codex):** no 5-hour window. First-pass research notes on
  the current workhorse (`gpt-6.1-sol`, high reasoning); cross-checks and
  reviews on the frontier model (`gpt-6-astra`). Run with
  `codex exec --skip-git-repo-check -C <repo> -m <model> "<prompt>"` in the
  background, one process per note.
- **Cross-checks:** contentious notes get an independent re-research by a
  different vendor's model, written to `reviews/`. Conclusions get a red-team
  pass by a fresh-context agent asked to break the argument.
- **Grok** output is a lead, never a citation: trace it to a primary source.
- Give each subagent `tasks/RESEARCH_BRIEF.md` (or a similar brief) and an
  explicit output path; it writes only its own files and never commits.
- **Patterns that worked (2026-10-17):** one Codex process per note or
  review, launched with `nohup ... &` and a log in the scratchpad; a
  background shell loop that polls the logs for "tokens used" so the lead is
  woken when a batch finishes; cross-check reviews written to `reviews/` and
  then a separate "apply the review to the note" job, so the reviewer never
  edits and the editor never judges; red-team reviews of the published pages
  after every substantive revision, each in fresh context. Commit by explicit
  path while agents are writing, or half-finished files get swept in.
- **What went wrong:** a 16-agent fan-out on the lead's own model, with
  agents spawning sub-agents, exhausted the Claude usage window in under an
  hour and killed every agent. Pace Claude agents (about six at a time on
  Opus), never let them spawn, and move breadth work to Codex.

### Browser

A full Google Chrome is available. Use it when the built-in search/fetch tools
can't reach part of the web.

- **Preferred:** the Claude and Codex Chrome extensions. Each works in the
  user's real Chrome profile, with their sign-ins. Grok has no extension.
- **Also allowed:** driving Chrome over its debugging port, e.g. with the
  chrome-devtools MCP. Agents may launch their own Chrome instance for this when
  they need it. Keep its profile in a temp folder.

## The VM

The whole VM is cleared for agentic use. The one concern is spill: don't leave
stray files around it.

- **This repo:** this is an agentic repo. Commit whenever you reach a usable
  step. You can work on `master` and/or create worktrees for subagents. Don't
  push: there are no GitHub credentials on this VM.
- **Usage limits:** use agent and model usage as you see fit. There is plenty
  available.
- **Packages:** use `uv` (Python) and `npm` within this repo.
- **Temporary files:** use your own temp folder or `/tmp`.
- **API keys:** some are in `~/.zshrc`, if any.
- **Elsewhere on the VM:** read-only access is fine, e.g. to check the logs of
  tools you use.

In short: work freely in the repo and temp folders, and keep spill onto the
rest of the VM to a minimum.

## Never pause to ask "shall I continue?"

Once a goal and a resource budget have been agreed, carry the work through to
that conclusion. Do not end a turn with "I made a step, shall I make the
next?" questions: the user checks in occasionally and such a question can
idle the project for hours. Pause only for a real problem: a destructive or
irreversible action, a scope change, a blocked dependency the user alone can
unblock, or a resource limit being reached (then back off and resume when it
resets). Pace against limits (check usage, keep a few agents at a time) rather
than stopping.

## Ask the user before

- Installing VM-wide packages.
- Anything that needs `sudo`. You don't have it.
- Creating files outside this folder, other than temp or cache files.
