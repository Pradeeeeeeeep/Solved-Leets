class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rev_txt = txt[::-1]
        if txt == rev_txt:
            return True
        else:
            return False