class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\n Balance = ${self.balance:.2f}")
        
    
    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")