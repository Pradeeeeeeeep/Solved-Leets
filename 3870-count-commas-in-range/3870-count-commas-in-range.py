class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        a = n - 999
        if a>0:
            total+=a
        return total