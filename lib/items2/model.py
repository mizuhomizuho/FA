import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, TIMESTAMP, ForeignKey
from lib.tools.db import DbTools

metadata = MetaData()

items2 = Table(
    'items2',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('params', JSON),
    Column('date', TIMESTAMP, default=DbTools.now_utc),
)

items3 = Table(
    'items3',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('items2_id', Integer, ForeignKey('items2.id')),
)

# engine = sqlalchemy.create_engine('xxxxxxxxxxxxxx', echo=True)
# metadata.create_all(engine)