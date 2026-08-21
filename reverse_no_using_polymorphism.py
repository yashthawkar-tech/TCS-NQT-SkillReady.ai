class Number:
    def reverse_number(self,number):
        rev_number=0
        while number>0:
            rem=number%10
            rev_number=rev_number*10+rem
            number//=10
        return rev_number
class ReverseNumber(Number):
    def reverse_number(self, number):
        res=0
        while number>0:
            rem=number%10
            res=res*10+rem
            number=number//10
        return res

object=ReverseNumber()
print(object.reverse_number(12345))
#Method Override That means
#run time Polymorphism