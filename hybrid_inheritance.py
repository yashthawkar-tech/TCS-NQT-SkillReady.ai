#Multiple inheritance types combinely use
#multilevel ,multiple ,single,hierarchical ==>
class Grandfather:
    def property(self):
        print("Grandfather's Property")
class Father(Grandfather):
    def car(self):
        print("Father has a Car")
class Uncle(Grandfather):
    def house(self):
        print("Uncle has a House")
class Son(Father):
    def bike(self):
        print("son has a bike")

s=Son()#Object 1
s.bike()
s.property()
s.car()

u=Uncle()#Object 2
u.house()
u.property()

