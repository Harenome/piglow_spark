#!/usr/bin/env python
"""PiGlow module."""

from components.board import Board
from components.led import Led
from components.arm import Arm
from components.ring import Ring

class PiGlow(Board):
    """Control the PiGlow board."""
    MIN_BRIGHTNESS = Led.MIN_BRIGHTNESS
    MAX_BRIGHTNESS = Led.MAX_BRIGHTNESS

    LED_NUMBER = Led.NUMBER
    LED_FIRST = Led.FIRST
    LED_AVAILABLE = Led.available()

    ARM_NUMBER = Arm.NUMBER
    ARM_FIRST = Arm.FIRST
    ARM_AVAILABLE = Arm.available()

    RING_NUMBER = Ring.NUMBER
    RING_FIRST = Ring.FIRST
    RING_AVAILABLE = Ring.available()

