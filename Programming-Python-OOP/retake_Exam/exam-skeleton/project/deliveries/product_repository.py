class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        if product in self.products:
            raise ValueError(f"Product {product.name} already exists.")
        self.products.append(product)
        return f"Product {product.name} successfully added to inventory."

    @staticmethod
    def decrease(product, quantity):
        product.quantity -= quantity
        return f"Left quantity of {product.name}: {product.quantity}"

    def find(self, product_name):
        try:
            a = [p for p in self.products if p.name == product_name][0]
        except:
            return "None"
        return a

