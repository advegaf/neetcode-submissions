class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
    # split on dots and compare each part as an int, left to right
    # a missing part counts as 0, so "1.0" equals "1.0.0"

        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        # we will need to loop based on the length of the greatest revisions 
        len1 = len(revisions1)
        len2 = len(revisions2)
        max_len = max(len1, len2) # how many times we need to loop to check all possible revisions
        for i in range(max_len): # go through each number of revisions
            if i < len1:
                r1 = int(revisions1[i])  #store a dummy variable for the integer that we are in right now 
            else: 
                r1 = 0
            if i < len2:
                r2 = int(revisions2[i])
            else: 
                r2 = 0
            # comparison work
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0 #every revision was identical 
        # Time Complexity:
        # O(N + M) where n is the length of our version 1 string and m is the length of version 2 
        # Space Complexity:
        # O(N + M) since we have at most the size of each string so we need to store them in our variables 
