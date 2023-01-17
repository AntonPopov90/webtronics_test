import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users, FastAPIUsers
from authentication.auth import auth_backend
from database import User
from authentication.manager import get_user_manager
from authentication.schemas import UserRead, UserCreate
from posts.router import router as posts_router

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title='Test task webtronics')
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"],
    prefix="/auth/jwt",
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(posts_router)
current_user = fastapi_users.current_user()


