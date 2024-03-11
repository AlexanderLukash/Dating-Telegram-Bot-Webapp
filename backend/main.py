from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot
from bot.misc import TgKeys
from db.models.user import User
from tortoise.contrib.fastapi import register_tortoise
from tortoise.queryset import QuerySet as Q

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": True, "data": "Connection success."}


@app.get("/users")
async def get_users():
    users = await User.all()
    return {"status": True, "data": users}


@app.get("/user/{user_id}")
async def get_user_data(user_id: int):
    user = await User.filter(telegram_id=user_id).first()

    if not user:
        return {"status": True, "data": "User not found!"}
    return {"status": True, "data": user}


@app.get("/users/city/{user_city}")
async def get_users_by_city(user_city: str):
    users = await User.filter(city=user_city)
    return {"status": True, "data": users}


@app.get("/users/age/{user_age}")
async def get_users_by_age(user_age: int):
    users = await User.filter(age=user_age)
    return {"status": True, "data": users}


@app.get("/users/best_results/{user_city}/{user_age}")
async def get_users_best_results(user_city: str, user_age: int):
    min_age = user_age - 3
    max_age = user_age + 3
    users = await User.filter(city=user_city, age__gte=min_age, age__lte=max_age)
    return {"status": True, "data": users}


register_tortoise(
    app,
    db_url="mysql://lukash:sasha2627@127.0.0.1:3306/dating_database",
    modules={'models': ['db.models.user']},
    generate_schemas=True,
    add_exception_handlers=True,
)
