class Solution(object):
    def rearrangeArray(self, nums):
        count={}

        for x in nums:
            count[x]=count.get(x,0)+1

        ans=[]

        while count:
            for x in sorted(count):
                ans.append(x)
                count[x]-=1

                if count[x]==0:
                    del count[x]

        return ans
        