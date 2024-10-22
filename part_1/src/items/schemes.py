from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

# class ItemType(Enum):
#     type1: str = 'type1'
#     type2: str = 'type2'

class ItemBase(BaseModel):
    name: str = Field(default='John', max_length=32)
    # non_negative: int = Field(ge=0)
    # negative: int = Field(lt=0)
    sort: int
    desc: str | None = None
    # type: ItemType
    # date_created: datetime

class Item(ItemBase):
    id: int

class ItemId(BaseModel):
    result: bool = True
    item_id: int