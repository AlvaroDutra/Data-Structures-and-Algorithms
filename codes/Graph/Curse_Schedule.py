# LeetCode 207. Course Schedule

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = { i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses
        # [0,0,0]
        # 0 = não visitado
        # 1 = visitando
        # 2 = visitado

        def has_cycle(v):
            if state[v] == 1:
                return True
            if state[v] == 2:
                return False
            
            state[v] = 1

            for neighbor in graph[v]:
                if has_cycle(neighbor):
                    return True
                
            state[v] = 2
            return False
        
        for i in range(numCourses):
            if has_cycle(i):
                return False
            
        return True