import environ
from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

# Importing inline keyboards and other utilities from the bot
from bot.keyboards.inline import profile_inline_kb
from bot.utils.states import UserForm, PhotoEditState, AboutEditState
from bot.keyboards.builders import user_name_keyboard
from bot.keyboards.reply import remove_keyboard, gender_select_keyboard, about_skip_keyboard

# Importing Cloudinary uploader and configurations
import cloudinary.uploader
import cloudinary

# Importing repositories for database operations
from backend.repositories.users import UsersRepository
from backend.repositories.likes import LikesRepository

# Creating a router instance
router = Router()
env = environ.Env()
environ.Env.read_env('.env')

cloudinary.config(
    cloud_name=env('CLOUDINARY_NAME'),  # Cloudinary cloud name
    api_key=env('CLOUDINARY_KEY'),  # Cloudinary API key
    api_secret=env('CLOUDINARY_SECRET')  # Cloudinary API secret
)


async def format_user_data(user) -> str:
    # Format user data for displaying in the profile
    about_user = f"<b>✍️ About you:</b> \n<i>{user.about}</i>" if user.about is not None else ""
    formatted_text = ("<b>✨ Your profile:</b> \n\n"
                      f"<b>👋 Name:</b> {user.name} | @{user.username}\n"
                      f"<b>🎀 Age:</b> {user.age}\n"
                      f"<b>🌆 City:</b> {user.city}\n"
                      f"<b>👫 Gender:</b> {user.gender}\n"
                      f"{about_user}")
    return formatted_text


async def gender_check(message):
    # Check the gender selected by the user
    if message.text.lower() == "👨 boy":
        gender = "Boy"
        return gender
    elif message.text.lower() == "👧 girl":
        gender = "Girl"
        return gender
    else:
        await message.answer(text="Click on the button 👇", reply_markup=gender_select_keyboard)
        return None


async def download_photo(bot: Bot, photo_file_id: str, user_id: int) -> str:
    # Download and save the photo from Telegram
    file = await bot.get_file(photo_file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"photos/{user_id}.jpg")
    return f"photos/{user_id}.jpg"


async def convert_http_to_https(url):
    # Convert HTTP URL to HTTPS
    if url.startswith('http://'):
        url = url.replace('http://', 'https://')
        return url
    else:
        return url


async def upload_photo_to_cloudinary(photo_path: str, user_id: int):
    # Upload the photo to Cloudinary
    photo_url = cloudinary.uploader.upload(photo_path,
                                           folder="photos",
                                           public_id=f"{user_id}")
    photo_url = await convert_http_to_https(photo_url.get('url'))
    return photo_url


# Handler for the /form command to start the user registration process
@router.message(Command("form"))
async def user_form(message: Message, state: FSMContext):
    user = await UsersRepository().get_one(message.from_user.id)

    if user:
        return message.answer(text="You are already registered.")
    elif not message.from_user.username:
        return message.answer(
            text="First, set the username in the settings of your Telegram account."
                 "\nAnd then use the /form command again"
        )
    else:
        await state.set_state(UserForm.name)
        await message.answer(
            text="Let's get started, enter your name.",
            reply_markup=await user_name_keyboard(message.from_user.first_name)
        )


# Handler for collecting user's name
@router.message(UserForm.name)
async def user_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserForm.age)
    await message.answer(
        text="How old are you?",
        reply_markup=remove_keyboard
    )


# Handler for collecting user's age
@router.message(UserForm.age)
async def user_gender(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserForm.gender)
        await message.answer(
            text="What gender are you?",
            reply_markup=gender_select_keyboard
        )
    else:
        await message.answer(text="Enter the number again!")


# Handler for collecting user's gender
@router.message(UserForm.gender)
async def user_city(message: Message, state: FSMContext):
    gender = await gender_check(message)

    if gender is not None:
        await state.update_data(gender=gender)
        await state.set_state(UserForm.city)
        await message.answer(
            text="What city are you from?",
            reply_markup=remove_keyboard
        )


# Handler for collecting user's city
@router.message(UserForm.city)
async def user_about(message: Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer(text="Enter the correct data.")
    else:
        await state.update_data(city=message.text)
        await state.set_state(UserForm.looking_for)
        await message.answer(
            text="Who do you want to find?",
            reply_markup=gender_select_keyboard
        )


# Handler for collecting who the user is looking for
@router.message(UserForm.looking_for)
async def user_about(message: Message, state: FSMContext):
    gender = await gender_check(message)

    if gender is not None:
        await state.update_data(looking_for=gender)
        await state.set_state(UserForm.about)
        await message.answer(
            text="Tell us a little about yourself. (Or click the button below to skip)",
            reply_markup=about_skip_keyboard
        )


# Handler for collecting user's about information
@router.message(UserForm.about)
async def user_photo(message: Message, state: FSMContext):
    if message.text.lower() == "🪪 skip":
        await state.update_data(about=None)
    else:
        await state.update_data(about=message.text)

    await state.set_state(UserForm.photo)
    await message.answer(
        text="Send your photo.",
        reply_markup=remove_keyboard
    )


# Handler for collecting user's photo
@router.message(UserForm.photo, F.photo)
async def user_reg(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    # Format the user data for display in the profile
    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {data.get('name')} | @{message.from_user.username}\n"
                      f"<b>🎀 Age:</b> {data.get('age')}\n"
                      f"<b>🌆 City:</b> {data.get('city')}\n"
                      f"<b>👫 Gender:</b> {data.get('gender')}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{data.get('about')}</i>")

    user_be_like = await LikesRepository().find_likes_to_user(message.from_user.id)

    # Send a message with the user's profile details and an inline keyboard for actions
    await message.answer_photo(
        photo=photo_file_id,
        caption=formatted_text,
        reply_markup=await profile_inline_kb(message.from_user.id, user_be_like)
    )

    # Download and upload the user's photo to Cloudinary
    photo_path = await download_photo(bot, photo_file_id, message.from_user.id)
    photo_url = await upload_photo_to_cloudinary(photo_path, message.from_user.id)

    # Update the user's information in the database
    data.update({'telegram_id': message.from_user.id, 'photo': photo_url, 'username': message.from_user.username})
    await UsersRepository().create_update_user(data)


# Handler for cases when the user doesn't send a photo during registration
@router.message(UserForm.photo, ~F.photo)
async def user_photo_error(message: Message, state: FSMContext):
    await message.answer("Send a photo!")


# Handler for editing the user's photo
@router.message(PhotoEditState.photo, F.photo)
async def photo_edit(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    await state.clear()
    user = await UsersRepository().get_one(message.from_user.id)
    user_be_like = await LikesRepository().find_likes_to_user(message.from_user.id)
    formatted_text = await format_user_data(user)

    # Send a message with the updated user's profile details and an inline keyboard for actions
    await message.answer_photo(photo=photo_file_id,
                               caption=formatted_text,
                               reply_markup=await profile_inline_kb(message.from_user.id, user_be_like))

    # Download and upload the updated photo to Cloudinary
    photo_path = await download_photo(bot, photo_file_id, message.from_user.id)
    photo_url = await upload_photo_to_cloudinary(photo_path, message.from_user.id)

    # Update the user's photo in the database
    data = {'telegram_id': message.from_user.id, 'photo_url': photo_url}
    await UsersRepository().photo_update(data)


# Handler for cases when the user doesn't send a photo during photo edit
@router.message(PhotoEditState.photo, ~F.photo)
async def user_photo_error(message: Message, state: FSMContext):
    await message.answer("Send a photo!")


# Handler for editing the user's about information
@router.message(AboutEditState.about)
async def about_edit_state(message: Message, state: FSMContext):
    if message.text.lower() == "🪪 skip":
        about = None
    else:
        about = message.text
    await state.clear()
    await message.answer("You have successfully updated your details.", reply_markup=remove_keyboard)

    # Update the user's about information in the database
    data = {'telegram_id': message.from_user.id, 'about': about}
    await UsersRepository().about_update(data)

    # Display the updated profile information to the user
    user = await UsersRepository().get_one(message.from_user.id)
    user_be_like = await LikesRepository().find_likes_to_user(message.from_user.id)
    formatted_text = await format_user_data(user)

    await message.answer_photo(photo=user.photo,
                               caption=formatted_text,
                               reply_markup=await profile_inline_kb(message.from_user.id, user_be_like))

# The code above defines handlers for different stages of user registration and profile editing,
# including collecting user information, handling photos, and updating database records.
