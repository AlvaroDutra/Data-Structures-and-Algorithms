# LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal
from Tree_Node import Node as TreeNode

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.data)

        root.right = self.buildTree(inorder[inorder_index+1:], postorder) 
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root