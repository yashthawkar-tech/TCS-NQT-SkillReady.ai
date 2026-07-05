
#Print the index of the values given in the list
# list=[1,2,3,4,5]
# for i in list:
#     print(i)#1 2 3 4 5 Compiler call the index
#     if i ==4:
#      print(list[i])#0 1 2 3 4 
#it will print the value of the index 
#we will get the value on that particular index


# list=[1,2,3,4,5]
# for i in list:
#     print(list.index(i))#will print index values
    
# for i in range(0,len(list)):#will print index values
#     print(i)

# #It will print
# list=[1,2,3,4,5]
# for i in list:
#     if i<len(list)+1:
#         print(i-1)



list=[1,2,3,4,5]
for i in range(len(list)):
    if list[i]==i+1:#list[i] will print values and i will print indexes from 0
        #list[1]==0+1
        #this condition is given for avoiding 
        #out of range condition
        print(i)


        

