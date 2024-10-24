from characterai import aiocai

from config import Config

config = Config()
token = config.AUTH_TOKEN

async def get_char(char_id):
    client = aiocai.Client(token)

    char = await client.get_char(char_id)

    return char.name


async def start_chat(char_id):
    client = aiocai.Client(token)
    me = await client.get_me()
    async with await client.connect() as chat:
        chat, answer = await chat.new_chat(char_id, me.id)
    return chat.chat_id, answer.text


async def send_message(chat_id, text, char_id):
    client = aiocai.Client(token)
    async with await client.connect() as chat:
        message = await chat.send_message(char_id, chat_id, text)
    return message.name, message.text

