from pydantic import BaseModel
from typing import Union


class ItemForCreateOrUpdate(BaseModel):
    name: str
    completed: Union[bool, None] = None


class Item(ItemForCreateOrUpdate):
    id: str
    url: str
