class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 is longer than s2 then we can't do anything with it
        if len(s1) > len(s2): 
            return False
            #s1 can't fit into s2 as a subtring 
            
        s1_sorted = sorted(s1)
        #loop whatever possible starting indices there are 
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i:i + len(s1)]
            window_sorted = sorted(window)
            if window_sorted == s1_sorted:
                return True
        return False

            