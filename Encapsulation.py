
#Building/Bundling the data
#(variables),(methods),(function)
#into a Single Unit class and restricting
#direct access to some of Objects Data
#Types==>Public,Protected and Private
#access Modifier in Python

class Bank_account:
    def __init__(self,balance):
        self.__balance=balance #__ Private attribute
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return self.__balance

b1=Bank_account(1000)
print(b1.get_balance())
b1.deposit(500)
print(b1.get_balance())
b1.withdraw(100)
print(b1.get_balance())

