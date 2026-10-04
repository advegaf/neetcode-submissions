class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep unique values
        charset = set()
        left = 0 
        result = 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            result = max(result, right - left + 1)
        return result
        #O(n) time since we have to go through the array, space complexity is O(m) where m is the number of characters that are unique in the string