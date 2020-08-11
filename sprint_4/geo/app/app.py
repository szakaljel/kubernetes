from app.base import app
from app.ports.resources.cities import CityDetailResource

app.add_route(CityDetailResource.as_view(), '/cities/<city_id>')
