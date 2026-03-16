class Order:
    def __init__(self, order_id, items, price):
        self.order_id = order_id
        self.items = items
        self.price = price
        self.status = "Принят"

    def update_status(self, new_status):
        self.status = new_status
        return f"Заказ {self.order_id} статус {self.status}"

    def calculate_delivery(self):
        return 200

    def __str__(self):
        return f"Заказ {self.order_id} {self.items} за {self.price}"


class ExpressOrder(Order):
    def __init__(self, order_id, items, price, courier_phone):
        super().__init__(order_id, items, price)
        self.courier_phone = courier_phone

    def call_courier(self):
        return f"Звонок курьеру на {self.courier_phone}"

    def calculate_delivery(self):
        return super().calculate_delivery() * 1.5


class PickupOrder(Order):
    def __init__(self, order_id, items, price, address):
        super().__init__(order_id, items, price)
        self.address = address

    def calculate_delivery(self):
        return 0

    def get_map_link(self):
        return f"Точка сбора {self.address}"