from typing import Any, Optional, Sequence, Type

from sqlalchemy import ColumnExpressionArgument, delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.interfaces.abstract_repository import AbstractRepository
from src.common.types import ModelType


class SQLAlchemyRepository(AbstractRepository[ModelType, AsyncSession, ColumnExpressionArgument[bool]]):
    model: Type[ModelType]

    async def create(self, data: dict[str, Any]) -> Optional[ModelType]:
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalar_one()

    async def get(self, *clauses: ColumnExpressionArgument[bool]) -> Optional[ModelType]:
        stmt = (
            select(self.model)
            .where(*clauses)
        )

        return (await self.session.execute(stmt)).scalars().first()

    async def get_many(
            self,
            *clauses: ColumnExpressionArgument[bool],
            offset: Optional[int] = None,
            limit: Optional[int] = None
    ) -> Sequence[ModelType]:
        stmt = (
            select(self.model)
            .where(*clauses)
            .offset(offset)
            .limit(limit)
        )

        return (await self.session.execute(stmt)).scalars().all()

    async def update(self, *clauses: ColumnExpressionArgument[bool], data: dict[str, Any]) -> Sequence[ModelType]:
        stmt = (
            update(self.model)
            .where(*clauses)
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalars().all()

    async def delete(self, *clauses: ColumnExpressionArgument[bool]) -> Sequence[ModelType]:
        stmt = (
            delete(self.model)
            .where(*clauses)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalars().all()
