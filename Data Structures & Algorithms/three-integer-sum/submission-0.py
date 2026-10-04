class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution 1: 
        # have 3 nested loops and check for duplicates 
        result = [] # needs to be returned as a list of list
        nums.sort() # sort array so we can prevent duplicates and use 2 pointers like for 2 sum 
        #look for first value 
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:  #not the first value then continue
                continue
            left = i + 1 # number after the initial one since we are checking for numbers after it
            right = len(nums) - 1
            while left < right:
                threesum = a + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else: 
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
