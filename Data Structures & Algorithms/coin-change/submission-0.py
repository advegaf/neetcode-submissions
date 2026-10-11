class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0: # try each possible coin                 # fewest coins needed to make the amount a

                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1

        #O(n * t) time where n is the input since we have to go through the entire array of coins in the inner loop and t is the amount that we are given. 
        # O(t) space since our array will grow at most the size of t where t is the amount 