
# tuple = (1,2,3,3,3,4,5,6,3,3,4,4,5,5,6,6,"yash" ,"yash")
# #how many times 3 is present in tuple
# print(tuple.count(3))#count() function is used to count the number of occurence of a value in tuple
# #how many times "yash" is present in tuple
# print(tuple.count("yash"))#count() function is used to count the number of occurence of a value in tuple

# #hard coded logic for count function in tuple
# value =3
# value2 = "yash"
# repeatvalue =0
# repeatvalue2 =0
# for i in tuple:
#     if i == value:
#         repeatvalue +=1
#     if i == value2:
#         repeatvalue2 +=1
# print("using for loop count =",repeatvalue)
# print("using for loop count =",repeatvalue2)

#Important Hard coded logic for finding all Repeated Values in tuple
tuple = (1,2,3,3,3,4,5,6,3,3,4,4,5,5,6,6,"yash" ,"yash")
value =()
for i in tuple:
    if i not in value:
        repeatvalue =0
        for j in tuple:
            if i == j:
                repeatvalue +=1
        print(i,"==>",repeatvalue)
        value+=(i,)
