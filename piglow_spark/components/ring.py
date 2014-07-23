#!/usr/bin/env python
"""Ring module."""
from piglow_spark.components.led_set import LedSet
from piglow_spark.error.id_error import IdError

class RingIdError(IdError):
    def __init__(self, wrong_id):
        IdError.__init__(self, "Ring", wrong_id)

class Ring(LedSet):
    """Control a ring."""

    NUMBER = 6
    FIRST = 1
    LEDS_NUMBER = 3
    __COLORS_ID = {"white": 1, "blue": 2, "green": 3, "yellow": 4,
        "orange": 5, "red": 6
    }

    def __init__(self, identifier, all_leds):
        ring_id = Ring.correct_id(identifier)
        indexes = Ring.list_leds(ring_id)
        leds = [all_leds[i-1] for i in indexes]

        LedSet.__init__(self, leds)
        self.__id = [key for (key, value) in Ring.__COLORS_ID.viewitems() \
            if value == ring_id][0]

    @staticmethod
    def __check_id(identifier):
        """Check the ID."""
        if (isinstance(identifier, int) \
            and Ring.FIRST <= identifier <= Ring.NUMBER) \
            or (isinstance(identifier, str) \
            and identifier.lower() in Ring.__COLORS_ID):
            return True
        else:
            raise RingIdError(identifier)

    @staticmethod
    def correct_id(identifier):
        """Return the correct ID."""
        if Ring.__check_id(identifier):
            if isinstance(identifier, int):
                return identifier
            else:
                return Ring.__COLORS_ID[identifier.lower()]

    @staticmethod
    def list_leds(identifier):
        """List the LEDS corresponding to a ring id."""
        ring_id = Ring.correct_id(identifier)
        ring_start = range(Ring.NUMBER, 0, -1)[ring_id-1]
        leds = [ring_start + Ring.NUMBER * i for i in range(Ring.LEDS_NUMBER)]

        return leds

    @staticmethod
    def available():
        """List the available rings/colors."""
        rings = Ring.__COLORS_ID.keys()[:]
        rings.sort()
        return rings

    def identifier(self):
        """Return the ID of the ring."""
        return self.__id
