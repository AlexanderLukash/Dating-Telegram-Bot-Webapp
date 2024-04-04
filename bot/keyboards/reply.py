from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import WebAppInfo

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="👨 Profile"
            ),
            KeyboardButton(
                text="❤️ Your likes"
            )
        ],
        [
            KeyboardButton(
                text="🤳 View questionnaires",
                web_app=WebAppInfo(
                    url="https://docs.aiogram.dev/en/latest/dispatcher/index.html"
                )
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Press the buttons",
    selective=True
)

gender_select_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="👨 Boy"
            ),
            KeyboardButton(
                text="👧 Girl"
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Press the buttons",
    selective=True
)

about_skip_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🪪 Skip"
            ),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Press the button",
    selective=True
)

remove_keyboard = ReplyKeyboardRemove()
