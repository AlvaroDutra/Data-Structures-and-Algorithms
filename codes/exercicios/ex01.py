# LeetCode 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int)-> bool:
        visto = {}

        for i, valor in enumerate(nums):

            if valor in visto and i - visto[valor] <= k:
                return True
            
            visto[valor] = i
        
        return False
    

s = Solution()

lista = [1,2,3,1,2,3]
k = 2
 
res = s.containsNearbyDuplicate(lista, k)

print(res)