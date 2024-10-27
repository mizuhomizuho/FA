import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from src.chat.router import router as router_chat
from src.operations.router import router as router_operation
from src.pages.router import router as router_pages
from src.tasks.router import router as router_tasks

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://fa_redis")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Trading App",
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_tasks)
app.include_router(router_pages)
app.include_router(router_chat)

origins = [
    "http://localhost:8014",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"],
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")

# https://fastapi.tiangolo.com/advanced/middleware/#adding-asgi-middlewares
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["meow"] = "meow"
    return response


# # yield
# async def get_async_session():
#     print("Получение сессии")
#     session = "session"
#     yield session
#     print("Уничтожение сессии")
#
# @app.get("/items")
# async def get_items(session=Depends(get_async_session)):
#     print(session)
#     return [{"id": 1}]
#
# # parameters
# def pagination_params(limit: int = 10, skip: int = 0):
#     return {"limit": limit, "skip": skip}
#
# @app.get("/subjects")
# async def get_subjects(pagination_params: dict = Depends(pagination_params)):
#     return pagination_params
#
# # class
# class Paginator:
#     def __init__(self, limit: int = 10, skip: int = 0):
#         self.limit = limit
#         self.skip = skip
#
# @app.get("/subjects_class")
# async def get_subjects_class(pagination_params: Paginator = Depends()):
#     return pagination_params
#
# # dependencies = [Depends(...)]
# # class call
# # request
#
# class AuthGuard:
#     def __init__(self, name: str):
#         self.name = name
#
#     def __call__(self, request: Request):
#         if "super_cookie" not in request.cookies:
#             raise HTTPException(status_code=403, detail="Запрещено")
#         # проверяем что в куках есть инфа о наличии прав пользователя
#         return True
#
# auth_guard_payments = AuthGuard("payments")
#
# router = APIRouter(
#     dependencies=[Depends(auth_guard_payments)]
# )
#
# @app.get("/payments", dependencies=[Depends(auth_guard_payments)])
# def get_payments():
#     return "my payments...."