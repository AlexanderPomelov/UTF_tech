### Запуск приложения

1.Запускаем контейнер

    docker-compose up -d

2.Применяем миграции

    docker-compose run django python manage.py migrate  

3.Создаем superuser

    docker-compose run django manage.py createsuperuser

    Пользователь:admin
    email:
    password:admin
    confirm_password:admin

4.Через ```localhost:8000/admin``` добавить данные в БД

5.Проверяем результат ```localhost:8000/api/v1/foods```
    
### Результат должен получиться такой 

```json
[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 2,
                "code": 200,
                "name_ru": "Байкал",
                "description_ru": "Байкал",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": null,
        "name_ch": null,
        "order_id": 20,
        "foods": [
            {
                "internal_code": 5,
                "code": 500,
                "name_ru": "Круасан",
                "description_ru": "Круасан",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "100.00",
                "additional": []
            }
        ]
    },
    {
        "id": 3,
        "name_ru": "Салат",
        "name_en": null,
        "name_ch": null,
        "order_id": 30,
        "foods": [
            {
                "internal_code": 6,
                "code": 600,
                "name_ru": "Оливье",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "50.00",
                "additional": []
            }
        ]
    }
]
```
