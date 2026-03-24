import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from backapi.models import Category, Product

def fill_db():
    Product.objects.all().delete()
    Category.objects.all().delete()

    cat1 = Category.objects.create(name="Смартфоны")
    cat2 = Category.objects.create(name="Ноутбуки")
    cat3 = Category.objects.create(name="Аксессуары")

    Product.objects.create(name="iPhone 15", price=450000.0, description="128GB, Black", count=10, is_active=True, category=cat1)
    Product.objects.create(name="Samsung S24", price=420000.0, description="256GB, Gray", count=5, is_active=True, category=cat1)

    Product.objects.create(name="MacBook Air M2", price=600000.0, description="8/256GB", count=3, is_active=True, category=cat2)
    Product.objects.create(name="Asus ROG", price=750000.0, description="Gaming laptop", count=2, is_active=True, category=cat2)

    Product.objects.create(name="AirPods Pro", price=120000.0, description="Wireless noise cancelling", count=15, is_active=True, category=cat3)

    print("База данных успешно заполнена!")

if __name__ == '__main__':
    fill_db()