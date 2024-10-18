from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    'sqlite+aiosqlite:///db.sqlite', echo=True
)

new_sess = async_sessionmaker(engine, expire_on_commit=False)

class ModelBase(DeclarativeBase):
    pass

class ItemsTable(ModelBase):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sort: Mapped[int]
    desc: Mapped[str | None]

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
