from typing import Optional, Sequence, Type

from src.common.dto.user import UserCreate, UserUpdate
from src.database.models import User
from src.database.repositories.sqlalchemy_repository import \
    SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[User]):
    model: Type[User] = User

    async def create_user(self, data: UserCreate) -> Optional[User]:
        user = await self.get_user(user_id=data.user_id)

        if not user:
            return await self.create(data=data.model_dump(exclude_none=True))

        return None

    async def get_user(self, user_id: Optional[int] = None, username: Optional[str] = None) -> Optional[User]:
        if user_id:
            return await self.get(self.model.user_id.__eq__(user_id))

        return await self.get(self.model.username.__eq__(username))

    async def get_list_admin_user(self) -> Sequence[User]:
        return await self.get_many(self.model.is_admin.__eq__(True))

    async def get_list_active_user(self) -> Sequence[User]:
        return await self.get_many(self.model.is_active.__eq__(True))

    async def update_user(self, user_id: int, data: UserUpdate) -> Sequence[User]:
        return await self.update(
            self.model.user_id.__eq__(user_id),
            data=data.model_dump(exclude_none=True)
        )

    async def delete_user(self, user_id: int) -> Sequence[User]:
        return await self.delete(self.model.user_id.__eq__(user_id))
