import asyncio

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from backend.repositories.likes import LikesRepository
from backend.repositories.users import UsersRepository
from bot.keyboards.inline import profile_inline_kb, match_keyboard, like_dislike_keyboard

router = Router()

# Define URLs and an empty list for users
texts_photo = "https://lukash.sirv.com/BotFiles/2323233323434344343.jpg"
users = []


async def format_user_data(user) -> str:
    # Format user data for display
    about_user = f"<b>✍️ About you:</b> \n<i>{user.about}</i>" if user.about is not None else ""
    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"{about_user}")
    return formatted_text


async def format_likes_data(user) -> str:
    # Format user likes data for display
    about_user = f"<i>{user.about}</i>" if user.about is not None else ""
    formatted_text = (f"<b>{user.name}</b>, {user.age}, {user.city}\n"
                      f"{about_user}")
    return formatted_text


async def match_data(user) -> str:
    # Format match data for display
    about_user = f"<i>{user.about}</i>" if user.about is not None else ""
    formatted_text = (f"<b>Super! I hope you have a great time ;) Start chatting 👇</b>\n"
                      f"<b>{user.name}</b> | @{user.username}, {user.age}, {user.city}\n"
                      f"{about_user}")
    return formatted_text


# Handle callback for profile page
@router.callback_query(F.data == "profile_page")
async def profile(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
    user = await UsersRepository().get_one(callback.from_user.id)

    if user:
        user_be_like = await LikesRepository().find_likes_to_user(callback.from_user.id)
        formatted_text = await format_user_data(user)
        await callback.message.answer_photo(photo=user.photo,
                                            caption=formatted_text,
                                            reply_markup=await profile_inline_kb(callback.from_user.id,
                                                                                 user_be_like))
    else:
        await callback.message.answer("First execute the /form command", )


current_index = 0
users_list = []


async def send_next_user(callback: CallbackQuery):
    # Send the next user from the list or end if no more users
    global current_index, users_list

    if current_index < len(users_list):
        user_data = users_list[current_index]
        current_index += 1
        formatted_text = await format_likes_data(user_data)
        await callback.message.answer_photo(photo=user_data.photo,
                                            caption=formatted_text,
                                            reply_markup=await like_dislike_keyboard(user_data))
    else:
        await callback.message.answer("That's all.")
        await asyncio.sleep(1)
        await profile(callback)


# Handle callback for seeing who liked the user
@router.callback_query(F.data == "see_who_liked")
async def see_who_liked(callbacks: CallbackQuery):
    global current_index, users_list

    likes = await LikesRepository().find_likes_to_user(callbacks.from_user.id)

    if likes:
        users_list = []
        for i in likes:
            user = i.from_user_id
            get_user = await UsersRepository().get_one(user)  # Get the user who received the like
            users_list.append(get_user)

    current_index = 0
    await send_next_user(callbacks)


# Handle callback for liking a user
@router.callback_query(lambda callback_query: callback_query.data.startswith("like_"))
async def like_user(callback: CallbackQuery, bot: Bot):
    global current_index, users_list
    await callback.message.delete()

    user_data = await UsersRepository().get_one(callback.data.split("_")[1])
    user_who_like = await UsersRepository().get_one(callback.from_user.id)
    formatted_text = await match_data(user_who_like)
    await bot.send_photo(user_data.telegram_id,
                         photo=user_who_like.photo,
                         caption=formatted_text,
                         reply_markup=await match_keyboard(user_who_like))

    formatted_text = await match_data(user_data)
    await callback.message.answer_photo(photo=user_data.photo,
                                        caption=formatted_text,
                                        reply_markup=await match_keyboard(user_data))
    await asyncio.sleep(3)
    await LikesRepository().delete_like(callback.data.split("_")[1], callback.from_user.id)
    await send_next_user(callback)


# Handle callback for disliking a user
@router.callback_query(lambda callback_query: callback_query.data.startswith("dislike_"))
async def dislike_user(callback: CallbackQuery):
    await callback.message.delete()
    await LikesRepository().delete_like(from_user=callback.data.split("_")[1], to_user=callback.from_user.id)
    await send_next_user(callback)
