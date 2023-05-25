from aiogram.types.inline_keyboard import InlineKeyboardMarkup,InlineKeyboardButton

inlinebtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="btn1",callback_data="btn1_inline"),
            InlineKeyboardButton(text="btn2",callback_data="btn2_inline")
        ]
    ]
)







