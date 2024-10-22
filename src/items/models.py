from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, JSON, Table
from src.tools.db import Tools
from src.tools.metadata import metadata

class ModelBase(DeclarativeBase):
    pass

class ItemsTable(ModelBase):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sort: Mapped[int]
    desc: Mapped[str | None]

items2_table = Table(
    'items2',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('params', JSON),
    Column('date', TIMESTAMP, default=Tools.now_utc),
)

items3_table = Table(
    'items3',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('items2_id', Integer, ForeignKey('items2.id')),
)