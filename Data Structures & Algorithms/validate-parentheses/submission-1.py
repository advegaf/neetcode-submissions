class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctp = {")" : "(", "]" : "[", "}" : "{"}
        #key is closing, value is opening
        for c in s: 
            if c in ctp:
                # -1 in python is the value at the top of the stack (last value)
                if stack and stack[-1] == ctp[c]:
                    stack.pop()
                else:
                    #parantheses do not match or stack is empty 
                    return False
            else:
                stack.append(c)
                #return true if there is nothing else in the stack meaning that we had a successful pair for every item, else false
        return True if len(stack) == 0 else False

        # Complexity:
        # Time: we are going through the array once so we have O(n) where n is the size of the string 
        # Space: Since we are creating a stack which can be upto the size of the input string so O(n) as welll
                    