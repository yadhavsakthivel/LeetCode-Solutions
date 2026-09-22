class Solution:
    def reorderedPowerOf2(self, n):
        digits=sorted(str(n))
        for i in range(31):
            pow=2**i
            
            if sorted(str(pow))==digits:
                return True

        return False