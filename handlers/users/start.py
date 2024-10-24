from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.start_kb import start_kb

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    keyboard = start_kb()
    await message.answer(
        "Hello! I'm a simple chatbot.",
        reply_markup=keyboard
    )


@router.callback_query(F.data == 'back_menu')
async def start_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    keyboard = start_kb()
    await call.message.edit_text(
        "Hello! I'm a simple chatbot.",
        reply_markup=keyboard
    )