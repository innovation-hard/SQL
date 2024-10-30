from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
database = {}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in database:
        return {"item_id": item_id, "item": database[item_id]}
    else:
        return {"item_id": item_id, "item": {}}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    database[item_id] = item
    return {"item_name": item.name, "item_id": item_id}
