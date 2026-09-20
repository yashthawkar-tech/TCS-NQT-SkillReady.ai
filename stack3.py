maxsize=5
stack=[]
def push_values():
    if len(stack)==maxsize:
        print("STACK IS OVERFLOW>>>>")
    else:
        users_input=int(input("Please Enter The Values to PUSH>>>>"))
        stack.append(users_input)
        print("Succesfully Pushed",users_input,"into Stack")
def pop_values():
    if len(stack)==0:
        print("STACK IS UNDERFLOW>>>>")
    else:
        user_pop =stack.pop()
        print("POPPED SUCCESSFULLY",user_pop)
def print_values():
    if len(stack)==0:
        print("STACK IS EMPTY>>>>")
    else:
        print("Elements Of Stack:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])


while True:
    print("\n1.push operation")
    print("2.pop operation")
    print("3.print the stack")
    print("4.stop the program")
    choice=int(input("Enter Your Choice :"))

    if choice ==1:
        push_values()
    if choice ==2:
        pop_values()
    if choice ==3:
        print_values()
    if choice ==4:
        print("STOPPING THE CODE....")
        break
    # else:
    #     print("Invalid Choice!PLEASE TRY AGAIN")