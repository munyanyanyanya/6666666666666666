class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[withdraw] -${amount}")
        else:
            raise ValueError

bank = BankAccount(100)
try:
    bank.withdraw(17)
    bank.withdraw(190)
except ValueError as ve:
    print("недостатньо коштів")

print(bank.balance)