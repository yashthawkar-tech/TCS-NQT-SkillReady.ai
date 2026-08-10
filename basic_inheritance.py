#What is Inheritance
#Parent class / Chlid Class
#parent class data access by child class
#parent class ==> base class
#child class ==> derived class

#Syntax:
# class parent:
#     #parent class data
#     pass
# class child:
#     #child class data
#     pass


#Parent class data
class Data:
    a=10
    b=2
    c=a+b
    def speak(self):
        print("Humans makes sound")
#child class
class data2(Data):#Single Inheritance
    def speak2(self):
        print("Animal makes sound")
d1=data2()
# d2=data2() #We can make Mul
# d2.speak()
print(d1.c)
d1.speak()
d1.speak2()