import random

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


    def show_balance(self):
        print(f"balance: {self.balance}")


    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_number} +{amount} ")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_number} -{amount} ")
        else:
            print("not enough money :/")



class Student(object):

    def __init__(self, name, age, BankAccount: BankAccount):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 100
        self.BankAccount = BankAccount

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        print(f"Skills: {self.skills}")
        print(f"Money: ${self.money}")
        print(f"Deposit: ${self.BankAccount.balance}")

    def study(self):
        self.skills += 1
        print("Time to study 🧑‍🎓📚")

    def chill(self):
        self.skills -= 0.5
        expenses = random.randint(25, 100)
        if expenses <= self.money:
            self.money -= expenses
        else:
            self.BankAccount.withdraw(expenses)

        print("Chilling ... 😎🍵")

    def work(self):
        self.skills += 0.5
        income = 50 + random.randint(0,50)
        amount = income + random.randint(25,100)
        self.money += 50 + random.randint(0, income)
        self.BankAccount.deposit(amount)
        self.money += (income - amount)
        print("Hard working ... 👷‍♂️💪")

mono = BankAccount("Mono", 100)
mono.show_balance()
alex = Student('Alex', 12, mono)
alex.info()

for day in range(366):
    alex_choice = random.randint(1, 3)

    if alex_choice == 1:
        alex.study()
    elif alex_choice == 2:
        alex.chill()
    else:
        alex.work()

alex.age += 1
alex.info()