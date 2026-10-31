class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        nums.sort()
        n=len(nums)
        return nums[n-1]+nums[n-2]-nums[0]
        