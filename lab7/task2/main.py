from models import Order, ExpressOrder, PickupOrder

def main():
    simple = Order(101, "Пицца", 600)
    fast = ExpressOrder(102, "Суши", 1500, "89991234567")
    self_service = PickupOrder(103, "Кофе", 450, "ул. Ленина 10")

    orders = [simple, fast, self_service]

    print("Список заказов")
    for o in orders:
        print(o)
        print(f"Доставка {o.calculate_delivery()}")

    print("\nСпец действия")
    print(fast.call_courier())
    print(self_service.get_map_link())

if __name__ == "__main__":
    main()