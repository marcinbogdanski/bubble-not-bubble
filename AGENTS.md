# AGENTS.md

Operating context for agents working in this repo. It describes what is
available and the boundaries, not how to do the work. It is not exhaustive:
infer the user's intent and use your judgement.

## Project

- Deep research into the economics of AI ("is it a bubble or not?"),
  published as a live web report (FastAPI, `main.py`).
- It is public at https://bubble.bogdanski.ai through a Cloudflare tunnel. The
  dev server runs in tmux session `bubble` with auto-reload, so saved edits go
  live straight away.
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

- **Model choice:** research notes, synthesis and reviews need judgement, so
  run them on the strongest model available (the lead's own model for Claude
  subagents, `gpt-6` at high reasoning for Codex). Cheaper models are for
  mechanical work (extraction, formatting, link checks).
- **Cross-checks:** contentious notes get an independent re-research by a
  different vendor's model, written to `reviews/`. Conclusions get a red-team
  pass by a fresh-context agent asked to break the argument.
- **Grok** output is a lead, never a citation: trace it to a primary source.
- Give each subagent `tasks/RESEARCH_BRIEF.md` (or a similar brief) and an
  explicit output path; it writes only its own files and never commits.

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

## Ask the user before

- Installing VM-wide packages.
- Anything that needs `sudo`. You don't have it.
- Creating files outside this folder, other than temp or cache files.
