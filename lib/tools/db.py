import datetime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from lib.items.model import ModelBase

engine = create_async_engine(
    'sqlite+aiosqlite:///db.sqlite', echo=True
)

new_sess = async_sessionmaker(engine, expire_on_commit=False)

class DbTools:

    async def create_db(self):
        async with engine.begin() as conn:
            await conn.run_sync(ModelBase.metadata.create_all)

    async def drop_db(self):
        async with engine.begin() as conn:
            await conn.run_sync(ModelBase.metadata.drop_all)

    @staticmethod
    def now_utc():
        return datetime.datetime.fromtimestamp(datetime.datetime.now(datetime.UTC).timestamp())