a={1,2,3,5}
b={3,4,5,6}
a.symmetric_difference_update(b)
print(a)

#hardcode logic
data=set()
for i in a:
    if a not in b:
        data.add(i)
print(a)

#multiple logics
