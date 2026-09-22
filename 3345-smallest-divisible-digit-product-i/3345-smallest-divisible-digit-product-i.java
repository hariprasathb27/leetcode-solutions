class Solution {
    public int smallestNumber(int n, int t) {
       while(prod(n)%t != 0){
        n++;
       }
       return n;
       }
    int prod(int n){
        int pro = 1;
        while(n>0){
          pro*=n%10;
          n/=10;  
        }
        return pro;
    }
}