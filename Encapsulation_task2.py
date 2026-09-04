#Online Shopping Cart
class Online_shopping:
    def __init__(self):
        self.__total=0
    def Add_product(self,name,Price):
        if Price>0:
            self.__total+=Price
            print("Product Added :",name)
    def Remove_product(self,Price):
        if Price<=self.__total:
            self.__total=Price
            print("Product Removed")
    def Show_product(self,products):
        self.__total=products
        print("Your Products are",products)
    def show_total(self):
        print("Total Amount =",self.__total)

a1=Online_shopping()
a1.Add_product("Watch",1200)
a1.show_total()
a1.Remove_product(600)
a1.show_total()
a1.Show_product("Masala Dosa")

        