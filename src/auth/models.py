from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, JSON, Table
from src.tools.db import Tools
from src.tools.metadata import metadata

role_table = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user_table = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=Tools.now_utc),
    Column("role_id", Integer, ForeignKey(role_table.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)