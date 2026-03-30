# Lab 8: Shop Backend

## Endpoints
    - [GET] /api/categories/
    - [GET] /api/categories/<int:id>/
    - [GET] /api/categories/<int:id>/products/
    - [GET] /api/products/
    - [GET] /api/products/<int:id>/
## Example of response
    {
    "id": 1,
    "name": "iPhone 15",
    "price": 450000.0,
    "description": "128GB, Black",
    "count": 10,
    "is_active": true,
    "category_id": 1
}

## Как запустить проект

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/Yogksai/web
   cd lab8
   python3 -m venv venv
   source venv/bin/activate # for Unix systems
   ```
2. **Установка и миграция**
    ```bash
   pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
   ```
3. **Запуск сервера**
    ```bash
   python manage.py runserver
    ```
