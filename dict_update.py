student={
    "name":"Aakash",
    "age" :28,
    "city" :"Tirora"
}
student["age"]=18
student["city"]="Banglore"
print(student["age"])
print(student["city"])
student["Club"]="FORAI" #New Update 

for key,value in student.items():
    if key=="age": #It will Give that Particular Output
      print(key,value)

key1=list(student.keys())[-1]
#It will Print the last element of the Dictnory
print(key1,":",student[key1])

last_keys=list(student.items())[-1:]
print(last_keys)
for key ,value in last_keys:
   print(key,":",value)
#It will Print Only new key value and pair


