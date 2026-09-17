#Stack ==> Last in First Out(LIFO)
#Data Add ==> Push operation
#Data Remove ==> pop operation
#Stack operations ==> push and pop

#Stack Conditions
#Stack Overflow
#Stack Underflow ==>-1
#underflow == stack is empty

#Always Set -1 By Default the Size of index (Underflow)
maxsize=10
stack=[]
def push_operation():
    if len(stack)==maxsize:
        print("stack is overflow")
    else:
        number=int(input("enter element for stack:"))
        stack.append(number)
def pop_operation():
    if len(stack)==0:
        print("stack is empty")
    else:
        number=stack.pop()
        print("stack element is deleted",number)


push_operation()
push_operation()

#PROJECTS
#Banking Application
#Student management system
#library management system
#online Quiz Application
#to do list
#contact management
#expense tracker
#simple shopping cart
#login registration system
#simple blog application


