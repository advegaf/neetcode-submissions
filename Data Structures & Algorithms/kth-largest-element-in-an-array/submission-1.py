class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # One option is to heapify the entire array which is O(n) time 
        # popping from the heap is k max times which is O(logn) thus we have O(n + klogn)

        # quick sort works by grabbing a pivot and we rearrange around that pivot to where smaller elements are on the left and anything greater is on the right 
        # after we split everything

        # Time complexity - O(n) on average since we have to go through the entire array to do quick select and O(n^2) in the worst case
        # Space complexity O(n) since we are not looking at both halfs of the partition, but at most once 

        k = len(nums) - k
        def quickselect(left, right):
            pivot, p = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p > k:
                return quickselect(left, p - 1)
            elif p < k:
                return quickselect(p + 1, right)
            else:
                return nums[p]
        return quickselect(0, len(nums) - 1)