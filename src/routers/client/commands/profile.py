from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.client.router import client_router
from src.utils.decorators import with_database
from src.utils.lexicon import PROFILE_COMMAND_MESSAGE


@client_router.message(
    StateFilter(default_state),
    Command(commands='profile')
)
@with_database
async def process_profile_command(
        message: Message,
        uow: AbstractUnitOfWork
):
    user = await uow.user.get_user(
        user_id=message.from_user.id
    )

    await message.answer(
        text=PROFILE_COMMAND_MESSAGE.format(
            user.user_id,
            user.created_at.date().strftime('%d-%m-%Y')
        )
    )
