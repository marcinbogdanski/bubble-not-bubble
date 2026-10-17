# AGENTS.md

Operating context for agents working in this repo. It describes what is
available and the boundaries, not how to do the work. It is not exhaustive:
infer the user's intent and use your judgement.

## Project

- A small live web financial report (FastAPI, `main.py`).
- It is public at https://bubble.bogdanski.ai through a Cloudflare tunnel. The
  dev server runs in tmux session `bubble` with auto-reload, so saved edits go
  live straight away.
- Claude chats for this repo are published on the site (`/claude`). Keep
  secrets out of conversations.

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
  step. You can work on `master` and/or create worktrees for subagents.
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
