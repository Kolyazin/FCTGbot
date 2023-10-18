from aiogram import types
from config import commands_list
from loader import dp
from keyboards import commands_default_keyboard

# функция для обработки команд, список команд строится из списка ключей словаря
@dp.message_handler(commands=commands_list.keys())
async def cmds(message: types.Message):
    # ответ берется из словаря в соответствии с принятой командой
    await message.answer(commands_list[message.text.removeprefix('/')], reply_markup=commands_default_keyboard)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(f'{commands_list}')
