#List ==> user 5 number
#2nd Largest And largest
# list=[]
# for i in range(1,6):
#     A=int(input("Enter Any Number"))
#     list.append(A)
# print(list)
# list=[34,5,3,2,55]
# largest_no=0
# second_largest=0
# third_largest=0
# for i in list: 
#     if i> largest_no:
#         third_largest=second_largest
#         second_largest=largest_no
#         largest_no=i
#     elif i>second_largest and i!=largest_no:
#         third_largest=second_largest
#         second_largest=i
#     elif i >third_largest and i!=second_largest and i!=largest_no:
#         third_largest=i
# print(largest_no)
# print(second_largest)
# print(third_largest)

list=[]
count=0
for i in range(1,11):
    A=int(input("Enter 10 Numbers"))
    list.append(A)
    if i == A:
        count=count+1

print(list)

print(count)