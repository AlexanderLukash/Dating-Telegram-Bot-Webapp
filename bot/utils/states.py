# Importing necessary modules for defining states in a finite state machine (FSM)
from aiogram.fsm.state import StatesGroup, State


# Defining a state group named UserForm to represent different stages of a user's form submission
class UserForm(StatesGroup):
    # Each State() instance represents a specific stage in the form submission process
    name = State()  # State for capturing the user's name
    age = State()  # State for capturing the user's age
    gender = State()  # State for capturing the user's gender
    city = State()  # State for capturing the user's city
    looking_for = State()  # State for capturing what the user is looking for
    about = State()  # State for capturing information about the user
    photo = State()  # State for capturing the user's photo


# Defining a state group named PhotoEditState to represent the stage of editing a user's photo
class PhotoEditState(StatesGroup):
    photo = State()  # State for capturing the edited photo


# Defining a state group named AboutEditState to represent the stage of editing the user's about information
class AboutEditState(StatesGroup):
    about = State()  # State for capturing the edited about information
