from typing import Any, Optional

from sqlalchemy import delete, insert, select, update

from src.common.interfaces.abstract_repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create(self, data: dict[str, Any]):
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalar_one()

    async def get(self, field: Any, value: Any):
        stmt = (
            select(self.model)
            .where(field == value)  # type: ignore
        )

        return (await self.session.execute(stmt)).scalars().first()

    async def get_many(self, field: Any, value: Any, limit: Optional[int] = None):
        if limit:
            stmt = (
                select(self.model)
                .where(field == value)  # type: ignore
                .limit(limit)
            )
        else:
            stmt = (
                select(self.model)
                .where(field == value)  # type: ignore
            )

        return (await self.session.execute(stmt)).scalars().all()

    async def update(self, field: Any, value: Any, data: dict[str, Any]):
        stmt = (
            update(self.model)
            .where(field == value)  # type: ignore
            .values(**data)
            .returning(self.model)
        )

        return (await self.session.execute(stmt)).scalars().all()

    async def delete(self, field: Any, value: Any):
        stmt = (
            delete(self.model)
            .where(field == value)  # type: ignore
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
