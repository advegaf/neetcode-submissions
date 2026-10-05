class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            #while the stack is not empty and the current temperature is greater than the element at the top of the stack
            while (len(stack) != 0) and temp > temperatures[stack[-1]]:
                top = stack.pop() # remove the top element
                result[top] = index - top # current index we are in - the last index that we saw in teh stack
            stack.append(index) # add that new index to the top of the stack
        return result