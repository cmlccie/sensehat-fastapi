"""Sense HAT singleton class."""

from typing import Optional

import sense_hat


class SenseHat(object):
    """Sense HAT Python API singleton class."""
    instance: Optional[sense_hat.SenseHat] = None

    def __new__(cls) -> sense_hat.SenseHat:
        if cls.instance is None:
            cls.instance = sense_hat.SenseHat()

        return cls.instance
