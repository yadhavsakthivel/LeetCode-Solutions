class Solution(object):
    def maxKDistinct(self, nums, k):
        arr=list(set(nums))
        sorted(arr, reverse=True)
        arr.sort(reverse=True)
        return arr[:k]

        