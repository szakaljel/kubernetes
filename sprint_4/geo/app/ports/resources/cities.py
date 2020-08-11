from sanic.views import HTTPMethodView
from sanic.response import json
from app.bl.cities import CityDetailCQ
from app.ports.repos.cities import CityRepository


class CityDetailResource(HTTPMethodView):

    async def get(self, request, city_id, *args, **kwargs):
        city_repo = CityRepository()
        city_detail_query = CityDetailCQ(city_repo)
        return json(city_detail_query(city_id))
