class Solution:
    def isPalindrome(self, x: int) -> bool:
 
        list_a = list(map(str,str(x)))
        start_order = 0
        end_order = len(list_a) -1
        while(start_order != end_order and start_order < end_order):
            if(list_a[start_order] != list_a [end_order]):
                return False
            else:
                start_order+=1
                end_order -=1
        return True
        