from pydantic import BaseModel
from typing import Union


class ItemForCreateAndUpdate(BaseModel):
    title: Union[str, None] = None
    completed: Union[bool, None] = None
    order: Union[int, None] = None


class Item(ItemForCreateAndUpdate):
    id: str
    url: str
