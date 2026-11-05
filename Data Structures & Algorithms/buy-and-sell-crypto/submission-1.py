class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can use a sliding window to check the values that we have in the given list and check whether our values at right is greater than our value at left and keep a track of the largest one that we have so far  
        buy = 0
        sell = 1
        maxProfit = 0 
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return maxProfit

        # Time complexity is O(n) since we have to go at max through all the elements in our list 
        # Space complexity is O(1) since we are just allocating variables and not creating any new data structures
