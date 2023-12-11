from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from src.common.keyboards.keyboard_generator import generate_inline_keyboard
from src.routers.client.router import client_router
from src.utils.lexicon import (DAY_PERIOD_MESSAGE, MONTH_PERIOD_MESSAGE,
                               SELECT_PERIOD_MESSAGE, YEAR_PERIOD_MESSAGE)


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'view_expenses'
)
async def process_view_expenses_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=SELECT_PERIOD_MESSAGE,
        reply_markup=generate_inline_keyboard(
            width=3,
            day_period=DAY_PERIOD_MESSAGE,
            month_period=MONTH_PERIOD_MESSAGE,
            year_period=YEAR_PERIOD_MESSAGE
        )
    )
    await callback.answer()
