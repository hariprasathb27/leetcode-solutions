class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if(m <= 0 or n <= 0):
            return []
        return ["." * n if i == 0 else "#" * (n - 1) + "." for i in range(m)]