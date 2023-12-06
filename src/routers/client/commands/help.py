from aiogram.filters.command import Command
from aiogram.types import Message

from src.routers.client.router import client_router
from src.utils.lexicon import HELP_COMMAND_MESSAGE


@client_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=HELP_COMMAND_MESSAGE)
