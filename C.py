from A import A_function
from B import B_function

class D:
    def data(self):
        self.A_function()
        self.B_function()
        print("All function call are done")

c_obj=D()
c_obj.data()


