class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) == 1):
            return 0
        
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if (prices[l] < prices[r]):
                max_profit = max(max_profit, prices[r] - prices[l])
            elif (prices[l] > prices[r]):
                l = r
            r += 1
        return max_profit
        