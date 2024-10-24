from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from src.operations.router import router as router_operation


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://fa_redis")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Trading App",
)

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

@app.get("/")
@cache(expire=60)
async def index():
    return dict(hello="world")