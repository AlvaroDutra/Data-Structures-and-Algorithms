# LeetCode 743. Network Delay Time
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        table = {}

        for t in times:
            if not table.get(t[0]):
                table[t[0]] = {t[1]:t[2]}
            else:
                table[t[0]] [t[1]] = t[2]

        distances = { k: 0 }
        
        min_heap = [(0, k)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            row = table.get(node)

            if row:
                for key, v in row.items():
                    table_dist = distances.get(key, float('inf'))
                    if dist + v < table_dist:
                        distances[key] = dist + v
