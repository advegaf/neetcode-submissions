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
        return True if len(stack) == 0 else False
                    