# ExpiryGuard Rx

ExpiryGuard Rx is a **Python + FastAPI** project intended to support batch-level pharmacy inventory operations with stronger expiry-loss controls.

> Current repository status: this version provides a production-ready project foundation (API skeleton, health check, secure configuration templates, and tests). Domain modules such as FEFO dispensing, forecasting, and supplier return workflows are not implemented yet.

## Problem Statement
Pharmacies often track stock at product level instead of batch level, which can lead to:
- avoidable expiry losses,
- weak FEFO (First-Expiry-First-Out) discipline,
- delayed risk visibility,
- and poor return/replenishment timing.

ExpiryGuard Rx is designed to evolve into a cloud-ready system that addresses those gaps with accurate, auditable batch-level workflows.

## Implemented Features (Current)
- FastAPI application entry point (`app/main.py`)
- Health endpoint: `GET /health`
- Pinned Python dependencies (`requirements.txt`)
- Basic pytest coverage for API readiness (`tests/test_health.py`)
- Safe environment template with placeholders (`.env.example`)
- Hardened `.gitignore` defaults for Python and local secrets

## Planned Features (Not Yet Implemented)
- Batch-level stock CRUD and movement tracking
- FEFO dispensing suggestions/enforcement
- Expiry-risk alerts and notification workflows
- Supplier return recommendation engine
- Forecasting and analytics reports
- Optional Azure integrations (Blob Storage, Key Vault, etc.)

## Architecture (Current)
- **API Layer:** FastAPI app with route registration in `app/main.py`
- **Health/Readiness:** `GET /health` for deployment checks
- **Test Layer:** pytest + FastAPI TestClient smoke test

## Technology Stack
- Python 3.11+
- FastAPI
- Uvicorn
- Pytest

## Repository Structure
```text
ExpiryGuard-Rx/
├── app/
│   └── main.py
├── tests/
│   └── test_health.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Local Setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy environment template:
   ```bash
   cp .env.example .env
   ```
5. Replace placeholder values in `.env` with your local settings.

## Run the API
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Health check:
```bash
curl http://127.0.0.1:8000/health
```

## Environment Variables
| Variable | Required | Purpose |
|---|---|---|
| `APP_ENV` | No | Runtime mode (e.g., development/production) |
| `DATABASE_URL` | Future | Placeholder DSN for upcoming persistence layer |
| `AZURE_STORAGE_CONNECTION_STRING` | Optional/Future | Placeholder for optional Azure storage integration |
| `AZURE_KEY_VAULT_URL` | Optional/Future | Placeholder for optional Azure Key Vault integration |

## Testing
Run tests with:
```bash
pytest -q
```

Current tests validate API startup and health endpoint behavior.

## Deployment Notes
### Current deployable scope
- The API can be deployed as a basic FastAPI service using `uvicorn app.main:app`.
- No database migrations or external service dependencies are required for the current code.

### Production considerations for future modules
When domain modules are added, production deployment should also define:
- managed database provisioning and migration strategy,
- secret management (e.g., Azure Key Vault),
- structured logging and monitoring,
- authentication/authorization policy,
- backup/retention and compliance controls.

## Troubleshooting
- **`ModuleNotFoundError` for FastAPI/Uvicorn**: reinstall with `pip install -r requirements.txt`.
- **`pytest` command missing**: ensure your virtual environment is active and dependencies are installed.
- **`/health` unreachable**: verify the server is running and port `8000` is not blocked/in use.

## GitHub Presentation Suggestions
- **Repository description:** `Batch-level pharmacy inventory foundation with FastAPI, focused on expiry-loss prevention workflows.`
- **Suggested topics:** `fastapi`, `python`, `pharmacy`, `inventory-management`, `expiry-tracking`, `fefo`, `healthcare-software`
- **Suggested future sections/assets:**
  - architecture diagram (`docs/architecture/`),
  - UI/API screenshots (`docs/screenshots/`),
  - milestone roadmap (issues/projects),
  - risk/compliance notes for healthcare data handling.

## Screenshots
No screenshots are included yet. Add real screenshots only after UI/API flows are implemented and testable.

## License
Licensed under the MIT License (see `LICENSE`).
