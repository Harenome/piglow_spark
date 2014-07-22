#!/usr/bin/env python
"""Arm module."""
from components.led_set import LedSet
from error.id_error import IdError

class ArmIdError(IdError):
    """Arm ID error."""
    def __init__(self, wrong_id):
        IdError.__init__(self, "Arm", wrong_id)

class Arm(LedSet):
    """Control an arm."""

    FIRST = 1
    NUMBER = 3
    LEDS_NUMBER = 6
    __DIRECTIONS_ID = {"up": 1, "right": 2, "left": 3}

    def __init__(self, identifier, all_leds):
        arm_id = Arm.correct_id(identifier)
        indexes = Arm.list_leds(arm_id)
        leds = [all_leds[i-1] for i in indexes]

        LedSet.__init__(self, leds)
        self.__id = [key for (key, value) in Arm.__DIRECTIONS_ID.viewitems() \
            if value == arm_id][0]

    @staticmethod
    def __check_id(identifier):
        """Check an id."""
        if (isinstance(identifier, int) \
            and Arm.FIRST <= identifier <= Arm.NUMBER) \
            or (isinstance(identifier, str) \
            and identifier.lower() in Arm.__DIRECTIONS_ID):
            return True
        else:
            raise ArmIdError(identifier)

    @staticmethod
    def list_leds(identifier):
        """List the LEDs corresponding to an arm id."""
        arm_id = Arm.correct_id(identifier)
        arm_start = Arm.LEDS_NUMBER * (arm_id - 1)
        leds = [(x+1) + arm_start for x in range(Arm.LEDS_NUMBER)]

        return leds

    @staticmethod
    def correct_id(identifier):
        """Return the id (an int) of an arm, if it exists."""
        if Arm.__check_id(identifier):
            if isinstance(identifier, int):
                return identifier
            else:
                return Arm.__DIRECTIONS_ID[identifier.lower()]

    @staticmethod
    def available():
        """List the available arms."""
        return Arm.__DIRECTIONS_ID.keys()

    def identifier(self):
        """Return the Arm's ID."""
        return self.__id
