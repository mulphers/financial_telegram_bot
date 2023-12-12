from aiogram.filters.callback_data import CallbackData


class ExpenseCallbackFactory(CallbackData, prefix='expense'):
    expense_id: int
