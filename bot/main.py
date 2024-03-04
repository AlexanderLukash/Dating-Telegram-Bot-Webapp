from aiogram import Bot, Dispatcher

from bot.misc import TgKeys
from bot.handlers import user_commands, questionaire


async def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        questionaire.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
