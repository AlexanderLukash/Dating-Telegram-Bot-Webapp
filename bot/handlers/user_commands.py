from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# Importing inline keyboards from the bot
from bot.keyboards.inline import profile_inline_kb, liked_by_keyboard

# Importing necessary modules from the main bot and backend repositories
from bot.main import bot
from backend.repositories.users import UsersRepository
from backend.repositories.likes import LikesRepository

# Creating a router instance
router = Router()


# Function to format user data into a string for displaying in the profile
async def format_user_data(user) -> str:
    about_user = f"<b>✍️ About you:</b> \n<i>{user.about}</i>" if user.about is not None else ""
    formatted_text = ("<b>✨ Your profile:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"{about_user}")
    return formatted_text


# Handler for the /start command
@router.message(CommandStart())
async def start(message: Message):
    user = await UsersRepository().get_one(message.from_user.id)

    if user:
        user_be_like = await LikesRepository().find_likes_to_user(message.from_user.id)
        formatted_text = await format_user_data(user)
        # Send a message with the user's profile details and an inline keyboard for actions
        await message.answer_photo(photo=user.photo,
                                   caption=formatted_text,
                                   reply_markup=await profile_inline_kb(message.from_user.id, user_be_like))
    else:
        await message.answer("First execute the /form command")


# Handler for the /profile command
@router.message(Command("profile"))
async def profile(message: Message):
    user = await UsersRepository().get_one(message.from_user.id)

    if user:
        user_be_like = await LikesRepository().find_likes_to_user(message.from_user.id)
        formatted_text = await format_user_data(user)
        # Send a message with the user's profile details and an inline keyboard for actions
        await message.answer_photo(photo=user.photo,
                                   caption=formatted_text,
                                   reply_markup=await profile_inline_kb(message.from_user.id, user_be_like))
    else:
        await message.answer("First execute the /form command")


# Function to send a message notifying the user that they were liked
async def send_liked_message(chat_id: int) -> Message:
    try:
        message = await bot.send_message(chat_id,
                                         text="<b>You were liked 💗</b>\nDo you want to see those who liked you?",
                                         reply_markup=await liked_by_keyboard())
        return message
    except Exception as e:
        error_message = f"Failed to send message: {e}"
        return {"error_message": error_message}
