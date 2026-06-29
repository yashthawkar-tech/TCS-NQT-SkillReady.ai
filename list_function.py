# #append() insert() 

# #append function in list 
# #what is the use of append ()?
# #Add one element at the end of the list
# list = [1,2,3,4,5,6]
# list.append(100)
# list.append(200)
# print(list)

# #insert function
# #inserts an element at a specific index
# #synrtax==>list.insert(indexnumber,value)
# list.insert(1,300)
# print(list)

# #extend()
# #adds all elememts of anather list to the current list
# list1=[1,2,3]
# list2=[4,5,6]
# # list1.extend(list2) #Prints all elements of both list
# # print(list1)#all data will added to list1

# list2.extend(list1)
# print(list2)

#remove function
#removes the first occurence
#of the specified value 
num=[10,20,30,40,20,20]
num.remove(20)
print(num)# repeated 1st occurence value will be removed

