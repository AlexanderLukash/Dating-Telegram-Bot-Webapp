from fastapi import FastAPI
from backend.api.routers import all_routers
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

# Create an instance of FastAPI with a title and a Swagger UI theme
app = FastAPI(
    title="Dating Telegram WebApp",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

# Add CORS middleware to allow cross-origin resource sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,  # Allow credentials like cookies
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
for router in all_routers:
    app.include_router(router)


# Define a root endpoint that returns a success message
@app.get("/")
async def root():
    return {"status": True, "data": "Connection success."}


# Register Tortoise ORM with FastAPI
register_tortoise(
    app,
    db_url="mysql://lukash:sasha2627@127.0.0.1:3306/dating_database",  # Database URL
    modules={'models': ['db.models.user', 'db.models.likes']},  # Models to register
    generate_schemas=True,
    add_exception_handlers=True,
)
