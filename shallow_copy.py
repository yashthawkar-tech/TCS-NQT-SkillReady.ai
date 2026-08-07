import copy
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

stud_obj=student("Yash",22)
print(stud_obj.name)
print(stud_obj.age)

#shallo copy
# s2=copy.copy(stud_obj)
# print(type(s2))
# print(s2.name)
# print(s2.age)
#Shallow copy is used to access data From the class
#without disturbing the object using a new Variable
