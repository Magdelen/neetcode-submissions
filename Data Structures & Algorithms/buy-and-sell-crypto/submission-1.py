class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        max_profit = 0

        for i in range(len(prices)):
            if  prices[i] < min_val:
                min_val = prices[i]
            profit = prices[i] - min_val 
            if profit > max_profit:
                max_profit = profit
   


        return max_profit
        