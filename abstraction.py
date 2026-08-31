#Hide the unnecessary details and show only information
#in python ABC (abstract base class)==> to use Abstraction

from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        print("Animals Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
d=Dog()
d.sound()



#1)Atm Machine


#Hidden Details
#2)Car Start() accelarete() Brake()
#3)Online payment
#enter amount ==>pay==> Payment Successfull
