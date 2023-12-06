from abc import ABC, abstractmethod
from typing import Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @abstractmethod
    async def create(self, data: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def get(self, field: Any, value: Any):
        raise NotImplementedError

    @abstractmethod
    async def get_many(self, field: Any, value: Any, limit: Optional[int] = None):
        raise NotImplementedError

    @abstractmethod
    async def update(self, field: Any, value: Any, data: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, field: Any, value: Any):
        raise NotImplementedError

    @abstractmethod
    async def create_relationship(self, model: Any, data: dict[str, Any]):
        raise NotImplementedError
