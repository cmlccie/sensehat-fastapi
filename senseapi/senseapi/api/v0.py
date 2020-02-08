"""Sense HAT FastAPI v0."""

from typing import List

from fastapi import FastAPI
from sense_hat import SenseHat


# Module Variables
sense = SenseHat()
api = FastAPI(openapi_prefix="/api/v0")


# API Endpoints
@api.get("/humidity", tags=["Environmental Sensors"])
def get_humidity():
    """Get the percentage of relative humidity from the humidity sensor."""
    return {
        "units": "%",
        "humidity_sensor": sense.get_humidity(),
    }


@api.get("/pressure", tags=["Environmental Sensors"])
def get_pressure():
    """Get the current pressure in Millibars from the pressure sensor."""
    return {
        "units": "mbar",
        "pressure_sensor": sense.get_pressure(),
    }


@api.get("/temperature", tags=["Environmental Sensors"])
def get_temperature():
    """Get the temperature in degrees Celsius from the Sense HAT sensors."""
    return {
        "units": "°C",
        "humidity_sensor": sense.get_temperature_from_humidity(),
        "pressure_sensor": sense.get_temperature_from_pressure(),
    }


@api.post("/message", tags=["LED Matrix"])
def show_message(
    text_string: str,
    scroll_speed: float = 0.1,
    text_colour: List[int] = (255, 255, 255),
    back_colour: List[int] = (0, 0, 0),
):
    """Scroll a text message from right to left across the LED matrix.

    Scrolls a text message from right to left across the LED matrix and at the
    specified speed, in the specified colour and background colour.

    Args:
        text_string: The message to scroll.
        scroll_speed: The speed at which the text should scroll. This value
            represents the time paused for between shifting the text to the
            left by one column of pixels. Defaults to 0.1
        text_colour: A list containing the R-G-B (red, green, blue) colour of
            the text. Each R-G-B element must be an integer between 0 and 255.
            Defaults to [255, 255, 255] white.
        back_colour: A list containing the R-G-B (red, green, blue) colour of
            the background. Each R-G-B element must be an integer between 0 and
            255. Defaults to [0, 0, 0] black / off.
    """
    sense.show_message(
        text_string=text_string,
        scroll_speed=scroll_speed,
        text_colour=text_colour,
        back_colour=back_colour,
    )
