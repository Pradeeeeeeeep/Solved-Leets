class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = re.sub(r'[^a-zA-Z0-9]', '', s)
        txt = txt.lower()
        l, r = 0, len(txt)-1
        while l<=r:
            if txt[l]!=txt[r]:
                return False
            l+=1
            r-=1
        return True