from sanic.views import HTTPMethodView
from sanic.response import json

from app.ports.services.geo_service import GeoService
from app.bl.times import TimeInCityCQ


class TimeInCityResource(HTTPMethodView):

    async def get(self, request, city_id):
        service = GeoService()
        query = TimeInCityCQ(geo_service=service)
        data = await query(city_id)
        data['time'] = data['time'].isoformat()
        return json(data)
