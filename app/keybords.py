from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='catalog',callback_data='catalog')],
    [InlineKeyboardButton(text='shop list',callback_data='shoplist')],
    [InlineKeyboardButton(text='contacts',callback_data='contacts')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK',url='https://vk.com')]
    ])


