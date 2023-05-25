from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import CHANNELS
from keyboards.default.menu import menu_btns
from loader import dp, bot
from utils.misc import obuna
                 
@dp.callback_query_handler(text="obunatek")
async def obuna_tek(call: types.CallbackQuery):
    result = str()
    for i in CHANNELS:
        status = await obuna.check(user_id=call.from_user.id, channel=i)
        channal = await bot.get_chat(i)
        if status:
            result += f"<b>Assalomu aleykum:</b>, {call.from_user.full_name}\n" \
                      f"<b>\"E`lon berish \"</b> rasmiy telegram botiga xush kelibsiz!"
        else:
            invite_link= await channal.export_invite_link()
            result = f"❌<b>{channal.title}</b> kanaliga obuna bo`lmagansiz!\n"\
                     f"👉<a href='{invite_link}'> Obuna bo`ling</a>\n\n"

    await call.message.answer(result, disable_web_page_preview=True, reply_markup=menu_btns)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Salom</b>, {message.from_user.full_name} "
                         f"<b> e`lon berish uchun </b>/elon_berish <b> so`zini bosing!</b>", reply_markup=menu_btns)
