from fastapi import FastAPI
from typing import List

from fastapi.responses import JSONResponse

from db.models.user import User, User_Pydantic
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/")
async def root():
    return await User.all()


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    users = await User_Pydantic.from_queryset(User.all())
    return JSONResponse(users, status_code=200)


register_tortoise(
    app,
    db_url="mysql://lukash:sasha2627@127.0.0.1:3306/dating_database",
    modules={'models': ['db.models.user']},
    generate_schemas=True,
    add_exception_handlers=True,
)
