# LeetCode 1. Two Sum

class Solution:
    def TwoSum(self, nums: list[int], target: int)-> list[int]:
        d = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in d:
                return [d[diff], i]
            
            d[num] = i
        
        return []


s = Solution()

lista = [2,7,11,15]
target = 9

res = s.TwoSum(lista, target)

print(res)