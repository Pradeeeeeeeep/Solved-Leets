class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_temp = "".join(sorted(s))
        t_temp = "".join(sorted(t))
        if s_temp==t_temp:
            return True
        return False