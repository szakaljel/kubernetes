from tortoise.exceptions import IntegrityError

from app.ports.repos.read_models import City as CityRead
from app.ports.repos.write_models import City as CityWrite

from app.bl.exceptions import BLObjectCreationError, BLObjectDoesNotExistsError


class CityRepository:

    @staticmethod
    def _city_to_dict(city):
        return {
            'id': city.id,
            'name': city.name,
            'time_zone': city.time_zone,
            'population': city.population
        }

    async def get_city(self, city_id):
        city = await CityRead.filter(id=city_id).first()
        if city is None:
            raise BLObjectDoesNotExistsError(f'city with id {city_id} does not exist')
        return self._city_to_dict(city)

    async def get_cities(self):
        cities = await CityRead.all()
        return [self._city_to_dict(city) for city in cities]

    async def create_city(self, name, population, time_zone):
        city = CityWrite(name=name, population=population, time_zone=time_zone)
        try:
            await city.save()
        except IntegrityError as ex:
            raise BLObjectCreationError(f'city {name} can not be created') from ex
        return self._city_to_dict(city)
