# Binary Tree Implamentation
from Tree_Node import Node
from collections import deque

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def dfs(self,data):
        return self._dfs(self.root, data)
    
    def _dfs(self, node, data):
        if node:
            print(node.data)

        if node is None:
            return False
        
        if node.data == data:
            return True
        
        if self._dfs(node.left, data):
            return True
        
        if self._dfs(node.right, data):
            return True

    def bfs(self, data):
        if self.root is None:
            return False
        
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.data)
            if node.data == data:
                return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return False
    
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self,node,result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.data)





tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)

print("preorder traversal:", tree.preorder_traversal())
print("inorder traversal:", tree.inorder_traversal())
print("postorder traversal:", tree.postorder_traversal())
# print("dfs:", tree.dfs(10))
# print("bfs:", tree.bfs(10))
