# Plan: M0 Step 1 — FastAPI Scaffold

## Goal

Stand up a minimal FastAPI backend with a single `/health` endpoint. No database yet, no frontend. The point is to get the project layout right and have a running server we can build on.

---

## Project layout after this step

```
kitchen-assistant/
├── backend/
│   ├── main.py           # FastAPI app entry point
│   └── requirements.txt  # Python dependencies
├── docs/
│   └── plans/
│       └── m0-step1-fastapi-scaffold.md
├── LICENSE
└── README.md
```

---

## Files to create

### `backend/requirements.txt`

```
fastapi>=0.111.0
uvicorn[standard]>=0.29.0
```

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

Dependencies are managed with `uv` to keep the system Python clean.

```bash
cd backend
uv venv          # creates .venv/ inside backend/
uv pip install -r requirements.txt
source .venv/bin/activate
uvicorn main:app --reload
```

- `uv venv` — creates an isolated virtual environment in `backend/.venv/`.
- `uv pip install` — installs into that venv without touching system Python.
- `main:app` — tells uvicorn to look in `main.py` for the object named `app`.
- `--reload` — restarts the server automatically when you save a file. Development only.

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
