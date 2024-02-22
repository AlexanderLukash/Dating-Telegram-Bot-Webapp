from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import WebAppInfo

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="👨 Профіль"
            ),
            KeyboardButton(
                text="❤️ Ваші лайки"
            )
        ],
        [
            KeyboardButton(
                text="🤳 Дивитися анкети",
                web_app=WebAppInfo(
                    url="https://docs.aiogram.dev/en/latest/dispatcher/index.html"
                )
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Натискай на кнопочки",
    selective=True
)
