from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.routers.client.router import client_router
from src.utils.lexicon import HELP_COMMAND_MESSAGE


@client_router.message(
    StateFilter(default_state),
    Command(commands='help')
)
async def process_help_command(message: Message) -> None:
    await message.answer(text=HELP_COMMAND_MESSAGE)
