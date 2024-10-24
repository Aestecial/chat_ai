from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='Choose a character', callback_data='characters'),
        InlineKeyboardButton(text='About us', callback_data='about')
    )

    return builder.as_markup()