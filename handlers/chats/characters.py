from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.characters_kb import characters_kb

router = Router()

characters = [
    "q7qfvgf068CT_le4d2dngdtR9PzITWi73vLTxgK6_iA",
    "rqqOwAe8skTSZ5avg480KbJW6wcaTr7dyDXZ0hiqlSw",
]

@router.callback_query(F.data == "characters")
async def characters_handler(call: CallbackQuery):
    keyboard = await characters_kb(characters)
    await call.message.edit_text("Choose a character:", reply_markup=keyboard)