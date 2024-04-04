from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bot.handlers.user_commands import send_message
from db.models.user import User, Likes
from tortoise.contrib.fastapi import register_tortoise

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


@app.get("/users/best_results/{user_id}/{user_city}/{user_age}")
async def get_users_best_results(user_id: int, user_city: str, user_age: int):
    min_age = user_age - 3
    max_age = user_age + 3
    users = await User.filter(city=user_city, age__gte=min_age, age__lte=max_age)
    return {"status": True, "data": users}


@app.get("/get/likes/from/{user}")
async def get_likes_from_user(user: int):
    likes = await Likes.filter(from_user_id=user)
    return {"status": True, "data": likes}


@app.get("/get/likes/to/{user}")
async def get_likes_to_user(user: int):
    likes = await Likes.filter(to_user_id=user)
    return {"status": True, "data": likes}


@app.get("/add/like/{from_user}/{to_user}")
async def add_like(from_user: int, to_user: int):
    like = await Likes.filter(from_user_id=from_user, to_user_id=to_user).first()

    if like:
        return {"status": True, "data": "The like is already there."}
    else:
        await Likes.create(
            from_user_id=from_user,
            to_user_id=to_user
        )
        await send_message(to_user, text="<b>You were liked 💗</b>")
        return {"status": True, "data": "Like added success."}


@app.get("/remove/like/{from_user}/{to_user}")
async def remove_like(from_user: int, to_user: int):
    like = await Likes.filter(from_user_id=from_user, to_user_id=to_user).first()

    if like:
        await like.delete()
        return {"status": True, "data": "Like removed success."}
    else:
        return {"status": True, "data": "The like is not already there."}


register_tortoise(
    app,
    db_url="mysql://lukash:sasha2627@127.0.0.1:3306/dating_database",
    modules={'models': ['db.models.user']},
    generate_schemas=True,
    add_exception_handlers=True,
)
