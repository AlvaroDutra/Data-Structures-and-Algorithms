# LeetCode 112. Path Sum
from Tree_Node import Node as TreeNode

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.right and not root.left and targetSum == root.data:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.data) or self.hasPathSum(root.right, targetSum - root.data)