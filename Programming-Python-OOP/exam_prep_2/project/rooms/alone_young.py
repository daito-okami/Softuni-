from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    default_room_members_count = 1
    room_cost = 10
    appliances = [TV()]

    def __init__(self,  name, salary):
        super().__init__(name, salary, self.default_room_members_count)
        self.calculate_expenses(self.appliances)