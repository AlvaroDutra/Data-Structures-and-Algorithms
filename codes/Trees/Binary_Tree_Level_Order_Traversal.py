# LeetCode 102. Binary Tree Level Order Traversal
from collections import deque

class Solution:
    def levelOrder(self, root):
        res = []

        q = deque()
        q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            if level:
                res.append(level)

        return res
