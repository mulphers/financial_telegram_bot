from aiogram.filters import KICKED, MEMBER, ChatMemberUpdatedFilter
from aiogram.types import Message

from src.common.dto.user import UserUpdate
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.client import client_router
from src.utils.decorators import with_database


@client_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
@with_database
async def process_blocked_bot(
        message: Message,
        uow: AbstractUnitOfWork
) -> None:
    await uow.user.update_user(
        user_id=message.from_user.id,
        data=UserUpdate(
            is_active=False
        )
    )


@client_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
@with_database
async def process_unblocked_bot(
        message: Message,
        uow: AbstractUnitOfWork
) -> None:
    await uow.user.update_user(
        user_id=message.from_user.id,
        data=UserUpdate(
            is_active=True
        )
    )
