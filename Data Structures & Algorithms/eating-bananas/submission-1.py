class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # in the worst case k would be the max number that is in our pile 
        # ex k = 11, 
        l = 1 #slowest it can be is 1 banana per hours
        # the fastest speed is the largest amount of bananas in the pile
        r = max(piles)
        # we know that for now the best speed we have seen is the largest amount of bananas in the pile
        res = r
        while l <= r:
            # k will be the speed per hour 
            k = (l + r) // 2
            hours = 0
            for p in piles:
                # we know that we need to find the minimum and it must be a whole number so we use its ceiling 
                hours += math.ceil(p / k)
            if hours <= h: #if the current hours it takes to eat the entire pile are less than the given from the parameter we can update our result and find whichever is lower, either our current res or k, 
                res = min(res, k)
                # decrease the right pointer to the left since we need to continue trying leftwards
                r = k - 1
            else: 
                l = k + 1
        return res
# Space complexity is constant time since we are not creating any new data structure 
# Time complexity is O(nlogm) where m is the max of the pile, and n is the amount of items in the pile
            
