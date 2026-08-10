# class Object inheritance polymorphism
#abstraction encapsulation

class Robot:
    def __init__(self,name):
        self.name=name
    def move(self):
        print(self.name,"is moving")
    def stop(self):
        print(self.name,"has stopped!")
class Wheelrobot(Robot):
    def rotate_wheels(self):
        print(self.name,"is rotating its wheels")
class Drone(Robot):
    def fly(self):
        print(self.name,"is flying")
robo_object=Wheelrobot("Sofiya")
robo_object.move()
robo_object.rotate_wheels()
robo_object.stop()

#Drone ko access krne ke liye alag se object Banana hoga
robo2=Drone("Alphadro")
robo2.move()
robo2.fly()
robo2.stop()
