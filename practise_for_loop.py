# Task 1: Print Numbers from 1 to N
# Problem: Take a number N as input and print numbers from 1 to N.
# Input:
# 5
# Output:
# 1
# 2
# 3
# 4
# 5
# n=int(input("Enter any Number:"))
# for i in range(1,n+1):
#     print(i)


# Task 2: Print Numbers from N to 1
# Problem: Take a number N and print numbers from N to 1.
# Input:
# 5
# Output:
# 5
# 4
# 3
# 2
# 1
# n =int(input("Enter Any number To Reverse:"))
# for i in range(n,0,-1): #-1 For Reverse and +1 for Forward Direction
#     print(i)


# Task 3: Print Even Numbers
# Problem: Print all even numbers from 1 to N.
# Input:
# 10
# Output:
# 2
# 4
# 6
# 8
# 10
# n = int(input("Enter Any Number:"))
# for i in range(1,n+1):
#     if i%2 ==0:
#      print(i)


# Task 4: Print Odd Numbers
# Problem: Print all odd numbers from 1 to N.
# Input:
# 10
# Output:
# 1
# 3
# 5
# 7
# 9
# n =int(input("Enter Any Number:"))
# for i in range(1,n):
#     if i%2 !=0:
#         print(i)


# Task 5: Find Sum of First N Numbers
# Problem: Calculate the sum of numbers from 1 to N.
# Input:
# 5
# Output:
# 15
# n =int(input("Enter Any Number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i #sum =0 [0 +i(1)]=1 ,[1 +i(2)]=3
# print(sum)


# Task 6: Print Multiplication Table
# Problem: Print the multiplication table of a given number up to 10.
# Input:
# 7
# Output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# n =int(input("Enter any Table Number:"))
# for i in range(1,11): #It will print From 1 to 10
#     Result = n*i # 7*1=7 ,7*2=14
#     print(n ," x ",i ,"=",Result)

# Task 7: Find Factorial
# Problem: Find the factorial of a given number.
# Input:
# 5
# Output:
# 120
# n=int(input("Enter Any Number:"))
# factorial=1 #factorial means Ex: Factorial Of 5 is 5*4*3*2*1=120
# for i in range(n,0,-1):#-1 means backwards/Reverse
#     factorial=factorial*i #1=1*5=5,5=5*4=20
# print(factorial)

# Task 8: Count Digits
# Problem: Count the total number of digits in a given number using a loop.
# Input:
# 45896
# Output:
# 5
n =(input("Enter Any Number:"))
count=0
for i in n:
    count=count+1
print(count)


