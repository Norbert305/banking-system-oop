from bank_account import * # import all from the bank_account.py file

# Lets create an instance for our Bank Account.
Dave = BankAccount(1000, "Dave") # fields are the amount and the name of the account that are stored in the variable Dave.
Sara = BankAccount(2000, "Sara") # Our banks accounts created with a balance


Dave.getBalance() # This instance outputs the account name and balance from the bank_account.py file.
Sara.getBalance() # Let's retrieve the account name and balance with getBalance()

Sara.deposit(500) # instance of the current balance + however much you put into the deposit param. 


Dave.withdraw(10000) # instance of the current balance in the account - the amount in the withdraw param.
Dave.withdraw(10) # If the amount you have doesn't exist in the current bank account their will be an exception handle error.

Dave.transfer(10000, Sara) # Transfers the balance from one user to another
Dave.transfer(100, Sara) 


Jim = InterestRewardsAcct(1000, "Jim") # Our new interest account of 5%.

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)


Blaze = SavingsAcct(1000, "Blaze") # Our savings account.

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)