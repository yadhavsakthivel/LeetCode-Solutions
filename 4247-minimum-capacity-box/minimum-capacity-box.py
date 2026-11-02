class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        n=len(capacity)
        mins=min(capacity)
        ans=-1
        for i in range(n):
            if capacity[i]==itemSize:
                return i
        for i in range(n):
            if capacity[i]>=itemSize:
                if ans==-1 or capacity[i]<mins:
                    mins=capacity[i]
                    ans=i
        return ans