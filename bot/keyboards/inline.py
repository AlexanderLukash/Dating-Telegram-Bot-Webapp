from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo

web_app_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Дивитися анкети',
                web_app=WebAppInfo(url="https://acc8-194-213-120-6.ngrok-free.app/about")
            )
        ]
    ]
)