class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window: the window between left and right never has a repeated character
        chars = set() # holds the characters that are in our current window
        left = 0
        best = 0 # longest window we have seen so far

        # move our right pointer through every character in the string
        for right in range(len(s)):
            # if we have seen this character in our window then we have a repeat
            # so we shrink from the left, removing characters until the repeat is gone
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # now we know the character is not in our window so we can add it
            chars.add(s[right])

            # check the size of our current window and keep the biggest one
            best = max(best, right - left + 1)

        # an empty string never enters the loop so best stays 0, no edge case needed
        return best

    # Time complexity: O(n) since every character gets added once and removed at most once
    # Space complexity: O(m) where m is the number of unique characters, since our set only holds the window