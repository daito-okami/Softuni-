class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        self.validate_expenses(value)
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            result += sum(x.get_monthly_expense for x in items)
        self.expenses = result

    @staticmethod
    def validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
