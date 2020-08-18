class BLError(Exception):
    pass


class BLObjectDoesNotExistsError(BLError):
    pass


class BLObjectCreationError(BLError):
    pass
