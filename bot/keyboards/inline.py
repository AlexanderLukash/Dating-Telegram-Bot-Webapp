# Importing necessary modules and classes
import environ
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

env = environ.Env()
environ.Env.read_env('.env')


# Function to create an inline keyboard for user profile options
async def profile_inline_kb(user_id, liked_by):
    builder = InlineKeyboardBuilder()
    if liked_by:
        builder.row(
            InlineKeyboardButton(text="You were liked by 💌", callback_data="see_who_liked"),
        )
    builder.row(
        InlineKeyboardButton(text="Edit your profile ⚙️", callback_data="profile_edit"),
    )
    builder.row(
        InlineKeyboardButton(text='💗 View surveys',
                             web_app=WebAppInfo(
                                 url=f"{env('FRONTEND_URL')}users/{user_id}"))
    )
    return builder.as_markup()


# Function to create an inline keyboard for profile editing options
async def profile_edit_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1",
                    callback_data="profile_page",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="2",
                    callback_data="form",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="3",
                    callback_data="photo_edit",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="4",
                    callback_data="about_edit",
                    one_time=True
                ),
            ]
        ],
    )
    return keyboard


# Functions to create inline keyboards for confirming various actions
async def form_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Yes ✅",
                    callback_data="form_confirm",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="No ❎",
                    callback_data="profile_edit",
                    one_time=True
                ),
            ]
        ],
    )
    return keyboard


# Function to create an inline keyboard for accept photo edit
async def photo_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Yes ✅",
                    callback_data="photo_confirm",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="No ❎",
                    callback_data="profile_edit",
                    one_time=True
                ),
            ]
        ],
    )
    return keyboard


# Function to create an inline keyboard for accept about edit
async def about_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Yes ✅",
                    callback_data="about_confirm",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="No ❎",
                    callback_data="profile_edit",
                    one_time=True
                ),
            ]
        ],
    )
    return keyboard


# Function to create an inline keyboard for show liked
async def liked_by_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Yes ✅",
                    callback_data="see_who_liked",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="No ❎",
                    callback_data="profile_page",
                    one_time=True
                ),
            ]
        ],
    )
    return keyboard


# Function to create an inline keyboard for liking or disliking a user
async def like_dislike_keyboard(user):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Like",
                    callback_data=f"like_{user.telegram_id}",
                    one_time=True
                ),
                InlineKeyboardButton(
                    text="Dislike",
                    callback_data=f"dislike_{user.telegram_id}",
                    one_time=True
                )
            ]
        ],
    )
    return keyboard


# Function to create an inline keyboard for starting a chat with a matched user
async def match_keyboard(user):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Start chatting 💌",
                    url=f"https://t.me/{user.username}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Your profile",
                    callback_data="profile_page"
                )
            ]
        ],
    )
    return keyboard
