class Solution(object):
    def vowelConsonantScore(self, s):
        vowels=set("aeiou")
        v=c=0
        for char in s:
            if char in vowels:
                v+=1
            elif char.isalpha():
                c+=1
        if c>0:
            return v//c
        else:
            return 0
        