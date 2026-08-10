#in single inheritence we can access the variable the function in the function
class Data:
    def speak(self):
        self.a = 10
        print("Human makes sound")
class Data2(Data):
    def speak2(self):
        print("value of a =",self.a)
d1=Data2()
d1.speak()
d1.speak2()