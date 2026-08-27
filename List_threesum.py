class Solution(object):
    def threeSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] ==target:
                      print("These are the Values",nums[i],nums[j],nums[k])
                      return i,j,k
nums=[1,2,4,5,3,5]
target=10
s1=Solution()
print("These are the Indexes",s1.threeSum(nums,target))