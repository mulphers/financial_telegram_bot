from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.utils.decorators import with_database


class IsAdminFilter(BaseFilter):
    @with_database
    async def __call__(
            self,
            message: Message,
            uow: AbstractUnitOfWork,
            *args,
            **kwargs
    ):
        return message.from_user.id in map(lambda obj: obj.user_id,
                                           await uow.user.get_list_admin_user()
                                           )
