class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_1 = str(x)
        reverse_str =""
        if(x > (2**31 -1) or x<(-2**31)):
            return 0
        if(str_1[0] == "-"):
            reverse_str = "-"+str_1[:-len(str_1):-1]
        else:
            reverse_str = str_1[::-1]
        num = int(reverse_str)
        if(num > (2**31 -1) or num <(-2**31)):
            return 0
        else:
            return num