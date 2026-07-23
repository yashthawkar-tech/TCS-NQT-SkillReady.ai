a={1,2,3}
b={3,4,5}
print(a.symmetric_difference(b))
#It Will remove the same Elements
#and print remaining values

print(a^b) 

#Hardcode Logic
#step 1 read the all values
#Check the values in i var They
#are not available in b(not in)
#add the value of i in variable
data=set()
for i in a:
    if i not in b:
        data.add(i)
for i in b:
    if i not in a:
        data.add(i)
print(data)