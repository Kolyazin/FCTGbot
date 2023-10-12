from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
from sys import exit
import logging
import os

# переменная с путем до файла .env где хранятся подгружаемые переменные окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# если файла .env нет рядом с исполняемым, то выхожу с ошибкой
if not os.path.exists(dotenv_path):
    exit("Файл .env в текущей директории не найден.")
# загружаю переменные окружения из файла
load_dotenv(dotenv_path)

# получаю токен телеграм бота из переменной окружения BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")
# а если такой нет, то выхожу с ошибкой
if not BOT_TOKEN:
    exit("Переменная окружения BOT_TOKEN в файле .env не найдена.")

# включаю логирование
logging.basicConfig(level=logging.INFO)

# инициализация бота
bot = Bot(BOT_TOKEN)
# инициализация диспетчера
dp = Dispatcher(bot)
# слова на которые буду реагировать
words_list = ['редис', 'помидоры', 'капуста']
# команды на которые буду реагировать
commands_list = {
    'add': 'Добавление',
    'item': 'Элемент',
    'help': 'Помощь'
}


# функция для обработки команд, список команд строится из списка ключей словаря
@dp.message_handler(commands=commands_list.keys())
async def cmds(message: types.Message):
    # ответ берется из словаря в соответствии с принятой командой
    await message.answer(commands_list[message.text.removeprefix('/')])


# функция для обработки текста
@dp.message_handler()
async def echo(message: types.Message):
    answer = message.text
    # проверяю, надо реагировать на присланное слово или нет
    if message.text.lower() in words_list:
        # если слово из списка, то отвечаю в зависимости от языка пользователя приславшего слово
        if message.from_user.language_code == 'ru':
            answer = 'Хорошо.'
        else:
            answer = 'Fine'

    await message.answer(answer)

# начало программы
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
