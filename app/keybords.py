from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],

    [KeyboardButton(text='Shop List'),
     KeyboardButton(text='Contacts')]

],                      

                        resize_keybord=True,
                        input_field_placeholder='chose'
),

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK',url='https://vk.com')]
    ])


