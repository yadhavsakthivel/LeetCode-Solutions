class Solution(object):
    def minOperations(self, nums, k):
        count=0
        n=set(nums)
        for i in nums:
            if i<k:
                return -1
        for i in n:
            if i>k:
                count+=1
        return count