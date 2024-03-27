from aiogram.fsm.state import StatesGroup, State


class UserForm(StatesGroup):
    name = State()
    age = State()
    gender = State()
    city = State()
    looking_for = State()
    about = State()
    photo = State()
