from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.about_kb import about_kb

router = Router()

@router.callback_query(F.data == "about")
async def about_handler(call: CallbackQuery):
    keyboard = about_kb()

    await call.message.edit_text("About us text", reply_markup=keyboard)