from pyglowerror import PyGlowError

class IdError(PyGlowError):
    def __init__(self, id_type, wrong_id):
        PyGlowError.__init__(self, (id_type, wrong_id))
        self.wrong_id = wrong_id
        self.id_type = id_type
        self.message = "Error: Unknown " + str(self.id_type) + " ID (" + str(self.wrong_id) + ")."
