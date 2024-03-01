import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.scene import ScenesManager
from bot.keyboards.inline import web_app_markup
from bot.keyboards.reply import main_keyboard
from db.models.user import User

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await User.create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.first_name,
        age=random.randrange(13, 35),
        gender=1
    )
    await message.answer("🍷 Починай знайомитись 👇", reply_markup=main_keyboard)
