#A single chain
class Grandfather:
    def house (self):
        print("Grandfather's House")
class Father(Grandfather):
    def car(self):
        print("Father's Car")
class Son(Father):
    def bike(self):
        print("Son's Bike")
#This chain Known as Multi-Level Inheritance
s=Son()
s.house()
s.car()
s.bike()
