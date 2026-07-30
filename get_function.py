student={"name":"Yash", "Age":21}
print(student.get("name"))
#to Access the value 

#Hardcode Logic for gate function
find="name"
data=False
for i in student:
    if i==find:
        print(student[i])
        data=True
        break
if data==False:
    print("Key Not Available")

#Total 5 logics to solve this
