from aiogram.fsm.state import State, StatesGroup


class FSMExpenseFillForm(StatesGroup):
    fill_amount_expense = State()
    fill_short_description = State()
