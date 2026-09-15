class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    palindrome[i][j] = True

                elif length == 2:
                    palindrome[i][j] = s[i] == s[j]

                else:
                    palindrome[i][j] = (
                        s[i] == s[j] and
                        palindrome[i + 1][j - 1]
                    )

        dp = [0] * (n + 1)

        for end in range(1, n + 1):

            dp[end] = dp[end - 1]

            for start in range(end - k + 1):

                if palindrome[start][end - 1]:
                    dp[end] = max(
                        dp[end],
                        dp[start] + 1
                    )

        return dp[n]