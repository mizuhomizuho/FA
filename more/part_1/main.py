from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from urllib.request import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from starlette import status
from starlette.responses import JSONResponse
from src.auth.auth import auth_backend
from src.auth.db import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.items.router import router as items_router
from src.lib import Lib
from fastapi_users import FastAPIUsers

@asynccontextmanager
async def lifespan(app: FastAPI):
    inst = Lib('tools/tools', 'Tools').get()()
    await inst.lifespan()
    yield
    await inst.lifespan_end()

app = FastAPI(lifespan=lifespan, title='FAProj')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'meow': True, 'detail': exc.errors()})
    )

app.include_router(items_router)

@app.get('/')
async def hi():
    return {'data': 'Hi'}
