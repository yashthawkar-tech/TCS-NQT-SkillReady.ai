class Student:
    def __init__(self,name):
        self.name=name
    def show_student(self):
        print("Name:",self.name)

class Engineering_student(Student):
    def __init__(self, name,branch):
        super().__init__(name)
        self.branch=branch
    def show_branch(self):
        print("branch:",self.branch)

class placement_student(Engineering_student):
    def __init__(self, name, branch,package):
        super().__init__(name, branch)
        self.package=package
    def show_package(self):
        print("Package:",self.package)

p=placement_student("Yash","Robotics and Ai",10)

p.show_student()
p.show_branch()
p.show_package()