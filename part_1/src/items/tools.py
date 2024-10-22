from src.items.models import ModelBase
from src.tools.db import engine

class Tools:

    async def create_db(self):
        async with engine.begin() as conn:
            await conn.run_sync(ModelBase.metadata.create_all)

    async def drop_db(self):
        async with engine.begin() as conn:
            await conn.run_sync(ModelBase.metadata.drop_all)