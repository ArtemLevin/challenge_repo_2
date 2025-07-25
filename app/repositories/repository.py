from typing import Protocol, TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class CacheRepository(Protocol, Generic[T]):
    async def get(self, key: str) -> T | None:  ...
    async def set(self, key: str, value: T, ttl: int | None = None) -> bool: ...
    async def setex(self, key: str, ttl: int, value: T) -> bool: ...
    async def rpush(self, key: str, value: T) -> int: ...
    async def lpop(self, key: str) -> T | None: ...
    async def llen(self, key: str) -> int: ...
    async def exists(self, key: str) -> bool: ...