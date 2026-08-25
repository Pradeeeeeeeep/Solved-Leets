class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            for j in range (i+1, len(prices)):
                if(prices[j]<=prices[i]):
                    output.append(prices[i]-prices[j])
                    break
            else:
                output.append(prices[i])

        return output