from sqlalchemy import (Table, Column, Integer, String, TIMESTAMP, ForeignKey,
                        JSON, Boolean, MetaData)
from lib.tools.db import DbTools

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=DbTools.now_utc),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

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