class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brainstorming: 
        # a hashmap is a data structure that stores data as a key value pair and lets you look up, insert or, update a value by its key in constant time 
        # here we can have an array counter that counts the characters for [a to z] and how many it has of each. 
        # our key can be the pattern of count and the value will be the actual word 
        # time complexity O(m * n) m = input string n = average len(m) 
        result = {} #mapping charcount to list of Anagrams
        for s in strs: 
            count  = [0] * 26 # a to z
            for c in s: 
                #position is current character c -  a since we start with a 
                # thus if we subtract ascii we get 25-25 = 0 which means we are at a 
                count[ord(c) - ord("a")] += 1 # count how many of the characters we have 
        # if the count does not exist we can change it to a default dictonary and right now our count is a list which can't be a key so we can change it to a tuple since it is non muttable 
            result.setdefault(tuple(count), []).append(s)
        return list(result.values())