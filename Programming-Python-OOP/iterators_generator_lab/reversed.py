class reverse_iter:
    def __init__(self, iter):
        self.list = list(iter)
        self.index = len(self.list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.list[self.index]
        self.index -= 1
        return value