class Solution:
    def check(self, nums):
        sort=sorted(nums)
        for i in range(len(nums)):
            rotated=nums[i:]+nums[:i]
            if rotated==sort:
                return True
        return False