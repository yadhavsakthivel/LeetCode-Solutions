class Solution(object):
    def splitNum(self, num):
        nums=sorted(str(num))
        n=len(nums)

        nums1=""
        nums2=""
        
        for i in range(n):
            if i%2==0:
                nums1+=nums[i]
            else:
                nums2+=nums[i]
        return int(nums1)+int(nums2)