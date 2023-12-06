from typing import Optional

from src.common.dto.user import UserCreate, UserDTO, UserUpdate
from src.database.models import User
from src.database.repositories.sqlalchemy_repository import \
    SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    async def create_user(self, data: UserCreate):
        user = await self.get_user(user_id=data.user_id)

        if not user:
            return await self.create(data=data.model_dump(exclude_none=True))

        return None

    async def get_user(self, user_id: Optional[int] = None, username: Optional[str] = None) -> UserDTO:
        if user_id:
            return await self.get(
                field=self.model.user_id,
                value=user_id
            )

        return await self.get(
            field=self.model.username,
            value=username
        )

    async def get_list_admin_user(self):
        return await self.get_many(
            field=self.model.is_admin,
            value=True
        )

    async def update_user(self, user_id: int, data: UserUpdate):
        return await self.update(
            field=self.model.user_id,
            value=user_id,
            data=data.model_dump(exclude_none=True)
        )

    async def delete_user(self, user_id: int):
        return await self.delete(
            field=self.model.user_id,
            value=user_id
        )
