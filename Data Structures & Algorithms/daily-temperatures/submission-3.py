class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #goal find amount of days it took us to find a new temperature that was greater than the previous
        result = [0] * len(temperatures)
        # pair of value [temp, index]
        stack = []
        for i, t in enumerate(temperatures): 
            #i index, t temp
            # is the stack empty and if it is check if the current temperature is greater than what we have at the top (since it is empty it should always be true)
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd) # number of days to find greater temp
            stack.append([t, i])
        return result

        # Complexity: O(n) time since we have to iterate through the entire input, O(n) space since we have to create a stack that can grow at most the size of the input 