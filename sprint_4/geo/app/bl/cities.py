class CityDetailCQ:

    def __init__(self, city_repo):
        self._city_repo = city_repo

    async def __call__(self, city_id):
        return await self._city_repo.get_city(city_id)


class CitiesListCQ:

    def __init__(self, city_repo):
        self._city_repo = city_repo

    async def __call__(self):
        return await self._city_repo.get_cities()


class CityCreateCQ:

    def __init__(self, city_repo):
        self._city_repo = city_repo

    async def __call__(self, data):
        return await self._city_repo.create_city(**data)
