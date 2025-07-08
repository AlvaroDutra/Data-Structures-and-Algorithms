# LeetCode 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        return inorder(root)

# Alternative implementation of inorder traversal in python