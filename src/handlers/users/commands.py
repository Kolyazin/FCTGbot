from aiogram import types
from config import commands_list
from loader import dp


# функция для обработки команд, список команд строится из списка ключей словаря
@dp.message_handler(commands=commands_list.keys())
async def cmds(message: types.Message):
    # ответ берется из словаря в соответствии с принятой командой
    await message.answer(commands_list[message.text.removeprefix('/')])
