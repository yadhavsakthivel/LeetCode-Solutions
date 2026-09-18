class Solution(object):
    def pivotArray(self, nums, pivot):
        ans=[]
        for i in nums:
            if i<pivot:
                ans.append(i)
        for i in nums:
            if i==pivot:
                ans.append(i)
        for i in nums:
            if i>pivot:
                ans.append(i)

        return ans
        