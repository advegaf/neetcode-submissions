class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # mapping the value with the index
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        # two pointer solution:
        '''left = 0
        right = len(nums) - 1
        while left < right: 
            twosum = nums[left] + nums[right]
            if twosum == target:
                return [left, right]
            elif twosum > target: 
                right -= 1
            elif twosum < target: 
                left += 1
        return []'''
        
    

