class Bank():
    def __init__(self,money):
        self.money=money
    def username(self):
        user=input("Enter Your Username =")
        password=int(input("Enter Your Password ="))
        if password==12345:
            print("Welcome !!!",user)
        else:
            print("InValid Credintials")
    def Deposit(self,money):
        deposit=int(input("Enter Amount to Deposit:"))
        self.money=self.money+deposit
        print("Money Deposited Successfully\n Balance =",self.money)
    def Withdraw(self,money):
        withdraw=int(input("Enter Amount to Withdraw:"))
        self.money =self.money-withdraw
        print("Money Withdraw Successfull \n Balance =",self.money)
class Menu(Bank):
    print("1.Get Your Details")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    value=print(int(input("ENTER YOUR CHOICE:")))
    while True:
        if value==1:
            def username(self):
                user=input("Enter Your Username =")
                password=int(input("Enter Your Password ="))
            
             
        elif value==2:
            def Deposit(self, money):
                pass
        else:
            def Withdraw(self, money):
                pass

b1=Bank(50000)
b1.username()
b1.Deposit(0)
b1.Withdraw(0)