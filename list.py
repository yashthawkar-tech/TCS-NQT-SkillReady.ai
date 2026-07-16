# Task 1: Create a List
# Problem: Take 5 integer inputs from the user and store them in a list.
# Input:
# 10
# 20
# 30
# 40
# 50
# Output:
# [10, 20, 30, 40, 50]
# a =int(input("number1:"))
# b =int(input("number2:"))
# c =int(input("number3:"))
# d =int(input("number4:"))
# e =int(input("number5:"))
# print([a])

# a=list(map(int,input().split()))
# print(a)


# Task 2: Print First Element
# Problem: Take 5 integers in a list and print the first element.
# Input:
# [15, 25, 35, 45, 55]
# Output:
# 15
# list =[15, 25, 35, 45, 55]
# print(list[0])


# Task 3: Print Last Element
# Problem: Print the last element of the list.
# Input:
# [11, 22, 33, 44, 55]
# Output:
# 55
# list=[11, 22, 33, 44, 55]
# print(list[-1])



# Task 4: Find Length of List
# Problem: Find the total number of elements in the list.
# Input:
# [2, 4, 6, 8, 10]
# Output:
# 5
# list=[2, 4, 6, 8, 10]
# print(len(list))


# Task 5: Sum of All Elements
# Problem: Find the sum of all numbers.
# Input:
# [5, 10, 15, 20]
# Output:
# 50
# list=[5, 10, 15, 20]
# sum=0
# for i in list:
#     sum =sum+i
# print(sum)
    

# Task 6: Find Maximum Number
# Problem: Print the largest number.
# Input:
# [12, 45, 7, 89, 32]
# Output:
# 89
list =[12, 45, 7, 89, 32]
largest_no=0
for i in list:
    if i>largest_no:
        largest_no=i
print(largest_no)


# Task 7: Find Minimum Number
# Problem: Print the smallest number.
# Input:
# [23, 11, 45, 7, 18]
# Output:
# 7








