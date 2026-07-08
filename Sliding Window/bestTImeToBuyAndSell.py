class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0 
        profit = 0

        for end in range(len(prices)):
            b = prices[start]
            s = prices[end]
            while s-b < 0:
                start += 1
                b = prices[start]
            profit = max(profit, s-b)
        return profit