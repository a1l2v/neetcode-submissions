from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      prev = [0] * len(prices)
      prev[0] = prices[0]
      max_profit = 0
      for i in range(1,len(prev)):
        prev[i] = min(prev[i-1],prices[i-1])

      for i in range(len(prev)):
         if prices[i] > prev[i]:
            max_profit = max(max_profit,prices[i]-prev[i])
      return max_profit
