from aiogram.filters.command import Command
from aiogram.types import Message

from src.common.keyboards.keyboard_generator import generate_inline_keyboard
from src.routers.client.router import client_router
from src.utils.lexicon import (ACTION_COMMAND_MESSAGE,
                               ACTION_ON_FINANCES_MESSAGE,
                               VIEW_EXPENSES_MESSAGE)


@client_router.message(Command(commands='action'))
async def process_action_command(message: Message):
    await message.answer(
        text=ACTION_COMMAND_MESSAGE,
        reply_markup=generate_inline_keyboard(
            width=2,
            actions_on_finances=ACTION_ON_FINANCES_MESSAGE,
            view_expenses=VIEW_EXPENSES_MESSAGE
        )
    )