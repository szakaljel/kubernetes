from sanic.views import HTTPMethodView
from sanic.response import json

from app.bl.health_check import DBHealthCheckCQ
from app.ports.repos.factory import RepoFactory, RepoTypeEnum


class HealthCheckResource(HTTPMethodView):
    async def get(self, request, *args, **kwargs):
        health_check_repo = RepoFactory.get(RepoTypeEnum.health_check)
        health_check_query = DBHealthCheckCQ(health_check_repo)
        health = await health_check_query()
        health['api'] = True

        status = 200
        if not all(health.values()):
            status = 503
        return json(health, status=status)
