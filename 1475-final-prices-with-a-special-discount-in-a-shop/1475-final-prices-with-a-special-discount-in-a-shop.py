class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      stk = []
      answer = []
      for i in range(len(prices)-1, -1 ,-1):
        while stk and stk[-1] > prices[i]:
            stk.pop()
        if stk:
            answer.append(prices[i] - stk[-1])
        else:
            answer.append(prices[i])
        stk.append(prices[i])
      return list(reversed(answer))