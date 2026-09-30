class Solution:
    def numberOfPairs(self, nums):
        freq=[0]*101

        for num in nums:
            freq[num]+=1

        pairs=0
        leftover=0

        for count in freq:
            pairs+=count//2
            leftover+=count%2

        return [pairs, leftover]