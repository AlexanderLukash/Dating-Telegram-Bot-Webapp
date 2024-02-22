from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.scene import ScenesManager
from bot.keyboards.inline import web_app_markup
from bot.keyboards.reply import main_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("🍷 Починай знайомитись 👇", reply_markup=main_keyboard)

