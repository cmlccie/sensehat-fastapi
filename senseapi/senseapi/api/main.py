"""FastAPI application."""

from fastapi import FastAPI

from senseapi.api import v0


# Initialize the top-level FastAPI application
app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


# Top-level API endpoints
@app.get("/api")
def get_api_root_paths():
    """Return the API root paths; by version."""
    return {
        "v0": "/api/v0/"
    }


# Mount the versioned sub-APIs
app.mount("/api/v0", v0.api)
