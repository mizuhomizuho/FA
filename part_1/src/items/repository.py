from sqlalchemy import select
from src.items.models import ItemsTable
from src.items.schemes import ItemBase, Item
from src.tools.db import new_sess

class ItemsRepo:

    async def add(self, data: ItemBase) -> int:
        async with new_sess() as sess:
            item_dict = data.model_dump()
            item_el = ItemsTable(**item_dict)
            sess.add(item_el)
            await sess.flush()
            await sess.commit()
            return item_el.id

    async def list(self, limit: int, offset: int) -> list[Item]:

        # xxx = [1,2,34,5,5668,78,67,56,7]
        # x1 = 2
        # x2 = 4
        # print(xxx[x1:][:x2])

        from starlette import status
        print(status.HTTP_422_UNPROCESSABLE_ENTITY)
        # ''  #

        async with new_sess() as sess:
            q = select(ItemsTable)
            res = await sess.execute(q)
            return [Item.model_validate(item.__dict__) for item in res.scalars().all()]