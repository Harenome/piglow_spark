#!/usr/bin/env python

from ledset import LedSet
from iderror import IdError

class ArmIdError(IdError):
    def __init__(self, wrong_id):
        IdError.__init__(self, wrong_id, "Arm")

class Arm(LedSet):
    """Control an arm."""

    FIRST = 1
    NUMBER = 3
    LEDS_NUMBER = 6
    __DIRECTIONS_ID = { "up": 1, "right": 2, "left": 3 }

    def __init__(self, id, all_leds):
        arm_id = Arm.correct_id(id)
        indexes = Arm.list_leds(arm_id)
        leds = [ all_leds[i-1] for i in indexes ]

        LedSet.__init__(self, leds)
        self.__id = [ key for (key, value) in Arm.__DIRECTIONS_ID.viewitems() \
            if value == arm_id ][0]

    @staticmethod
    def __check_id(id):
        """Check an id."""
        if (isinstance(id, int) and Arm.FIRST <= id <= Arm.NUMBER) \
            or (isinstance(id, str) and id.lower() in Arm.__DIRECTIONS_ID):
            return True
        else:
            raise ArmIdError(id)

    @staticmethod
    def list_leds(id):
        """List the LEDs corresponding to an arm id."""
        arm_id = Arm.correct_id(id)
        arm_start = Arm.LEDS_NUMBER * (arm_id - 1)
        leds = [ (x+1) + arm_start for x in range(Arm.LEDS_NUMBER) ]

        return leds

    @staticmethod
    def correct_id(id):
        """Return the id (an int) of an arm, if it exists."""
        if Arm.__check_id(id):
            if isinstance(id, int):
                return id
            else:
                return Arm.__DIRECTIONS_ID[id.lower()]

    @staticmethod
    def available():
        """List the available arms."""
        return Arm.__DIRECTIONS_ID.keys()

    def id(self):
        return self.__id
