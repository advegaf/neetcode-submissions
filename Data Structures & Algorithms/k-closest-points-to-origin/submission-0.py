class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we need to first sort our points which is O(n*logn)

        # heapify is O(n) so linear time algorithm to put all of the elements into the heap 
        # popping k times is k * logn 
        minHeap = []
        for x,y in points: 
            distance = (x ** 2 ) + (y ** 2)
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res

        # Time complexity: O(n + k*logn) since popping is k*logn and going through the array is linear time so we have n at most for the size of the list.
        # Space complexity is O(n) since our heap can grow at most the size of the input