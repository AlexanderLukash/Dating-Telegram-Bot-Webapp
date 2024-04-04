from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def user_name_keyboard(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text = txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
