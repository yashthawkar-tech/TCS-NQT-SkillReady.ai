tuple=(1,2,3,4,5,6)
#     (0 1 2 3 4 5)
t =tuple.index(6)#index() function is used to find the index of a value in tuple
print("index of 6 is :",t)

#Hard coded logic for finding index of a value in tuple
value = 6
for i in range(len(tuple)):
    if tuple[i]==value:
        print("the index of value is",i)
        break