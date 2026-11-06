class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is the amount of numbers that are the most frequent elements 
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        # create an empty list for each number that can apppear 
        # so lets say that we have nums = [1,1,1,2,2,3]
        # then freq = [[], [], [], [], [], [], []]

        # loop for each number within nums array 
        for num in nums: 
            # for each number in our count dictionary we want to check if it exists, if so add its current count + 1, it will also handle the error in case we have never seen it
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items(): # for each number and its count as pairs in the count dictionary we want to go ahead and add it to our frequency List of lists where we want the most frequent at the far right 
            frequency[cnt].append(num)

        res = []
        #go through the entire list frequency starting from the back, stop at the front and walk it backwards
        for i in range(len(frequency) - 1, 0, -1):
            # for each number that we see in the frequency list of lists given at list i we want to add that result to our results 
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res


        #Time complexity: 
        # O(n) since we have to go through each element in our input list
        # SPace complexity: 
        # O(n) since it can be the case that we have k = n distinct elements
