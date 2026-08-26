class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_a = s.split()
        last_val=len(list_a[len(list_a) -1].strip())
        
        return last_val