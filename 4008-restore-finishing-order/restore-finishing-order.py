class Solution(object):
    def recoverOrder(self, order, friends):
        ans=[]
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i]==friends[j]:
                    ans.append(order[i])
        return ans
        