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
        if Led.check_brightness(brightness):
            self.unsafe_buffer(brightness)

    def light(self, brightness):
        """Immediately light the set of LEDs."""
        if self.__leds and Led.check_brightness(brightness):
            self.unsafe_light(brightness)

    def gamma_buffer(self, brightness):
        """Buffer a gamma corrected brightness value."""
        if self.__leds:
            correct_brightness = Led.gamma_correct(brightness)
            self.unsafe_buffer(correct_brightness)

    def gamma_light(self, brightness):
        """Immediately light the set of LEDs."""
        if self.__leds:
            correct_brightness = Led.gamma_correct(brightness)
            self.unsafe_light(correct_brightness)

    def unsafe_buffer(self, brightness):
        """(Unsafe) Buffer a brightness value."""
        for led in self.__leds:
            led.unsafe_buffer(brightness)

    def unsafe_set(self, brightness):
        """(Unsafe) Set the LED set's brightness."""
        for led in self.__leds:
            led.unsafe_set(brightness)

    def unsafe_light(self, brightness):
        """(Unsafe) Immediately light the LED set."""
        self.unsafe_set(brightness)
        self.__bus.update()

    def off(self):
        """Switch off the set of LEDs."""
        if self.__leds:
            self.unsafe_light(0)

    def number(self):
        """Number of LEDs in the set."""
        return len(self.__leds)

    def leds(self):
        """Return the LEDs in the set."""
        return self.__leds
