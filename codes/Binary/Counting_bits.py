# LeetCode 338. Counting Bits

class Solution1:
    def countBits(self, n: int):
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, n +1):
            if offset*2 == i:
                offset = i
            
            ans[i] = 1 + ans[i - offset]

        return ans
    
# Alternative solution using bit manipulation

class Solution2:
    def countBits(self, n: int):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans