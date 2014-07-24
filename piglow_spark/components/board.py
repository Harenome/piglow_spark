#!/usr/bin/env python
"""Board module."""
from piglow_spark.components.bus import Bus
from piglow_spark.components.led import Led
from piglow_spark.components.led_set import LedSet
from piglow_spark.components.arm import Arm
from piglow_spark.components.ring import Ring

class Board(object):
    """Control the board."""
    def __init__(self):
        self.__bus = Bus()

        self.__leds = []
        for identifier in range(Led.FIRST, Led.NUMBER+1):
            self.__leds.append(Led(identifier, self.__bus))

        self.__arms = []
        for identifier in range(Arm.FIRST, Arm.NUMBER+1):
            self.__arms.append(Arm(identifier, self.__leds))

        self.__rings = []
        for identifier in range(Ring.FIRST, Ring.NUMBER+1):
            self.__rings.append(Ring(identifier, self.__leds))

    def all(self, brightness):
        """Immediately light all the LEDs."""
        for led in self.__leds:
            led.light(brightness)

    def led(self, identifier, brightness):
        """Immediately light a LED."""
        index = Led.correct_id(identifier) - 1
        self.__leds[index].light(brightness)

    def arm(self, identifier, brightness):
        """Immediately light an arm."""
        index = Arm.correct_id(identifier) - 1
        self.__arms[index].light(brightness)

    def ring(self, identifier, brightness):
        """Immediately light a ring."""
        index = Ring.correct_id(identifier) - 1
        self.__rings[index].light(brightness)

    def color(self, identifier, brightness):
        """Immediately light all LEDs of the same color. Akin to ring."""
        self.ring(identifier, brightness)

    def led_set(self, leds, brightness):
        """Immediately light a set of LEDs."""
        for led in leds:
            index = Led.correct_id(led) - 1
            self.__leds[index].light(brightness)

    def buffer(self, leds, brightness):
        """Buffer values for a set of LEDs."""
        for led in leds:
            index = Led.correct_id(led) - 1
            self.__leds[index].buffer(brightness)

    def dump(self):
        """Backup the current state of the Piglow."""
        return self.__bus.dump()

    def restore(self, backup):
        """Restore previously dumped state."""
        self.__bus.restore(backup)

    def flush(self):
        """Flush the PiGlow's buffer."""
        self.__bus.flush()

    def off(self):
        """Turn off all the LEDs."""
        for led in self.__leds:
            led.off()

    def up_to_date(self):
        """Check whether values have been buffered and are not effective yet."""
        return self.__bus.up_to_date()
