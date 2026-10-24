class Solution(object):
    def maximumWealth(self, accounts):
        maxs=0
        for i in accounts:
            sums=sum(i)
            if sums>maxs:
                maxs=sums
        return maxs
        