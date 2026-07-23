a={1,2,3}
b={2,3,4}
a.intersection_update(b)
print(a)
#Always print common values in both sets


#hardcode logic
#read the values from set a
data=set()
for i in a:
    if i in b:
        data.add(i)
print(data)