#single parent class==> multiple child  class inhrit
class Father:
    def property(self):
        print("Father's Property")
class Son(Father):
    def bike(self):
        print("Son's Bike")
class Daughter(Father):
    def car (self):
        print("Daughter has a Car")
d=Daughter()
d.car()

