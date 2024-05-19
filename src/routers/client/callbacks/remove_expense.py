from typing import Annotated

from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery
from fast_depends import Depends, inject

from src.common.callback_factory.expense import ExpenseCallbackFactory
from src.common.keyboards.keyboard_generator import \
    generate_remove_expense_keyboard
from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway
from src.routers.client.router import client_router
from src.utils.lexicon import (EXPENSE_DELETE_MESSAGE,
                               EXPENSE_DELETE_WARNING_MESSAGE,
                               SELECT_DELETE_EXPENSE_MESSAGE)


@client_router.callback_query(
    StateFilter(default_state),
    F.data == 'remove_expense'
)
@inject
async def process_remove_expense_press(
        callback: CallbackQuery,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    expense_repository = gateway.expense_repository()

    result = await expense_repository.get_expense_for_day(user_id=callback.from_user.id)

    await callback.message.answer(
        text=SELECT_DELETE_EXPENSE_MESSAGE,
        reply_markup=generate_remove_expense_keyboard(result)
    )
    await callback.answer()


@client_router.callback_query(
    StateFilter(default_state),
    ExpenseCallbackFactory.filter()
)
@inject
async def process_remove_expense(
        callback: CallbackQuery,
        callback_data: ExpenseCallbackFactory,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]

) -> None:
    expense_repository = gateway.expense_repository()

    result = await expense_repository.delete_expense(expense_id=callback_data.expense_id)

    if result:
        await callback.message.edit_text(text=EXPENSE_DELETE_MESSAGE)
    else:
        await callback.message.edit_text(text=EXPENSE_DELETE_WARNING_MESSAGE)

    await callback.answer()
