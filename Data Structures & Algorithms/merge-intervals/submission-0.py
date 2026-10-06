class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity, since we have to sort the entire input and then interating through the input so we have O(nlogn) where n is input 
        # space complexity is O(n) since we are creating a new output array of max size n 
        intervals.sort(key = lambda i : i[0]) # sort by the start value
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end_int = output[-1][1]
            if start <= last_end_int: #then they overlapping 
                output[-1][1] = max(last_end_int, end) # grab the very last item which would be the highest element 
                # ex: [1,5], [2,3] = [1,5]
            else: 
                output.append([start, end])
        return output
         