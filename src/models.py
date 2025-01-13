from pydantic import BaseModel, Field
from typing import List


class Mushroom(BaseModel):
    id: int
    name: str = Field(..., title="Название гриба")
    edibility: str = Field(..., title="Съедобность гриба")  # Например, "съедобный" или "несъедобный"
    weight: float = Field(..., gt=0, title="Вес в граммах")  # Вес должен быть положительным
    freshness: str = Field(..., title="Свежесть гриба")  # Например, "свежий", "вялый"


class Basket(BaseModel):
    id: int
    owner: str = Field(..., title="Кому принадлежит корзинка")
    capacity: float = Field(..., gt=0, title="Вместительность в граммах")  # Вместительность должна быть положительной
    mushrooms: List[Mushroom] = Field(default_factory=list, title="Список грибов в корзинке")