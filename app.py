from fastapi import Request, HTTPException, APIRouter
from uuid import uuid4
from models.item import Item, ItemForCreateOrUpdate
from typing import List

router = APIRouter(prefix='/todos')
cache = dict()


@router.get('')
async def get_all() -> List[Item]:
    return list(cache.values())


@router.get('/{item_id}')
async def get_by_id(item_id) -> Item:
    item = cache.get(item_id, None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post('')
async def create_item(item: ItemForCreateOrUpdate, request: Request) -> Item:
    new_item_id = str(uuid4())
    created_item = Item(
        id=new_item_id,
        title=item.title,
        url=f'{request.base_url}todos/{new_item_id}',
        completed=item.completed
    )

    if created_item.completed is None:
        created_item.completed = False
    cache[new_item_id] = created_item
    return created_item


@router.patch('/{item_id}')
async def edit_item(item_id: str, item: ItemForCreateOrUpdate) -> Item:
    saved_item = cache.get(item_id, None)

    if saved_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = Item(
        id=item_id,
        title=item.title,
        completed=item.completed,
        url=saved_item.url
    )
    if updated_item.completed is None:
        updated_item.completed = saved_item.completed
    cache[item_id] = updated_item
    return updated_item


@router.delete('')
async def delete_all():
    cache.clear()


@router.delete('/{item_id}')
async def delete_item(item_id):
    saved_item = cache.get(item_id, None)

    if saved_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    del cache[item_id]
