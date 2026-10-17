# Bubble or Not Bubble

A live research report on the economics of AI: is the current AI boom a bubble
or not? The research and the site are built by AI agents (Claude Code, Codex,
Grok), steered by a human.

- **Live report:** https://bubble.bogdanski.ai
- **Agent chats that built it:** https://bubble.bogdanski.ai/claude (each chat
  is also available as JSON by adding `.json` to its URL)
- **Source:** https://github.com/marcinbogdanski/bubble-not-bubble

The report is at version 0.2: a three-part answer with explicit, resolvable
probability forecasts, built on 25 research notes, each with a graded claim
table and sources, and reviewed by an independent red-team.

## What is where

- `report/`: the published pages. `index.md` is the answer, `theory.md` the
  mechanism and precedents, `stack.md` the layer-by-layer synthesis,
  `methodology.md` the rules.
- `forecasts/register.md`: the forecast register, with resolution rules and
  the history of every revision.
- `research/`: one note per company, layer or topic (`theory/`, `stack/`,
  `macro/`), following `research/TEMPLATE.md`.
- `signals/`: dated log of new information, verified against sources.
- `reviews/`: independent reviews and cross-checks by other agents.
- `data/`: CSV series extracted from primary sources, served at `/data/`.
- `tasks/`: task tracker and the briefs given to agents.

Every markdown page is served rendered at its path and raw at
`/raw/<path>.md`; `/llms.txt` indexes them for agents.

## How it's built

- FastAPI app (`main.py`) with Jinja2 templates (`templates/`);
  `content.py` turns the markdown folders into pages.
- `transcripts.py` publishes this repo's Claude Code chats: user prompts and
  Claude's replies only, without tool calls or subagents.
- Research notes are written by Claude and Codex agents from primary sources
  (SEC filings, company releases, statistical agencies); Grok scans x.com for
  leads, which are traced to sources before use. Conclusions are red-teamed
  by a different vendor's model. See [AGENTS.md](AGENTS.md).
- Served from a VM through a Cloudflare Tunnel. No inbound ports are open.
- [AGENTS.md](AGENTS.md) holds the operating context for agents working on the
  repo.

## Run locally

```bash
uv sync
uv run fastapi dev main.py    # auto-reload, http://127.0.0.1:8000
```

Endpoints: `/` (report), `/claude` (chats), `/health`, `/docs` (API docs).

On the VM the app runs this way in tmux session `bubble`, so saved edits go
live straight away.

## Deployment: Cloudflare Tunnel

The tunnel is remotely managed. Hostnames are configured in the Cloudflare
dashboard, and the VM only runs the `cloudflared` daemon with a token.

1. Cloudflare dashboard → Zero Trust → Networks → Tunnels → **Create a
   tunnel** (Cloudflared). Copy the token; keep it out of git.
2. Add a published application route: `bubble.bogdanski.ai` →
   `http://127.0.0.1:8000`. Cloudflare creates the DNS record.
3. On the VM:

   ```bash
   brew install cloudflared
   sudo cloudflared service install <TUNNEL_TOKEN>   # daemon, starts at boot
   ```

The site is public by design. Every response carries `X-Robots-Tag: noindex`
to stay out of search results, and `robots.txt` allows all crawlers, including
AI bots.
