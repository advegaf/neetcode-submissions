class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        right = len(intervals) - 1
        left = 0
        target = newInterval[0]
        while left <= right:
            mid = (left + right) // 2
            # ex intervals = [[0,4],[7,8],[13,15]] newInterval = [5,6]
            # then target = 5 
            # mid = intervals[2] = [7,8]
            # then intervals[mid][0] = 7 
            # target = 5 
            # move right pointer to the left since we do not need to check the right side
            if intervals[mid][0] < target:
                left = mid + 1
            else: 
                right = mid - 1
        intervals.insert(left, newInterval)
        # then use the same old logic since we are just merging
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

        
