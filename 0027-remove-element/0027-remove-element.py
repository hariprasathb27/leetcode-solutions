class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        n = 0
        while(n < k):
            if(nums[n] ==val):
                nums.remove(nums[n])
                k-=1 
            else:
                n+=1
        return k