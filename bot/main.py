import asyncio
import logging

from aiogram import Dispatcher, Bot
from tortoise import run_async

from bot.handlers import user_commands, questionaire
from bot.callbacks import likes_pagination
from config.env import TgKeys
from db.db_config import init

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
dp = Dispatcher()


async def start_bot():
    dp.include_routers(
        user_commands.router,
        questionaire.router,
        likes_pagination.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run_async(init())
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("Exit")
