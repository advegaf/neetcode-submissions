class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is the amount of numbers that are the most frequent elements 
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) #key is the number, value 1 + whatever its current count is and if there is nothing for n just toss a 0 
        for n, c in count.items(): # return key value pair (number in count)
           freq[c].append(n) # this value n occurs c times
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res