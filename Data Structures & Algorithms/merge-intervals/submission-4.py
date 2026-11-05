class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the start value 
        intervals.sort(key = lambda i: i[0]) # where we know that for each value in intervals the first element will be the start value since we have the [start, end]
        output = [intervals[0]] # i am going to actually add the first interval so we avoid an edge case

        start = 0 #we know that the start will be the first element so i can just let it be the 0th element for ease of use
        end = 1 # our end of our given interval that we are at, will be the second element in the list so we can just call it end for ease of use


        # go through each interval in the list of intervals 
        #skip the first one since it is already in the list
        for interval in intervals[1:]: 
            # grab the most recently added interval (last element)
            lastEnd = output[-1][end] 
            if interval[start] <= lastEnd:
                # we know that the interval will end at the max value between the self or the current end that we are in so we merge them together 
                output[-1][end] = max(lastEnd, interval[end])
            else: 
                output.append([interval[start], interval[end]])
        return output
            
    # Time complexity:
    # we are sorting and then interating so we can reduce everything to a complexity of O(nlogn)
    # Space complexity: 
    # O(n) since we our output can be at max the size of the input