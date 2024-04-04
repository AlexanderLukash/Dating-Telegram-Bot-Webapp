from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, InputMediaVideo, FSInputFile
from aiogram.exceptions import TelegramBadRequest

from contextlib import suppress
from bot.keyboards.inline import paginator_photo, UserLikedByPagination, UsVideoPagination, paginator_videos, \
    PhotoMePagination, paginator_photo_me, TextsPagination, paginator_texts, plofile_inline_kb

from db.models.user import Likes, User

router = Router()

texts_photo = "https://lukash.sirv.com/BotFiles/2323233323434344343.jpg"
users = []


@router.callback_query(UserLikedByPagination.filter(F.action.in_(["prev", "next"])))
async def pagination_user_liked_by_handler(call: CallbackQuery, callback_data: UserLikedByPagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(users) - 1) else 0

    if callback_data.action == "prev":
        page = page_num - 1 if page_num != 0 else (len(users) - 1)

    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {users[page].name} | @{users[page].username}\n"
                      f"<b>🎀 Age:</b> {users[page].age}\n"
                      f"<b>🌆 City:</b> {users[page].city}\n"
                      f"<b>👫 Gender:</b> {users[page].gender}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{users[page].about}</i>")

    await call.message.edit_media(InputMediaPhoto(media=users[page].photo,
                                                  caption=formatted_text),
                                  reply_markup=paginator_photo(page))
    await call.answer()


@router.callback_query(F.data == "pag")
async def photo_pag(callback: CallbackQuery) -> None:
    user_be_like = await Likes.filter(to_user_id=callback.from_user.id)
    for like in user_be_like:
        user = await User.filter(telegram_id=like.from_user_id)
        if user:
            users.append(user[0])  # Додаємо першого знайденого користувача

    await callback.message.edit_media(InputMediaVideo(media=users[0].photo,
                                                      caption=f"Likes by @{users[0].username}"
                                                              " <b>Натискай на кнопочки ️</b>‍💌👇"),
                                      reply_markup=paginator_photo())


@router.callback_query(F.data == "profile_page")
async def profile(callback: CallbackQuery):
    user = await User.filter(telegram_id=callback.from_user.id).first()
    user_be_like = await Likes.filter(to_user_id=callback.from_user.id)
    user_liked = await Likes.filter(from_user_id=callback.from_user.id)
    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{user.about}</i>")
    await callback.message.edit_media(InputMediaPhoto(media=user.photo,
                                                      caption=formatted_text,
                                                      ),
                                      reply_markup=await plofile_inline_kb(callback.from_user.id, user_be_like,
                                                                           user_liked))
