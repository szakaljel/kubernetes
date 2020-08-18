from app.base import app
from app.ports.resources.times import TimeInCityResource
from app.error_handlers import register_error_handlers

app.add_route(TimeInCityResource.as_view(), '/times/<city_id>')
register_error_handlers(app)
