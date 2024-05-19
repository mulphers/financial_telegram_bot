from typing import Annotated

from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from fast_depends import Depends, inject

from src.common.dto.expense import ExpanseCreate
from src.common.fsm.expense_filling_state import FSMExpenseFillForm
from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway
from src.routers.client.router import client_router
from src.utils.lexicon import (EXPENSE_SAVED_MESSAGE,
                               WARNING_AMOUNT_EXPENSE_MESSAGE,
                               WARNING_SHORT_DESCRIPTION_MESSAGE,
                               WRITE_SHORT_DESCRIPTION_MESSAGE)


@client_router.message(
    StateFilter(FSMExpenseFillForm.fill_amount_expense),
    F.text.regexp(r'^\d+(\.\d+)?$')
)
async def process_amount_expense_message(
        message: Message,
        state: FSMContext
) -> None:
    await state.update_data(amount_expense=float(message.text))
    await message.answer(text=WRITE_SHORT_DESCRIPTION_MESSAGE)
    await state.set_state(FSMExpenseFillForm.fill_short_description)


@client_router.message(StateFilter(FSMExpenseFillForm.fill_amount_expense))
async def warning_amount_expense_message(message: Message) -> None:
    await message.answer(text=WARNING_AMOUNT_EXPENSE_MESSAGE)


@client_router.message(
    StateFilter(FSMExpenseFillForm.fill_short_description),
    F.text
)
@inject
async def process_short_description_expense_message(
        message: Message,
        state: FSMContext,
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    expense_repository = gateway.expense_repository()

    await state.update_data(short_description=message.text)

    state_data = await state.get_data()

    await expense_repository.create_expense(
        data=ExpanseCreate(
            user_id=message.from_user.id,
            amount_expense=state_data.get('amount_expense'),
            short_description=state_data.get('short_description')
        )
    )

    await message.answer(text=EXPENSE_SAVED_MESSAGE)
    await state.clear()


@client_router.message(StateFilter(FSMExpenseFillForm.fill_short_description))
async def warning_short_description_expense_message(message: Message) -> None:
    await message.answer(text=WARNING_SHORT_DESCRIPTION_MESSAGE)
