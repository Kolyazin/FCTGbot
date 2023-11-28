from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Список товаров'),
            KeyboardButton(text='Каталог')
        ],
        [
            KeyboardButton(text='Корзина'),
            KeyboardButton(text='Купить')
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='Найти товар')
        ],
        [
            KeyboardButton(text='Подтвердить номер телефона', request_contact=True)
        ],
        [
            KeyboardButton(text='Скрыть клавиатуру')
        ]
    ],
    resize_keyboard=True
)
