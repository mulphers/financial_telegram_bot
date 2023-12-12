from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from src.common.fsm.expense_filling_state import FSMExpenseFillForm
from src.routers.client.router import client_router
from src.utils.lexicon import WRITE_AMOUNT_EXPENSE_MESSAGE


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'add_expense'
)
async def process_add_expense_press(
        callback: CallbackQuery,
        state: FSMContext
):
    await callback.message.answer(text=WRITE_AMOUNT_EXPENSE_MESSAGE)
    await state.set_state(FSMExpenseFillForm.fill_amount_expense)
    await callback.answer()
