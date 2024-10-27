from aiogram import Router, F, Bot
from aiogram.enums import ChatAction
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.message_state import MessageState
from utils.api import start_chat, send_message

router = Router()

@router.callback_query(F.data.startswith("character_"))
async def chat_handler(call: CallbackQuery, state: FSMContext):
    char_id = call.data[10:]
    chat_id, answer = await start_chat(char_id)
    await call.message.edit_text(text=answer, reply_markup=None)

    await state.update_data(chat_id=chat_id)
    await state.update_data(char_id=char_id)
    await state.set_state(MessageState.message)


@router.message(F.text, MessageState.message)
async def message_handler(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    name, text = await send_message(data['chat_id'], message.text, data['char_id'])
    body = f"{text}"

    await message.answer(text=body)

