from bus import Bus
from led import Led
from ledset import LedSet
from arm import Arm
from ring import Ring

class Board:
    """Control the board."""
    def __init__(self):
        self.__bus = Bus()

        self.__leds = []
        for id in range(Led.FIRST, Led.NUMBER+1):
            self.__leds.append(Led(id, self.__bus))

        self.__arms = []
        for id in range(Arm.FIRST, Arm.NUMBER+1):
            self.__arms.append(Arm(id, self.__leds))

        self.__rings = []
        for id in range(Ring.FIRST, Ring.NUMBER+1):
            self.__rings.append(Ring(id, self.__leds))

    def all(self, brightness):
        """Immediately light all the LEDs."""
        for led in self.__leds:
            led.light(brightness)

    def led(self, id, brightness):
        """Immediately light a LED."""
        index = Led.correct_id(id) - 1
        self.__leds[index].light(brightness)

    def arm(self, id, brightness):
        """Immediately light an arm."""
        index = Arm.correct_id(id) - 1
        self.__arms[index].light(brightness)

    def ring(self, id, brightness):
        """Immediately light a ring."""
        index = Ring.correct_id(id) - 1
        self.__rings[index].light(brightness)

    def color(self, id, brightness):
        """Immediately light all LEDs of the same color. Akin to ring."""
        self.ring(id, brightness)

    def ledset(self, leds, brightness):
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

    def update(self):
        """Update the Piglow according to the values previously buffered."""
        self.__bus.update()

    def off(self):
        """Turn off all the LEDs."""
        for led in self.__leds:
            led.off()

    def up_to_date(self):
        """Check whether values have been buffered and are not effective yet."""
        return self.__bus.up_to_date()
