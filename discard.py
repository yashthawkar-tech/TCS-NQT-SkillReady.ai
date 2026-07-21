#Remove the elements if elements are not available 
#then show the error 
#does not provide the error
# color={"red","blue","green"}
# color.discard("red") #It will discard this color
# print(color)


#Hardcode Logic for remove function
color=["red","blue","green","ornage"]
rmv="red"
list=[]
for i in color:
    if i !=rmv:
        list.append(i)
print(list)

#Task ==> Write down the hardcode logic for discard
