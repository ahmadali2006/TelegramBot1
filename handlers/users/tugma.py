from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Text
from loader import dp


@dp.message_handler(Text(equals="Ma`lumot"))
async def bot_start(message:types.Message):
    await message.answer(f"<b>Botdan foydalanish davomida nosozlik bo`lsa adminga murojat qiling</b>\n"
                         f"<b>Admin</b> @ahmad_0628")