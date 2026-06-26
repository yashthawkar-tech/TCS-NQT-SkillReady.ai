#function with return keyword
#return ==> 50

def addition(a,b):
    c =a + b
    return c #return will vapas bhejega value print nahi krega
print('Addition =',addition(40,20)) #uske lie print ke andar function ko call krna pdega

#without argument

def addition2():
    a = 12
    b= 14
    # c = a + b
    # return c
    return a+b # in case if you dont want to declare anathor keyword
print(addition2())