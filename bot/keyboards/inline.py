from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder


async def plofile_inline_kb(user_id, liked_by, liked):
    builder = InlineKeyboardBuilder()
    if liked_by:
        builder.row(
            InlineKeyboardButton(text="You were liked by 💌", callback_data="pag"),
        )
    if liked:
        builder.row(
            InlineKeyboardButton(text="Your likes 💓", url="https://c80e-194-213-120-6.ngrok-free.app/users"),
        )
    builder.row(
        InlineKeyboardButton(text='💗 View questionnaires',
                             web_app=WebAppInfo(url=f"https://c80e-194-213-120-6.ngrok-free.app/users/{user_id}"))
    )
    return builder.as_markup()


class UserLikedByPagination(CallbackData, prefix="pag"):
    action: str
    page: int


class PhotoMePagination(CallbackData, prefix="me_pag"):
    action: str
    page: int


class UsVideoPagination(CallbackData, prefix="video_pag"):
    action: str
    page: int


class TextsPagination(CallbackData, prefix="texts_pag"):
    action: str
    page: int


def paginator_photo(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=UserLikedByPagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=UserLikedByPagination(action="next", page=page).pack()),
        width=2
    )
    builder.row(
        InlineKeyboardButton(text="Main menu ✨", callback_data="profile_page")
    )
    return builder.as_markup()


def paginator_photo_me(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=PhotoMePagination(action="prev_page", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=PhotoMePagination(action="next_page", page=page).pack()),
        width=2
    )
    return builder.as_markup()


def paginator_videos(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=UsVideoPagination(action="pre", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=UsVideoPagination(action="nex", page=page).pack()),
        width=2
    )
    return builder.as_markup()


def paginator_texts(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=TextsPagination(action="previ", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=TextsPagination(action="nexts", page=page).pack()),
        width=2
    )
    return builder.as_markup()
