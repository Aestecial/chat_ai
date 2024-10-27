from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.api import get_char


async def characters_kb(characters):
    builder = InlineKeyboardBuilder()
    for char in characters:
        char = char['char_id']
        name = await get_char(char)
        builder.add(
            InlineKeyboardButton(text=f"{name}", callback_data=f"character_{char}")
        )

    builder.adjust(3)

    builder.row(
        InlineKeyboardButton(text="Back", callback_data="back_menu")
    )

    return builder.as_markup()