class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a= str(n)
        list_a = list(map(int,a))
        addtion = sum(list_a)
        multiple = 1
        for i in list_a:
            multiple *= i
        addtion = multiple+addtion
        divider = n%addtion
        if(divider == 0):
            return True
        else:
            return False
        