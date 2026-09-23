class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue (self,value):
        """Add The Value to rear of the queue"""
        self.queue.append(value)
    def dequeue(self):
        """Remove and return the front value"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    def empty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    def print_queue(self):
        if len(self.queue)==0:
            print("Queue is Empty")
        else:
            print("Queue elements are:")
            # print(self.queue)
            for i in self.queue:
                print(i,end=" ")
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_queue()
print("\nsize of Queue is",q.size())
print(q.dequeue())
print(q.size())
q.print_queue()