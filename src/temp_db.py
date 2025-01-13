# Временное хранилище для грибов и корзинок
from typing import Dict

from models import Mushroom, Basket

mushrooms_db: Dict[int, Mushroom] = {}
baskets_db: Dict[int, Basket] = {}
