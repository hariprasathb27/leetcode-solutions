class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} 
        sum_of_val = 0 
        length = len(s)
        found = False
        for i in range(0,length):
            if(found):
                found = False
                continue
            if((i!=length-1) and ( dict_1[s[i]] < dict_1[s[i+1]] )):
                sum_of_val += (dict_1[s[i+1]] - dict_1[s[i]])
                found = True
            else:
                sum_of_val += dict_1[s[i]]
        
        return sum_of_val