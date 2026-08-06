import copy
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

stud_obj=student("Yash",22)
# print(stud_obj.name)
# print(stud_obj.age)

#shallo copy
# s2=copy.copy(stud_obj)
s3=copy.deepcopy(stud_obj)
print(type(s3))
print(s3.name)
print(s3.age)

#shallow copy ==> Outer Data Copy
#deep copy ==> object data copy
#object==>object==>object==>deepcopy
#This can be Only done by deep Copy

