import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.scene import ScenesManager
from bot.keyboards.inline import web_app_markup
from bot.keyboards.reply import main_keyboard
from db.models.user import User

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user = await User.filter(telegram_id=message.from_user.id)
    if user:
        await message.answer("🍷 Починай знайомитись 👇", reply_markup=main_keyboard)
    else:
        await message.answer("Спочатку виконай команду /form",)
