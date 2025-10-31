#bank account
class bank_account:
    def __init__(self,balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
account = bank_account(230)
account.deposit(70)
account.withdraw(160)

print(account.balance)
        