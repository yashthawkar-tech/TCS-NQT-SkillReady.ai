class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_data(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=student("Yash",28)
s2=student("Akash",23)
s1.print_data()
s2.print_data()