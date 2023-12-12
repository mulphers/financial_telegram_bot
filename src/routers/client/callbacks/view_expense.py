from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery

from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.common.keyboards.keyboard_generator import generate_inline_keyboard
from src.routers.client.router import client_router
from src.utils.decorators import with_database
from src.utils.lexicon import (DAY_PERIOD_MESSAGE, EXPENSE_PERIOD_MESSAGE,
                               MONTH_PERIOD_MESSAGE, SELECT_PERIOD_MESSAGE,
                               YEAR_PERIOD_MESSAGE)


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


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'day_period'
)
@with_database
async def process_day_period_press(
        callback: CallbackQuery,
        uow: AbstractUnitOfWork
):
    result = await uow.expense.get_expense_for_day(user_id=callback.from_user.id)

    await callback.message.answer(text=EXPENSE_PERIOD_MESSAGE.format(
        'день',
        sum(expense.amount_expense for expense in result)
    ))
    await callback.answer()


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'month_period'
)
@with_database
async def process_month_period_press(
        callback: CallbackQuery,
        uow: AbstractUnitOfWork
):
    result = await uow.expense.get_expense_for_month(user_id=callback.from_user.id)

    await callback.message.answer(text=EXPENSE_PERIOD_MESSAGE.format(
        'месяц',
        sum(expense.amount_expense for expense in result)
    ))
    await callback.answer()


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'year_period'
)
@with_database
async def process_year_period_press(
        callback: CallbackQuery,
        uow: AbstractUnitOfWork
):
    result = await uow.expense.get_expense_for_year(user_id=callback.from_user.id)

    await callback.message.answer(text=EXPENSE_PERIOD_MESSAGE.format(
        'год',
        sum(expense.amount_expense for expense in result)
    ))
    await callback.answer()
