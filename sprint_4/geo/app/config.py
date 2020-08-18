from app.utils import get_env_var
from collections import namedtuple

_BaseConfig = namedtuple('BaseConfig', ('host', 'port', 'db_user', 'db_password',
                                        'db_host_read', 'db_host_write', 'db_port', 'db_name'))


class Config(_BaseConfig):
    _prefix = 'KU_GEO'

    @classmethod
    def from_env(cls):
        host = get_env_var(cls._prefix, 'host', default='0.0.0.0')
        port = get_env_var(cls._prefix, 'port', default=8000)
        db_host_read = get_env_var(cls._prefix, 'db_host_read', raise_ex=True)
        db_host_write = get_env_var(cls._prefix, 'db_host_write', raise_ex=True)
        db_port = get_env_var(cls._prefix, 'db_port', default=3306)
        db_user = get_env_var(cls._prefix, 'db_user', raise_ex=True)
        db_password = get_env_var(cls._prefix, 'db_password', raise_ex=True)
        db_name = get_env_var(cls._prefix, 'db_name', default='kube')
        return cls(
            host=host,
            port=port,
            db_host_read=db_host_read,
            db_host_write=db_host_write,
            db_port=db_port,
            db_user=db_user,
            db_password=db_password,
            db_name=db_name
        )


config = Config.from_env()
