#!/usr/bin/env python

from components.board import Board
from components.led import Led
from components.led import LedIdError
from components.arm import Arm
from components.ring import Ring

class PiGlow(Board):
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

if __name__ == '__main__':
    try:
        piglow = PiGlow()
        while True:
            led = input("Led : ")
            brightness = input("Brightness : ")
            try:
                piglow.led(led, brightness)
            except LedIdError as error:
                print(error.msg)
    except KeyboardInterrupt:
        piglow.off()
