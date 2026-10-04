class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first compute every prefix and store the prefix for every number in the array 
        # keep a default value of one 
        #then do a pass from end to beginning, computing the post fix 
        # O(n) time and O(1) space since it says that the output will not account for any extra memory
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res