# инициализация бота
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
# инициализация диспетчера
dp = Dispatcher(bot)
