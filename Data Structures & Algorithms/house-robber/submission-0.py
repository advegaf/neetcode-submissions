class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

        # O(n) for space and time since we create a enw array of the length of the input, and we have to go through the loop for the size of the input