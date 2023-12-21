class BalanceException(Exception):
    pass



class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\n Balance = ${self.balance:.2f}")
        
    
    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")
        
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Balance.")
        self.getBalance()
        
        
    def viableTransacton(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
        
    def withdraw(self, amount):
        try:
            self.viableTransacton(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
        
        

        