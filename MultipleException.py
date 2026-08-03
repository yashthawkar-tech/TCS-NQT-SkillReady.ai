#Handling Multiple Exceptions

try: 
    number =int(input())
    print(10/number)
except ValueError:
    print("please Enter a Valid Error")
else:
    print("you entered number",number)
finally:
    print("program is finished")


