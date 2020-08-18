from enum import Enum

from app.ports.services.geo import GeoService


class ServiceTypeEnum(Enum):
    geo = 'geo'


class ServiceFactory:

    @staticmethod
    def get(type_: ServiceTypeEnum):
        if type_ is ServiceTypeEnum.geo:
            return GeoService()
        raise RuntimeError(f'service do not exist for type {type_}')
