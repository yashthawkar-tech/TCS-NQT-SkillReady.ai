list=[1,4,7,3,4,2,6,8,5]
target=8
for i in range(1,len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==target:
            print(i,j)

target1=10
for i in range(1,len(list)):
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            if list[i]+list[j]+list[k]==target1:
                print(i,j,k)