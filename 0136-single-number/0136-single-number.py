class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for i in nums:
            k=k^i 
        return k