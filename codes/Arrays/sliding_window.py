# LeetCode 3090. Maximum Length Sobstring With Two Occurences

class Solution:
    def maximumLengthSubstring(self, s:str) -> int:
        l, r = 0, 0
        _max = 1
        couter = {}

        couter[s[0]] = 1

        while r < len(s) -1:
            r+=1
            if couter.get(s[r]):
                couter[s[r]] +=1
            else:
                couter[s[r]] = 1
            
            while couter[s[r]] == 3:
                couter[s[l]] -= 1
                l += 1

            _max = max(_max, r-l+1)

        print(f'maior sequencia: {s[l:r+1]}')
        return _max
    

s = Solution()
l = ['b','c','b','b','b','c','b','a']

res = s.maximumLengthSubstring(l)

print(res)