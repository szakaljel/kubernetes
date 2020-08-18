from sanic.exceptions import NotFound, InvalidUsage

from app.bl.exceptions import BLObjectCreationError, BLObjectDoesNotExistsError


async def http_404_error_handler(request, exception):
    raise NotFound(str(exception))


async def http_400_error_handler(request, exception):
    raise InvalidUsage(str(exception))


def register_error_handlers(app):
    app.error_handler.add(BLObjectDoesNotExistsError, http_404_error_handler)
    app.error_handler.add(BLObjectCreationError, http_400_error_handler)
