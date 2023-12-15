from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.common.keyboards.keyboard_generator import generate_inline_keyboard
from src.routers.client.router import client_router
from src.utils.lexicon import (ACTION_COMMAND_MESSAGE,
                               ACTION_ON_FINANCES_MESSAGE,
                               VIEW_EXPENSES_MESSAGE)


@client_router.message(
    StateFilter(default_state),
    Command(commands='action')
)
async def process_action_command(message: Message) -> None:
    await message.answer(
        text=ACTION_COMMAND_MESSAGE,
        reply_markup=generate_inline_keyboard(
            width=2,
            actions_on_finances=ACTION_ON_FINANCES_MESSAGE,
            view_expenses=VIEW_EXPENSES_MESSAGE
        )
    )
