# LeetCode 146. LRU Cache
class Node:
    def __init__(self, key, value, next=None, prev=None) -> None:
        self.key, self.value = key, value
        self.next, self.prev = next, prev
        

class LRUCache:
    def __init__(self, capacity) -> None:
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next =  self.right
        self.right.prev = self.left

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key] # type: ignore


    def remove(self, node):
        prev, _next = node.prev, node.next
        prev.next = _next
        _next.prev = prev

    def insert(self, node):
        prev, _next = self.left, self.left.next
        prev.next = _next.prev = node # type: ignore
        node.next = _next
        node.prev = prev
