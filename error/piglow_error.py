#!/usr/bin/env python
"""PiGlow error module."""

class PiGlowError(Exception):
    """PiGlow error."""
    def __init__(self, args):
        Exception.__init__(self, args)
        self.message = "PiGlowError."
