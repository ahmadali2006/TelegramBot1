import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery

from data.config import ADMINS,CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard,post_callback
from loader import dp,bot
from states.newpoststate import NewPost


@dp.message_handler(commands=['elon_berish'])
async def create_post(message: Message):
    await message.answer("E`lon berish uchun quyidagi shablonni to`ldiring.")
    shablon=f"<b>📱Modeli:</b>\n" \
            f"<b>📆Yili:</b>\n"\
            f"<b>📦Holati:</b>\n" \
            f"<b>🌎Region:</b>\n" \
            f"<b>💵Narxi:</b>\n" \
            f"<b>💾Hotira:</b>\n" \
            f"<b>🔋Batareyasi:</b>\n" \
            f"<b>🌐Manzili:</b>\n"\
            f"<b>📞tel:</b>\n"\
            f"<b>❗️Qoshimcha:</b>\n"\
            \
            f"<b>👥Admin:</b>@ahmad_0628\n"
    image="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/galaxy-s21/gallery/uz-ru-galaxy-s21-5g-g991-sm-g991bzvdskz-thumb-368839956?$344_344_PNG$"
    await message.answer_photo(photo=image,caption=shablon)
    await NewPost.NewMessage.set()

@dp.message_handler(state=NewPost.NewMessage,content_types='text')
async def enter_message(message: Message,state: FSMContext):
    await state.update_data(text=message.html_text,mention=message.from_user.get_mention())
    await message.answer(f"E`lonni chop etish uchun yuboraymi?",
                         reply_markup=confirmation_keyboard)
    await NewPost.Confirmtext.set()

@dp.message_handler(state=NewPost.NewMessage,content_types='photo')
async def enter_message(message: Message,state: FSMContext):
    image=message.photo[-1].file_id
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention(), image=image)
    await message.answer(f"E`lonni chop etish uchun yuboraymi?",
                         reply_markup=confirmation_keyboard)
    await NewPost.Confirmimage.set()


@dp.callback_query_handler(post_callback.filter(action="post"),state=NewPost.Confirmtext)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text= data.get("text")
        mention=data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("E`lonni chop etish uchun adminga yuborildi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi e`lonni chop etmoqchi:")
    await bot.send_message(ADMINS[0], text,parse_mode="HTML",reply_markup=confirmation_keyboard)

@dp.callback_query_handler(post_callback.filter(action="post"),state=NewPost.Confirmimage)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text= data.get("text")
        mention=data.get("mention")
        image=data.get("image")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("E`lonni chop etish uchun adminga yuborildi")
    await bot.send_message(ADMINS[0],f"Foydalanuvchi{mention} quyidagi e`lonni chop etmoqchi:")
    await bot.send_photo(ADMINS[0],photo=image,caption=text,parse_mode="HTML",reply_markup=confirmation_keyboard)

@dp.callback_query_handler(post_callback.filter(action="cancel"),state=[NewPost.Confirmimage,NewPost.Confirmtext])
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("E`lon rad etildi.")

@dp.message_handler(state=[NewPost.Confirmimage,NewPost.Confirmtext])
async def post_unknown(message:Message):
    await message.answer("E`lonni chop etishni yoki rad etishni tanlang!!!")

@dp.callback_query_handler(post_callback.filter(action="post"),user_id=ADMINS)
async def approve_post(call:CallbackQuery):
    await call.answer("E`lonni chop etishga ruhsat berdingiz.",show_alert=True)
    target_channel=CHANNELS[0]
    message=await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)

@dp.callback_query_handler(post_callback.filter(action="cancel"),user_id=ADMINS)
async def decline_post(call:CallbackQuery):
    await call.answer("E`lon rad etildi.",show_alert=True)
    await call.message.edit_reply_markup()


