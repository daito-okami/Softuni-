from project.appliances.appliance import Appliance


class Fridge(Appliance):
    appliance_cost = 1.2

    def __init__(self):
        super().__init__(Fridge.appliance_cost)