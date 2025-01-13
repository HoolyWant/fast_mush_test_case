from typing import List

from fastapi import FastAPI, HTTPException

from models import Mushroom, Basket
from temp_db import mushrooms_db, baskets_db

app = FastAPI()


# Эндпоинты для работы с грибами
@app.post("/mushrooms/", response_model=Mushroom)
def create_mushroom(mushroom: Mushroom):
    if mushroom.id in mushrooms_db:
        raise HTTPException(status_code=400, detail="Mushroom already exists")
    mushrooms_db[mushroom.id] = mushroom
    return mushroom


@app.put("/mushrooms/{mushroom_id}", response_model=Mushroom)
def update_mushroom(mushroom_id: int, mushroom: Mushroom):
    if mushroom_id not in mushrooms_db:
        raise HTTPException(status_code=404, detail="Mushroom not found")
    mushrooms_db[mushroom_id] = mushroom
    return mushroom


@app.get("/mushrooms/{mushroom_id}", response_model=Mushroom)
def get_mushroom(mushroom_id: int):
    if mushroom_id not in mushrooms_db:
        raise HTTPException(status_code=404, detail="Mushroom not found")
    return mushrooms_db[mushroom_id]


# Эндпоинт для получения списка всех грибов
@app.get("/mushrooms/", response_model=List[Mushroom])
def get_mushrooms():
    return list(mushrooms_db.values())


# Эндпоинты для работы с корзинами
@app.post("/baskets/", response_model=Basket)
def create_basket(basket: Basket):
    if basket.id in baskets_db:
        raise HTTPException(status_code=400, detail="Basket already exists")
    baskets_db[basket.id] = basket
    return basket


@app.post("/baskets/{basket_id}/mushrooms/{mushroom_id}")
def add_mushroom_to_basket(basket_id: int, mushroom_id: int):
    if basket_id not in baskets_db:
        raise HTTPException(status_code=404, detail="Basket not found")
    if mushroom_id not in mushrooms_db:
        raise HTTPException(status_code=404, detail="Mushroom not found")

    basket = baskets_db[basket_id]
    basket.mushrooms.append(mushrooms_db[mushroom_id])
    return basket


@app.delete("/baskets/{basket_id}/mushrooms/{mushroom_id}")
def remove_mushroom_from_basket(basket_id: int, mushroom_id: int):
    if basket_id not in baskets_db:
        raise HTTPException(status_code=404, detail="Basket not found")

    basket = baskets_db[basket_id]
    for mushroom in basket.mushrooms:
        if mushroom.id == mushroom_id:
            basket.mushrooms.remove(mushroom)
            return {"detail": "Mushroom removed from basket"}

    raise HTTPException(status_code=404, detail="Mushroom not found in the basket")


@app.get("/baskets/{basket_id}", response_model=Basket)
def get_basket(basket_id: int):
    if basket_id not in baskets_db:
        raise HTTPException(status_code=404, detail="Basket not found")
    return baskets_db[basket_id]