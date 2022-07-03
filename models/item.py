from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    id: Union[str, None] = None
    name: Union[str, None] = None
    completed: Union[bool, None] = None
    url: Union[str, None] = None
