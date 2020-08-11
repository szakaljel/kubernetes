from enum import Enum

from app.ports.repos.cities import CityRepository


class RepoTypeEnum(Enum):
    cities = 'cities'


class RepoFactory:

    @staticmethod
    def get(type_: RepoTypeEnum):
        if type_ is RepoTypeEnum.cities:
            return CityRepository()
        raise RuntimeError(f'repository do not exist for type {type_}')
