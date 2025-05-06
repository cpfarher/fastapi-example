from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import script

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

external_data = {
    "name": "John Doe",
    "description": "A very nice item that has a long description",
    "price": 100.0,
    "is_offer": True,
}

Item(**external_data)

@app.get("/")
async def read_root():
    return {"message": "Hello, World! " + script.get_full_name("Christian", "Pfarher")}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item": item}
