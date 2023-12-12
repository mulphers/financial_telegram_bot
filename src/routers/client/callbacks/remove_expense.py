from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from src.common.callback_factory.expense import ExpenseCallbackFactory
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.common.keyboards.keyboard_generator import \
    generate_remove_expense_keyboard
from src.routers.client.router import client_router
from src.utils.decorators import with_database
from src.utils.lexicon import (EXPENSE_DELETE_MESSAGE,
                               EXPENSE_DELETE_WARNING_MESSAGE,
                               SELECT_DELETE_EXPENSE_MESSAGE)


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'remove_expense'
)
@with_database
async def process_remove_expense_press(
        callback: CallbackQuery,
        uow: AbstractUnitOfWork
):
    result = await uow.expense.get_expense_for_day(user_id=callback.from_user.id)

    await callback.message.answer(
        text=SELECT_DELETE_EXPENSE_MESSAGE,
        reply_markup=generate_remove_expense_keyboard(result)
    )
    await callback.answer()


@client_router.callback_query(
    StateFilter(default_state),
    ExpenseCallbackFactory.filter()
)
@with_database
async def process_remove_expense(
        callback: CallbackQuery,
        callback_data: ExpenseCallbackFactory,
        uow: AbstractUnitOfWork

):
    result = await uow.expense.delete_expense(expense_id=callback_data.expense_id)

    if result:
        await callback.message.edit_text(text=EXPENSE_DELETE_MESSAGE)
    else:
        await callback.message.edit_text(text=EXPENSE_DELETE_WARNING_MESSAGE)

    await callback.answer()
