class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0 
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k: # number of replacements allowed
                count[s[left]] -= 1 
                left += 1

            res = max(res, right - left + 1)
        return res
        # O(n) time since we have to go through the entire string O(1) space since our count will always be of size 26 max for 26 characters in the alphabet 