from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.common.fsm.expense_filling_state import FSMExpenseFillForm
from src.routers.client.router import client_router
from src.utils.lexicon import WRITE_AMOUNT_EXPENSE_MESSAGE


@client_router.callback_query(F.data == 'add_expense')
async def process_add_expense_press(
        callback: CallbackQuery,
        state: FSMContext
):
    await callback.message.edit_text(
        text=WRITE_AMOUNT_EXPENSE_MESSAGE
    )
    await state.set_state(FSMExpenseFillForm.fill_amount_expense)
    await callback.answer()
