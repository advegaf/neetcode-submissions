class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 

        # [rob1, rob2, n, n+1, ...]
        # if we want to rob n, we have to rob1, 
        # but if we rob2 then we can't rob n or rob1
        for n in nums:

            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2 # by the time that we get to the end, rob2 will be the max we can rob from the entire neighborhood of houses
        # O(n) time since we have to go through the entire array for the loop, O(1) for space since we do not have to create any new data structure we just have 3 variables 