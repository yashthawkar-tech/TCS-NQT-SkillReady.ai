#convert from tuple to list type conversion

# tuple =(10,20,30,40,50)
# print(type(tuple))
# list = list(tuple)
# print(type(list))
# list.append(100)
# print(list)

#tuple to list to tuple by using list properties
tup=(1,2,3,4,5)
list1=list(tup)
list1.append(6)
tup=tuple(list1)
print(tup)