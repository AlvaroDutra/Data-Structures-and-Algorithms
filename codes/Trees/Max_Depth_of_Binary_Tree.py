# LeetCode 104. Maximum Depth of Binary Tree

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        depth = 0
        
        q = deque()
        q.append(root)

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return depth