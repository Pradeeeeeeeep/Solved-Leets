class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = re.sub(r'[^a-zA-Z0-9]', '', s)
        txt = txt.lower()
        left=0
        right=len(txt)-1
        while left<=right:
            if txt[left]!=txt[right]:
                return False
            left+=1
            right-=1
        return True