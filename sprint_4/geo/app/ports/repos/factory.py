from enum import Enum

from app.ports.repos.cities import CityRepository
from app.ports.repos.health_check import HealthCheckRepository


class RepoTypeEnum(Enum):
    cities = 'cities'
    health_check = 'health_check'


class RepoFactory:

    @staticmethod
    def get(type_: RepoTypeEnum):
        if type_ is RepoTypeEnum.cities:
            return CityRepository()
        if type_ is RepoTypeEnum.health_check:
            return HealthCheckRepository()
        raise RuntimeError(f'repository do not exist for type {type_}')
