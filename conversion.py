#type conversion
#implicite type conversion
#explicite type conversion
#implicite ==> Python automatically converts one data 
#type to anather when needed

# #implicite type
# a =10 #int
# b =20.00 #float
# c = a+b
# print(type(c))# result will be float

#explicite type
#programmer manually convert one data type into anather
#data type using built-in function

# int() int("25") 25
# float() float("3.14") 3.14
# str() str(100) "100"
# bool() bool(1) TRUE
# list() list("123") ['1','2','3']
# tuple() 
# set()

#string is converted into List
# a = "123"
# b = list(a)
# print(b)
# print(type(b))

#Strings to Integer
# a ="100"
# y = int (a)
# print(y)
# print(type(y))

#boolean
# print(bool(0))
# print(bool(1))

# #always False for 0 and True For any Other value
# a ="10"
# b=bool (a)
# print(b)

# data =["rahul","priya"] 
# if bool (data):
#     print("Are present") #Always True Except 0 or Null or []
# else:
#     print("Not Present") #False only when 0 or null [] is present


data = ["12", "30", "20" , "50"]
addition = 0
for i in data:
    addition +=int(i)#45 "44"==> 44 , 44 +45 
print(addition)


