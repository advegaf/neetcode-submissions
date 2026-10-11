class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1 
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one 

        # Time complexity O(n) since we have to go through the loop for the size of the input 
        # Space complexity O(1) since we are using 3 variables and not creating any new data structure