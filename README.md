# Тестовое задание подготовлено Салтыковым Алексеем

## Описание проекта
    
"Mushroom Basket API" — это тестовое веб-приложение, разработанное с использованием FastAPI, которое позволяет управлять грибами и корзинами для их хранения. Пользователи могут добавлять, обновлять и удалять грибы и корзины, а также управлять содержимым корзин.

###Установка

Требования:

    Python 3.7 или выше
    FastAPI
    Uvicorn (для запуска сервера)

Установка зависимостей
Сначала клонируйте репозиторий:

    git clone https://github.com/HoolyWant/fast_mush_test_case.git

    cd <папка_проекта>

Установите необходимые зависимости:

    pip install fastapi uvicorn

### Запуск приложения

Для запуска приложения используйте Uvicorn:

     uvicorn main1:app --reload --host 0.0.0.0

Здесь main — это имя файла (без расширения), в котором находится код вашего приложения.


### Эндпоинты API

Грибы:

    Создать гриб
        POST /mushrooms/
        Тело запроса: {"id": int, "name": str, "edible": bool, "weight": float, "freshness": str}
        
    Обновить гриб
        PUT /mushrooms/{mushroom_id}
        Тело запроса: аналогично созданию гриба
        
    Получить гриб по ID
        GET /mushrooms/{mushroom_id}
        
    Получить список всех грибов
        GET /mushrooms/
    

Корзины:

    Создать корзину
        POST /baskets/
        Тело запроса: {"id": int, "owner": str, "capacity": float}
        
    Добавить гриб в корзину
        POST /baskets/{basket_id}/mushrooms/{mushroom_id}
        
    Удалить гриб из корзины
        DELETE /baskets/{basket_id}/mushrooms/{mushroom_id}
        
    Получить корзину по ID
        GET /baskets/{basket_id}

Примеры запросов в формате JSON:

    Гриб:
        {
        "id": 1,
        "name": "Белый гриб",
        "edibility": "съедобный",
        "weight": 300.5,
        "freshness": "свежий"
        }

    Корзина:
        {
        "id": 1,
        "owner": "Иван Иванов",
        "capacity": 2000.0,
        "mushrooms": [
            {
            "id": 1,
            "name": "Белый гриб",
            "edibility": "съедобный",
            "weight": 300.5,
            "freshness": "свежий"
            },
            {
            "id": 2,
            "name": "Мухомор",
            "edibility": "несъедобный",
            "weight": 150.0,
            "freshness": "вялый"
            }
        ]
        }    
