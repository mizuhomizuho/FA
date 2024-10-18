from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    sort: int
    desc: str | None = None
    # def __init__(self):
    #     super().__init__()
    #     pass

class Item(ItemBase):
    id: int

class ItemId(BaseModel):
    result: bool = True
    item_id: int