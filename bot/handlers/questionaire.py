from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline import web_app_markup
from bot.utils.states import UserForm
from bot.keyboards.builders import user_name_keyboard
from bot.keyboards.reply import remove_keyboard, gender_select_keyboard, about_skip_keyboard
from db.models.user import User
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
        return message.answer(text="Ви вже зарегістровані.")
    else:
        await state.set_state(UserForm.name)
        await message.answer(
            text="Давайте почнемо, введіть своє ім'я.",
            reply_markup=await user_name_keyboard(message.from_user.first_name)
        )


@router.message(UserForm.name)
async def user_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserForm.age)
    await message.answer(
        text="Скільки вам років? (Мінімальний вік 13 років.)",
        reply_markup=remove_keyboard
    )


@router.message(UserForm.age)
async def user_gender(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserForm.gender)
        await message.answer(
            text="Хто ви?",
            reply_markup=gender_select_keyboard
        )
    else:
        await message.answer(text="Введіть число ще раз!")


@router.message(UserForm.gender)
async def user_city(message: Message, state: FSMContext):
    if message.text.lower() == "👨 хлопець":
        gender = "Хлопець"
    elif message.text.lower() == "👧 дівчина":
        gender = "Дівчина"
    else:
        await message.answer(text="Натисніть на кнопку 👇", reply_markup=gender_select_keyboard)
        return

    await state.update_data(gender=gender)
    await state.set_state(UserForm.city)
    await message.answer(
        text="З якого ви міста?",
        reply_markup=remove_keyboard
    )


@router.message(UserForm.city)
async def user_about(message: Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer(text="Введіть коректні дані.")
    else:
        await state.update_data(city=message.text)
        await state.set_state(UserForm.about)
        await message.answer(
            text="Розкажіть трошки про себе. (Або натисніть на кнопку нижче, щоб провустити)",
            reply_markup=about_skip_keyboard
        )


@router.message(UserForm.about)
async def user_photo(message: Message, state: FSMContext):
    if message.text.lower() == "🪪 пропустити":
        await state.update_data(about=None)
    else:
        await state.update_data(about=message.text)

    await state.set_state(UserForm.photo)
    await message.answer(
        text="Надішліть своє фото.",
        reply_markup=remove_keyboard
    )


@router.message(UserForm.photo, F.photo)
async def user_reg(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    formatted_text = ("<b>✨ Ваша анкета:</b> \n\n"
                      f"<b>👋 Ім'я:</b> {data.get('name')} | @{message.from_user.username}\n"
                      f"<b>🎀 Вік:</b> {data.get('age')}\n"
                      f"<b>🌆 Місто:</b> {data.get('city')}\n"
                      f"<b>👫 Стать:</b> {data.get('gender')}\n"
                      f"<b>✍️ Про вас:</b> \n"
                      f"<i>{data.get('about')}</i>")

    await message.answer_photo(
        photo=photo_file_id,
        caption=formatted_text,
        reply_markup=web_app_markup
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
        city=data.get('city'),
        about=data.get('about'),
        photo=photo_url.get('url')
    )


@router.message(UserForm.photo, ~F.photo)
async def user_photo_error(message: Message, state: FSMContext):
    await message.answer("Відправте фото!")
