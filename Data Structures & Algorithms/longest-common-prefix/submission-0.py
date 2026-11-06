class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # a valid prefix must be common to all 3 of the strings 
        # if nothing is common then return ""
        # we need to go through all 3 strings at the same time 
        # our bound is only at max the length of the shortest string

        # Time Complexity :
        # O(nm) => n = average size of the strings, m = amount of strings
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # what if s is out of bounds? then check if i == len(s) and exit
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                
            res += strs[0][i]
        return res


