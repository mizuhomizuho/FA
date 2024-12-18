import asyncio
from typing import AsyncGenerator
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from src.config import DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST, DB_USER_TEST
from src.database import get_async_session, metadata
from src.main import app

DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    # async with engine_test.begin() as conn:
    #     await conn.run_sync(metadata.drop_all)

# # Рекомендуется по документации для асинхронного клиента для старых версий
# # SETUP
# @pytest.fixture(scope='session')
# def event_loop(request):
#     """Create an instance of the default event loop for each test case."""
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()

# Синхронный клиент
client = TestClient(app)

# Асинхронный клиент
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
