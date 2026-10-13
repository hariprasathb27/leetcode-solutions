class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        n=len(nums)
        for i in range(n):
            nums[i] = nums[i]**2
        nums.sort();
        half = n/2
        for i in range(n):
            if(i<half):
                score -= nums[i]
            else:
                score += nums[i]
        return score
        
        