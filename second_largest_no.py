#Second Largest Number using PolyMorphism
class Largest_number: 
    def large(self,list):
        largest_no=0
        second_largest=0
        for i in list:
            if i>largest_no:
                second_largest=largest_no
                largest_no=i
            elif i>second_largest and i!=largest_no:
                second_largest=i
        return second_largest
# class Largest_number1(Largest_number): 
#     def large(self,list):
#         largest_no=0
#         for i in list:
#             if i>largest_no:
#                 largest_no=i
#         return largest_no
        
object=Largest_number()
print(object.large([1,2,3,4,5,10,26,33,5,4]))