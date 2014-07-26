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

        self.__all = LedSet(self.__leds)

    def all(self, brightness):
        """Immediately light all the LEDs."""
        self.__all.light(brightness)

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
        set_ = LedSet([self.__leds[Led.correct_id(led) - 1] for led in leds])
        set_.light(brightness)

    def buffer(self, leds, brightness):
        """Buffer values for a set of LEDs."""
        set_ = LedSet([self.__leds[Led.correct_id(led) - 1] for led in leds])
        set_.buffer(brightness)

    def gamma_all(self, brightness):
        """Immediately light all the LEDs."""
        self.__all.gamma_light(brightness)

    def gamma_led(self, identifier, brightness):
        """Immediately light a LED."""
        index = Led.correct_id(identifier) - 1
        self.__leds[index].gamma_light(brightness)

    def gamma_arm(self, identifier, brightness):
        """Immediately light an arm."""
        index = Arm.correct_id(identifier) - 1
        self.__arms[index].gamma_light(brightness)

    def gamma_ring(self, identifier, brightness):
        """Immediately light a ring."""
        index = Ring.correct_id(identifier) - 1
        self.__rings[index].gamma_light(brightness)

    def gamma_color(self, identifier, brightness):
        """Immediately light all LEDs of the same color. Akin to ring."""
        self.gamma_ring(identifier, brightness)

    def gamma_led_set(self, leds, brightness):
        """Immediately light a set of LEDs."""
        set_ = LedSet([self.__leds[Led.correct_id(led)] for led in leds])
        set_.gamma_light(brightness)

    def gamma_buffer(self, leds, brightness):
        """Buffer values for a set of LEDs."""
        set_ = LedSet([self.__leds[Led.correct_id(led)] for led in leds])
        set_.gamma_buffer(brightness)

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
        self.__all.off()

    def up_to_date(self):
        """Check whether values have been buffered and are not effective yet."""
        return self.__bus.up_to_date()
