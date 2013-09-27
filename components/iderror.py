class IdError(Exception):
    def __init_self(self, wrong_id, type):
        self.wrong_id = wrong_id
        self.type = type
        self.msg = "Error: Unknown " + self.type + " ID (" + self.wrong_id + ")."
