from bot import start_bot
from db.db_config import init
from tortoise import run_async
import logging
import asyncio

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run_async(init())
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("Exit")
