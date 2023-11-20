from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlines.callback_data import navigation_items_callback
from loader import db


def get_item_inline_keyboard(id: int = 1) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    left_id = id - 1
    right_id = id + 1
    if id == 1:
        btm = InlineKeyboardButton(text=">>>",
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=right_id)
                                   )
        item_inline_keyboard.add(btm)
    elif id == db.get_items_count():
        btm = InlineKeyboardButton(text='<<<',
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=left_id)
                                   )
        item_inline_keyboard.add(btm)
    else:
        btm_left = InlineKeyboardButton(text='<<<',
                                        callback_data=navigation_items_callback.new(
                                            for_data='items',
                                            id=left_id)
                                        )
        btm_right = InlineKeyboardButton(text=">>>",
                                         callback_data=navigation_items_callback.new(
                                             for_data='items',
                                             id=right_id)
                                         )
        item_inline_keyboard.add(btm_left, btm_right)

    btm_bucket = InlineKeyboardButton(text='В корзину',
                                      callback_data=navigation_items_callback.new(
                                          for_data='bucket',
                                          id=id)
                                      )
    btm_buy = InlineKeyboardButton(text="Купить",
                                   callback_data=navigation_items_callback.new(
                                       for_data='buy',
                                       id=id)
                                   )
    item_inline_keyboard.add(btm_bucket, btm_buy)
    return item_inline_keyboard
