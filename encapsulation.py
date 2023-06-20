class Bank_account:
    def __init__(self,_accountNumber,_balance):
        self._accountNumber = _accountNumber
        self._balance = _balance

    def deposit(self,amount):
        self._balance+=amount

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance-=amount
        else:
            print('insufficient funds')

    def getBalance(self):
        return self._balance
    
newbank = Bank_account(5001010102457,1200)
print(newbank._balance)
newbank.deposit(5000)
newbank.withdraw(1800)
print(newbank.getBalance())