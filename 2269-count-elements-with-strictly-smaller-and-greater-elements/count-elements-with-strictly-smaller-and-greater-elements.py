class Solution(object):
    def countElements(self, nums):
        nums.sort()
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[0] and nums[i]<nums[-1]:
                count+=1
        return count