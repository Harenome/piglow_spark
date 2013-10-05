from led import Led

class LedSet:
    """Control a set of LEDs."""

    def __init__(self, leds):
        self.__leds = leds

    def buffer(self, brightness):
        """Buffer a brightness value."""
        for led in self.__leds:
            led.buffer(brightness)

    def light(self, brightness):
        """Immediately light the set of LEDs."""
        for led in self.__leds:
            led.light(brightness)

    def off(self):
        """Switch off the set of LEDs."""
        for led in self.__leds:
            led.off()

    def number(self):
        """Number of LEDs in the set."""
        return len(self.__leds)

    def leds(self):
        return self.__leds
