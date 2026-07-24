#issupeset()==> boolean type of values T F
a={1,2,3,4,5}
b={1,2,5}
# print(a.issuperset(b))
# All values of b variable should be available in a 

#Hardcode logic
#declare boolean variable
#read the all values from b
#check the values in a variable 
boolvar=True
for i in b:
    if i not in a:
        boolvar=False
        break
print(boolvar)


#2nd logic
boolvar1=False
for i in b:
    if i not in a:
        boolvar1=True
    else:
        boolvar1=False
        break
print(boolvar1)


#3rd logic
booleanvar2=False
read=0
for i in b:
    if i in a:
        read+=1
if read==len(b):
    booleanvar2=True
print("boolean 2 =",booleanvar2)


#4th Logic
read2=0
for i in b:
    if i in a:
        read2+=1
if read2==len(b):
    print(True)
else:
    print(False)


#5th logic
for i in b:
    if i not in a:
        print(False)
    else:
        print(True)
    break


#Nested if ,difference , Multiple approaches
