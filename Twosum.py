
# list=[1,2,3,4,5,6]
# #index[0 1 2 3 4]
# target=3    #index 3  value
# for i  in list:
#    # print(i) #values
#    #print(list.index(i))  # index of element
#     if i +(i+1)==target:
#         print("value is availbel",i)
#         print(list[i]) #element
#         print(list.index(i)) #index 
list=[2,3,7,11]
target=9
#2+7 ==> 9  2 = 9-2=7
#i + i+1==target i, i+1
for i in range(len(list)):
    for j in range(i+1,len(list)):
         if list[i]+list[j]==target:
              print(i,j)
              break
# for i in range(0,11,2):
#      print(i)
# print("length of list = ",len(list))
# for i in range(1,len(list)):
#      print(i)

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#          if i + i+1==target:
#               print(i,j)
#               break