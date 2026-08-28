class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d = n//8
        r= n%8
        return (d+1)*(4*d+r)