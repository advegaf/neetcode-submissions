class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, left = 0, 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right 
            else: 
                profit = max(profit, prices[right] - prices[left])
        return profit