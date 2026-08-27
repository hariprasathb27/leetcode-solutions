class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = "".join(map(str,digits))
        num = int(num)
        num +=1
        num = str(num)
        list_1 = list(num)
        list_a = list(map(int,list_1))
        return (list_a)
        