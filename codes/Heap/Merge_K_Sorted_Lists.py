# LeetCode 23. Merge K Sorted Lists
import heapq

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        for node in lists:
            push_node(heap, node)

        dummy = ListNode()
        current = dummy

        while heap:
            _,_,node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                push_node(heap, node.next)
            
        return dummy.next