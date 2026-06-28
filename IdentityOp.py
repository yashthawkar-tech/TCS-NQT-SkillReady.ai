#To check whether the value is same or not
#is isnot
#is ==> identity 
#isnot ==> not identity 

a =[10,20,30]
b = a
print (a is b)

a =[1 ,2 ,3]
b =[1,2,3]
print(a is b)#memory location differnt Thats why it is false

a = 12.5
b =12.5
print(a is b)

a = [2,4,6]
b = [2,4,6]
print( a is not b) # is not will not compare values 
