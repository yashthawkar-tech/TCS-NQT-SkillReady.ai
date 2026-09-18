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
def print_stack():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("Elements of stack:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i],end=" ")
            print() 
while True:
    print("\n1.PUSH")
    print("2.POP")
    print("3.Print stack")
    print("4.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        push_operation()
    elif choice==2:
        pop_operation()
    elif choice==3:
        print_stack()
    elif choice==4:
        print("Programm is stopped...") 
        break
    else:
        print("Invalid choice..")                           


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


