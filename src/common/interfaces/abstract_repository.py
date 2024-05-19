from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Sequence, Type

from src.common.types import ColumnType, EntryType, SessionType


class AbstractRepository(ABC, Generic[EntryType, SessionType, ColumnType]):
    model: Type[EntryType]

    def __init__(self, session: SessionType) -> None:
        self.session = session

    @abstractmethod
    async def create(self, data: dict[str, Any]) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, *clauses: ColumnType) -> Optional[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def get_many(
            self,
            *clauses: ColumnType,
            offset: Optional[int] = None,
            limit: Optional[int] = None
    ) -> Sequence[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *clauses: ColumnType, data: dict[str, Any]) -> Sequence[EntryType]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *clauses: ColumnType) -> Sequence[EntryType]:
        raise NotImplementedError
