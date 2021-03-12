class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @staticmethod
    def cant_add_item(items, capacity):
        total_items = sum(value for value in items.values())
        return total_items == capacity

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items and amount <= items[item_name]

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item_name):
        if self.cant_add_item(self.items, self.capacity):
            return "Not enough capacity in the store"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if not self.can_remove_item(self.items, item_name, amount):
            return f'Cannot remove {amount} {item_name}'
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

