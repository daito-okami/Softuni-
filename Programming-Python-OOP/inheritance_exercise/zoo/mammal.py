from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.Animal__name = name


