#2)Car Start() accelarete() Brake()

from abc import ABC
class Car(ABC):
    def start(self):
        pass
    def accelerate(self,speed):
        pass
    def brake(self,speed):
        pass
class BMW(Car):
    def start(self):
        print("BMW is Start!")
    def accelerate(self,speed):
        print("BMW is accelarting at the speed of",speed)
    def brake(self,speed):
        print("BMW Brakes its higher speed at",speed)
class Thar(Car):
    def start(self):
        print("Thar is Start!")
    def accelerate(self,speed):
        print("Thar is accelarting at the speed of",speed)
    def brake(self,speed):
        print("Thar Brakes its higher speed at",speed)
class Fortuner(Car):
    def start(self):
        print("Fortuner is Start!")
    def accelerate(self,speed):
        print("Fortuner is accelarting at the speed of",speed)
    def brake(self,speed):
        print("Fortuner Brakes its higher speed at",speed)

#Objects
bmw1=BMW()
bmw1.start()
bmw1.accelerate(20)
bmw1.brake(150)
thar1=Thar()
thar1.start()
thar1.accelerate(20)
thar1.brake(150)
fortuner1=Fortuner()
fortuner1.start()
fortuner1.accelerate(20)
fortuner1.brake(150)