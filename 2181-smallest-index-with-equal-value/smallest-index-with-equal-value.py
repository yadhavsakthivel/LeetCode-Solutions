class Solution(object):
    def smallestEqual(self, nums):
        ans=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                ans.append(i)
        if len(ans)==0:
            return -1
        else:
            return min(ans)
        