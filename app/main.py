from fastapi import FastAPI

app = FastAPI(
    title="ExpiryGuard Rx",
    description=(
        "Cloud-based batch-level inventory and expiry-loss prevention system "
        "for pharmacy workflows."
    ),
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Simple readiness endpoint for local/dev deployment checks."""
    return {"status": "ok"}
