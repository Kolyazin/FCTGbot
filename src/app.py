from aiogram.utils import executor
from handlers import dp

# начало программы
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
