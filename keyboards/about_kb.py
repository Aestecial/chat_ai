from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def about_kb():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="Back", callback_data="back_menu")
    )

    return builder.as_markup()