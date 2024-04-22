import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from tortoise import run_async  # Used for asynchronous database operations

# Importing custom handlers and callbacks from separate modules
from bot.handlers import user_commands, form
from bot.callbacks import main_callback, profile_edit
from db.db_config import init  # Assuming this module contains database initialization logic

import environ

env = environ.Env()
environ.Env.read_env('.env')

# Creating a Bot instance with the provided Telegram API token and default properties
bot = Bot(token=env('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()  # Creating a Dispatcher instance for handling bot updates


# Asynchronous function to start the bot and set up routing for different handlers and callbacks
async def start_bot():
    # Including routers for various functionalities such as user commands, forms, callbacks, etc.
    dp.include_routers(
        user_commands.router,
        form.router,
        main_callback.router,
        profile_edit.router
    )
    # Deleting any existing webhook and starting the bot with polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Configuring logging for the bot
    run_async(init())  # Asynchronously initializing the database
    try:
        # Running the asynchronous start_bot function using asyncio.run
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("Exit")  # Handling keyboard interrupt to gracefully exit the bot
