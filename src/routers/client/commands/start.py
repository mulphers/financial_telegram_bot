from aiogram.filters.command import CommandStart
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.common.dto.user import UserCreate
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.client.router import client_router
from src.utils.decorators import with_database
from src.utils.lexicon import START_COMMAND_MESSAGE


@client_router.message(
    StateFilter(default_state),
    CommandStart()
)
@with_database
async def process_start_command(
        message: Message,
        uow: AbstractUnitOfWork
) -> None:
    await uow.user.create_user(
        data=UserCreate(
            user_id=message.from_user.id,
            username=message.from_user.username
        )
    )

    await message.answer(text=START_COMMAND_MESSAGE)
