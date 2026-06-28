#left shift <<
a =5
print(a<<1) # 5 * 2 # Multiply the operator
print(a<<2) # 5 * 4  (2^2)
print(a<<3) # 5 * 8 (2^3)
print(a<<4) # 5 * 16 (2^4)
print(a<<5) # 5 * 32 (2^5)

#Right shift 

print(a>>1) # 5 /  2 ^ 1  = 2 
print(a>>2) # 5 /  2 ^ 2  = 1 
print(a>>3) # 5 /  2 ^ 3  = 0 
print(a>>4) # 5 /  2 ^ 4  = 0 
print(a>>5) # 5 /  2 ^ 5  = 0 

# a = 5 Left Shift 
#32 26 8 4 2 1
#      0 1 0 1==> 5
#0  1  0 1 0 0==> 16 + 4 = 20 

# a = 5 Right Shift 
#8 4 2 1 
#0 1 0 1 ==> 5
#0 0 0 1==>1