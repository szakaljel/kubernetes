class CityDetailCQ:

    def __init__(self, city_repo):
        self._city_repo = city_repo

    async def __call__(self, city_id):
        return await self._city_repo.get_city(city_id)
