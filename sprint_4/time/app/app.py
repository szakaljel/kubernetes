from app.base import app
from app.ports.resources.times import TimeInCityResource

app.add_route(TimeInCityResource.as_view(), '/times/<city_id>')
