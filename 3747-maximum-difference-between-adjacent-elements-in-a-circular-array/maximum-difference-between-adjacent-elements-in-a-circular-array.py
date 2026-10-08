class Solution:
    def maxAdjacentDistance(self, nums):
        n=len(nums)
        maxs=0

        for i in range(n):
            num=(i+1)%n
            diff=abs(nums[i]-nums[num])

            if diff>maxs:
                maxs=diff

        return maxs