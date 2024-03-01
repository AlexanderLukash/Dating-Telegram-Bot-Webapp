from fastapi import FastAPI
from typing import List
from db.models.user import User, User_Pydantic
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/")
async def root():
    return await User.all()


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


register_tortoise(
    app,
    db_url="mysql://lukash:sasha2627@127.0.0.1:3306/dating_database",
    modules={'models': ['db.models.user']},
    generate_schemas=True,
    add_exception_handlers=True,
)
