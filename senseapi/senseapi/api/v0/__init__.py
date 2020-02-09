"""Sense HAT FastAPI v0."""

from fastapi import FastAPI

from senseapi.api.v0 import environment, led_matrix


# Create the API version FastAPI instance
api = FastAPI(
    openapi_prefix="/api/v0",
    title="Raspberry Pi Sense HAT REST API",
    version="0",
)


# Endpoint Routers
api.include_router(
    environment.router,
    tags=["Environmental Sensors"],
)

api.include_router(
    led_matrix.router,
    prefix="/led_matrix",
    tags=["LED Matrix"],
)
