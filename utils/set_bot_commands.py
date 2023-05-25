from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('elon_berish', "Kanalga yangi e`lon berish"),
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),

        ]
    )
