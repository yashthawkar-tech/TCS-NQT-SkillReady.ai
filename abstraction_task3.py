#3)Online payment
#enter amount ==>pay==> Payment Successfull
from abc import ABC
class Online_Payment(ABC):
    def amount(self):
        pass
    def pay(self):
        pass
    def pay_done(self):
        pass
class UPI(Online_Payment):
    def amount(self,amount1):
        print("Enter The Amount:",amount1)
    def pay(self,amount1):
        print(amount1,"is the Amount You Selected!")
    def pay_done(self):
        print("You Have Succesfully Done the Payment!")
upi=UPI()
upi.amount(100)
upi.pay(100)
upi.pay_done()