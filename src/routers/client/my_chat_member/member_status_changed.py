from typing import Annotated

from aiogram.filters import KICKED, MEMBER, ChatMemberUpdatedFilter
from aiogram.types import Message
from fast_depends import Depends, inject

from src.common.dto.user import UserUpdate
from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway
from src.routers.client import client_router


@client_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
@inject
async def process_blocked_bot(
        message: Message,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    user_repository = gateway.user_repository()

    await user_repository.update_user(
        user_id=message.from_user.id,
        data=UserUpdate(
            is_active=False
        )
    )


@client_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
@inject
async def process_unblocked_bot(
        message: Message,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    user_repository = gateway.user_repository()

    await user_repository.update_user(
        user_id=message.from_user.id,
        data=UserUpdate(
            is_active=True
        )
    )
