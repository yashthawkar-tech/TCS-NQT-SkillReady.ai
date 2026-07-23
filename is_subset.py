a={1,3}
b={1,2,3}
# print(a.issubset(b))
#Return true if  sets values are 
#present in anather set
#Then it will provide True 
#Otherwise provides False 

booleanvar=False
for i in a:
    if i in b:
        booleanvar=True
        break      
print(booleanvar)
