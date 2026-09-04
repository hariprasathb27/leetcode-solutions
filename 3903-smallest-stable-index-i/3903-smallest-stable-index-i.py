class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            maximum = max(nums[:i+1])
            minimum = min(nums[i:])
            if((maximum-minimum)<=k):
                return i
        return -1
        