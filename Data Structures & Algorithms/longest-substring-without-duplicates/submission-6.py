class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can use a set to keep track of everything since sets do not contain duplicate values
        # ex:
        "abcabcbb" #remove a, remove b, remove c, etc always popping from the left 
        chars = set()
        left = 0 
        res = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            res = max(res, right - left + 1)
        
        return res


    # Time complexity: O(n) since every character gets added once and removed at most once
    # Space complexity: O(m) where m is the number of unique characters, since our set only holds the window