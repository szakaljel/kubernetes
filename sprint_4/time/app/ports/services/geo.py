from typing import AsyncGenerator
from abc import ABC, abstractmethod
import asyncio

import aiohttp
import async_timeout

from app.config import config


class AsyncBaseSession(ABC):

    @abstractmethod
    async def _prepare_gen(self) -> AsyncGenerator:
        pass

    async def __aenter__(self):
        self._gen = self._prepare_gen()
        return await self._gen.__anext__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self._gen.__anext__()
        except StopAsyncIteration:
            return
        else:
            raise RuntimeError("generator didn't stop")


class AsyncSession(AsyncBaseSession):

    def __init__(self, timeout=10):
        super().__init__()
        self._timeout = timeout

    async def _prepare_gen(self):
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(self._timeout):
                yield session


class AsyncRequest:

    @staticmethod
    async def get(url, timeout=10):
        async with AsyncSession(timeout=timeout) as session:
            async with session.get(url) as response:
                return await response.json()


class GeoService:

    def __init__(self):
        self._url = config.geo_service_url

    async def get_city(self, city_id):
        return await AsyncRequest.get(f'{self._url}/cities/{city_id}')
