# #Find the even odd number using function

# def find_evenodd():
#     a = 9
#     if a%2 == 0:
#         print("Even Number")
#     else:
#         print("odd number")

# find_evenodd()

#runtime
def evenodd(n):
    if n% 2==0:
        print("even number")
    else:
        print("odd number")

x =int(input("enter any number :" ))
evenodd(x)