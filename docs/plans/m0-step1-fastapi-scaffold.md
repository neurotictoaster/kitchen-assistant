# Plan: M0 Step 1 — FastAPI Scaffold

## Goal

Stand up a minimal FastAPI backend with a single `/health` endpoint. No database yet, no frontend. The point is to get the project layout right and have a running server we can build on.

---

## Project layout after this step

```
kitchen-assistant/
├── backend/
│   ├── main.py           # FastAPI app entry point
│   ├── pyproject.toml    # Project metadata and dependencies
│   └── uv.lock           # Pinned dependency lockfile (committed)
├── docs/
│   └── plans/
│       └── m0-step1-fastapi-scaffold.md
├── LICENSE
└── README.md
```

---

## Files to create

### `backend/pyproject.toml`

```toml
[project]
name = "kitchen-assistant-backend"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.111.0",
    "uvicorn[standard]>=0.29.0",
]
```

- **pyproject.toml** — the standard Python project manifest. `uv` reads dependencies from here rather than a `requirements.txt`.
- **uv.lock** — generated automatically by `uv`; pins every transitive dependency to an exact version. Committed to the repo so installs are reproducible across machines.
- **FastAPI** — the web framework. Chosen for automatic OpenAPI docs, async support, and clean route definitions.
- **uvicorn** — the ASGI server that actually runs FastAPI. The `[standard]` extra adds WebSocket and HTTP/2 support we'll want later.

---

### `backend/main.py`

```python
from fastapi import FastAPI

app = FastAPI(title="Kitchen Assistant")


@app.get("/health")
def health():
    return {"status": "ok"}
```

**What's happening here:**

- `FastAPI()` creates the application instance. `title` shows up in the auto-generated API docs at `/docs`.
- `@app.get("/health")` registers a route that responds to HTTP GET requests at `/health`.
- The function returns a plain dict — FastAPI automatically serializes it to JSON and sets the correct `Content-Type` header.
- No `async` here yet. FastAPI supports both sync and async route functions; sync is fine until we have I/O to await.

---

## How to run it

```bash
cd backend
uv run uvicorn main:app --reload
```

- `uv run` — automatically creates and activates `.venv/`, syncs dependencies from `uv.lock`, then runs the command. No manual `source .venv/bin/activate` needed.
- `main:app` — tells uvicorn to look in `main.py` for the object named `app`.
- `--reload` — restarts the server automatically when you save a file. Development only.

To add a new dependency: `uv add <package>` — updates `pyproject.toml` and regenerates `uv.lock`.

Once running, three URLs are available:
- `http://localhost:8000/health` — the endpoint we built
- `http://localhost:8000/docs` — interactive Swagger UI (free, generated from your code)
- `http://localhost:8000/redoc` — alternative docs UI

---

## How to verify

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

The Swagger UI at `http://localhost:8000/docs` is also worth opening once — it shows every route the API exposes and lets you call them interactively.

---

## What this step does NOT include

- Database (Step 2)
- Frontend (Step 3)
- Environment configuration / `.env` files (Step 2, when we need DB path)
- Any auth or middleware

---

## Branch and PR

- Branch: `feature/m0-step1-fastapi-scaffold`
- Closes: part of #1 (M0)
- Merge after: server runs locally and `/health` returns `{"status": "ok"}`
