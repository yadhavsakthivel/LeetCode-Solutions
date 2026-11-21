class Solution {
    public int maximizeSum(int[] nums, int k) {
        int n=nums[0];
        for(int i=1; i<nums.length; i++)
        {
            if(nums[i]>n)
            {
                n=nums[i];
            }
        }
        int sum=0;
        for(int i=0; i<k; i++)
        {
            sum+=n;
            n++;
        }
        return sum;
    }
}