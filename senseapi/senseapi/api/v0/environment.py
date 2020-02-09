"""Sense HAT FastAPI v0 - Environment Endpoints."""

from fastapi import APIRouter

from senseapi.infrastructure import SenseHat


# Module Variables
router = APIRouter()
sense = SenseHat()


# API Endpoints
@router.get("/humidity")
def get_humidity():
    """Get the percentage of relative humidity from the humidity sensor."""
    return {
        "units": "%",
        "humidity_sensor": sense.get_humidity(),
    }


@router.get("/pressure")
def get_pressure():
    """Get the current pressure in Millibars from the pressure sensor."""
    return {
        "units": "mbar",
        "pressure_sensor": sense.get_pressure(),
    }


@router.get("/temperature")
def get_temperature():
    """Get the temperature in degrees Celsius from the Sense HAT sensors."""
    return {
        "units": "°C",
        "humidity_sensor": sense.get_temperature_from_humidity(),
        "pressure_sensor": sense.get_temperature_from_pressure(),
    }
