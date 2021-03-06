#!/usr/bin/env python
"""Brightness error module."""
from piglow_spark.error.piglow_error import PiGlowError

class BrightnessError(PiGlowError):
    """Brightness error."""

    def __init__(self, wrong_brightness):
        PiGlowError.__init__(self, ("brightness", wrong_brightness))
        self.wrong_brightness = wrong_brightness
        self.message = "Invalid brightness value. (" \
            + str(self.wrong_brightness) + ")"
