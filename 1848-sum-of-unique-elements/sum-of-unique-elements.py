class Solution(object):
    def sumOfUnique(self, nums):
        ans=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                ans.append(nums[i])
        return sum(ans)