class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open_braket = 0
        for i in s:
            if(i=='('):
                open_braket +=1
            else:
                if(open_braket==0):
                    ans+=1
                else:
                    open_braket -=1
        return ans+open_braket
        