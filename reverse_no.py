#Logic 1
# a=12345
# reverse_number=int(str(a)[::-1])
# print(reverse_number)

#2nd Logic Hard Code
#10 se kisi bhi number ko divide Karte hai
#To remainder Hamesha last index ka number hoga
#Thats why hum 10 se divide kr rhe hai 
#For getting Reverse Number

number=12345
reverse_number=0
while number>0:
    remainder=number%10
    reverse_number=reverse_number*10+remainder
    number=number//10
print(reverse_number)
