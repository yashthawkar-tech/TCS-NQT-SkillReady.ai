class Node:
    def __init__(self,value):
        self.value=value
        self.address=None
class LinkedList:
    def __init__(self):
        self.start_node=None
    def insert_node(self):
        value=int(input("enter any number"))
        temp=Node(value)
        if self.start_node is None:
            self.start_node=temp
        else:
            t1=self.start_node
            t1.address=temp
            