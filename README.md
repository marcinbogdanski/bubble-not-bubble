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
Cloudflare, so no ports need to be opened on your router. The tunnel is
remotely managed: it is configured in the Cloudflare dashboard and the local
daemon just runs with a token (same setup as the P15 / Beast Linux boxes).

### 1. Create the tunnel in the dashboard

Requires a domain whose DNS is managed by Cloudflare (`example.com` below).

1. Cloudflare dashboard → Zero Trust → Networks → Tunnels → **Create a tunnel**.
2. Connector type **Cloudflared**, name it (e.g. `bubble`), save.
3. Copy the token from the install command shown (the long string after
   `service install`). Keep it secret and out of git.
4. Add a public hostname (published application route):
   subdomain `report`, domain `example.com`, service type `HTTP`,
   URL `127.0.0.1:8000`. Cloudflare creates the DNS record for you.

### 2. Install and run the connector

```bash
brew install cloudflared                      # macOS
cloudflared tunnel run --token <TUNNEL_TOKEN> # run once in foreground to test
sudo cloudflared service install <TUNNEL_TOKEN>   # install as daemon, starts at boot
```

On Debian/Ubuntu install from Cloudflare's apt repo (`pkg.cloudflare.com`) and
manage the daemon with `systemctl {is-active,disable --now,enable --now} cloudflared`.
On macOS remove the daemon with `sudo cloudflared service uninstall`.

The app itself must be running (`uv run fastapi run main.py --host 127.0.0.1 --port 8000`)
for `https://report.example.com` to respond. Further changes to hostnames or
routing are made in the dashboard; no local config file is needed.

### Quick test without a domain

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```

Prints a random `https://<random>.trycloudflare.com` URL. Testing only.

### Restricting access

To restrict who can see the report, add a Cloudflare Access application for
`report.example.com` (Zero Trust → Access → Applications), e.g. allowing only
your email address.
