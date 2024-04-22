from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import WebAppInfo

# Creating a ReplyKeyboardMarkup for profile editing options with numbered buttons
profile_edit_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="1"
            ),
            KeyboardButton(
                text="2"
            ),
            KeyboardButton(
                text="3"
            ),
            KeyboardButton(
                text="4"
            )
        ]
    ],
    resize_keyboard=True,  # Allows the keyboard to resize dynamically
    input_field_placeholder="👇 Press the buttons",  # Placeholder text displayed in the input field
    selective=True  # Ensures the keyboard is shown only to the specific user who triggered it
)

# Creating a ReplyKeyboardMarkup for gender selection with emoji buttons
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
    resize_keyboard=True,  # Allows the keyboard to resize dynamically
    input_field_placeholder="👇 Press the buttons",  # Placeholder text displayed in the input field
    selective=True  # Ensures the keyboard is shown only to the specific user who triggered it
)

# Creating a ReplyKeyboardMarkup for skipping the "about" section with a single button
about_skip_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🪪 Skip"
            ),
        ]
    ],
    resize_keyboard=True,  # Allows the keyboard to resize dynamically
    input_field_placeholder="👇 Press the button",  # Placeholder text displayed in the input field
    selective=True  # Ensures the keyboard is shown only to the specific user who triggered it
)

# Creating a special keyboard to remove the current keyboard from the chat interface
remove_keyboard = ReplyKeyboardRemove()
