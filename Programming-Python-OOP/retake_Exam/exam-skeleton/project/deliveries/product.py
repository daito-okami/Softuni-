from abc import ABC


class Product(ABC):
    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The product cannot be an empty string.")
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity cannot be equal to or below zero.")
        self.__quantity = value
