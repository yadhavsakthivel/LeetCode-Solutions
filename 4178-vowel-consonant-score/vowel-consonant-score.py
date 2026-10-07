class Solution(object):
    def vowelConsonantScore(self, s):
        v=c=0
        for ch in s:
            if ch in "aeiou":
                v+=1
            elif ch in "bcdfghjklmnpqrstvwxyz":
                c+=1
        if c>0:
            return v//c
        else:
            return 0
        