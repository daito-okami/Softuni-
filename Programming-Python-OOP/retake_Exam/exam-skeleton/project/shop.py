from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type, name):
        product = self.make_product(product_type, name)
        self.product_repository.add(product)

    def sell(self, customer_name, **shopping_list):
        customer = self.make_customer(customer_name)
        bought_items = {}
        result = ""

        if customer not in self.customer_repository.customers:
            self.customer_repository.add(customer)
        for key, value in shopping_list.items():
            product = self.product_repository.find(key)
            try:
                result += self.product_repository.decrease(product, value)
            except ValueError:
                self.product_repository.products.remove(product)
                result += f"Left quantity of {product.name}: 0"
            result += "\n"
            bought_items[key] = product.quantity
        customer.products = bought_items

        return result


    @staticmethod
    def make_product(product_type, name):
        if product_type == "Drink":
            product = Drink(name)
            return product
        elif product_type == "Food":
            product = Food(name)
            return product

    @staticmethod
    def make_customer(customer_name):
        customer = Customer(customer_name)
        return customer

tester = Shop()
tester.deliver("Drink", "pepsi")
tester.deliver("Drink", "cola")
tester.deliver("Drink", "fanta")
tester.deliver("Food", "kartofi")
tester.deliver("Food", "apple")
tester.deliver("Food", "banana")
print(tester.sell("Daito", pepsi=10, banana=7))
