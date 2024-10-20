from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    sort: int
    desc: str | None = None

class Item(ItemBase):
    id: int

class ItemId(BaseModel):
    result: bool = True
    item_id: int