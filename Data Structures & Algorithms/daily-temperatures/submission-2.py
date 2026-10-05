class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # keep colder temps here since we haven't seen a warmer temp
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while (len(stack) != 0) and t > temperatures[stack[-1]]:
                top_element = stack.pop() # if we have a temperature higher than the top element in the stack then we can remove it from the stack
                result[top_element] = i - top_element
            #if the stack is empty or the temperature in the list is less than, then add it to the stack
            stack.append(i)
        return result

        # complexity: O[n] since we have to go through the entire list of temps, O(n) space since our stack could grow to the size of the input