class atm:
    def __init__(self,amount):
        self.amount = amount 
        self.pin = "1234"
        self.currency = 'ugx'
    def check_balance(self,pin):
        if pin == self.pin:
            print{"amount is :", self.amount}
            
        else:
            ValueError = "invalid pin"
    
    def deposit(self,amount,pin):
        if amount <= 0:
            print{"deposite failed"}
            
            
        if pin == self.pin:
            print{"successful"}
            
class account:
    def __init__(self, balance):
        self.balance = balance #public varaible, any one can change
        
    acc = account(1000)
    print(acc.balance)
    
    acc.deposite(500)
    print(acc.balance)  
    
class hello:
    def __init__(self,name):
        self.a = 10
        self._b = 20
        self. __c = 30

hello = hello("name")
print(hello.a)
print(hello._b)
print(hello.__c)
            
