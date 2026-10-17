from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Bubble or Not Bubble")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bubble or Not Bubble</title>
</head>
<body style="font-family: system-ui, sans-serif; max-width: 40rem; margin: 3rem auto; padding: 0 1rem;">
  <h1>Hello, world</h1>
  <p>Financial report coming soon.</p>
  <p><small>Rendered at {now}</small></p>
</body>
</html>"""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
