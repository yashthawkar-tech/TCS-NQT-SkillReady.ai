#in python lambda is a small anonymous
#nameless function ==> Number of argument 
# but uses only one expression
#lambda argument :expression

add =lambda x,y:x+y
print(add(10,40))

def addition():
    a=10
    b=40
    c=a+b
    print(c)
addition()

number =[1,2,3,4,5]
data =list(map(lambda a:a*a*a,number))
print(type(data))
print(data)