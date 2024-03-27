from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo

main_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='💗 View questionnaires',
                web_app=WebAppInfo(url="https://533b-194-213-120-6.ngrok-free.app/users")
            )
        ]
    ]
)



