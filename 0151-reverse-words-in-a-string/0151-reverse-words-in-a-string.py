class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        stack = []
        s = s.split()
        for word in s:
                stack.append(word)
        for i in range(len(stack)):
            words.append(stack.pop())
        return " ".join(words)
