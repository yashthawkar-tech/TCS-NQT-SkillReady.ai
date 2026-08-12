from A import A_function
from B import B_function

class C:
    def data(self):
        self.A_function()
        self.B_function()
        print("All function call are done")

c_obj=C()
c_obj.data()


