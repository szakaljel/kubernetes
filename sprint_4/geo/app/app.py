from tortoise.contrib.sanic import register_tortoise
from app.base import app
from app.ports.resources.cities import CityDetailResource, CitiesResource
from app.ports.resources.health_check import HealthCheckResource
from app.config import config
from app.error_handlers import register_error_handlers

app.add_route(CitiesResource.as_view(), '/cities')
app.add_route(CityDetailResource.as_view(), '/cities/<city_id>')
app.add_route(HealthCheckResource.as_view(), '/health')

register_tortoise(
    app=app,
    config={
        'connections': {
            'read': f'mysql://{config.db_user}:{config.db_password}@'
                    f'{config.db_host_read}:{config.db_port}/{config.db_name}?charset=utf8',
            'write': f'mysql://{config.db_user}:{config.db_password}@'
                     f'{config.db_host_write}:{config.db_port}/{config.db_name}?charset=utf8'
        },
        "apps": {
            'read': {'models': ['app.ports.repos.read_models'], 'default_connection': 'read'},
            'write': {"models": ['app.ports.repos.write_models'], 'default_connection': 'write'}
        }
    },
    generate_schemas=False
)

register_error_handlers(app)
