class Solution(object):
    def isAnagram(self, s, t):
        sort_s=''.join(sorted(s))
        sort_t=''.join(sorted(t))

        if sort_s==sort_t:
            return True
        else:
            return False
        