from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.utils.states import UserForm
from bot.keyboards.builders import user_name_keyboard
from bot.keyboards.reply import remove_keyboard, gender_select_keyboard, about_skip_keyboard
from db.models.user import User

router = Router()


@router.message(Command("form"))
async def user_form(message: Message, state: FSMContext):
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
    await state.update_data(age=message.text)
    await state.set_state(UserForm.gender)
    await message.answer(
        text="Хто ви?",
        reply_markup=gender_select_keyboard
    )


@router.message(UserForm.gender)
async def user_city(message: Message, state: FSMContext):
    if message.text.lower() == "👨хлопець" or "хлопець" or "парень":
        gender = 1
    elif message.text.lower() == "👧 дівчина" or "дівчина" or "девушка":
        gender = 2
    else:
        await message.answer(text="Введіть коректні дані.")
        return

    await state.update_data(gender=gender)
    await state.set_state(UserForm.city)
    await message.answer(text="З якого ви міста?")


@router.message(UserForm.city)
async def user_country(message: Message, state: FSMContext):
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
async def user_about(message: Message, state: FSMContext):
    if message.text.lower() == "🪪 пропустити":
        await state.update_data(about=None)
    else:
        await state.update_data(about=message.text)

    await state.set_state(UserForm.photo)
    await message.answer(text="Надішліть своє фото.")


@router.message(UserForm.photo, F.photo)
async def user_photo(message: Message, state:FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    fromatted_text = ("Ваша анкета: \n"
                      f"Ім'я: {data.get('name')}\n"
                      f"Вік: {data.get('age')}\n"
                      f"Місто: {data.get('city')}\n"
                      f"Стать: {data.get('gender')}\n"
                      f"Про вас: {data.get('about')}")

    await message.answer_photo(
        photo=photo_file_id,
        caption=fromatted_text
    )

    await User.create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.first_name,
        age=data.get('age'),
        gender=data.get('gender'),
        city=data.get('city'),
        about=data.get('about'),
        photo=photo_file_id
    )


@router.message(UserForm.photo, ~F.photo)
async def user_photo_error(message: Message, state:FSMContext):
    await message.answer("Відправте фото!")
