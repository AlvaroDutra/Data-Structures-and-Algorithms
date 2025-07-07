#LeetCode 191. Number of 1 Bits

class Solution1:
    def hammingWeight(self, n: int) -> int:
        setBits = 0
        bits = bin(n)

        for bit in bits:
            if bit == '1':
                setBits +=1
        
        return setBits
    
# Alternative solution using bit manipulation
# Interative solution

class Solution2:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n != 0:
            counter += n & 1
            n >>= 1
        
        return counter
    
# Brian Kernighan's Algorithm
class Solution3:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # This operation reduces the number of set bits by 1
            count += 1
        return count
