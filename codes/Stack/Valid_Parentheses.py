# LeetCode 20. Valid Parentheses

class Solution:
    def isValid(self, s):
        stack = []
        mapping = { ")": "(", "]":"[", "}": "{" }

        for ch in s:
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not len(stack)