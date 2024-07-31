import redis
import os
from hello_api.repo import RepositoryInterface


class RedisRepository(RepositoryInterface):
    host: str = os.environ.get('DB_HOST', 'localhost')
    port: str = os.environ.get('DB_PORT', '6379')
    default_language: str = os.environ.get('DEFAULT_LANG', 'english')

    def __init__(self, client=None) -> None:
        if client is None:
            self.client = redis.Redis(host=self.host, port=self.port)
        else:
            self.client = client

    def translate(self, language: str, word: str) -> str:
        lang = language.lower() if language else self.default_language
        key = f'{word.lower()}:{lang}'
        return self.client.get(key)
