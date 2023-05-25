from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,KeyboardButton

menu_btns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ma`lumot")
        ]
    ]
    ,
    resize_keyboard=True
)