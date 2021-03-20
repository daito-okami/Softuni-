import random


class RandomList(list):
    def get_random_element(self):
        element_index = random.randint(0, len(self) - 1)
        element = self[element_index]
        self.pop(element_index)
        return element


