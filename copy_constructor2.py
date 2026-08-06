class Student:
    a=10
    def __init__(self,object):#object=s1(name,age)
        print("its a student class init fun")
        self.name=object.name
        self.age=object.age
class Data:
    a=4567
    def __init__(self,name,age):
        print("its a data class init fun")
        self.name=name
        self.age=age      
data_object=Data("aakash",28)
#copy constructor
Student_object=Student(data_object)
print(Student_object.name)
print(Student_object.age)
print(Student_object.a)
data_object.a