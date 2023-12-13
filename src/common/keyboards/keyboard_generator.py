from typing import Sequence

from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)

from src.common.callback_factory.expense import ExpenseCallbackFactory
from src.database.models.expense import Expense


def generate_inline_keyboard(
        width: int,
        **kwargs
) -> InlineKeyboardMarkup:
    inline_kb_builder = InlineKeyboardBuilder()
    buttons = []

    if kwargs:
        for callback_data, text in kwargs.items():
            buttons.append(
                InlineKeyboardButton(
                    text=text,
                    callback_data=callback_data
                )
            )

    inline_kb_builder.row(*buttons, width=width)

    return inline_kb_builder.as_markup()


def generate_remove_expense_keyboard(expenses: Sequence[Expense]) -> InlineKeyboardMarkup:
    return generate_inline_keyboard(
        width=1,
        **{
            ExpenseCallbackFactory(expense_id=expense.expense_id).pack(): expense.short_description
            for expense in expenses}
    )


def generate_ad_keyboard(text: str, url: str) -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text=text,
                url=url
            )
        ]]
    )

    return inline_keyboard
