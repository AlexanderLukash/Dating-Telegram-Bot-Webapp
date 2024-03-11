import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bot.keyboards.inline import web_app_markup
from bot.keyboards.reply import main_keyboard
from db.models.user import User
from faker import Faker

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user = await User.filter(telegram_id=message.from_user.id).first()
    if user:
        await message.answer("🍷 Start dating 👇", reply_markup=main_keyboard)
    else:
        await message.answer("Спочатку виконай команду /form", )


@router.message(Command("profile"))
async def profile(message: Message):
    user = await User.filter(telegram_id=message.from_user.id).first()
    formatted_text = ("<b>✨ Ваша анкета:</b> \n\n"
                      f"<b>👋 Ім'я:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Вік:</b> {user.age}\n"
                      f"<b>🌆 Місто:</b> {user.city}\n"
                      f"<b>👫 Стать:</b> {user.gender}\n"
                      f"<b>✍️ Про вас:</b> \n"
                      f"<i>{user.about}</i>")
    await message.answer_photo(photo=user.photo,
                               caption=formatted_text,
                               reply_markup=web_app_markup)


@router.message(Command("test"))
async def test(message: Message):
    await message.answer("Test", reply_markup=web_app_markup)


@router.message(Command("create_users"))
async def create_users(message: Message):
    fake = Faker()
    try:
        for _ in range(20):
            await User.create(
                telegram_id=random.randint(1000000, 9999999),
                name=fake.name(),
                username=fake.user_name(),
                age=random.randint(13, 60),
                gender=random.choice(['Хлопець', 'Дівчина']),
                city=fake.city(),
                about=fake.text(max_nb_chars=225),
                photo="https://dummyimage.com/732x967"
            )
        await message.answer(text="Користувачі створені")
    except Exception as error:
        await message.answer(text=f"Користувачі не створені, виникла помилка: {error}.")
