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
        self.money-=withdraw
        print("Money Withdraw Successfull \n Balance =",self.money)


b1=Bank(50000)

print("1.Get Your Details")
print("2.Deposit Money")
print("3.Withdraw Money")
value=int(input("ENTER YOUR CHOICE:"))
while True:
    if value==1:
        b1.username()
        break
    elif value==2:
        b1.Deposit(0)
        break
    else:
        b1.Withdraw(0)
        break
