# LeetCode 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            
            stack.append(i)
        
        return results