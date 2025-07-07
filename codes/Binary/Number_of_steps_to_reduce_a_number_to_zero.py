# LeetCode 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int)-> int:
        
        steps = 0
        while num > 0:
            if num & 1:  # Check if the last bit is 1 using bitwise AND 
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps