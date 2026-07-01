#Important Question
#Can i declare tuple inside list?
#so can i declare the data as a tuple format inside a list?

data =[1,2,3,4,5]
print(type(data))
data =[
    ("yash",100 ,"java"),
    ("Ayush",200 ,"python"),
    ("Rohit",300 ,"c++"),
]
for name,marks ,age in data:
    print(name,"=",marks)
