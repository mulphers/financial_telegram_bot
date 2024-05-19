from typing import Annotated

from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message
from fast_depends import Depends, inject

from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway
from src.routers.client.router import client_router
from src.utils.lexicon import PROFILE_COMMAND_MESSAGE


@client_router.message(
    StateFilter(default_state),
    Command(commands='profile')
)
@inject
async def process_profile_command(
        message: Message,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    user_repository = gateway.user_repository()

    user = await user_repository.get_user(
        user_id=message.from_user.id
    )

    await message.answer(
        text=PROFILE_COMMAND_MESSAGE.format(
            user.user_id,
            user.created_at.date().strftime('%d-%m-%Y')
        )
    )
