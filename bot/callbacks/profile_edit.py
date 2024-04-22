from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

# Importing keyboard builders and keyboards from the bot
from bot.keyboards.builders import user_name_keyboard
from bot.keyboards.inline import profile_edit_keyboard, form_confirm_keyboard, photo_confirm_keyboard, \
    about_confirm_keyboard
from bot.keyboards.reply import about_skip_keyboard
from bot.utils.states import UserForm, PhotoEditState, AboutEditState

# Creating a router instance
router = Router()


# Callback function for editing the profile options
@router.callback_query(F.data == "profile_edit")
async def profile_edit(callback: CallbackQuery):
    await callback.message.delete()  # Delete the original message
    # Send a new message with profile edit options and the respective keyboard
    await callback.message.answer(
        text="1. Cancel.\n"
             "2. Fill out the profile again.\n"
             "3. Change photo.\n"
             "4. Change the text of the profile.\n",
        reply_markup=await profile_edit_keyboard()
    )


# Callback function for confirming filling out the profile again
@router.callback_query(F.data == "form")
async def from_profile(callback: CallbackQuery):
    # Edit the message to confirm filling out the profile again
    await callback.message.edit_text(text="Are you sure you want to fill out your profile again?",
                                     reply_markup=await form_confirm_keyboard())


# Callback function for confirming profile edit and initiating the form filling process
@router.callback_query(F.data == "form_confirm")
async def form_edit(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()  # Delete the confirmation message
    await state.set_state(UserForm.name)  # Set the state to UserForm.name
    # Send a message to start the form filling process with a keyboard to enter the user's name
    await callback.message.answer(
        text="Let's get started, enter your name.",
        reply_markup=await user_name_keyboard(callback.from_user.first_name)
    )


# Callback function for confirming photo edit
@router.callback_query(F.data == "photo_edit")
async def photo_profile(callback: CallbackQuery):
    # Edit the message to confirm changing the photo
    await callback.message.edit_text(text="Are you sure you want to change your photo?",
                                     reply_markup=await photo_confirm_keyboard())


# Callback function for confirming photo edit and initiating the photo changing process
@router.callback_query(F.data == "photo_confirm")
async def photo_edit(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()  # Delete the confirmation message
    await state.set_state(PhotoEditState.photo)  # Set the state to PhotoEditState.photo
    # Send a message to prompt the user to send a new photo for their profile
    await callback.message.answer(text="Send us a new photo for your profile.")


# Callback function for confirming about edit
@router.callback_query(F.data == "about_edit")
async def about_profile(callback: CallbackQuery):
    # Edit the message to confirm changing the about section
    await callback.message.edit_text(text="Are you sure you want to change your about section?",
                                     reply_markup=await about_confirm_keyboard())


# Callback function for confirming about edit and initiating the about section changing process
@router.callback_query(F.data == "about_confirm")
async def about_edit(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()  # Delete the confirmation message
    await state.set_state(AboutEditState.about)  # Set the state to AboutEditState.about
    # Send a message to prompt the user to input something about themselves or skip
    await callback.message.answer(
        text="Tell us something about yourself that might interest someone, "
             "or click the button to leave this field blank.",
        reply_markup=about_skip_keyboard  # Provide a keyboard to skip the about section
    )
