from aiogram import Bot
from aiogram.types import BotCommand

from src.utils.lexicon import COMMAND_MENU


async def set_command_menu(bot: Bot):
    command = [
        BotCommand(
            command=command,
            description=description
        )
        for command, description in COMMAND_MENU.items()
    ]

    await bot.set_my_commands(command)
