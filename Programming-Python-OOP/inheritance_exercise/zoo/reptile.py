from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._Animal__name = name


    @property
    def Animal__name(self):
        return self._Animal__name