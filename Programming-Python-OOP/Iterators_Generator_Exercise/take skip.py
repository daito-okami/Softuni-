class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.value = 0
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration
        value = self.value
        self.value += self.step
        self.counter += 1
        return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
