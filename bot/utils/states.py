from aiogram.fsm.state import StatesGroup, State

class UserForm(StatesGroup):
    name = State()
    age = State()
    gender = State()
    city = State()
    about = State()
    photo = State()
