from tortoise.contrib.sanic import register_tortoise
from app.base import app
from app.ports.resources.cities import CityDetailResource
from app.config import config


app.add_route(CityDetailResource.as_view(), '/cities/<city_id>')

register_tortoise(
    app=app,
    db_url=f'mysql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}',
    modules={"models": ["app.ports.repos.models"]},
    generate_schemas=False
)
