#Use case of Factory Method Pattern
from abc import ABC, abstractmethod

class IPaymentMethods(ABC):

    @abstractmethod
    def validatePaymentDetails(): 
        '''This is an interface method'''

    @abstractmethod
    def processTransaction():
        '''This is an interface method'''

class CreditCard(IPaymentMethods):

    def __init__(self, totalBalance):
        self.__balance = totalBalance
        self.__amount = 0
    
    def setAmount(self,amount):
        self.__amount = amount

    def validatePaymentDetails(self):
        print("✅ Credit card validated.")
        if self.__balance > self.__amount:
            return True
        else:
            return False
        
    def processTransaction(self):
        if self.validatePaymentDetails():
            self.__balance-=self.__amount
            print(f"Transaction Completed. Remaining balance is {self.__balance}")
        else:
            print("Transaction can't be completed due to low balance")

class PayPal(IPaymentMethods):
    def __init__(self, totalBalance):
        self.__balance = totalBalance
        self.__amount = 0
    
    def setAmount(self,amount):
        self.__amount = amount

    def validatePaymentDetails(self):
        print("✅ PayPal account validated.")
        if self.__balance > self.__amount:
            return True
        else:
            return False
        
    def processTransaction(self):
        if self.validatePaymentDetails():
            self.__balance-=self.__amount
            print(f"Transaction Completed. Remaining balance is {self.__balance}")
        else:
            print("Transaction can't be completed due to low balance")


class BankTransfer(IPaymentMethods):
    def __init__(self, totalBalance):
        self.__balance = totalBalance
        self.__amount = 0
    
    def setAmount(self,amount):
        self.__amount = amount

    def validatePaymentDetails(self):
        print("✅ Bank account validated.")
        if self.__balance > self.__amount:
            return True
        else:
            return False
        
    def processTransaction(self):
        if self.validatePaymentDetails():
            self.__balance-=self.__amount
            print(f"Transaction Completed. Remaining balance is {int(self.__balance)}")
        else:
            print("Transaction can't be completed due to low balance")

class FactoryPayment():

    def buildPayment(choice, balance):
        if choice == "creditcard":
            return CreditCard(balance)
        
        elif choice == "paypal":
            return PayPal(balance)
        
        elif choice == "bank":
            return BankTransfer(balance)
        

if __name__ == "__main__":
    paymentType = input("Payment Type: ")
    totalBalance = int(input("Total Balance: "))
    transaction = FactoryPayment.buildPayment(paymentType,totalBalance)
    amount = int(input("Enter amount: "))
    transaction.setAmount(amount)

    transaction.processTransaction()





