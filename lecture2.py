# Inheritance

from abc import ABC, abstractmethod
from typing import override

class Account(ABC): #abstract class

    count=0 #class variable

    def __init__(self,acccountNumber, owner,amount):
        self._accountNumber = acccountNumber
        self._owner = owner
        self._amount = amount
        Account.count+=1

    @abstractmethod
    def getAccountDetail(self):
        pass

    @abstractmethod
    def withdraw(self,money):
        pass

    @abstractmethod
    def deposit(self,money):
        pass

class CurrentAccount(Account):
    def __init__(self, accountNumber, owner, amount):
        super().__init__(accountNumber, owner, amount)
        
    @override
    def getAccountDetail(self):
        return f'{self._accountNumber} owner {self._owner} having amount PKR {str(self._amount)}'
    
    @override
    def withdraw(self, money):
        if money > self._amount:
            return "Insufficient balance"
        self._amount -= money
        return self._amount
    
    @override
    def deposit(self, money):
        if money<=0:
            return "Deposit must be positive"
        
        self._amount +=money
        return self._amount
    
#Assuming saving accounts has interest rates, penalty charges
class SavingAccount(Account):
    def __init__(self, accountNumber, owner, amount, interestRate=5.0, minBalance=1000):
        super().__init__(accountNumber, owner, amount)
        self._interestRate = interestRate
        self._minBalance = minBalance
    

    @override
    def getAccountDetail(self):
        return (
            f"Savings Account: {self._accountNumber}, "
            f"Owner: {self._owner}, "
            f"Balance: PKR {self._amount}, "
            f"Interest Rate: {self._interestRate}%"
        )

    @override
    def withdraw(self, money):
        if money <= 0:
            return "Withdrawal amount must be positive."
        if money > self._amount:
            return "Insufficient balance."
        if (self._amount - money) < self._minBalance:
            return f"Cannot withdraw. Minimum balance of PKR {self._minBalance} must be maintained."
        
        self._amount -= money
        return f"Withdrawal successful. Remaining balance: PKR {self._amount}"
    
    @override
    def deposit(self, money):
        if money <= 0:
            return "Deposit must be positive."
        self._amount += money
        return f"Deposit successful. New balance: PKR {self._amount}"
    

    

    

    
class Bank:
    def __init__(self,name,location,account):
        self.__name = name
        self.__location = location
        self.__account = account

    def  displayInfo(self):
        print(f'{self.__name} located in {self.__location} showing details of {self.__account.getAccountDetail()}  ')


def main():
    account1 = CurrentAccount("HPK12321E32", "Hassan Shahzad", 1000000 )
    account1.deposit(2000)
    account1.withdraw(100)

    account2 = SavingAccount("PK98765SAV", "Hassan Shahzad", 15000, interestRate=6.5)

    bank1 = Bank("Alfalah", "Johar Town",account1)
    bank2 = Bank("Alfalah","Johar Town", account2)

    bank1.displayInfo()
    print(" ")
    bank2.displayInfo()


    print(f'Total accounts in all banks {Account.count}')

if __name__ =="__main__":
    main()