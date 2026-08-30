tuples=(1,2,2,3,2,2,1,2,3,4,3,2,2,4,5,3,3,2,1,1,3,4,3,2,3,"Yash","Yash")
value=2
value1=3
value2="Yash"
count1=0
count2=0
count3=0
for i in tuples:
    if i==value:
        count1+=1
    elif i==value1:
        count2+=1
    elif i==value2:
        count3+=1
print(count1)
print(count2)
print(count3)