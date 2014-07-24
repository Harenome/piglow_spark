#!/usr/bin/env python
"""Led set module."""
from piglow_spark.components.led import Led

class LedSet(object):
    """Control a set of LEDs."""

    def __init__(self, leds):
        self.__leds = leds
        if self.__leds:
            self.__bus = self.__leds[0].bus()

    def buffer(self, brightness):
        """Buffer a brightness value."""
        if self.__leds and Led.check_brightness(brightness):
            correct_brightness = Led.GAMMA_TABLE_256[brightness]
            for led in self.__leds:
                led.unsafe_buffer(correct_brightness)

    def light(self, brightness):
        """Immediately light the set of LEDs."""
        if self.__leds and Led.check_brightness(brightness):
            correct_brightness = Led.GAMMA_TABLE_256[brightness]
            for led in self.__leds:
                led.unsafe_set(correct_brightness)
            self.__bus.update()

    def off(self):
        """Switch off the set of LEDs."""
        if self.__leds:
            for led in self.__leds:
                led.unsafe_set(0)
            self.__bus.update()

    def number(self):
        """Number of LEDs in the set."""
        return len(self.__leds)

    def leds(self):
        """Return the LEDs in the set."""
        return self.__leds
