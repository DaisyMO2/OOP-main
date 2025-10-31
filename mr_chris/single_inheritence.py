class Person:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
        
    def intro(self):
        return {"hello, i am" + self.name}
        
class Child(Person):
    def Child_id(self):
        return {"my child id is 12345"}
    
    
#object creation
c = Child("chris")
p = Person("Adimin")

class Vehicle:
    def move(self):
        return ("The vehicle is moving")
    
class Car(Vehicle):
    def hook(self):
        return ("beep beep")
    
#object creation
my_car = Car()
my_car.move()
my_car.hook()


class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            
class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance = self.balaance * (1 + rate)
        
#object creation
Account = SavingsAccount(1000)
Account.deposit(500)
Account.add_interest(0.05)
Account.balance
    
    
        
