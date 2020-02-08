"""Environment Data Models."""

from enum import Enum

from pydantic import BaseModel


# Measurement Units
class TemperatureUnit(str, Enum):
    """Temperature units."""
    kelvin = "K"
    celsius = "°C"
    fahrenheit = "°F"


class PressureUnit(str, Enum):
    """Pressure units."""
    millibar = "mbar"
    pascal = "Pa"


class HumidityUnit(str, Enum):
    """Humidity units."""
    relative_humidity = "%"


# Data Models
class HumidityReading(BaseModel):
    """Humidity reading from the Sense HAT sensors."""
    units: HumidityUnit
    humidity_sensor: float


class PressureReading(BaseModel):
    """Pressure reading from the Sense HAT sensors."""
    units: PressureUnit
    pressure_sensor: float


class TemperatureReading(BaseModel):
    """Temperature reading from the Sense HAT sensors."""
    units: TemperatureUnit
    humidity_sensor: float
    pressure_sensor: float
