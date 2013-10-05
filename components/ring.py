from ledset import LedSet
from error.iderror import IdError

class RingIdError(IdError):
    def __init__(self, wrong_id):
        IdError.__init__(self, "Ring", wrong_id)

class Ring(LedSet):
    """Control a ring."""

    NUMBER = 6
    FIRST = 1
    LEDS_NUMBER = 3
    __COLORS_ID = {"white": 1, "blue": 2, "green": 3, "yellow": 4, "orange": 5, "red": 6}

    def __init__(self, id, all_leds):
        ring_id = Ring.correct_id(id)
        indexes = Ring.list_leds(ring_id)
        leds = [ all_leds[i-1] for i in indexes ]

        LedSet.__init__(self, leds)
        self.__id = [ key for (key, value) in Ring.__COLORS_ID.viewitems() \
            if value == ring_id ][0]

    @staticmethod
    def __check_id(id):
        if (isinstance(id, int) and Ring.FIRST <= id <= Ring.NUMBER) \
            or (isinstance(id, str) and id.lower() in Ring.__COLORS_ID):
            return True
        else:
            raise RingIdError(id)

    @staticmethod
    def correct_id(id):
        if Ring.__check_id(id):
            if isinstance(id, int):
                return id
            else:
                return Ring.__COLORS_ID[id.lower()]

    @staticmethod
    def list_leds(id):
        """List the LEDS corresponding to a ring id."""
        ring_id = Ring.correct_id(id)
        ring_start = range(Ring.NUMBER,0,-1)[ring_id-1]
        leds = [ ring_start + Ring.NUMBER * i for i in range(Ring.LEDS_NUMBER) ]

        return leds

    @staticmethod
    def available():
        """List the available rings/colors."""
        return Ring.__COLORS_ID.keys()

    def id(self):
        return self.__id
