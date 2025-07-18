# LeetCode 347. Top K Frequent Elements
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        heap = []
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res



# [(-3, 1)]
# [(-3, 1), (-2, 2)]
# [(-3, 1), (-2, 2), (-1, 3)]
# [1]
# [1, 2]