class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        list_a = []
        for i in s:
            if i in mapping.values():
                list_a.append(i)
            elif i in mapping:
                if not list_a or mapping[i] != list_a.pop():
                    return False
        return not list_a
        