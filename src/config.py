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


# слова на которые буду реагировать
words_list = ['редис', 'помидоры', 'капуста']
# команды на которые буду реагировать
commands_list = {
    'add': 'Добавление',
    'item': 'Элемент',
    'help': 'Помощь'
}