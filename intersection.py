a={1,2,3}
b={2,3,5,6}#It will print The elements 
           #which are present in both sets 
print(a.intersection(b))

#operator &
print(a&b)


#Empty set Way
data=set()
for i in a:
    if i in b:
        data.add(i)
print("hard code logic",data)


#anathor way
for i in a:
    for j in b:
        if i==j:
            data.add(i)
print(data)


#anathor way
data=[]
for i in a:
    if i in b:
        data.append(i)
print(set(data))