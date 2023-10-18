from aiogram import types
from config import words_list
from loader import dp


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
