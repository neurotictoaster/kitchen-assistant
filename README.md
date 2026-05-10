# Kitchen Assistant

> 🚧 Early Development

A personal kitchen management app that tracks pantry inventory, suggests recipes based on what's on hand, minimizes food waste, generates smart shopping lists, and provides real-time cooking assistance.

Built in spare time as a solo project.

---

## Overview

Kitchen Assistant is a personal tool for managing what's in the kitchen and making the most of it. The core idea: stop throwing away food, stop buying duplicates at the store, and get useful recipe suggestions based on what you actually have.

## Planned Features

- **Pantry tracking** — add items manually, by photo of a receipt, or by syncing grocery order confirmation emails
- **Expiration awareness** — visual warnings for items expiring soon, surfaced on the dashboard
- **Recipe suggestions** — ranked by how many ingredients you already have on hand
- **AI recipe generation** — generate recipes from pantry contents, respecting dietary preferences and prioritizing items about to expire
- **Smart shopping lists** — auto-generated from selected recipes, filtered to only what you're missing
- **Waste reduction** — patterns analysis to flag items you consistently over-buy

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Database | SQLite |
| Frontend | React |
| AI | AWS Bedrock (Claude) |

## Getting Started

**Prerequisites:** Python 3.13+, [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
cd backend
uv venv
source .venv/bin/activate
uv pip install -e .
uvicorn main:app --reload
```

API is available at `http://localhost:8000`. Health check: `curl http://localhost:8000/health`

Interactive API docs: `http://localhost:8000/docs`

## Milestone Progress

| Milestone | Status | Branch | What it adds |
|---|---|---|---|
| M0: Scaffold + pantry data model | Complete | `feature/m0-step1-fastapi-scaffold` | FastAPI `/health`, SQLite `pantry_items` table, `get_db()` factory, single-page add/list UI |
| M1a: Natural language pantry entry | Not started | — | Type "2 lbs ground beef" → Claude parses and saves it |
| M1b: Receipt OCR | Not started | — | Photo of a receipt → line items extracted |
| M1c: Email sync | Not started | — | Grocery order confirmation emails → pantry update |
| M2: Expiration tracking | Not started | — | Categories, quantity adjustment, expiry warnings |
| M3: Recipe suggestions | Not started | — | Recipe storage, pantry-aware ranking |
| M4: AI recipe generation | Not started | — | Generate recipes from pantry, respects dietary prefs |
| M5: Shopping lists + waste reduction | Not started | — | Auto shopping lists, over-buy pattern analysis |

### Resuming after a break

1. Check this table for where things left off.
2. The open GitHub issue for the current milestone has the acceptance criteria and "Done When" definition.
3. Start the backend with the commands above and verify `/health` returns `{"status": "ok"}` before doing anything else.

## Roadmap

See [Issues](../../issues) for full milestone details.

## License

Copyright 2026 James Beatty. See [LICENSE](./LICENSE) for terms.
