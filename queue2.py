class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        self.queue.pop(0)
    def print_queue(self):
        if len(self.queue)==0:
            print("Empty Queue")
        else:
            print("The Values of Queues:",self.queue)
q1=Queue()
q1.enqueue(101)
q1.enqueue(102)
q1.print_queue()
# q1.dequeue()
# q1.print_queue()
q1.enqueue(103)
q1.enqueue(104)
q1.enqueue(105)
q1.print_queue()
