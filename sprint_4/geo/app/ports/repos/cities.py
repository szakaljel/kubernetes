from app.ports.repos.models import City


class CityRepository:

    async def get_city(self, city_id):
        city = await City.filter(id=city_id).first()
        return {
            'id': city.id,
            'name': city.name,
            'time_zone': city.time_zone,
            'population': city.population
        }
