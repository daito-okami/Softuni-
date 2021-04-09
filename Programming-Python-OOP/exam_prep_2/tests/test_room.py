from unittest import TestCase, main

from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class RoomTest(TestCase):

    def test_innit_attributes_set(self):
        room = Room("Room", 1, 1)
        self.assertEqual(room.family_name, "Room")
        self.assertEqual(room.budget, 1)
        self.assertEqual(room.members_count, 1)
        self.assertEqual(room.children, [])
        self.assertEqual(room.expenses, 0)

    def test_expenses_when_negative_expect_raise(self):
        room = Room("Room", 1, 1)
        with self.assertRaises(ValueError) as ex:
            room.expenses = -5

        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_when_positive_to_set(self):
        room = Room("Room", 1, 1)
        room.expenses = 5
        self.assertEqual(room.expenses, 5)

    def test_expenses_when_0_to_set(self):
        room = Room("Room", 1, 1)
        room.expenses = 0
        self.assertEqual(room.expenses, 0)

    def test_calculate_expenses_when_zero_consumer_expect_expenses_0(self):
        room = Room("Room", 1, 1)
        room.calculate_expenses([])
        self.assertEqual(room.expenses, 0)

    def test_calculate_expenses_when_1_consumer_expect_expenses(self):
        room = Room("Room", 1, 1)
        consumers = [TV()]
        room.calculate_expenses(consumers)
        self.assertEqual(consumers[0].get_monthly_expense, room.expenses)

    def test_calculate_expenses_when_multiple_consumer_expect_expenses(self):
        room = Room("Room", 1, 1)
        appliances = [TV()]
        children = [Child(5,1 ,2, 4)]
        room.calculate_expenses(appliances, children)
        expected = appliances[0].get_monthly_expense + children[0].get_monthly_expense
        self.assertEqual(expected, room.expenses)


if __name__ == '__main__':
    main()