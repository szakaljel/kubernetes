from sanic.exceptions import NotFound, ServiceUnavailable

from app.bl.exceptions import BLObjectDoesNotExistsError, BLUpstreamError


async def http_404_error_handler(request, exception):
    raise NotFound(str(exception))


async def http_503_error_handler(request, exception):
    raise ServiceUnavailable(str(exception))


def register_error_handlers(app):
    app.error_handler.add(BLObjectDoesNotExistsError, http_404_error_handler)
    app.error_handler.add(BLUpstreamError, http_503_error_handler)
