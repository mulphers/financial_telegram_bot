from typing import Any, Optional, Sequence, Type

from sqlalchemy import ColumnExpressionArgument, delete, insert, select, update

from src.common.interfaces.abstract_repository import AbstractRepository
from src.common.types import Model


class SQLAlchemyRepository(AbstractRepository[Model]):
    model: Type[Model]

    async def create(self, data: dict[str, Any]) -> Model:
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalar_one()

    async def get(self, *clauses: ColumnExpressionArgument[bool]) -> Optional[Model]:
        stmt = (
            select(self.model)
            .where(*clauses)
        )

        return (await self.session.execute(stmt)).scalars().first()

    async def get_many(self, *clauses: ColumnExpressionArgument[bool], limit: Optional[int] = None) -> Sequence[Model]:
        if limit:
            stmt = (
                select(self.model)
                .where(*clauses)
                .limit(limit)
            )
        else:
            stmt = (
                select(self.model)
                .where(*clauses)
            )

        return (await self.session.execute(stmt)).scalars().all()

    async def update(self, *clauses: ColumnExpressionArgument[bool], data: dict[str, Any]) -> Sequence[Model]:
        stmt = (
            update(self.model)
            .where(*clauses)
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalars().all()

    async def delete(self, *clauses: ColumnExpressionArgument[bool]) -> Sequence[Model]:
        stmt = (
            delete(self.model)
            .where(*clauses)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalars().all()

    async def create_relationship(self, model: Any, data: dict[str, Any]) -> None:
        stmt = (
            insert(model)
            .values(**data)
            .returning(model)
        )

        await self.session.execute(stmt)
