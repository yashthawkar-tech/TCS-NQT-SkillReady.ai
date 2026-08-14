#print multiple skills of Student
#programmming :Python c c++
#dsa Score 78
#English:45
#presentation Skills
#Solve This
#Using Inheritance 

class Student:
    def student_name(self,name):
        self.name=name
        print("Name Of The Student:",self.name)
class Skills(Student):
    def skills_of_student(self):
        print("Skills of The Student")
class Programming(Skills):
    def programming_skills(self):
        print('''Programming Skills:
Java,C++,Python''')
class Dsa(Programming):
    def Dsa_score(self):
        print("Dsa Score=86")
class softskill(Skills):
    def softskills(self):
        print('''\nSoft Skills:
Presentation
Confidence
Leadership Qualities
Time Management
Communication
        ''')
class English(softskill):
    def English_Level(self):
        print("Intermidiate Level English")
obj_skill=Skills()
obj_skill.student_name("Yash Thawkar")
obj_skill.skills_of_student()


obj1_softskill=softskill()
obj1_softskill.softskills()

obj2_dsa=Dsa()
obj2_dsa.Dsa_score()

obj3_program=Programming()
obj3_program.programming_skills()

obj4_eng=English()
obj4_eng.English_Level()


#                     Student
#                        │
#                        ▼
#                     Skills
#                    /      \
#                   ▼        ▼
#           Programming    softskill
#                │            │
#                ▼            ▼
#               Dsa         English
