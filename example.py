#!/usr/bin/env python
"""Example."""

from time import sleep
from piglow_spark.piglow import PiGlow

## Terminal utilities.
NORMAL_TEXT = "\033[0m"
BOLD_TEXT = "\033[1m"
DIM_TEXT = "\033[2m"
UNDERLINED_TEXT = "\033[4m"
RED_TEXT = "\033[38;5;196m"
BLUE_TEXT = "\033[38;5;74m"
GREEN_TEXT = "\033[38;5;148m"
ORANGE_TEXT = "\033[38;5;214m"
YELLOW_TEXT = "\033[38;5;227m"
TEXT_COLORS = {
    "white": "",
    "blue": BLUE_TEXT,
    "green": GREEN_TEXT,
    "yellow": YELLOW_TEXT,
    "orange": ORANGE_TEXT,
    "red": RED_TEXT,
}

## Fade constants.
FADE_STEP = 1.0/512
FADE_WAIT = 0.5

piglow = PiGlow()
leds = piglow.LED_AVAILABLE

def fade(func, identifier):
    for brightness in xrange(256):
        func(identifier, brightness)
        sleep(FADE_STEP)
    sleep(FADE_WAIT)
    for brightness in xrange(255, -1, -1):
        func(identifier, brightness)
        sleep(FADE_STEP)
    sleep(FADE_WAIT)

def find_color(string):
    for key in TEXT_COLORS.keys():
        if key in string:
            return TEXT_COLORS[key]
    return ""

print "\nLEDs"
print "----"
for led in piglow.LED_AVAILABLE:
    color = find_color(led)
    print "Lighting " + BOLD_TEXT + color + led + NORMAL_TEXT + " LED."
    fade(piglow.led, led)

print "\nRings"
print "-----"
for color in piglow.RING_AVAILABLE:
    print "Lighting " + BOLD_TEXT + TEXT_COLORS[color] + color + NORMAL_TEXT \
        + " LEDs."
    fade(piglow.ring, color)

print "\nArms"
print "----"
for arm in piglow.ARM_AVAILABLE:
    print "Lighting " + BOLD_TEXT + arm + NORMAL_TEXT + " arm."
    fade(piglow.arm, arm)
