from typing import Annotated
from fastapi import APIRouter, Depends

from repository import ItemsRepo
from schemes import ItemBase, Item, ItemId

router = APIRouter(prefix='/items', tags=['Elements'])

@router.post('/add')
async def add(item: Annotated[ItemBase, Depends()]) -> ItemId:
    return {'result': True, 'item_id': await ItemsRepo().add(item)}

@router.post('')
async def list() -> dict[str, list[Item]]:
    return {'list': await ItemsRepo().list()}