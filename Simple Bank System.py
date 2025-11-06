class Bank:
    def __init__(self, balance: list[int]):
        self.b = balance  # 0-indexed list

    def _valid(self, acc: int) -> bool:
        return 1 <= acc <= len(self.b)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid(account1) or not self._valid(account2):
            return False
        i, j = account1 - 1, account2 - 1
        if self.b[i] < money:
            return False
        self.b[i] -= money
        self.b[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.b[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        i = account - 1
        if self.b[i] < money:
            return False
        self.b[i] -= money
        return True
