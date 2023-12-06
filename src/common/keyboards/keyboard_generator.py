from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)


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
