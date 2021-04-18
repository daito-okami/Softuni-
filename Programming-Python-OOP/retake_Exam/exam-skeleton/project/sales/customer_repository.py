# TODO ne raboti

class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add(self, customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        self.customers.append(customer)

    def remove(self, customer_name):
        customer = [c for c in self.customers if c.name == customer_name]
        if not customer:
            raise ValueError(f"Customer {customer_name}does not exist.")
        self.customers.remove(customer)
        return f"Removed customer: {customer_name}"

    def find(self, customer_name):
        try:
            customer = [c for c in self.customers if c.name == customer_name][0]
        except:
            return "None"
        return customer


