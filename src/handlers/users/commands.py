from aiogram import types
from config import commands_list
from loader import dp
from keyboards import commands_default_keyboard
from loader import db


# функция для обработки команд, список команд строится из списка ключей словаря
@dp.message_handler(commands=['list'])
async def cmds(message: types.Message):
    # ответ берется из словаря в соответствии с принятой командой
    await message.answer(f'{db.select_all_items()}')


@dp.message_handler(commands=['add'])
async def add_item(message: types.Message):
    data = message.text.split(' ')
    db.add_item(int(data[1]), data[2], int(data[3]))
    await message.answer(text='Товар добавлен.')


@dp.message_handler(commands=['del'])
async def del_item(message: types.Message):
    data = message.text.split(' ')
    db.delete_item(id=int(data[1]))
    await message.answer(text='Товар удален.')


@dp.message_handler(commands=['item'])
async def item(message: types.Message):
    data = message.text.split(' ')
    info = db.select_item_info(id=int(data[1]))
    await message.answer(text=f'ID: {info[0][0]}\nНазвание: {info[0][1]}\nКоличество: {info[0][2]}')


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await message.answer(text='Меню.', reply_markup=commands_default_keyboard)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(
        f'/menu - показать меню\n' \
        '/list - показать список товаров\n' \
        '/add - добавить товар (/add id name amount)\n' \
        '/del - удалить товар (/del id)\n' \
        '/item - показать информацию о товаре (/item id)\n'
    )

# @dp.message_handler(content_types=['contact'])
# async def answer_contact_command(message: types.Message):
#     if message.contact.user_id == message.from_user.id:
#         await message.answer(text='Регистрация прошла успешно!')
#         db.add_user(message.from_user.id, message.contact.phone_number)
#     else:
#         await message.answer(text='Увы(')
