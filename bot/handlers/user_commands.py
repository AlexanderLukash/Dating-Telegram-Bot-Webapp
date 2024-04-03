import random
from aiogram import Bot, F
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bot.keyboards.inline import plofile_inline_kb
from bot.keyboards.reply import main_keyboard

from bot.main import bot
from db.models.user import User, Likes
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
    user_be_like = await Likes.filter(to_user_id=message.from_user.id)
    user_liked = await Likes.filter(from_user_id=message.from_user.id)
    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{user.about}</i>")
    await message.answer_photo(photo=user.photo,
                               caption=formatted_text,
                               reply_markup=await plofile_inline_kb(message.from_user.id, user_be_like, user_liked))


async def send_message(chat_id: int, text: str) -> Message:
    try:
        message = await bot.send_message(chat_id, text)
        return message
    except Exception as e:
        error_message = f"Failed to send message: {e}"
        return {"error_message": error_message}


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
