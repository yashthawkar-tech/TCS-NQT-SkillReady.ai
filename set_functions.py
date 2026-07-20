#add function 
#adds one element to the set
data ={"Rahul","Ashwin"}
# data.add("Ayush")
# print(data)
#hard code logic
new_value="Shravni"
if new_value not in data:
    data=data|{new_value}#add new value
print(data)




