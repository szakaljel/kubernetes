from sanic.views import HTTPMethodView
from sanic.response import json
from app.bl.cities import CityDetailCQ
from app.ports.repos.factory import RepoFactory, RepoTypeEnum


class CityDetailResource(HTTPMethodView):

    async def get(self, request, city_id, *args, **kwargs):
        city_repo = RepoFactory.get(RepoTypeEnum.cities)
        city_detail_query = CityDetailCQ(city_repo)
        city_detail = await city_detail_query(city_id)
        return json(city_detail)
