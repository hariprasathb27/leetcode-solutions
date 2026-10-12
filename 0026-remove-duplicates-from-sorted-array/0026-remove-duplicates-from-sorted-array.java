class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        if(nums.length==1){
            count=1;
        }
        for(int i=1;i<nums.length;i++){
            if(nums[count]!=nums[i]){
                count++; 
               int t = nums[count];
               nums[count] = nums[i]; 
               nums[i] = t; 
            }
            if(i==nums.length-1){
                count++;
            }
        }
        return count;
    }
}