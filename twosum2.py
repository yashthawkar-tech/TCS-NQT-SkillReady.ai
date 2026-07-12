def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                 return i,j

num=[2,11,7,15]
#   [0 1  2  3]
target=9
print(twosum(num,target))

#Solved using My own logic To avoid Printing Duplicate Values in the index 
#By converting it into sets

list=[3,7,4,2,4]
set=set(list)
target=11
for i in range(len(set)):
    for j in range(i+1,len(set)):
        if list[i]+list[j]== target:
            print(i,j)

#INPUT=list=[3,7,4,2,4]
#OUTPUT=1 2
#index 1 + index 2 = 7 + 4 =11 = Target Value
