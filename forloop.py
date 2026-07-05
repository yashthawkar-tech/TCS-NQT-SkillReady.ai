#i want to print 10 numbers using for loop

#approach 1
# for i in range(1,11):
#     print(i)

#approach2
# for i in range (1,11,1):
#     print(i)

# #approach 3
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(i)

# #approach 4
# for i in range(11):
#     print(i)


# # approach 5
# for i in range(10):
#     print(i+1)#it will print values upto 10 


# #approach 6
# print('using string')
# str='12345678910'
# for i in str:
#     print(i)

# #approach 7
# #step 1 condition 10
# print("using function without any loop")
# def print_10_numbers(number):
#     if number>10:#1>10
#         return
#     print(number)#1
#     print_10_numbers(number+1)
#     #print_10_numbers(numbers=2)
    
# print_10_numbers(number=1)


# #Practise 
# #Print number from 1 to 20 
# def nums(a):
#     if a>20:
#       return 
#     print(a)
#     nums(a+1)
# nums(1)


#approach 8
list(map(print,range(1,11))) #function()
print(type(list))
print(id(list))#address of memory location
#map(key,value)




