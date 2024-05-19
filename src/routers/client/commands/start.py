from typing import Annotated

from aiogram.filters.command import CommandStart
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from fast_depends import Depends, inject

from src.common.dto.user import UserCreate
from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway
from src.routers.client.router import client_router
from src.utils.lexicon import START_COMMAND_MESSAGE


@client_router.message(
    StateFilter(default_state),
    CommandStart()
)
@inject
async def process_start_command(
        message: Message,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    user_repository = gateway.user_repository()

    await user_repository.create_user(
        data=UserCreate(
            user_id=message.from_user.id,
            username=message.from_user.username
        )
    )

    await message.answer(text=START_COMMAND_MESSAGE)
