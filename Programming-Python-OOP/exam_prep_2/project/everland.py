from project.rooms import room
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(room.expenses + room.room_cost for room in self.rooms)
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        room_results = [self.__pay_for_rooms(room) for room in self.rooms]
        return '\n'.join(room_results)

    def status(self):
        pass

    def __pay_for_rooms(self, room):
        if room.budget < room.expenses:
            self.__remove_room(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

        room.budget -= room.expenses
        return f'{room.family_name} paid {room.expenses:.2f}$ and have {room.budget:.2f}$ left.'

    def __remove_room(self, room):
        self.rooms.remove(room)

