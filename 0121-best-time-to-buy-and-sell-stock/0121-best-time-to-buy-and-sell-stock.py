class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i]>bestBuy:
                maxProfit = max(maxProfit, prices[i]-bestBuy)
            bestBuy = min(bestBuy, prices[i])
        return maxProfit