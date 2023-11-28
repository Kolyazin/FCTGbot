from aiogram import types
from aiogram.types import InputFile, InputMediaPhoto
from config import commands_list
from loader import dp
from keyboards import commands_default_keyboard, get_item_inline_keyboard, navigation_items_callback
from loader import db, bot


# функция для обработки команд, список команд строится из списка ключей словаря
@dp.message_handler(text='Список товаров')
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


# @dp.message_handler(commands=['item'])
# async def item(message: types.Message):
#     data = message.text.split(' ')
#     info = db.select_item_info(id=int(data[1]))
#     await message.answer(text=f'ID: {info[0][0]}\nНазвание: {info[0][1]}\nКоличество: {info[0][2]}')
@dp.message_handler(text=['Каталог'])
@dp.message_handler(commands=['item'])
async def answer_menu_command(message: types.Message):
    first_item_info = db.select_item_info(id=1)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f"Название товара: {name}" \
                f"\nКоличество товара: {count}"
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                               caption=item_text,
                               reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_items(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f"Название товара: {name}" \
                f"\nКоличество товара: {count}"
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),
                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_item_inline_keyboard(id=current_item_id))


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
        '/item - показать каталог\n'
    )


@dp.message_handler(text='Скрыть клавиатуру')
async def hide_keyboard(message: types.Message):
    await message.answer(text='Ok', reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='buy'))
async def buy(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f"{current_item_id}, {name}, {count}"
    await call.message.answer(text=item_text)


@dp.callback_query_handler(navigation_items_callback.filter(for_data='to_bucket'))
async def bucket(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    db.add_item_to_bucket(call.from_user.id, current_item_id)
    await call.message.answer(text='В корзине')


@dp.message_handler(text='Корзина')
async def bucket(message: types.Message):
    await message.answer(text=db.select_users_bucket(message.from_user.id))


# @dp.message_handler(content_types=['contact'])
# async def answer_contact_command(message: types.Message):
#     if message.contact.user_id == message.from_user.id:
#         await message.answer(text='Регистрация прошла успешно!')
#         db.add_user(message.from_user.id, message.contact.phone_number)
#     else:
#         await message.answer(text='Увы(')
