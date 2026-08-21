# list=[1,2,4,5,7]
# largest_no=0
# for i in list:
#     if i>largest_no:
#         largest_no=i
# print(largest_no)


#Largest Number using PolyMorphism
class Largest_number: 
    def large(self,list):
        largest_no=0
        for i in list:
            if i>largest_no:
                largest_no=i
        return largest_no
# class Largest_number1(Largest_number): 
#     def large(self,list):
#         largest_no=0
#         for i in list:
#             if i>largest_no:
#                 largest_no=i
#         return largest_no
        
object=Largest_number()
print(object.large([1,2,3,4,5,10,26,33,5,4]))