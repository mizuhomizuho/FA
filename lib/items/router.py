from typing import Annotated
from fastapi import APIRouter, Depends
from lib.items.schemes import ItemBase, ItemId, Item
from lib.lib import Lib

router = APIRouter(prefix='/items', tags=['Elements'])

@router.post('/add')
async def add(item: Annotated[ItemBase, Depends()]) -> ItemId:
    inst = Lib('items/repository', 'ItemsRepo').get()
    return {'result': True, 'item_id': await inst().add(item)}

@router.get('', response_model=dict[str, list[Item]])
async def list(limit: int = 20, offset: int = 0) -> dict[str, list[Item]]:
    inst = Lib('items/repository', 'ItemsRepo').get()
    return {'list': await inst().list(limit, offset)}

@router.get('/{id}')
async def get(id: int) -> Item:
    inst = Lib('items/repository', 'ItemsRepo').get()
    return {'list': await inst().get(id)}