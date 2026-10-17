# bubble-not-bubble

Small live web financial report (FastAPI).

## Run locally

```bash
uv sync
uv run fastapi dev main.py          # dev, auto-reload, http://127.0.0.1:8000
uv run fastapi run main.py --host 127.0.0.1 --port 8000   # production-style
```

Endpoints: `/` (report page), `/health` (JSON health check), `/docs` (API docs).

## Expose via Cloudflare Tunnel

The app binds to `127.0.0.1` only; `cloudflared` makes an outbound connection to
Cloudflare, so no ports need to be opened on your router.

```bash
brew install cloudflared
```

### Quick test (no account, random URL)

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```

Prints a `https://<random>.trycloudflare.com` URL. Good for testing only.

### Permanent tunnel on your own domain

Requires a domain whose DNS is managed by Cloudflare (`example.com` below).

```bash
cloudflared tunnel login                      # authorize in browser, pick the zone
cloudflared tunnel create bubble              # creates ~/.cloudflared/<UUID>.json
cloudflared tunnel route dns bubble report.example.com
```

`~/.cloudflared/config.yml`:

```yaml
tunnel: bubble
credentials-file: /Users/<you>/.cloudflared/<UUID>.json

ingress:
  - hostname: report.example.com
    service: http://127.0.0.1:8000
  - service: http_status:404
```

```bash
cloudflared tunnel run bubble                 # foreground
cloudflared service install                   # or: start at login (LaunchAgent)
```

To restrict who can see the report, add a Cloudflare Access application for
`report.example.com` (Zero Trust dashboard → Access → Applications).
