from aiogram import F
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.dto.expense import ExpanseCreate
from src.common.fsm.expense_filling_state import FSMExpenseFillForm
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.client.router import client_router
from src.utils.decorators import with_database
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
):
    await state.update_data(amount_expense=float(message.text))
    await message.answer(text=WRITE_SHORT_DESCRIPTION_MESSAGE)
    await state.set_state(FSMExpenseFillForm.fill_short_description)


@client_router.message(StateFilter(FSMExpenseFillForm.fill_amount_expense))
async def warning_amount_expense_message(message: Message):
    await message.answer(text=WARNING_AMOUNT_EXPENSE_MESSAGE)


@client_router.message(
    StateFilter(FSMExpenseFillForm.fill_short_description),
    F.text
)
@with_database
async def process_short_description_expense_message(
        message: Message,
        state: FSMContext,
        uow: AbstractUnitOfWork
):
    await state.update_data(short_description=message.text)

    state_data = await state.get_data()

    await uow.expense.create_expense(
        data=ExpanseCreate(
            user_id=message.from_user.id,
            amount_expense=state_data.get('amount_expense'),
            short_description=state_data.get('short_description')
        )
    )

    await message.answer(text=EXPENSE_SAVED_MESSAGE)
    await state.clear()


@client_router.message(StateFilter(FSMExpenseFillForm.fill_short_description))
async def warning_short_description_expense_message(message: Message):
    await message.answer(text=WARNING_SHORT_DESCRIPTION_MESSAGE)
