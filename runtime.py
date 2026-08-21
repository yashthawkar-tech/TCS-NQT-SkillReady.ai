#Method overriding
class calculator:
    def calculate(self,a,b):
        print("Addition=",a+b)
class AdvanceCalculator(calculator):
    def calculate(self,a,b):
        print("Division =",a/b)
object1=calculator()
object2=AdvanceCalculator()

object2.calculate(10,20)

#Mantrimall / Dream 11 
#This Method call is overriding

#Task Using Polymorphism 
#Print The Reverse Number
#Pallindrome Number

#Largest Number in given Number
#Second Largest number in given number

