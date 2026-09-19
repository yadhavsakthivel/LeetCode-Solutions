class Solution {
    public int calPoints(String[] operations) {
        Deque<Integer> stack=new ArrayDeque<>();
        for(int i=0; i<operations.length; i++)
        {
            String op=operations[i];

            if(op.equals("C"))
            {
                stack.pop();
            }
            else if(op.equals("D"))
            {
                int prev=stack.peek();
                stack.push(2*prev);
            }
            else if(op.equals("+"))
            {
                int new1=stack.pop();
                int new2=stack.peek();
                int sum=new1+new2;
                stack.push(new1);
                stack.push(sum);
            }
            else
            {
                int num=Integer.parseInt(op);
                stack.push(num);
            }
        }
        int ans=0;
        while(!stack.isEmpty())
        {
            ans=ans+stack.pop();
        }
        return ans;
    }
}