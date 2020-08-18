from datetime import datetime
from pytz import timezone


class TimeInCityCQ:

    def __init__(self, geo_service):
        self._geo_service = geo_service

    async def __call__(self, city_id):
        city = await self._geo_service.get_city(city_id)
        time = datetime.now(timezone(city['time_zone']))
        return {
            **city,
            'time': time
        }
