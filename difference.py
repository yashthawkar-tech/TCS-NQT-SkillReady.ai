a={1,2,3}
b={2,3,4}
print(a.difference(b))
#Output will be different value
print(b.difference(a))

#hardcode logic
data=set()
for i in a:
    if i not in b:
        data.add(i)
print("Hardcode Logic",data)