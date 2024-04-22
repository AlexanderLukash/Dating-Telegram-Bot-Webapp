# Importing the necessary module for keyboard creation
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Defining an asynchronous function to create a username keyboard
async def user_name_keyboard(text: str | list):
    # Initializing a ReplyKeyboardBuilder object
    builder = ReplyKeyboardBuilder()

    # Checking if the input text is a string, if so, convert it to a list
    if isinstance(text, str):
        text = [text]

    # Adding buttons to the keyboard builder for each text element in the list
    [builder.button(text=txt) for txt in text]

    # Returning the keyboard as a markup with resize and one-time keyboard options
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
