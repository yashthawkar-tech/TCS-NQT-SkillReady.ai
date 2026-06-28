#bitwise NOT 
#~ 
#What is the use ?
#bits reversed / invert 
# 0 become 1 
# 1 become 0 
# ones compliment
a = 10
print(~a)#-11
#10 ==>0 0 0 0 1 0 1 0 Takes 4 Extra 0's
#   ==>1 1 1 1 0 1 0 1

#Formula 
#-a = -(a+b)
#-10 = -(10+1)
#a = -11

b = 44
print(~b)
#Formula 
#-a = -(a+b)
#-44 = -(44+1)
#a = -45

#11110101 ==> 10
#00001010 ==> Add 1
#       1
#00001011 ==> 11 add negetive sign 
#~ a = ~a -1
#    = -10-1 = -11
print(bin(a))# Checks binary number 
print(~a)#bit manipulation
#reset ==> calculation backdate ==> start

