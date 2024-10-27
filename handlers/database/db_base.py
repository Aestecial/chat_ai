import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._database = os.getenv("DB_NAME")
        self._host = os.getenv("DB_HOST")
        self._port = os.getenv("DB_PORT")
        self._connection = None

    async def __aenter__(self):
        try:
            self._connection = await asyncpg.connect(
                user=self._user,
                password=self._password,
                database=self._database,
                host=self._host,
                port=self._port
            )
            return self
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._connection:
            try:
                await self._connection.close()
            except Exception as e:
                print(f"Ошибка при отключении от базы данных: {e}")
                raise

    async def execute(self, query, *args):
        """Выполняет запрос без возвращения результатов (например, INSERT, UPDATE)."""
        try:
            await self._connection.execute(query, *args)
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise

    async def fetch(self, query, *args):
        """Выполняет запрос и возвращает результаты (например, SELECT)."""
        try:
            records = await self._connection.fetch(query, *args)
            return records
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise

    async def fetchrow(self, query, *args):
        """Выполняет запрос и возвращает одну строку результата."""
        try:
            record = await self._connection.fetchrow(query, *args)
            return record
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise

    async def fetchval(self, query, *args):
        """Выполняет запрос и возвращает одно значение."""
        try:
            value = await self._connection.fetchval(query, *args)
            return value
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise
