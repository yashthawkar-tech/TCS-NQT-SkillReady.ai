maxsize=10
stack=[0]*maxsize
index=-1
def pushop(number):
    global index
    if index==maxsize-1:
        print("stack is overflow")
    else:
        index=index+1
        stack[index]=number
def pop_Op():
    global index
    if (index==-1):
        return None
    else:
        number=stack[index]
        index=index-1
        return number
        #print("ELements of stack:",end=" ")

def isValid(s):
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            pushop(ch)
        #close the bracket
        else:
            if index==-1:
                return False
            top_value=pop_Op()
            if ch==')' and top_value=='(':
                continue
            if ch=='}' and top_value=='{':
                continue
            if ch==']' and top_value=='[':
                continue
            return False
    if index==-1:
        return True
    else:
        return False
s=input("enter brackets:")
print(isValid(s))