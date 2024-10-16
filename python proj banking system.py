#parent class:user
#child class:bank
#stores details about the amount
#allows for,withdraw,view_balance

#parent class:
class User:
    def __init__(self, name, age, gender):
       self.name=name
       self.age=age
       self.gender=gender
    def show_details(self):
        print("personal detials:")
        print(" ")
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Balance available: ", self.balance)
        else:
            self.balance -= amount
            print("Account balance has been updated: ", self.balance)

    def view(self):
        self.show_details()
