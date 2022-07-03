from fastapi import FastAPI, Request
from uuid import uuid4
from models.item import Item
from typing import List, Dict

db: Dict[str, Item] = dict()

tutorial_app = FastAPI()


@tutorial_app.get('/')
def get_all() -> List[Item]:
    return list(db.values())


@tutorial_app.get('/{item_id}')
def get_by_id(item_id) -> Item:
    return db[item_id]


@tutorial_app.post('/')
def create_item(item: Item, request: Request) -> Item:
    new_item_id = str(uuid4())
    item.id = new_item_id
    item.url = f'{request.base_url}{new_item_id}'
    if item.completed is None:
        item.completed = False
    db[new_item_id] = item
    return db[new_item_id]


@tutorial_app.patch('/{item_id}')
def edit_item(item_id: str, item: Item) -> Item:
    item.id = item_id
    if item.completed is None:
        item.completed = db[item_id].completed
    if item.url is None:
        item.url = db[item_id].url
    if item.completed is None:
        item.completed = False
    db[item_id] = item
    return db[item_id]


@tutorial_app.delete('/')
def delete_all():
    db.clear()
    return db


@tutorial_app.delete('/{item_id}')
def delete_item(item_id):
    del db[item_id]
