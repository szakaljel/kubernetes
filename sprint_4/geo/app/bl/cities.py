class CityDetailCQ:

    def __init__(self, city_repo):
        self._city_repo = city_repo

    def __call__(self, city_id):
        return self._city_repo.get_city(city_id)
