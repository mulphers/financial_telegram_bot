from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from src.common.types import EntryType


class AbstractRepository(ABC, Generic[EntryType]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @abstractmethod
    async def create(self, data: dict[str, Any]) -> EntryType:
        raise NotImplementedError

    @abstractmethod
    async def get(self, *clauses: Any) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get_many(self, *clauses: Any, limit: Optional[int] = None) -> Sequence[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *clauses: Any, data: dict[str, Any]) -> Sequence[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *clauses: Any) -> Sequence[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def create_relationship(self, model: Any, data: dict[str, Any]) -> None:
        raise NotImplementedError
