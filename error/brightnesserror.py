from pyglowerror import PyGlowError

class BrightnessError(PyGlowError):
    def __init__(self, wrong_brightness):
        PyGlowError.__init__(self, ("brightness", wrong_brightness))
        self.wrong_brightness = wrong_brightness
        self.message = "Error: Invalid brightness value. (" \
            + str(self.wrong_brightness) + ")"
