

class Student:
    def __init__(self,object):
        print("its a student class init fun")
        self.name=object.name
        self.age=object.age
class Data:
    def __init__(self,name,age):
        print("its a data class init fun")
        self.name=name
        self.age=age      
s1=Data("aakash",28)
#copy constructor
s2=Student(s1)
print(s2.name)
print(s2.age)
        