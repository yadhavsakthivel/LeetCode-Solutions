class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        int min1=nums1[0];
        int min2=nums2[0];
        int num=10;
        for(int i=0; i<nums1.length; i++)
        {
            if(nums1[i]<min1)
            {
                min1=nums1[i];
            }
        }
        for(int i=0; i<nums2.length; i++)
        {
            if(nums2[i]<min2)
            {
                min2=nums2[i];
            }
        }
        for(int i=0; i<nums1.length; i++)
        {
            for(int j=0; j<nums2.length; j++)
            {
                if (nums1[i]==nums2[j])
                {
                    if(nums1[i]<num)
                    {
                        num = nums1[i];
                    }
                }
            }
        }
        if(num!=10)
        {
            return num;
        }
        if(min1<min2)
        {
            return min1*10+min2;
        }
        else
        {
            return min2*10+min1;
        }
    }
}