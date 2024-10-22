import datetime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
    'sqlite+aiosqlite:///db.sqlite', echo=True
)

new_sess = async_sessionmaker(engine, expire_on_commit=False)

class Tools:

    @staticmethod
    def now_utc():
        return datetime.datetime.fromtimestamp(datetime.datetime.now(datetime.UTC).timestamp())