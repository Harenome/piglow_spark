#!/usr/bin/env python
"""Led module."""
from piglow_spark.components.bus import Bus
from piglow_spark.error.brightness_error import BrightnessError
from piglow_spark.error.id_error import IdError

# Gamma correction...
GAMMA_32 = [
    0, 1, 2, 4, 6, 10, 13, 18,
    22, 28, 33, 39, 46, 53, 61, 69,
    78, 86, 96, 106, 116, 126, 138, 149,
    161, 173, 186, 199, 212, 226, 240, 255
]
# ~ 128
GAMMA_128 = [
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 40,
    41, 42, 43, 44, 45, 46, 47, 48,
    50, 51, 52, 53, 54, 55, 57, 58,
    59, 60, 62, 63, 64, 66, 67, 69,
    70, 72, 74, 75, 77, 79, 80, 82,
    84, 86, 88, 90, 91, 94, 96, 98,
    100, 102, 104, 107, 109, 111, 114, 116,
    119, 122, 124, 127, 130, 133, 136, 139,
    142, 145, 148, 151, 155, 158, 161, 165,
    169, 172, 176, 180, 184, 188, 192, 196,
    201, 205, 210, 214, 219, 224, 229, 234,
    239, 244, 250, 255
]
GAMMA_TABLE = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
    8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12,
    12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 18, 18, 18,
    19, 19, 20, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 26, 26, 27, 27,
    28, 29, 29, 30, 31, 31, 32, 33, 33, 34, 35, 36, 36, 37, 38, 39, 40, 41, 42,
    42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 62,
    63, 64, 66, 67, 69, 70, 72, 74, 75, 77, 79, 80, 82, 84, 86, 88, 90, 91, 94,
    96, 98, 100, 102, 104, 107, 109, 111, 114, 116, 119, 122, 124, 127, 130,
    133, 136, 139, 142, 145, 148, 151, 155, 158, 161, 165, 169, 172, 176, 180,
    184, 188, 192, 196, 201, 205, 210, 214, 219, 224, 229, 234, 239, 244, 250,
    255
]

class LedBrightnessError(BrightnessError):
    """Led brightness error."""
    def __init__(self, wrong_brightness):
        BrightnessError.__init__(self, wrong_brightness)

class LedIdError(IdError):
    """Led ID error."""
    def __init__(self, wrong_id):
        IdError.__init__(self, "LED", wrong_id)

class Led(object):
    """Control a LED."""

    FIRST = 1
    NUMBER = 18
    MIN_BRIGHTNESS = 0
    MAX_BRIGHTNESS = 255
    __ADDRESSES = {
        1: 0x07, 2: 0x08, 3: 0x09, 4: 0x06, 5: 0x05, 6: 0x0A, 7: 0x12, 8: 0x11,
        9: 0x10, 10: 0x0E, 11: 0x0C, 12: 0x0B, 13: 0x01, 14: 0x02, 15: 0x03,
        16: 0x04, 17: 0x0F, 18: 0x0D
    }
    __LEDS_ID = {
        "red1": 1, "orange1": 2, "yellow1": 3, "green1": 4, "blue1": 5,
        "white1": 6, "red2": 7, "orange2": 8, "yellow2": 9, "green2": 10,
        "blue2": 11, "white2": 12, "red3": 13, "orange3": 14, "yellow3": 15,
        "green3": 16, "blue3": 17, "white3": 18
    }

    def __init__(self, identifier, bus):
        led_id = Led.correct_id(identifier)

        self.__bus = bus
        self.__address = Led.__ADDRESSES[led_id]
        self.__id = [key for (key, value) in Led.__LEDS_ID.viewitems() \
            if value == led_id][0]

    @staticmethod
    def __check_id(identifier):
        """Check if an id is valid."""
        if (isinstance(identifier, int) \
                and Led.FIRST <= identifier <= Led.NUMBER) \
                or (isinstance(identifier, str) \
                and identifier.lower() in Led.__LEDS_ID):
            return True
        else:
            raise LedIdError(identifier)

    @staticmethod
    def __check_brightness(brightness):
        """Check if a brightness is valid."""
        if Led.MIN_BRIGHTNESS <= brightness <= Led.MAX_BRIGHTNESS:
            return True
        else:
            raise LedBrightnessError(brightness)

    @staticmethod
    def correct_id(identifier):
        """Get the id corresponding to a color."""
        if Led.__check_id(identifier):
            if isinstance(identifier, int):
                return identifier
            else:
                return Led.__LEDS_ID[identifier.lower()]

    @staticmethod
    def available():
        """List the available LEDs."""
        return Led.__LEDS_ID.keys()

    def buffer(self, brightness):
        """Buffer a brightness value."""
        if Led.__check_brightness(brightness):
            gc_value = GAMMA_TABLE[brightness]

            self.__bus.buffer(self.__address, gc_value)

    def light(self, brightness):
        """Immediately light the LED."""
        if Led.__check_brightness(brightness):
            gc_value = GAMMA_TABLE[brightness]

            self.__bus.light_led(self.__address, gc_value)

    def brightness(self):
        """Return the brightness of a LED."""
        return self.__bus.led_state(self.__address)

    def off(self):
        """Switch off the LED."""
        self.light(0)

    def identifier(self):
        """Get the LED's ID."""
        return self.__id
