#update add multiple elements
lang ={"Python","Java","Cpp"}#set indexing Not imp
lang.update(["C","Javascript"])
print(lang)

#condition Controlstatement function def ,for, while ,if else ,nested if

#Hardcode
list =["C","Javascript"]
for i in list: #Iteration Means Read Karna
    if lang not in list:
        lang.add(i)
print(lang)


#Hard Code 
set2={"React","Node"}
lang=lang|set2
print(lang)

for i in list:
    lang.add(i)
print(lang)

lang =lang.union({"C","Javascript"})
print(lang)