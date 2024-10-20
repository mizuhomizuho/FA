from sqlalchemy import select
from sqlalchemy.util import await_only

from lib.items.schemes import ItemBase, Item
from lib.tools.db import new_sess, ItemsTable

class ItemsRepo:

    async def add(self, data: ItemBase) -> int:
        async with new_sess() as sess:
            item_dict = data.model_dump()
            item_el = ItemsTable(**item_dict)
            sess.add(item_el)
            await sess.flush()
            await sess.commit()
            return item_el.id

    async def list(self) -> list[Item]:
        async with new_sess() as sess:
            q = select(ItemsTable)
            res = await sess.execute(q)
            return [Item.model_validate(_.__dict__) for _ in res.scalars().all()]