#!/usr/bin/env python
"""ID error module."""
from error.piglow_error import PiGlowError

class IdError(PiGlowError):
    """ID error."""

    def __init__(self, id_type, wrong_id):
        PiGlowError.__init__(self, (id_type, wrong_id))
        self.wrong_id = wrong_id
        self.id_type = id_type
        self.message = "Unknown " + str(self.id_type) + " ID (" \
            + str(self.wrong_id) + ")."
