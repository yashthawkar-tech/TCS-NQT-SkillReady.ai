a=list({1,2,3,4})
b={1,2,3,4}
# print(a.isdisjoint(b))
#Both Sets Values are Different ==> True

#5 ways Hard code logic
#Hardcode logic
# bool_var=True
# for i in a:
#     if i in b:
#         bool_var=False
#         break
# print(bool_var)

#2nd way
bool_var2=True
for i in a :
    if i in b:
        print(False)
        break


#3rd Logic
bool_var3=True
for i in a:
    for j in b:
        if i==j:
            bool_var3=False
            break
    if bool_var3 == False:
        break
print(bool_var3)


#4th Logic
i =0
bool_var4=True

while i <len(a):
    if a[i] in b:
        bool_var4=False
        break
    i+=1
print(bool_var4)







