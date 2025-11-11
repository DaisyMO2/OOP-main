class MenuItem:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

class Drink(MenuItem):
    def __init__(self, name, price, available, size):
        super().__init__(name, price, available)
        self.size = size

    def order(self):
        print(f"Drink: {self.name}, Size: {self.size}, Price: {self.price}")

class Food(MenuItem):
    def __init__(self, name, price, available, is_vegetarian):
        super().__init__(name, price, available)
        self.is_vegetarian = is_vegetarian

    def order(self):
        print(f"Food: {self.name}, Veg: {self.is_vegetarian}, Price: {self.price}")

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_order(self):
        total = 0
        for i in self.items:
            i.order()
            total += i.price
        print(f"Total: {total}")


# Example
drink1 = Drink("Coke", 3000, True, "500ml")
food1 = Food("Burger", 8000, True, False)

order1 = Order()
order1.add_item(drink1)
order1.add_item(food1)
order1.display_order()
