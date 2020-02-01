"""Sense HAT FastAPI v0."""

from fastapi import FastAPI

from sense_hat import SenseHat


sense = SenseHat()
api = FastAPI(openapi_prefix="/api/v0")


@api.get("/temperature")
def get_temperature():
    return {
        "celsius": sense.get_temperature(),
    }
