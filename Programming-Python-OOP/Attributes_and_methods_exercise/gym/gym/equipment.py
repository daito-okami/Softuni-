class Equipment:
    _id = 0

    def __init__(self, name):
        Equipment._id += 1
        self.name = name
        self.customer_id = Equipment._id

    def __repr__(self):
        return f"Equipment <{self._id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment._id + 1