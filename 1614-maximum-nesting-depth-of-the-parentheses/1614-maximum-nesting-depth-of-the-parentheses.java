class Solution {
    public int maxDepth(String s) {
        int count = 0;
        int maximum = 0;
        for(char ch: s.toCharArray()){
            if(ch=='('){
                count++;
                maximum = Math.max(maximum,count);
            }
            else if(ch==')'){
                count--;
            }
        }
        return maximum;
    }
}