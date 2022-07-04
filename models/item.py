from pydantic import BaseModel
from typing import Union


class ItemForCreateOrUpdate(BaseModel):
    title: str
    completed: Union[bool, None] = None


class Item(ItemForCreateOrUpdate):
    id: str
    url: str
