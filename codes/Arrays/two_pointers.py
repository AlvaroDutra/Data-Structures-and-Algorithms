# LeetCode 557. Reverse Words in a String III

class Solution:
    def reverseWords_manual(self, s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != '':
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r 
                
        res += s[l:r+2][::-1]
        return res
    
s = Solution()

res = s.reverseWords_manual('ola meu nome e')

print(res)