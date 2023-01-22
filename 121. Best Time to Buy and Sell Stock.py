class Solution:
    def maxProfit(self,prices):
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
        return max_profit
