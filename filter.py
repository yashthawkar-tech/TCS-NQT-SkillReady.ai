number =[1,2,3,4,5,6,7,8,9,10]
data=list(filter(lambda a:a%2==0,number))
print("Even Number:",data)

number =[1,2,3,4,5,6,7,8,9]
data=list(filter(lambda a:a%2!=0,number))
print("Odd Number:",data)


student=[("ram",90),("yash",94),("sharvari",99)]
print(sorted(student,key=lambda a:a[1]))


student=[(44,90),(22,94),(14,99)]
print(sorted(student,key=lambda a:a[0]))

student=[(44,"yash"),(22,"arya"),(14,"shakuni")]
print(sorted(student,key=lambda a:a[1]))
#Priority of A-Z is First
#small a-z after that

#It will Reverse it According the condition you give
student=[(44,"yash"),(22,"arya"),(14,"shakuni")]
print(sorted(student,key=lambda a:a[1],reverse=True))

