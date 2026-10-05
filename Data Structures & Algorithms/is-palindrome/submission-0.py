class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        # while the pointers haven't crossed each other or met yet
        while left < right: 
            #if not a digit or number just skip it 
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]): 
                right -= 1
            if s[left].lower() != s[right].lower(): #if they are not the same character we can just return false
                return False
            left, right = left + 1, right - 1
        return True
        # a palindrome is a string where it is the same in reverse as it is in the normal order
        # solution 2:
        # have 2 pointers coming from left and right 
        # check if they are the same char at the given space
        # yes? move inwards no? return false
        # string must be already converted to lowercase and skip spaces
        # linear time algo but memory complexisy is constant because we are not using any extra memory 
    def alphaNum(self, c):
            # first check if the character is alpha numeric by getting the ascii characters
            #values are contigous from A-Z and a-z same for digits
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or  ord('0') <= ord (c) <= ord ('9')) 

