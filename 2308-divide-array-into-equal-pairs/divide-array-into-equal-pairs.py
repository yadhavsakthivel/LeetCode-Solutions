class Solution(object):
    def divideArray(self, nums):
        for num in set(nums):
            if nums.count(num)%2!=0:
                return False
        return True
        