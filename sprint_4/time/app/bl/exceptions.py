class BLError(Exception):
    pass


class BLObjectDoesNotExistsError(BLError):
    pass


class BLUpstreamError(BLError):
    pass
