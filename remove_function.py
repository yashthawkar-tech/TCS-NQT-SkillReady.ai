# colors={"green","yellow","red"}
# colors.remove("red")
# print(colors)

# # colors.remove("white") #It will Throw an error
# # print(colors)

# #Hardcode
# colors =colors-{"yellow"}
# print(colors)

#2nd Approach List Logic
color=["Orange","Blue","Purple","Green"]
remove="Blue"
list=[]
for i in color:
    if i !=remove:
        list.append(i)
print(list)




