import random
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 100

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        print(f"skills: {self.skills}")
        print(f"money: {self.money}")

    def study(self):
        self.skills += 1
        print("time to study.")

    def chill(self):
        self.skills -= 0.5
        self.money -= 50
        print("chilling.")

    def work(self):
        self.skills += 0.5
        self.money += 50
        print("hard working.")

alex = Student('Alex', 14)
#john = Student('John', 12)
#john.info()

for day in range(365):
    alex_choise = random.randint(1, 3)
    if alex_choise == 1:
        alex.study()
    if alex_choise == 2:
        alex.chill()
    else:
        alex.work()

alex.age += 1
alex.info()
