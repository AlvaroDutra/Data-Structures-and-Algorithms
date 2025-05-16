# LeetCode 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, char in enumerate(s):
            if not d.get(char):
                d[char] = [idx, 1]
            else:
                d[char][1] += 1

        for k,v in d.items():
            if v[1] == 1:
                return v[0]
        
        return -1
    

s = Solution()

res = s.firstUniqChar('paralelepipedo')

print(res)

    