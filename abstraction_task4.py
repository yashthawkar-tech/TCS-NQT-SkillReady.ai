from abc import ABC
class Online_food(ABC):
    def select_item(self):
        pass
    def Bill(self):
        pass
    def Success(self):
        pass
class Zomato(Online_food):
    def select_item(self,Your_choice):
        print("Your Cart:",Your_choice)
    def Bill(self,Amount):
        print("Your Total Bill is",Amount)
    def Success(self,Your_choice,Amount):
        print("Your Order of",Your_choice,"of Amount",Amount,"is Placed Successfully")
class Swiggy(Online_food):
    def select_item(self,Your_choice):
        print("Your Cart:",Your_choice)
    def Bill(self,Amount):
        print("Your Total Bill is",Amount)
    def Success(self,Your_choice,Amount):
        print("Your Order of",Your_choice,"of Amount",Amount,"is Placed Successfully")
class Tooing(Online_food):
    def select_item(self,Your_choice):
        print("Your Cart:",Your_choice)
    def Bill(self,Amount):
        print("Your Total Bill is",Amount)
    def Success(self,Your_choice,Amount):
        print("Your Order of",Your_choice,"of Amount",Amount,"is Placed Successfully")
app_zomato=Zomato()
app_zomato.select_item("Muttor Panir,Tawa Roti")
app_zomato.Bill(247.00)
app_zomato.Success("Muttor Panir,Tawa Roti",247.00)
app_swiggy=Swiggy()
app_swiggy.select_item("Mutton Biryani")
app_swiggy.Bill(349.00)
app_swiggy.Success("Mutton Biryani",349.00)
app_tooing=Tooing()
app_tooing.select_item("Dosa,Idli")
app_tooing.Bill(328.00)
app_tooing.Success=("Dosa,Idli",328.00)
