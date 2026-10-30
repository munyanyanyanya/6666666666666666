class ATM:
    def __init__(self, balance):
        self.balance = balance

    def login(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    def deposit(self):
        pass

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[withdraw] -${amount}")
        else:
            raise ValueError("You cannot withdraw money")

atm = ATM(1000)

attempts = 3
is_login = False

while True:
    if not is_login:
        pin = input(f"Enter your pin ({attempts}): ")
        if not atm.login(pin):
            attempts -= 1
            print("Invalid PIN")
            if attempts <= 0:
                print("Card blocked")
                break
            continue

is_login = True
print("Menu:")
print("1. Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"balance: {atm.balance}")
elif choice == 2:
    amount = int(input("Enter your amount: "))
    atm.deposit(amount)
elif choice == 3:
    amount = int(input("Enter your amount: "))
     try:
        atm.withdraw(amount)
     except ValueError as e:
        print(e)
else:
    break
