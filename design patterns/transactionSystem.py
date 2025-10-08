'''
You are designing a Banking System that allows users to withdraw money from their accounts using an ATM Machine.

However:

You do not want the ATM (client) to access the real bank account object directly.

The real account object contains sensitive data (PIN, account number, etc.).

You want to control access, add security checks, and maybe log activities.'''

from abc import ABC, abstractmethod

class IBank(ABC):

    @abstractmethod
    def withdraw(self,amount):
        pass

class Bank(IBank):
    
    def __init__(self,balance, accountNumber):
        self.__balance = balance
        self.__accountNumber = accountNumber

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount} successful.")
            print(f"Remaining balance: ${self.__balance}")

class proxyBank(IBank): #proxy layer added for extra verfications

    def __init__(self,balance, accountNumber, pin):
        self.__pin = pin
        self.__account = Bank(balance,accountNumber)
    
    def verifyPin(self):
        pinVerification = int(input("Enter your 4 digit PIN :"))
        if pinVerification == self.__pin:
            return True
        
        return False

    
    def withdraw(self,amount):
        print("Trying to access account...proxy layer")
        if self.verifyPin():
            self.__account.withdraw(amount)
        else:
            print("Wrong PIN")


if __name__ == "__main__":

    proxyLayer = proxyBank(10000, "321232" , 4543)
    amount = int(input("Enter amount to withdraw: "))
    proxyLayer.withdraw(amount)
        

     

