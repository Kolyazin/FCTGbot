# инициализация бота
import sqlite3

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db_api import Database
from pathlib import Path

bot = Bot(BOT_TOKEN)
# инициализация диспетчера
dp = Dispatcher(bot)
db_path = Path('db_api', 'database', 'shop_database.db')
db = Database(path_db=db_path)

try:
    db.create_table_items()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_table_bucket()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)
