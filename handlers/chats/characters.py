from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from handlers.database.db_base import Database
from keyboards.characters_kb import characters_kb

router = Router()

@router.callback_query(F.data == "characters")
async def characters_handler(call: CallbackQuery):
    async with Database() as db:
        rows = await db.fetch("SELECT * FROM characters")
        keyboard = await characters_kb(rows)
        await call.message.edit_text("Choose a character:", reply_markup=keyboard)