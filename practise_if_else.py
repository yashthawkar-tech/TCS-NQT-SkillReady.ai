# Task 1: Check Positive or Negative
# Problem: Take an integer as input and check whether it is Positive or Negative.
# Input:
# 15
# Output:
# Positive Number



# Task 2: Check Even or Odd
# Problem: Take an integer and check whether it is Even or Odd.
# Input:
# 27
# Output:
# Odd Number
# n = int(input("Enter any number:"))
# if n%2 ==0:
#     print("Even Number")
# else:
#     print("Odd number")

# Task 3: Check Eligible to Vote
# Problem: Take age as input and check if the person is eligible to vote (18 years or above).
# Input:
# 20
# Output:
# Eligible to Vote
# age =int(input("Enter Your Age:"))
# if age<18:
#     print("Sorry! You are not Eligible to vote")
# else:
#     print("Congrats! You are Eligible to Vote")


# Task 4: Find Greater Number
# Problem: Take two numbers and print the greater number.
# Input:
# 45
# 67
# Output:
# 67 is Greater
# a = int(input("Enter 1st Number:"))
# b = int(input("Enter 2nd Number:"))
# if a>b:
#     print("The Greater Number is",a)
# else:
#     print("The Greater Number is",b)


# Task 5: Find Greatest Among Three Numbers
# Problem: Take three numbers and print the greatest one.
# Input:
# 12
# 56
# 34
# Output:
# 56 is Greatest
# a=int(input("Enter 1st Number:"))
# b=int(input("Enter 2nd Number:"))
# c=int(input("Enter 3rd Number:"))
# if a>(b and c):
#     print("The Greatest Number is",a)
# elif b> (a and c):
#     print ("The Greatest Number is",b)
# else:
#     print("The Greatest Number is",c)


# Task 6: Check Leap Year
# Problem: Take a year as input and check whether it is a leap year.
# Input:
# 2024
# Output:
# Leap Year
# n=int(input("Enter Year:"))
# if n%4==0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# Task 7: Check Divisibility by 5
# Problem: Check whether a number is divisible by 5.
# Input:
# 45
# Output:
# Divisible by 5
# n=int(input("Enter any number:"))
# if n%5 ==0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")
    

# Task 8: Check Divisibility by 5 and 11
# Problem: Check whether a number is divisible by both 5 and 11.
# Input:
# 55
# Output:
# Divisible by both 5 and 11
# n=int(input("Enter any number:"))
# if n%5 ==0 and n%11 ==0:
#     print("Divisible by both 5 and 11")
# else:
#     print("Not Divisible by 5 and 11")


# Task 9: Pass or Fail
# Problem: Take marks as input. If marks are 35 or above, print "Pass", otherwise print "Fail".
# Input:
# 72
# Output:
# Pass
# marks = int (input("Enter Your Marks Here:"))
# if marks<35:
#     print("Fail")
# else:
#     print("Pass")


# Task 10: Grade Calculator
# Problem: Assign grades based on marks.
# •	90–100 → A+ 
# •	80–89 → A 
# •	70–79 → B 
# •	60–69 → C 
# •	35–59 → D 
# •	Below 35 → Fail 
# Input:
# 84
# Output:
# Grade A
# marks = int(input("Enter Your marks here:"))
# if marks>=90:
#     print("Grade A+")
# elif marks>=80<=89:
#     print("Grade A")
# elif marks>=70<=79:
#     print("Grade B")
# elif marks>=60<=69:
#     print("Grade C")
# elif marks>=35<=59:
#     print("Grade D")
# else:
#     print("Fail")

# Task 11: Check Character Case
# Problem: Take a character as input and check whether it is uppercase or lowercase.
# Input:
# G
# Output:
# Uppercase Letter


# Task 12: Check Alphabet, Digit, or Special Character
# Problem: Identify whether the input is an alphabet, digit, or special character.
# Input:
# @
# Output:
# Special Character


# Task 13: Find Largest of Four Numbers
# Problem: Take four numbers and print the largest.
# Input:
# 15
# 89
# 47
# 56
# Output:
# 89 is Largest
# a=int(input("Enter 1st Number:"))
# b=int(input("Enter 2nd Number:"))
# c=int(input("Enter 3rd Number:"))
# d=int(input("Enter 4th Number:"))
# if a>(b and c and d):
#     print("The Greatest Number is",a)
# elif  b>(a and c and d):
#     print("The Greatest Number is",b)
# elif  c>(a and b and d):
#     print("The Greatest Number is",c)
# else:
#     print("The Greatest Number is",d)



# Task 14: Electricity Bill Category
# Problem: Determine the electricity bill category.
# •	Units < 100 → Low Bill 
# •	Units 100–300 → Medium Bill 
# •	Units > 300 → High Bill 
# Input:
# 275
# Output:
# Medium Bill
# units = int (input("Enter Your electricity consumed units:"))
# if units<100:
#     print("Low Bill")
# elif units>=100 and units<=300:#100-300
#     print("Medium Bill")
# else:
#     print("High Bill")


# Task 15: Check Age Category
# Problem: Determine the age category.
# •	0–12 → Child 
# •	13–19 → Teenager 
# •	20–59 → Adult 
# •	60 and above → Senior Citizen 
# Input:
# 18
# Output:
# Teenager
# age=int(input("Enter Your Age:"))
# if age<=12:
#     print("Child")
# elif age>=13 and age<=19:
#     print("Teenager")
# elif age>=20 and age<=59:
#     print("Adult")
# else:
#     print("Senior Citizen")


# Task 16: Login Authentication
# Problem: Take username and password as input. Print "Login Successful" if both are correct, otherwise print "Invalid Credentials".
# Input:
# admin
# 1234
# Output:
# Login Successful
# username=input("Enter Your Username Here:")
# password=int(input("Enter Your Password Here:"))
# if username=="admin" and password ==1234:
#     print("Login Successfull")
# else:
#     print("Invalid Credentials")


# Task 17: Check Profit or Loss
# Problem: Take Cost Price (CP) and Selling Price (SP) as input and determine whether there is a Profit, Loss, or No Profit No Loss.
# Input:
# 500
# 650
# Output:
# Profit
# cost_price=int(input("Enter Cost price:"))
# selling_price=int(input("Enter Selling Price"))
# if cost_price<selling_price:
#     print("Profit")
# elif cost_price>selling_price:
#     print("Loss")
# elif cost_price==selling_price:
#     print("No Profit No Loss")


# Task 18: Find Second Largest Among Three Numbers
# Problem: Take three numbers and print the second largest.
# Input:
# 45
# 78
# 62
# Output:
# 62 is Second Largest

# Task 19: Check Triangle Validity
# Problem: Take three angles of a triangle. Check whether the triangle is valid.
# Input:
# 60
# 60
# 60
# Output:
# Valid Triangle
# a =int(input("Enter Angle 1:"))
# b =int(input("Enter Angle 2:"))
# c =int(input("Enter Angle 3:"))
# if a+b+c == 180:
#     print("Valid Triangle")
# else:
#     print("Not a Valid Triangle")


# Task 20: ATM Withdrawal
# Problem: The account balance is ₹10,000. Take the withdrawal amount as input.
# •	If the amount is less than or equal to the balance, print "Transaction Successful". 
# •	Otherwise, print "Insufficient Balance". 
# Input:
# 4500
# Output:
# Transaction Successful
# a=int(input("Enter Your Withdrawl Amount:"))
# balance=10000
# if a<=balance:
#     print("Transaction Successfull")
# else:
#     print("Not Sufficient Balance")



