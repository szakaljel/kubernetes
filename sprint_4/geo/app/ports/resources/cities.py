from sanic.views import HTTPMethodView
from sanic.response import json
from app.bl.cities import CityDetailCQ, CityCreateCQ, CitiesListCQ
from app.ports.repos.factory import RepoFactory, RepoTypeEnum


class CityDetailResource(HTTPMethodView):
    async def get(self, request, city_id, *args, **kwargs):
        city_repo = RepoFactory.get(RepoTypeEnum.cities)
        city_detail_query = CityDetailCQ(city_repo)
        city_detail = await city_detail_query(city_id)
        return json(city_detail)


class CitiesResource(HTTPMethodView):
    async def post(self, request, *args, **kwargs):
        city_repo = RepoFactory.get(RepoTypeEnum.cities)
        city_create_command = CityCreateCQ(city_repo)

        data = request.json
        city_detail = await city_create_command(data)
        return json(city_detail)

    async def get(self, request, *args, **kwargs):
        city_repo = RepoFactory.get(RepoTypeEnum.cities)
        cities_query = CitiesListCQ(city_repo)
        cities = await cities_query()
        return json(cities)
