#Atm Machine using Abstraction
from abc import ABC
class ATM(ABC):
    def withdraw(self,amount):
        pass
    def check_balance(self,balance):
        pass
class HDFC_ATM(ATM):
    def withdraw(self,amount):
        print(amount,"withdrawed Successfully!")
    def check_balance(self,balance):
        print("Your Balance is",balance)
class CanaraBank_ATM(ATM):
    def withdraw(self,amount):
        print(amount,"withdrawed Successfully!")
    def check_balance(self,balance):
        print("Your Balance is",balance)

atm1=HDFC_ATM()
atm1.withdraw(10000)
atm1.check_balance(1343454)
atm2=CanaraBank_ATM()
atm2.withdraw(1200)
atm2.check_balance(1500)
