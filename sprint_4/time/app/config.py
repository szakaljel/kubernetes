from app.utils import get_env_var
from collections import namedtuple

_BaseConfig = namedtuple('BaseConfig', ('host', 'port', 'geo_service_url'))


class Config(_BaseConfig):
    _prefix = 'KU_TIME'

    @classmethod
    def from_env(cls):
        host = get_env_var(cls._prefix, 'host', default='0.0.0.0')
        port = get_env_var(cls._prefix, 'port', default=7000)
        geo_service_url = get_env_var(cls._prefix, 'geo_service_url', raise_ex=True)
        return cls(
            host=host,
            port=port,
            geo_service_url=geo_service_url
        )


config = Config.from_env()
