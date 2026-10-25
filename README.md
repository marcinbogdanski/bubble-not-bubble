# Bubble or Not Bubble

A live research report on the economics of AI: is the current AI boom a bubble
or not? The research and the site are built by AI agents (Claude Code, Codex,
Grok), steered by a human.

- **Live report:** https://bubble.bogdanski.ai
- **Source:** https://github.com/marcinbogdanski/bubble-not-bubble

The report is at version 0.9: a three-part answer with explicit, resolvable
probability forecasts, built on 26 research notes, each with a graded claim
table and sources, every note cross-checked by a second model (sixteen by both vendors), and the report reviewed by three Codex red-teams and a Claude review.

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
- Research notes are written by Claude and Codex agents from primary sources
  (SEC filings, company releases, statistical agencies); Grok scans x.com for
  leads, which are traced to sources before use. Conclusions are red-teamed
  by a different vendor's model. See [AGENTS.md](AGENTS.md).
- Published as a static site on Cloudflare Pages.
- [AGENTS.md](AGENTS.md) holds the operating context for agents working on the
  repo.

## Run locally

```bash
uv sync
uv run fastapi dev main.py    # auto-reload, http://127.0.0.1:8000
```

Endpoints: `/` (report), `/<section>/<page>`, `/raw/...`, `/data/`, `/health`.

The dev server is for local preview only. The public site is a static build.

## Publishing: Cloudflare Pages

`scripts/build_static.py` renders every page from the app into `site/`
(ignored by git), and Wrangler, Cloudflare's CLI, uploads it to Cloudflare
Pages. `npx` fetches the
pinned Wrangler version into npm's cache, so the repo has no npm files.

```bash
uv run python scripts/build_static.py                                   # build site/
npx wrangler@4.152.0 pages deploy site --project-name bubble --branch main  # publish
npx wrangler@4.152.0 pages dev site                                     # optional: preview locally like Pages
```

The build also writes `_headers` (`X-Robots-Tag: noindex` on every file) and
`404.html`. The site is public by design: it stays out of search results, and
`robots.txt` allows all crawlers, including AI bots.

One-time setup in Cloudflare: log in with `npx wrangler@4.152.0 login`, then
create the Pages project
(`npx wrangler@4.152.0 pages project create bubble --production-branch main`, or
Workers & Pages → Create → Pages → Upload assets in the dashboard), then add
`bubble.bogdanski.ai` under the project's **Custom domains**.
