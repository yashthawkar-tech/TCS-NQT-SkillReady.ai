a={1,2,5,3,4}
b={3,4,5}
c=a.difference(b)
print("Value of C:",c)
print("value of A:",a)
#It will Not modify the original set


a.difference_update(b)
print(a)
#It will update the original set
