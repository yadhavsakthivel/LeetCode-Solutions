class Solution {
    public int minAbsoluteDifference(int[] nums) {
        int n=nums.length;
        int count=0;
        int min=1000;
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(nums[i]==1 && nums[j]==2)
                {
                    int diff=Math.abs(i-j);
                    if(diff<min)
                    {
                        min=diff;
                    }
                }
            }
        }
        if(min==1000)
        {
            return -1;
        }
        else
        {
            return min;
        }
    }
}