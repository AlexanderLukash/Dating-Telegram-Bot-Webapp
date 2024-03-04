from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
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

gender_select_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="👨 Хлопець"
            ),
            KeyboardButton(
                text="👧 Дівчина"
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Натискай на кнопочки",
    selective=True
)

about_skip_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🪪 Пропустити"
            ),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Натискай на кнопочки",
    selective=True
)

remove_keyboard = ReplyKeyboardRemove()
