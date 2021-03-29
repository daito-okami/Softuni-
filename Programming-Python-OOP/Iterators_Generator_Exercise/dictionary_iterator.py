class dictionary_iter:
    def __init__(self, dic_object):
        self.dic_object = dic_object
        self.keys = list(self.dic_object)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == len(self.dic_object):
            raise StopIteration
        key = self.keys[self.current_index]
        value = self.dic_object[key]
        self.current_index += 1
        return key, value