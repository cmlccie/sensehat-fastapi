"""Sense HAT FastAPI v0."""

from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from sense_hat import SenseHat


# Module Variables
sense = SenseHat()
api = FastAPI(openapi_prefix="/api/v0")


# Data Models
class HumidityUnit(str, Enum):
    """Humidity units."""
    relative_humidity = "%"


class HumidityReading(BaseModel):
    """Humidity reading from the Sense HAT sensors."""
    units: HumidityUnit
    humidity_sensor: float


class PressureUnit(str, Enum):
    """Pressure units."""
    millibar = "mbar"
    pascal = "Pa"


class PressureReading(BaseModel):
    """Pressure reading from the Sense HAT sensors."""
    units: PressureUnit
    pressure_sensor: float


class TemperatureUnit(str, Enum):
    """Temperature units."""
    kelvin = "K"
    celsius = "°C"
    fahrenheit = "°F"


class TemperatureReading(BaseModel):
    """Temperature reading from the Sense HAT sensors."""
    units: TemperatureUnit
    humidity_sensor: float
    pressure_sensor: float


# API Endpoints
@api.get(
    "/humidity",
    response_model=HumidityReading,
    tags=["Environmental Sensors"],
)
def get_humidity() -> HumidityReading:
    """Get the percentage of relative humidity from the humidity sensor."""
    return HumidityReading(
        units=HumidityUnit.relative_humidity,
        humidity_sensor=sense.get_humidity(),
    )


@api.get(
    "/pressure",
    response_model=PressureReading,
    tags=["Environmental Sensors"],
)
def get_pressure() -> PressureReading:
    """Get the current pressure in Millibars from the pressure sensor."""
    return PressureReading(
        units=PressureUnit.millibar,
        pressure_sensor=sense.get_pressure(),
    )


@api.get(
    "/temperature",
    response_model=TemperatureReading,
    tags=["Environmental Sensors"],
)
def get_temperature() -> TemperatureReading:
    """Get the temperature in degrees Celsius from the Sense HAT sensors."""
    return TemperatureReading(
        units=TemperatureUnit.celsius,
        humidity_sensor=sense.get_temperature_from_humidity(),
        pressure_sensor=sense.get_temperature_from_pressure(),
    )
