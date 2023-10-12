from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
from sys import exit
import logging
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(dotenv_path):
    exit("Файл .env в текущей директории не найден.")
load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    exit("Переменная окружения BOT_TOKEN в файле .env не найдена.")

# включаю логирование
logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
words_list = ['редис', 'помидоры', 'капуста']
commands_list = {
    'add': 'Добавление',
    'item': 'Элемент',
    'help': 'Помощь'
}


@dp.message_handler(commands=commands_list.keys())
async def cmds(message: types.Message):
    await message.answer(commands_list[message.text.removeprefix('/')])


@dp.message_handler()
async def echo(message: types.Message):
    answer = 'Хорошо.' if message.text.lower() in words_list else message.text
    await message.answer(answer)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)