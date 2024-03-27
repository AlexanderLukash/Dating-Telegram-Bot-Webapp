import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bot.keyboards.inline import main_inline_kb
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
        await message.answer("First execute the /form command", )


@router.message(Command("profile"))
async def profile(message: Message):
    user = await User.filter(telegram_id=message.from_user.id).first()
    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{user.about}</i>")
    await message.answer_photo(photo=user.photo,
                               caption=formatted_text,
                               reply_markup=main_inline_kb)


@router.message(Command("test"))
async def test(message: Message):
    await message.answer("Test", reply_markup=main_inline_kb)


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
                gender=random.choice(['Boy', 'Girl']),
                looking_for=random.choice(['Boy', 'Girl']),
                city=fake.city(),
                about=fake.text(max_nb_chars=225),
                photo="https://dummyimage.com/732x967"
            )
        await message.answer(text="Users are created.")
    except Exception as error:
        await message.answer(text=f"Users not created, an error occurred: {error}.")
