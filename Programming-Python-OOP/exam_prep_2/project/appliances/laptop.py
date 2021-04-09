from project.appliances.appliance import Appliance


class Laptop(Appliance):
    appliance_cost = 1

    def __init__(self):
        super().__init__(Laptop.appliance_cost)