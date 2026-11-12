class Solution(object):
    def mostFrequentEven(self, nums):
        ans=[]
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                ans.append(nums[i])
        n1=len(ans)
        maxs=0
        num=-1
        if n1==0:
            return -1
        for i in range(n1):
            count=0
            for j in range(n1):
                if ans[i]==ans[j]:
                    count+=1
            if count>maxs:
                maxs=count
                num=ans[i]
            elif count==maxs and ans[i]<num:
                num=ans[i]

        return num