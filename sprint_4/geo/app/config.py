from app.utils import get_env_var
from collections import namedtuple

_BaseConfig = namedtuple('BaseConfig', ('host', 'port', 'db_user', 'db_password', 'db_host', 'db_port'))


class Config(_BaseConfig):
    _prefix = 'KU_GEO'

    @classmethod
    def from_env(cls):
        host = get_env_var(cls._prefix, 'host', default='0.0.0.0')
        port = get_env_var(cls._prefix, 'port', default=8000)
        db_host = get_env_var(cls._prefix, 'db_host', raise_ex=True)
        db_port = get_env_var(cls._prefix, 'db_port', default=3306)
        db_user = get_env_var(cls._prefix, 'db_user', raise_ex=True)
        db_password = get_env_var(cls._prefix, 'db_password', raise_ex=True)
        return cls(
            host=host,
            port=port,
            db_host=db_host,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password
        )


config = Config.from_env()
