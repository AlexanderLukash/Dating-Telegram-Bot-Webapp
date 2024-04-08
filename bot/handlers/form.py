from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline import plofile_inline_kb
from bot.utils.states import UserForm
from bot.keyboards.builders import user_name_keyboard
from bot.keyboards.reply import remove_keyboard, gender_select_keyboard, about_skip_keyboard
from db.models.user import User
from db.models.likes import Likes
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="dndstfjbu",
    api_key="399658246291491",
    api_secret="lSMOzkIj3JUOnNpZ0rvHz9pIDC4"
)

router = Router()


@router.message(Command("form"))
async def user_form(message: Message, state: FSMContext):
    user = await User.filter(telegram_id=message.from_user.id).first()
    if user:
        return message.answer(text="You are already registered.")
    else:
        await state.set_state(UserForm.name)
        await message.answer(
            text="Let's get started, enter your name.",
            reply_markup=await user_name_keyboard(message.from_user.first_name)
        )


@router.message(UserForm.name)
async def user_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserForm.age)
    await message.answer(
        text="How old are you?",
        reply_markup=remove_keyboard
    )


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


@router.message(UserForm.gender)
async def user_city(message: Message, state: FSMContext):
    if message.text.lower() == "👨 boy":
        gender = "Boy"
    elif message.text.lower() == "👧 girl":
        gender = "Girl"
    else:
        await message.answer(text="Click on the button 👇", reply_markup=gender_select_keyboard)
        return

    await state.update_data(gender=gender)
    await state.set_state(UserForm.city)
    await message.answer(
        text="What city are you from?",
        reply_markup=remove_keyboard
    )


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


@router.message(UserForm.looking_for)
async def user_city(message: Message, state: FSMContext):
    if message.text.lower() == "👨 boy":
        gender = "Boy"
    elif message.text.lower() == "👧 girl":
        gender = "Girl"
    else:
        await message.answer(text="Click on the button 👇", reply_markup=gender_select_keyboard)
        return

    await state.update_data(looking_for=gender)
    await state.set_state(UserForm.about)
    await message.answer(
        text="Tell us a little about yourself. (Or click the button below to skip)",
        reply_markup=about_skip_keyboard
    )


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


@router.message(UserForm.photo, F.photo)
async def user_reg(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    formatted_text = ("<b>✨ Your survey:</b> \n\n"
                      f"<b>👋 Name:</b> {data.get('name')} | @{message.from_user.username}\n"
                      f"<b>🎀 Age:</b> {data.get('age')}\n"
                      f"<b>🌆 City:</b> {data.get('city')}\n"
                      f"<b>👫 Gender:</b> {data.get('gender')}\n"
                      f"<b>✍️ About you:</b> \n"
                      f"<i>{data.get('about')}</i>")

    user_be_like = await Likes.filter(to_user_id=message.from_user.id)
    user_liked = await Likes.filter(from_user_id=message.from_user.id)

    await message.answer_photo(
        photo=photo_file_id,
        caption=formatted_text,
        reply_markup=await plofile_inline_kb(message.from_user.id, user_be_like, user_liked)
    )

    file = await bot.get_file(photo_file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"photos/{message.from_user.id}.jpg")
    photo_url = cloudinary.uploader.upload(f"photos/{message.from_user.id}.jpg",
                                           folder="photos",
                                           public_id=f"{message.from_user.id}")

    await User.create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.first_name,
        age=data.get('age'),
        gender=data.get('gender'),
        looking_for=data.get('looking_for'),
        city=data.get('city'),
        about=data.get('about'),
        photo=photo_url.get('url')
    )


@router.message(UserForm.photo, ~F.photo)
async def user_photo_error(message: Message, state: FSMContext):
    await message.answer("Send a photo!")
