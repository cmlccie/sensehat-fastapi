"""Sense HAT FastAPI v0."""

from typing import List

from fastapi import FastAPI
from sense_hat import SenseHat
from enum import Enum


# Module Variables
sense = SenseHat()
api = FastAPI(openapi_prefix="/api/v0")


# API Endpoints

# Environment
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


# LED Matrix
@api.post("/led_matrix", tags=["LED Matrix"])
def set_pixels(pixel_list: List[List[int]]):
    """Update the entire LED matrix with a list of 64 pixel values [R, G, B].
    \f
    Args:
        pixel_list: A list containing 64 smaller lists of [R, G, B] pixels
            (red, green, blue). Each R-G-B element must be an integer between
            0 and 255.
    """
    sense.set_pixels(pixel_list)


@api.get("/led_matrix", tags=["LED Matrix"])
def get_pixels() -> List[List[int]]:
    """Get the pixel values for the entire LED matrix.
    \f
    Returns:
        List[List[int]]: A list containing 64 smaller lists of
            [R, G, B] pixels (red, green, blue) representing the flipped image.
    """
    return sense.get_pixels()


@api.delete("/led_matrix", tags=["LED Matrix"])
def clear(color: str = "0,0,0"):
    """Set the entire LED matrix to a single color, defaults to black/off.
    \f
    Args:
        color: A string containing the R,G,B (red, green, blue) color for the
            pixel. Each R,G,B element must be an integer between 0 and 255.
            Defaults to 0,0,0 black/off.
    """
    color = [int(v) for v in color.split(",")]
    sense.clear(color)


@api.post("/led_matrix/letter", tags=["LED Matrix"])
def show_letter(
    letter: str,
    text_color: str = "255,255,255",
    back_color: str = "0,0,0",
):
    """Display a single text character on the LED matrix.
    \f
    Args:
        letter: The letter to show.
        text_color: A string containing the R,G,B (red, green, blue) color of
            the text. Each R,G,B element must be an integer between 0 and 255.
            Defaults to 255,255,255 white.
        back_color: A list containing the R,G,B (red, green, blue) color of
            the background. Each R,G,B element must be an integer between 0 and
            255. Defaults to 0,0,0 black/off.
    """
    text_color = [int(v) for v in text_color.split(",")]
    back_color = [int(v) for v in back_color.split(",")]
    sense.show_letter(
        s=letter,
        text_colour=text_color,
        back_colour=back_color,
    )


@api.post("/led_matrix/message", tags=["LED Matrix"])
def show_message(
    text_string: str,
    scroll_speed: float = 0.1,
    text_color: str = "255,255,255",
    back_color: str = "0,0,0",
):
    """Scroll a text message from right to left across the LED matrix.
    \f
    Args:
        text_string: The message to scroll.
        scroll_speed: The speed at which the text should scroll. This value
            represents the time paused for between shifting the text to the
            left by one column of pixels. Defaults to 0.1
        text_color: A string containing the R,G,B (red, green, blue) color of
            the text. Each R,G,B element must be an integer between 0 and 255.
            Defaults to 255,255,255 white.
        back_color: A list containing the R,G,B (red, green, blue) color of
            the background. Each R,G,B element must be an integer between 0 and
            255. Defaults to 0,0,0 black/off.
    """
    text_color = [int(v) for v in text_color.split(",")]
    back_color = [int(v) for v in back_color.split(",")]
    sense.show_message(
        text_string=text_string,
        scroll_speed=scroll_speed,
        text_colour=text_color,
        back_colour=back_color,
    )


@api.post("/led_matrix/pixel", tags=["LED Matrix"])
def set_pixel(x: int, y: int, color: str = "255,255,255"):
    """Set an individual LED matrix pixel the specified color.
    \f
    Args:
        x: 0 is on the left, 7 on the right.
        y: 0 is at the top, 7 at the bottom.
        color: A RGB (red, green, blue) pixel. Each element must be an integer
            between 0 and 255.
    """
    color = [int(v) for v in color.split(",")]
    sense.set_pixel(x, y, color)


@api.get("/led_matrix/pixel", tags=["LED Matrix"])
def get_pixel(x: int, y: int) -> List[int]:
    """Get the pixel value for the specified x, y coordinate..
    \f
    Returns:
        List[int]: Returns an [R, G, B] list representing the color
            of an individual LED matrix pixel at the specified x, y coordinate.
    """
    return sense.get_pixel(x, y)


@api.post("/led_matrix/rotation", tags=["LED Matrix"])
def set_rotation(r: int, redraw: bool = True):
    """Set the rotation of the image shown on the LED Matrix.
    \f
    Args:
        r: The rotation angle; 0 is with the Raspberry Pi HDMI port facing
            downwards (valid values: 0, 90, 180, 270).
        redraw: Redraw what is already displayed on the LED matrix
            (default:  True)?
    """
    sense.set_rotation(r, redraw=redraw)


class FlipDirection(str, Enum):
    vertical = "vertical"
    horizontal = "horizontal"


@api.post("/led_matrix/flip", tags=["LED Matrix"])
def flip(direction: FlipDirection, redraw: bool = True) -> List[List[int]]:
    """Flips the image on the LED matrix horizontally.
    \f
    Args:
        direction: Direction to flip the image ("vertical" or "horizontal").
        redraw: Redraw what is already displayed on the LED matrix
            (default:  True)?

    Returns:
        List[List[int]]: A list containing 64 smaller lists of [R, G, B] pixels
            (red, green, blue) representing the flipped image.
    """
    if direction == FlipDirection.vertical:
        return sense.flip_v(redraw=redraw)
    elif direction == FlipDirection.horizontal:
        return sense.flip_h(redraw=redraw)


@api.post("/led_matrix/low_light", tags=["LED Matrix"])
def set_low_light(on: bool = False):
    """Enable or disable low-light mode.

    Low-light mode is useful if the Sense HAT is being used in a dark
    environment.
    \f
    Args:
        on: Enable or disable low-light mode.
    """
    sense.low_light = on


@api.get("/led_matrix/low_light", tags=["LED Matrix"])
def get_low_light() -> bool:
    """Get the status of low-light mode.
    \f
    Returns:
        bool: True if low-light mode is enabled.
    """
    return sense.low_light


@api.post("/led_matrix/gamma", tags=["LED Matrix"])
def set_gamma(lookup_table: List[int]):
    """Set the gamma lookup table.

    For advanced users. Most users will just need the low_light mode.

    The Sense HAT python API uses 8 bit (0 to 255) colours for R, G, B. When
    these are written to the Linux frame buffer they're bit shifted into RGB
    5 6 5. The driver then converts them to RGB 5 5 5 before it passes them
    over to the ATTiny88 AVR for writing to the LEDs.

    The gamma property allows you to specify a gamma lookup table for the final
    5 bits of colour used. The lookup table is a list of 32 numbers that must
    be between 0 and 31. The value of the incoming 5 bit colour is used to
    index the lookup table and the value found at that position is then written
    to the LEDs.
    """
    sense.gamma = lookup_table


@api.delete("/led_matrix/gamma", tags=["LED Matrix"])
def reset_gamma():
    """Reset the gamma lookup table."""
    sense.gamma_reset()
