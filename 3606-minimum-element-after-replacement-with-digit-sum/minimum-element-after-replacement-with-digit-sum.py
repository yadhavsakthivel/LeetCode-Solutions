class Solution:
    def minElement(self, nums):
        minimum=float('inf')
        for num in nums:
            digit_sum=0

            while num>0:
                digit=num%10
                digit_sum+=digit
                num//=10
            minimum=min(minimum, digit_sum)
            
        return minimum