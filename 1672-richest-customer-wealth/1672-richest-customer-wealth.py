class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for i in range(len(accounts)):
            currSum=0
            for j in range(len(accounts[i])):
                currSum+=accounts[i][j]
            maxSum = max(currSum, maxSum)
        return maxSum