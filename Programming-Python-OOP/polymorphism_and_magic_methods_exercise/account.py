class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        # self.index = 0

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance {account.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount )

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    # def __iter__(self):
    #     return self._transactions
    #
    # def __next__(self):
    #     if self.index < len(self._transactions):
    #         return self._transactions[self.index]
    #     self.index += 1

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        acc._transactions = self._transactions + other._transactions
        return acc

    def __reversed__(self):
        return reversed(self._transactions)



