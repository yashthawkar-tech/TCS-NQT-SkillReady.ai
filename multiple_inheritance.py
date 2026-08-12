#One child class and multiple parent class
class father:
    def skill(self):
        print("coding")
class mother:
    def skill2(self):
        print("cooking")
class child (father,mother):#Parent class
    def skill3(self):
        print("playing cricket")
c=child()
c.skill()
c.skill2()
c.skill3()