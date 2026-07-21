#pop()==> remove the random element from set
#set={} dict={key:value}
# number = {10,20,30,40,50}
# print(number.pop())
# data =number.pop()
# print(data)
# print(number)


#Hardcode Logic
# number = {10,20,30,40,50}
# temp=list(number)
# print(temp)
# data = temp[0]
# number.remove(data)
# print(data)
# print(number)


#hardcode logic for string 
# num2={"Tv","Mobile","mouse","keyboard"}
# data = None
# for i in num2:
#     data =i
#     break
# num2.remove(data)
# print(data)
# print(num2)

num3={"Tv","Mobile","Remote","mouse","keyboard"}
removed = None
new_set=set()
for i in num3:
    if removed is None:
        removed =i
    else:
        new_set.add(i)
num3=new_set
print(removed)
print(num3)
