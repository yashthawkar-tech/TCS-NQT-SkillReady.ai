#what is tuple
#it is a collection datatype 
#it is a collection data structure list tuple set dictnory
#tuple is a built in python data type
#used to store the multiple values in a single variable
#it is ordered and immutable collection
#which means once a tuple is created 
#we cannot remove , change or add the values of the tuple
#tuple_name =(val1,val2,val3,....)
student =("yash",20 , "python")
print(type(student))
print(student)

#characteristics of tuple
#1. ordered collection of elements
tuple = (5,4,3,2,1)
print(tuple)

#2. immutable (cannot be changed after creation)
tuple2 = (5,4,3,2,1)
# print(tuple2[2]) = 40  # This will raise an error

#3. allows duplicate values
tuple3 = (1,2,3,4,5,1,2,3)
print(tuple3)

#4. indexed (can be accessed by index)
tuple1 = (1,2,3,4,5)
print(tuple1[1])#it will print 2nd element of the tuple

#5. heterogeneous (can contain different data types)
tuple4 = (1, "hello", 3.14, True)
print(tuple4)

#support negative indexing
#0 start last size size -1==>-1
tuple5=(10,20,30,40,50)
print(tuple5[-1])#it will print last element of the tuple


#How to create an empty tuple
tuple = ()
print(tuple)
print(type(tuple))

#can i store a single value in tuple
#yes we can store a single value in tuple but we have to add a comma after thetuple_name = (10,)
tuple = (10,)
print(tuple)
print(type(tuple))#it will print tuple because it has a comma

