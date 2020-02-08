"""FastAPI application."""

import time

from fastapi import FastAPI
from starlette.requests import Request

from senseapi.api import v0, v1


# Initialize the top-level FastAPI application
app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


# Application Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Top-level API endpoints
@app.get("/api")
def get_api_root_paths():
    """Return the API root paths; by version."""
    return {
        "v0": "/api/v0/",
        "v1": "/api/v1/",
    }


# Mount the versioned sub-APIs
app.mount("/api/v0", v0.api)
app.mount("/api/v1", v1.api)
