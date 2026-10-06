class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity, since we have to sort the entire input and then interating through the input so we have O(nlogn) where n is input 
        # space complexity is O(n) since we are creating a new output array of max size n 
        intervals.sort(key = lambda i : i[0]) # sort by the start value
        output = []
        start = 0
        end = 1
        # go through each integer pair in the list and 
        for interval in intervals:
            # if there is nothing in our array so far, or the end integer of the first element is less than the interval we are in start then we do not have an overlap
            if not output or output[-1][end] < interval[start]: 
                output.append(interval)
            else:
                output[-1] = [output[-1][start], max(output[-1][end], interval[end])]
        return output

         