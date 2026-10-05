class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            # first determine where in the array are we 
            if nums[left] <= nums[mid]:
                # we are on the left sorted side 
                # if the target is greater than where we are then we need to move our left pointer to the right or if our target is less than the furthest most number we. also need to move our number to the left
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: 
                    right = mid - 1
            else: 
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1
        return -1