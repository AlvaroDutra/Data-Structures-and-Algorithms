# LeetCode 268. Missing Number

class Solution:
    def missingNumber(self, nums):
        x = 0

        for num in nums:
            x ^= num
            

        for i in range(len(nums) + 1):
            x ^= i
            
        return x

s= Solution()
s.missingNumber([0, 2])
s.missingNumber([0, 1])
s.missingNumber([9,6,4,2,3,5,7,0,1])  