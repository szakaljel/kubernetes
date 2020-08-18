class DBHealthCheckCQ:

    def __init__(self, health_check_repo):
        self._health_check_repo = health_check_repo

    async def __call__(self):
        return await self._health_check_repo.get_db_status()
