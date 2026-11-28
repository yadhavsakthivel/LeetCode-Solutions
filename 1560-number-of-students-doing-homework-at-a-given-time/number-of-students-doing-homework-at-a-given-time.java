class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int count=0;
        int n1=startTime.length;
        for(int i=0; i<n1; i++)
        {
            if(startTime[i]<=queryTime && endTime[i]>=queryTime)
            {
                count++;
            }
        }
        return count;
    }
}