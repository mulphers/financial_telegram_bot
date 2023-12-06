from aiogram import F
from aiogram.types import CallbackQuery

from src.common.keyboards.keyboard_generator import generate_inline_keyboard
from src.routers.client.router import client_router
from src.utils.lexicon import (ADD_EXPENSE_MESSAGE, FINANCIAL_ACTIONS_MESSAGE,
                               REMOVE_EXPENSE_MESSAGE)


@client_router.callback_query(F.data == 'actions_on_finances')
async def process_actions_on_finances_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=FINANCIAL_ACTIONS_MESSAGE,
        reply_markup=generate_inline_keyboard(
            width=2,
            add_expense=ADD_EXPENSE_MESSAGE,
            remove_expense=REMOVE_EXPENSE_MESSAGE
        )
    )
    await callback.answer()
