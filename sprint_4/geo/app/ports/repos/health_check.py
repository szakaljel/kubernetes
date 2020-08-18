from tortoise import Tortoise


class HealthCheckRepository:

    @staticmethod
    async def check_connection(connection):
        try:
            await connection.execute_query('select 1')
            return True
        except Exception:
            return False

    async def get_db_status(self):
        read = Tortoise.get_connection('read')
        write = Tortoise.get_connection('write')

        return {
            'read_connection': await self.check_connection(read),
            'write_connection': await self.check_connection(write)
        }
