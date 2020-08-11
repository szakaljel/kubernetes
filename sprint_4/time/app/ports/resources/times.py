from sanic.views import HTTPMethodView
from sanic.response import json

from app.ports.services.factory import ServiceFactory, ServiceTypeEnum
from app.bl.times import TimeInCityCQ


class TimeInCityResource(HTTPMethodView):

    async def get(self, request, city_id):
        service = ServiceFactory.get(ServiceTypeEnum.geo)
        query = TimeInCityCQ(geo_service=service)
        data = await query(city_id)
        data['time'] = data['time'].isoformat()
        return json(data)
