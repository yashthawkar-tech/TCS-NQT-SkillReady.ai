#Unpack the data
#print the 1st value in tuple without indexing or loop
student =("yash",20,"python")
print(student)

#Using Loop
for i in student:
    if i =="yash":
        print("My name is",i)
        break

#Using Indexing
print(student[0])#it will print 1st value of the tuple

#using unpacking
name ,age ,course = student
print("My name is",name)
print("My age is",age)
print("My course is",course)

