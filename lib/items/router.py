from typing import Annotated
from fastapi import APIRouter, Depends
from lib.items.schemes import ItemBase, ItemId, Item
from lib.lib import Lib

router = APIRouter(prefix='/items', tags=['Elements'])

@router.post('/add')
async def add(item: Annotated[ItemBase, Depends()]) -> ItemId:
    inst = Lib('items/repository', 'ItemsRepo').get()
    return {'result': True, 'item_id': await inst().add(item)}

@router.post('')
async def list() -> dict[str, list[Item]]:
    inst = Lib('items/repository', 'ItemsRepo').get()
    return {'list': await inst().list()}