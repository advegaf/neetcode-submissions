class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brainstorming: 
        # string s should have the same amount of characters and same characters as string does, disregard their order
        # ex: s = aaangrm & t = aaangrm => True!
        # same characters and same quantiy of characters
        # we can use a hashmap for each string, and have the key be the character since they must be unique and the value be the count 
        # and at the end both hasmaps must look the same 
        # so we can just go through the keys and check their value if they are the same then we return true!

        # O(s+t) since we have to iterate through the entire string 
        # same for the space complexity 
        # check whether their lengths are the same 
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True