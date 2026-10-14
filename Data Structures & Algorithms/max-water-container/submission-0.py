class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        area = 0
        width = 0 
        result = 0
        while left <= right:
            width = right - left
            area = min(heights[left], heights[right]) * width
            result = max(result, area)
            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1
        return result

    # O(n) time since we have to go through the entire array in the worst case
    # O(1) space since we are just using local variables