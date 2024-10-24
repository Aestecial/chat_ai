from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.start_kb import start_kb

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    keyboard = start_kb()
    await message.answer(
        "Hello! I'm a simple chatbot.",
        reply_markup=keyboard
    )