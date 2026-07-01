#nested Tuple means tuple inside another tuple
data=(
    ("yash",100 ,"java"),
    ("Ayush",200 ,"python"),
    ("Rohit",300 ,"c++"),
)
print(data)

for name,marks ,age in data:
    print(name,"=",marks)