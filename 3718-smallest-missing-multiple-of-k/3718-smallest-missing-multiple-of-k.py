class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = 1
        x =k
        while( True):
            if(x in nums):
                x=k
                x= x*n
                n +=1
            else:
                return x