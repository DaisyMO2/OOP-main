class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            
class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance = self.balance * (1 + rate)
        
#object creation
Account = SavingsAccount(1000)
Account.deposit(500)
Account.add_interest(0.05)
Account.balance