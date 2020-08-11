class CityRepository:

    def get_city(self, city_id):
        return {
            'id': city_id,
            'name': 'Gdańsk',
            'time_zone': 'Europe/Warsaw'
        }
